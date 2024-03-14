import os

op_sys = os.name

if op_sys == "nt":
    print("Windows")
elif op_sys == "posix":
    print("Linux/IOS")
else:
    print("OS is unknown")