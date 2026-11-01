#!/bin/python3
import os
import subprocess 
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


print("works for now")
print("now that we have the bootmgr.py file, we can start working on the boot manager functionality.")

#hollup lemme copy some code from the other file to get started
vm = ctk.CTk()
vm.geometry("900x720")
vm.title("EMPTY OS")
vm.configure(bg_color="blue")
from pathlib import Path
from PIL import Image

# After creating vm
background = Image.open(Path(__file__).with_name("background.png")).convert("RGB")
bg_image = ctk.CTkImage(
    light_image=background,
    dark_image=background,
    size=(900, 720),
)
bg_label = ctk.CTkLabel(vm, text="", image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.lower()
def idk():
    print("hollup lemme think what im gonna put here")

btn1 = ctk.CTkButton(
    master=vm,
    text="start.menu",
    command=idk,
    width=50,
    height=50,
)
btn1.place(relx=0, rely=1, anchor="sw", x=20, y=-10)
btn1.size = (4000, 4000)
#composed it myself (: so proud 
def okok():
    print("ringtone time BABY")
    print("(this needs mpv and nohup installed to work properly btw)")
    subprocess.run(["nohup mpv ./ringtone.mp3 > /dev/null 2>&1 &"], shell=True)
btn2 = ctk.CTkButton(
    master=vm,
    text="ringtone (composed by me)",
    command=okok,
    width=30,
    height=30,
)
btn2.place(relx=0, rely=1, anchor="sw", x=100, y=-10)


vm.mainloop()