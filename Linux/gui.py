from pathlib import Path
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import subprocess
import os
import zipfile
import sys

config = ConfigParser()

try:
    config.read("config.ini")
    update = config["Settings"]["update"]

except Exception as e:
    messagebox.showerror("Config Error", "Config File Is Corrupted or does not Exist!")
    sys.exit("Config File Is Corrupted or does not Exist!")

if update == "True":

    subprocess.call(["Dependencies.sh"])

    config.set("Settings", "update", "False")

    with open("config.ini", "w") as configfile:
        config.write(configfile)

class MyDialog:
    def __init__(self, parent, ttt):
        top = self.top = Toplevel(parent)
        top.geometry("200x100")
        top.iconbitmap("Icon.ico")
        self.myLabel = Label(top, text=ttt)
        self.myLabel.pack()

        self.myEntryBox = Entry(top)
        self.myEntryBox.pack()

        self.mySubmitButton = Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        global output
        output = self.myEntryBox.get()
        self.top.destroy()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def Install():
    subprocess.call(["Install.bat"])

    skia_path_ins = MyDialog(window, ttt = "Path to Skia File")
    window.wait_window(skia_path_ins.top)
    skia_path = output

    try:
        with zipfile.ZipFile(skia_path, "r") as zf:
            zf.extractall(os.path.expanduser("~")+"/deps/skia")

    except Exception as e:
        messagebox.showerror("Unzip Error!", str(e))

    subprocess.call(["Compile.sh"])

    messagebox.showinfo("Done!", "Finisched Compiling Aseprite! It can be found in $HOME/aseprite/bin")

def Update():
    subprocess.call(["Update.sh"])

    subprocess.call(["Compile.sh"])

    messagebox.showinfo("Done!", "Finisched Compiling Aseprite! It can be found in $HOME/aseprite/bin")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def Start():
    if Mode.get() == "Auto":

        if os.path.isdir(os.path.expanduser("~")+"/aseprite") and os.path.isdir(os.path.expanduser("~")+"/deps"):
            Update()

        else:
            Install()

    elif Mode.get() == "Install":
        Install()

    elif Mode.get() == "Update":
        Update()

def Help():
    messagebox.showinfo("Help", "Please Refer to https://github.com/TheLiteCrafter/AsepriteTool")


window = Tk()

window.geometry("700x800")
window.configure(bg = "#FFFFFF")
window.title("AsepriteTool")
window.iconbitmap("Icon.ico")

Mode = StringVar(window)
Mode.set("Auto")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    350.0000000000001,
    250.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))

button_1 = OptionMenu(window, Mode, "Install", "Update", "Auto")
button_1.configure(indicatoron = 0, image = button_image_1)

button_1.place(
    x=35.000000000000114,
    y=723.0,
    width=170.0,
    height=60.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=Help,
    relief="flat"
)
button_2.place(
    x=495.0000000000001,
    y=723.0,
    width=170.0,
    height=60.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=Start,
    relief="flat"
)
button_3.place(
    x=265.0000000000001,
    y=723.0,
    width=170.0,
    height=60.0
)
window.resizable(False, False)
window.mainloop()