import ctypes

from ctypes.wintypes import HANDLE,DWORD,LPSTR,WORD,LPBYTE

k_handle = ctypes.WinDLL("kernel32.dll")

#process info structure
class PROCESS_INFORMATION(ctypes.Structure):
    _fields_ = [
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
        ]   
 
#startup info structure
class STARTUPINFOA(ctypes.Structure):
    _fields_ = [
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
        ("lpReserved2", LPBYTE),
        ("cbReserved2", WORD),
        ("wShowWindow", WORD),
        ("cb", DWORD),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD),
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("lpReserved", LPSTR),
        ("lpDesktop", LPSTR),
        ("lpTitle", LPSTR),
        ]   
        
lpApplicationName = "C:\\Windows\\System32\\cmd.exe"
lpCommandLine = None
lpProcessAttributes = None
lpThreadAttributes = None
lpEnviroment = None
lpCurrentDirectory = None

dwCreationFlags = 0x00000010

bInheritHandle = False

lpProcessInformation = PROCESS_INFORMATION()

lpStartupInfo = STARTUPINFOA()

lpStartupInfo.wShowWindow = 0x1

lpStartupInfo.dwFlags = 0x1

response = k_handle.CreateProcessW(
    lpApplicationName,
    lpCommandLine,
    lpProcessAttributes,
    lpThreadAttributes,
    bInheritHandle,
    dwCreationFlags,
    lpEnviroment,
    lpCurrentDirectory,
    ctypes.byref(lpStartupInfo),
    ctypes.byref(lpProcessInformation))

if response > 0:
    print("proc is running")
else:
    print("failed. Error code: {0}".format(k_handle.GetLastError()))