/**
 * @file encrypt.h
 * @brief Encrypt data.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-13
 * @par GitHub
 * https://github.com/czs108
 */

#pragma once

#include <windows.h>

/**
 * @brief Encrypt data.
 * 
 * @param base  The base address of the data.
 * @param size  The size of the data.
 */
void EncryptData(BYTE* const base, const DWORD size);