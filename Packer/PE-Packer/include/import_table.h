/**
 * @file import_table.h
 * @brief Transform the import table.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-10
 * @par GitHub
 * https://github.com/czs108
 * 
 * @see @ref new-import-table
 */

#pragma once

#include "image.h"

#include <windows.h>

#include <stdbool.h>

/**
 * @brief Calculate the size required for the import table of the new format.
 * 
 * @param image_info    The PE image.
 * @return The required size.
 */
DWORD CalcNewImpTableSize(const PE_IMAGE_INFO* const image_info);


/**
 * @brief Transform the import table into the new format.
 * 
 * @param image_info    The PE image.
 * @param new_table
 * The space where the new table will be constructed,
 * and its size must be larger than the value returned by @em CalcNewImpTableSize() method.
 * Set this to @em NULL to get the required size.
 * 
 * @return The required size for the new import table.
 * 
 * @see @ref new-import-table
 */
DWORD TransformImpTable(const PE_IMAGE_INFO* const image_info,
                        BYTE* const new_table);


/**
 * @brief Clear the original import table.
 * 
 * @param image_info    The PE image.
 */
void ClearImpTable(const PE_IMAGE_INFO* const image_info);