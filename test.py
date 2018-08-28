import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, 'Entry Sucessfull', 'Sucess', 0)