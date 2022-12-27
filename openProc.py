import ctypes

k_handle = ctypes.WinDLL("kernel32.dll")

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF) # quick way to process all access 

#to get process id from user 
pid = int(input("throw a process ID: "))

dwDesiredAccess = PROCESS_ALL_ACCESS 
bInheritHandele = False #not used for now
dwProcessId = "{:x}".format(pid) # the process id in hex string 

response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandele, dwProcessId) # gain a handle to the process

#print(response) # to test it to see the raw value of our handler

error = k_handle.GetLastError() #our error handler
if error !=0:
    print("error Code: {0}".format(error))
    exit(1)
#user notification
if response <= 0:
    print("handle was not created")
else:
    print("handle was created")
