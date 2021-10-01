/**
 * @file platform_check.h
 * @brief Check if the PE image matches the program platform.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-14
 * @par GitHub
 * https://github.com/czs108
 * 
 * @note The implementation is different between x64 and x86 platforms.
 */

#pragma once

#include "../image.h"

#include <stdbool.h>

/**
 * @brief Check if the PE image matches the program platform.
 * 
 * @param image_info    The PE image.
 * @return @em true if the PE image matches the program platform, otherwise @em false.
 */
bool IsPeMatchPlatform(const PE_IMAGE_INFO* const image_info);