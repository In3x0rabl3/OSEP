/**
 * @file extra_data.c
 * @brief Process the extra data behind the PE image.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-12
 * @par GitHub
 * https://github.com/czs108
 */

#include "extra_data.h"
#include "utility/file_access.h"

#include <assert.h>


bool WriteExtraDataToFile(const EXTRA_DATA_VIEW* const data,
                          const HANDLE file) {
    assert(data != NULL);
    assert(file != INVALID_HANDLE_VALUE);

    if (data->size > 0) {
        assert(data->base != NULL);

        return WriteAllToFile(file, data->base, data->size);
    } else {
        return true;
    }
}