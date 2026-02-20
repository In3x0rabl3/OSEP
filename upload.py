#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import cgi

UPLOAD_DIR = os.getcwd()
PORT = 8000

class UploadHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"""
        <html>
        <body>
        <h2>Upload File</h2>
        <form enctype="multipart/form-data" method="post">
            <input type="file" name="file"><br><br>
            <input type="submit" value="Upload">
        </form>
        </body>
        </html>
        """)

    def do_POST(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        if "file" in form:
            file_item = form["file"]
            filename = os.path.basename(file_item.filename)

            filepath = os.path.join(UPLOAD_DIR, filename)

            with open(filepath, "wb") as f:
                f.write(file_item.file.read())

            self.send_response(200)
            self.end_headers()
            self.wfile.write(f"Uploaded: {filename}".encode())
            print(f"[+] Received file: {filename}")
        else:
            self.send_response(400)
            self.end_headers()

if __name__ == "__main__":
    print(f"Serving upload directory: {UPLOAD_DIR}")
    print(f"Listening on http://0.0.0.0:{PORT}")
    HTTPServer(("0.0.0.0", PORT), UploadHandler).serve_forever()
