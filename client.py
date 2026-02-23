#!/usr/bin/env python3

import socket
import re
import sys
import time
from struct import unpack
import select
import optparse
import errno
import threading
import logging

# ===============================
# Minimal internal replacements
# ===============================

class RelayMainError(Exception):
    pass


def ls(x):
    return list(x)


def create_logger(name, console, verbose, logfile):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if verbose else logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    if console:
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    if logfile:
        fh = logging.FileHandler(logfile)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger


# Minimal relay constants
PING_CMD = b"\x01"
FORWARD_CONNECTION_SUCCESS = b"\x02"
FORWARD_CONNECTION_FAILURE = b"\x03"
CLOSE_RELAY = b"\x04"

banner = b"RPIVOT"
banner_response = b"RPIVOT_OK"

delay = 0.1
relay_timeout = 30


class Relay:
    def __init__(self, command_socket):
        self.command_socket = command_socket
        self.input_connections = [command_socket]
        self.channels = {}
        self.last_ping = time.time()
        self.ping_delay = 10
        self.remote_side_is_down = False
        self.relay_timeout = relay_timeout

    def send_proxy_cmd(self, cmd, channel_id=None):
        try:
            if channel_id is not None:
                self.command_socket.send(cmd + channel_id.to_bytes(2, "little"))
            else:
                self.command_socket.send(cmd)
        except socket.error:
            raise RelayMainError()

    def _set_channel(self, sock, channel_id):
        self.channels[channel_id] = sock

    def unset_channel(self, channel_id):
        if channel_id in self.channels:
            del self.channels[channel_id]

    def close_sockets(self, sockets):
        for s in sockets:
            try:
                s.close()
            except:
                pass

    def shutdown(self):
        self.close_sockets(self.input_connections)

    def manage_proxy_socket(self):
        data = self.command_socket.recv(4096)
        if not data:
            raise RelayMainError()

    def manage_socks_client_socket(self, sock):
        data = sock.recv(4096)
        if not data:
            raise RelayMainError()


# ===============================
# Your original code below
# ===============================

def key_by_value(my_dict, value):
    for k, v in my_dict.items():
        if v == value:
            return k
    return None


class SocksRelay(Relay):

    def __init__(self, command_socket):
        super(SocksRelay, self).__init__(command_socket)
        self.establishing_dict = {}
        self.forward_socket = None
        self.data = None

        self.ping_thread = threading.Thread(target=self.ping_worker, name='Ping')
        self.ping_thread.daemon = True
        self.ping_thread.start()

    def ping_worker(self):
        while True:
            time.sleep(self.ping_delay)
            current_time = time.time()

            if self.remote_side_is_down:
                log.debug('Remote side down. Exiting ping worker')
                return

            if current_time - self.last_ping > self.relay_timeout:
                log.error('No response from remote side. Restarting relay...')
                self.command_socket.close()
                return

    def close_connection_with_server(self):
        self.command_socket.close()
        self.input_connections.remove(self.command_socket)

    def establish_forward_socket(self, channel_id, host, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setblocking(0)
            log.debug(f"[{channel_id}] Opening {host}:{port}")
            sock.connect_ex((host, port))
        except socket.error as err:
            log.error(f"[{channel_id}] Socket error: {err}")
            self.send_proxy_cmd(FORWARD_CONNECTION_FAILURE, channel_id)
            return

        log.debug(f"[{channel_id}] Pending forward connection")
        self.establishing_dict[sock] = channel_id

    def run(self):
        while True:
            try:
                time.sleep(delay)

                ready_to_read, ready_to_write, _ = \
                    select.select(self.input_connections,
                                  self.establishing_dict.keys(), [], 15)

            except KeyboardInterrupt:
                log.info('SIGINT received. Closing relay.')
                self.send_proxy_cmd(CLOSE_RELAY)
                self.shutdown()
                return

            except (select.error, socket.error) as err:
                log.error(f'Select error: {err}')
                self.shutdown()
                return

            for sock in ready_to_write:
                channel_id = self.establishing_dict[sock]
                log.info(f'Connection established on channel {channel_id}')
                sock.setblocking(1)

                self.send_proxy_cmd(FORWARD_CONNECTION_SUCCESS, channel_id)
                del self.establishing_dict[sock]
                self.input_connections.append(sock)
                self._set_channel(sock, channel_id)

            for selected_input_socket in ready_to_read:
                if selected_input_socket == self.command_socket:
                    try:
                        self.manage_proxy_socket()
                    except RelayMainError:
                        log.debug('Remote side closed socket')
                        self.close_sockets(self.input_connections)
                        return
                else:
                    try:
                        self.manage_socks_client_socket(selected_input_socket)
                    except RelayMainError:
                        pass


def main():
    global log

    parser = optparse.OptionParser(description='Reverse socks client')
    parser.add_option('--server-ip', dest='server_ip')
    parser.add_option('--server-port', dest='server_port', default='9999')
    parser.add_option('--verbose', action="store_true", dest="verbose", default=False)
    parser.add_option('--logfile', dest="logfile", default=None)

    cmd_options = parser.parse_args()[0]

    if cmd_options.server_ip is None:
        print('Server IP required')
        sys.exit()

    log = create_logger(__name__, True, cmd_options.verbose, cmd_options.logfile)

    while True:
        log.info(f'Connecting to {cmd_options.server_ip}:{cmd_options.server_port}')

        try:
            bc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            bc_sock.connect((cmd_options.server_ip, int(cmd_options.server_port)))
        except socket.error as err:
            log.error(f'Connection failed: {err}. Retrying...')
            time.sleep(5)
            continue

        try:
            bc_sock.send(banner)
            banner_response_rcv = bc_sock.recv(4096)

            if banner_response_rcv != banner_response:
                log.error("Wrong banner response")
                bc_sock.close()
                time.sleep(5)
                continue

        except socket.error as err:
            log.error(f'Banner error: {err}')
            bc_sock.close()
            time.sleep(5)
            continue

        socks_relayer = SocksRelay(bc_sock)

        try:
            socks_relayer.run()
        except socket.error as err:
            log.error(f'Relay crashed: {err}. Restarting...')
            bc_sock.close()
            continue


if __name__ == '__main__':
    main()
