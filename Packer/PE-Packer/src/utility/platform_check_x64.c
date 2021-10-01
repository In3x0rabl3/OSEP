/**
 * @file platform_check_x64.c
 * @brief Check if the PE image matches the program platform.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-14
 * @par GitHub
 * https://github.com/czs108
 * 
 * @note This implementation is for x64 platforms.
 */

#include "platform_check.h"

#include <assert.h>


bool IsPeMatchPlatform(const PE_IMAGE_INFO* const image_info) {
    assert(image_info != NULL);

    return IsPe64(image_info);
}