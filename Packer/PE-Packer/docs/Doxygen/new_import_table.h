/**
 * @file new_import_table.h
 * @brief The Doxygen page about the new format of the import table.
 * 
 * @author Chen Zhenshuo (chenzs108@outlook.com)
 * @version 1.0
 * @date 2020-01-10
 * @par GitHub
 * https://github.com/czs108
 */

/**
 * @page new-import-table The New Format of the Import Table
 * @brief The new format of the import table, constructed by `TransformImpTab()` method.
 * 
    <table border="1" align="center" cellspacing="5" cellpadding="5">
        <caption>The New Format of the Import Table</caption>
        <tr>
            <th>Field</th>
            <th>Type</th>
        </tr>
        <tr align="center">
            <td>FirstThunk</td>
            <td>IMAGE_THUNK_DATA</td>
        </tr>
        <tr align="center">
            <td>The size of DLL name</td>
            <td>BYTE</td>
        </tr>
        <tr align="center">
            <td>The DLL name</td>
            <td>C-Style String</td>
        </tr>
        <tr align="center">
            <td>The number of functions</td>
            <td>DWORD</td>
        </tr>
        <tr>
            <td colspan="2">
                <table border="1" cellspacing="5" cellpadding="5">
                    <caption><b>Each function has two possible formats</b></caption>
                    <tr>
                        <th>By Name</th>
                        <th>By Order</th>
                    </tr>
                    <tr>
                        <td>
                            <table border="1" cellspacing="5" cellpadding="5">
                                <tr align="center">
                                    <td>The size of function(1) name</td>
                                    <td>BYTE</td>
                                </tr>
                                <tr align="center">
                                    <td>The function(1) name</td>
                                    <td>C-Style String</td>
                                </tr>
                                <tr align="center">
                                    <td colspan="2">......</td>
                                </tr>
                            </table>
                        </td>
                        <td>
                            <table border="1" cellspacing="5" cellpadding="5">
                                <tr align="center">
                                    <td>0x00</td>
                                    <td>BYTE</td>
                                </tr>
                                <tr align="center">
                                    <td>The function(1) order</td>
                                    <td>VOID*</td>
                                </tr>
                                <tr align="center">
                                    <td colspan="2">......</td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
 *
 * @attention The size of C-Style String includes the '\0'.
 */