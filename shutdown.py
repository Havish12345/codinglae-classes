import os
import platform

def shutdown():
    """shutdown the computer"""
    system=platform.system()
    if system == "Windows":
        os.system("shutdown /s /t 1")
    else:
        print("Unsupported OS")
if __name__ == "__main__":
    shutdown()        
