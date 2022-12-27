import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll") #grab a handle to kernel32
u_handle = ctypes.WinDLL("User32.dll") #grab a handle to user32


PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF) # Access rights 

# Token Access Rights
STANDARD_RIGHTS_REQUIRED = 0x000F0000
STANDARD_RIGHTS_READ = 0x00020000
TOKEN_ASSIGN_PRIMARY = 0x0001
TOKEN_DUPLICATE = 0x0002
TOKEN_IMPERSONATION = 0x0004
TOKEN_QUERY = 0x0008
TOKEN_QUERY_SOURCE = 0x0010
TOKEN_ADJUST_PRIVILEGES = 0x0020
TOKEN_ADJUST_GROUPS = 0x0040
TOKEN_ADJUST_DEFAULT = 0x0080
TOKEN_ADJUST_SESSIONID = 0x0100
TOKEN_READ = (STANDARD_RIGHTS_READ | TOKEN_QUERY)
TOKEN_ALL_ACCESS = (STANDARD_RIGHTS_REQUIRED | 
					TOKEN_ASSIGN_PRIMARY     |
					TOKEN_DUPLICATE          |
					TOKEN_IMPERSONATION      |
					TOKEN_QUERY              |
					TOKEN_QUERY_SOURCE       |
					TOKEN_ADJUST_PRIVILEGES  |
					TOKEN_ADJUST_GROUPS      |
					TOKEN_ADJUST_DEFAULT     |
					TOKEN_ADJUST_SESSIONID)

lpWindowName = ctypes.c_char_p(input("inter a window name: ").encode('utf-8'))#to get window name from user 

hWnd = u_handle.FindWindowA(None, lpWindowName) #get  a handle to the process

#check to see if we got one
error = k_handle.GetLastError() #our error handler
if hWnd ==0:
    print("Could not grab a handle.Error Code: {0}".format(error))
    exit(1)
else:
    print("we got a handle")

lpwProcessId = ctypes.c_ulong() #get the PID of process

response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpwProcessId)) 

#check to see if the call completed
if response == 0:
    print("Could not get PID.Error Code: {0}".format(error))
else:
    print("PID Found")
   
#opening the process by PID    
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessId = lpwProcessId

#calling the windows API Call to open the process
hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

#check to see if the call completed
if response <= 0:
    print("didnt grab a privelege handle.Error Code: {0}".format(error))
else:
    print("handle open")
    
ProcessHandle = hProcess
DesiredAccess = TOKEN_ALL_ACCESS
TokenHandle = ctypes.c_void_p()

response = k_handle.OpenProcessToken(ProcessHandle, DesiredAccess, ctypes.byref(TokenHandle))

if response > 0:
    print("got handle")
else:
    print("couldnt grab a privelege Token handle.Error Code: {0}".format(error))