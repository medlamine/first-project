import ctypes

user_handel = ctypes.WinDLL("User32.dll") #handle to user32.dll
k_handle = ctypes.WinDLL("Kernel32.dll") #handle to kernel32.dll

hWnd = None # not used : a handle to the owner window of the message box
lpText = "hello World"  # the message of the box window
lpCaption = "hello" # the title of the box window
uType = 0x00000001  # the options that will be shown in the box window

response = user_handel.MessageBoxW(hWnd, lpText, lpCaption, uType) # the response of the user

error = k_handle.GetLastError() #error handler 
if error !=0:       #just in case there was an error 
    print("Error code: {0}".format(error))
    exit(1)    
if response == 1:   # to tell if the user clicked ok
    print("User Clicked OK!")
elif response ==2:  #to tell if the user clicked cancel 
    print("User Clicked Cancel!")