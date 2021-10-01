/**
 * @file encrypt.c
 * @brief Encrypt data.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-13
 * @par GitHub
 * https://github.com/czs108
 */

#include "encrypt.h"

#include <assert.h>


void EncryptData(BYTE* const base, const DWORD size) {
    if (size == 0) {
        return;
    }

    assert(base != NULL);

    for (DWORD i = 0; i != size; ++i) {
        base[i] += 0xCC;
    }
}