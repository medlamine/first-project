import ctypes

user_handle = ctypes.WinDLL("User32.dll") #handle to user32.dll
k_handle = ctypes.WinDLL("Kernel32.dll") #handle to kernel32.dll

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF) # quick way to process all access 

lpWindowName = ctypes.c_char_p(input("enter window name: ").encode('utf-8'))

hWnd = user_handle.FindWindowA(None, lpWindowName)

error = k_handle.GetLastError() #error handler 

if hWnd ==0:
    print("Error code: {0} - could not grab handle".format(error))
    exit(1)
else:
    print("we have the handle")
    
lpdwprocessId = ctypes.c_ulong()
response = user_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwprocessId))

if response == 0:       #just in case there was an error 
    print("Error code: {0} - could not grab PID".format(error))
    exit(1)  
else:
    print("got the PID")


dwDesiredAccess = PROCESS_ALL_ACCESS 
bInheritHandele = False #not used for now
dwProcessId = lpdwprocessId # the process id 

hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandele, dwProcessId)

if hProcess <= 0:       #just in case there was an error 
    print("Error code: {0} - could not grab privileged handle".format(error))
    exit(1)  
else:
    print("got the handle")

uExitCode = 0x1

response = k_handle.TerminateProcess(hProcess, uExitCode)

if response == 0:       #just in case there was an error 
    print("Error code: {0} - could not kill process".format(error))
    exit(1)  
else:
    print("process terminated")
