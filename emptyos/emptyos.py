#!/bin/python3
import customtkinter as ctk
import subprocess
import sys
import time
from pathlib import Path

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("1920x1080")
app.title("EMPTY OS 💯️")
app.configure(bg_color="purple")

def happy():
    print(f"HEY IM HERE THE OUPUT WORKS")

btn = ctk.CTkButton(app, text="Test output", command=happy)
btn.pack(padx=20, pady=35)

def boot():
    subprocess.run(["echo 'Starting up!'"], shell=True)
    print(f"Dont forget to regularly check this output for any errors or warnings. If you see any, please report them to the developer.")
    time.sleep(1)
    bootmgr_path = Path(__file__).resolve().parent / "bootmgr.py"
    result = subprocess.run(
        [sys.executable, str(bootmgr_path)],
        capture_output=True,
        text=True,
    )
    print(result.stdout, end="", flush=True)
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr, flush=True)
    result.check_returncode()
    print(f"Welcome to this godamn emptyos based on customtkinter! (please do not bemchmark this os seriously or im cooked but you can modify the bootmgr tough)")


btn = ctk.CTkButton(app, text="boot", command=boot)
btn.pack(padx=25, pady=40)

app.mainloop()
