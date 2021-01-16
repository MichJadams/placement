import tkinter as tk
import os
import shutil
import json
from tkinter.filedialog import askopenfilename, asksaveasfilename
from constants import fileSetup

def get_file(destination, frame, col, option):
    target = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    shutil.copy2(target, destination)
    load_list_of_files(frame, destination, col, option)

def load_list_of_files(frame, directory, col, option):
    fm_files = tk.Frame(frame)
    index = 1
    for file_name in os.listdir(directory):
        lb_file_name = tk.Label(fm_files, text=file_name)
        lb_file_name.grid(row=index, column=0)
        btn_set_default = tk.Button(fm_files, text="Set as Default", command=lambda file_name=file_name: set_default(option, file_name))
        btn_set_default.grid(row=index, column=1)
        index += 1
    fm_files.grid(row=1, column=col)

def load_settings(window):
    fm_settings = tk.Frame(window)
    load_snippits(fm_settings)

    btn_resume = tk.Button(fm_settings, text="Add Resume", command=lambda: get_file(fileSetup.resumes, fm_settings, 0, "resumes"))
    btn_cover_letter = tk.Button(fm_settings, text="Add Cover Letter", command=lambda: get_file(fileSetup.cover_letters, fm_settings, 1, "cover_letters"))
    btn_resume.grid(row=1, column=0)
    btn_cover_letter.grid(row=1, column=1)

    load_list_of_files(fm_settings, fileSetup.resumes, 0, "resumes")
    load_list_of_files(fm_settings, fileSetup.cover_letters, 1, "cover_letters")

    fm_settings.grid(row=0, column=1, sticky="nsew")
    fm_settings.tkraise()

def set_default(option, new_default_file):
    with open(fileSetup.settings_file) as settings_file:
        try:
            old_settings = json.load(settings_file)
        except:
            old_settings = fileSetup.empty_defaults

        if option in old_settings:
            old_settings[option]["default"] = new_default_file
        else:
            old_settings[option]={
                "default" : new_default_file
            }

    with open(fileSetup.settings_file, "w") as settings_file:
        settings_file.write(json.dumps(old_settings))


def load_snippits(frame):
    fm_snippits = tk.Frame(frame, bg="blue")
    ent_snippit_name = tk.Entry(fm_snippits)
    ent_snippit_name.grid(row=0, column=0)

    btn_add = tk.Button(fm_snippits, text="Add Snippit", command=lambda: add_snippit(fm_snippits,ent_snippit_name, load_saved_snippits, fm_snippits, 1, 0))
    btn_add.grid(row=0, column=1)

    load_saved_snippits(fm_snippits, 1, 0)
    fm_snippits.grid(row=0, column=0, sticky="nsew")

def load_saved_snippits(frame, row, col):
    fm_files = tk.Frame(frame)
    with open(fileSetup.settings_file) as settings_file:
        settings = json.load(settings_file)
        index = 0
        for snippit in settings["snippits"]:
            lb_file_name = tk.Label(fm_files, text=snippit)
            lb_file_name.grid(row=index, column=0)
            index += 1
    fm_files.grid(row=row, column=col, sticky="nsew")

def add_snippit(frame, snippit_name, reload, reload_frame, reload_row, reload_col):
    target = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    shutil.copy2(target, fileSetup.snippits_dir)
    file_name = fileSetup.snippits_dir

    with open(fileSetup.settings_file) as settings_file:
        try:
            old_settings = json.load(settings_file)
        except:
            old_settings = fileSetup.empty_defaults

        if "snippits" in old_settings:
            old_settings["snippits"][snippit_name.get()] = file_name
        else:
             old_settings["snippits"]={
                snippit_name.get() : file_name
            }
    snippit_name.delete(0, 'end')
    with open(fileSetup.settings_file, "w") as settings_file:
        settings_file.write(json.dumps(old_settings))

    reload(reload_frame, reload_row, reload_col)