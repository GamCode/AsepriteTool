import os
import sys
import subprocess
from configparser import ConfigParser
import zipfile

first = True
command = "req"
InstallMode = "Auto"

def change_install_mode(mode):
    InstallMode = mode
    print("Success! Install-Mode is now: " + InstallMode)

def Install():
    subprocess.call(["Install.bat"])

    skia_path = str(input("Please enter the path of the downloaded Skia.zip File: "))
    ninja_path = str(input("Please enter the path of the downloaded Ninja.zip File: "))

    try:
        with zipfile.ZipFile(skia_path, "r") as zf:
            zf.extractall("C:/deps/skia")

        with zipfile.ZipFile(ninja_path, "r") as zf:
            zf.extractall("C:/Program Files/CMake/bin")

    except Exception as e:
        print(str(e))

    if os.path.isdir("C:/Program Files/Microsoft Visual Studio/2022/Community/Common7/Tools"):
        subprocess.call(["Compile22.bat"])

    elif os.path.isdir("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common7/Tools"):
        subprocess.call(["Compile19.bat"])

    else:
        print("No Visual Studio installation found", "No Visual Studio installation found. Please refer to https://github.com/TheLiteCrafter/AsepriteTool")

    subprocess.call(["Shortcut.bat"])

def Update():
    subprocess.call(["Update.bat"])

    if os.path.isdir("C:/Program Files/Microsoft Visual Studio/2022/Community/Common7/Tools"):
        subprocess.call(["Compile22.bat"])

    elif os.path.isdir("C:/Program Files (x86)/Microsoft Visual Studio/2019/Community/Common7/Tools"):
        subprocess.call(["Compile19.bat"])

    subprocess.call(["Shortcut.bat"])

while 1:
    if first == False:
        command = input("Please Enter a Command: ")
        command = str(command).lower()

    if command == "help":
        print("List of avilable commands:")
        print("help - Shows a List of all avilable commands")
        print("start - Starts the install/update process")
        print("exit - Exists the programm")
        print("req - Shows all requierments")
        print("InstallMode Auto/Update/Install - Changes the Installation-Mode")

    elif command == "installmode auto":
        change_install_mode("Auto")

    elif command == "installmode install":
        change_install_mode("Install")
    
    elif command == "installmode update":
        change_install_mode("Update")

    elif command == "exit":
        sys.exit()

    elif command == "start":

        if InstallMode == "Auto":

            if os.path.isdir("C:/aseprite") and os.path.isdir("C:\deps"):
                print("Update Mode detected.")

                Update()
            
            else:
                print("Install mode detected.")

                Install()

        elif InstallMode == "Install":
            Install()

        elif InstallMode == "Update":
            Update()

    elif command == "req":
        print("Requierments: ")
        print("")
        print("Skia - https://github.com/aseprite/skia/releases")
        print("")
        print("Ninja - (https://github.com/ninja-build/ninja/releases)")
        print("")
        print("Visual Studio and Cmake will automatically be downloaded. On Cmake dont forget to select add to Path for all Users, and on Visual Studio the Desktop Development with C++ and under Individual Items (Check on Aseprite Guide: https://github.com/aseprite/aseprite/blob/main/INSTALL.md#windows-dependencies)")

        first = False