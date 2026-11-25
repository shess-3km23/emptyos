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

menu_panel = ctk.CTkFrame(vm, width=360, height=500)
menu_panel.place(x=20, y=150)
menu_panel.lower()

ctk.CTkLabel(
    menu_panel,
    text="START MENU",
    font=ctk.CTkFont(size=20, weight="bold"),
).pack(padx=20, pady=(20, 12), anchor="w")

ctk.CTkButton(menu_panel, text="Test app").pack(padx=20, pady=8, fill="x")
ctk.CTkButton(menu_panel, text="Settings").pack(padx=20, pady=8, fill="x")


def shutdown():
    vm.destroy()


ctk.CTkButton(
    menu_panel,
    text="Shutdown",
    command=shutdown,
).pack(padx=20, pady=8, fill="x")

menu_visible = False


def toggle_menu():
    global menu_visible
    if menu_visible:
        menu_panel.lower()
        menu_visible = False
    else:
        menu_panel.lift()
        menu_visible = True


btn1 = ctk.CTkButton(
    master=vm,
    text="start.menu",
    command=toggle_menu,
    width=50,
    height=50,
)
btn1.place(relx=0, rely=1, anchor="sw", x=20, y=-10)
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