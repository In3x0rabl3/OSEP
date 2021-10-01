/**
 * @file error_handling.h
 * @brief Error handling.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-09
 * @par GitHub
 * https://github.com/czs108
 * 
 * @see https://docs.microsoft.com/en-us/windows/win32/debug/system-error-codes
 */

#pragma once

#include <windows.h>

/**
 * @brief Get the last-error code.
 * 
 * @return The last-error code.
 */
DWORD GetLastErrorCode();


/**
 * @brief Set the last-error code got from @em GetLastError API.
 * 
 * @warning This method can only and must be called after a direct Windows API call failed.
 * 
 * @attention
 * Do not recommend using this method when freeing resources like memory and handles.
 * The failure of related APIs may cover the error during initialization.
 */
void SetLastErrorCode();


/**
 * @brief Reset the last-error code to @em ERROR_SUCCESS.
 */
void ResetLastErrorCode();


/**
 * @brief Get the message from an error code.
 * 
 * @param error_code    An error code got from @em GetLastErrorCode method.
 * @return A message or @em NULL if the method failed.
 * 
 * @warning The reture value must be free by @em FreeErrorMessage() method if it is not @em NULL.
 */
TCHAR* FormatErrorMessage(const DWORD error_code);


/**
 * @brief Free the memory of a message.
 * 
 * @param message   A message got from @em FormatErrorMessage() method.
 */
void FreeErrorMessage(TCHAR* const message);