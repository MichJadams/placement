import tkinter as tk
import json
import os
import pyperclip
from fpdf import FPDF 
from constants import fileSetup
from datetime import datetime 
from tkinter import ttk

application = {}

def load_new_application(window):
    fm_new_application = tk.Frame(window)
    load_fields(fm_new_application)
    fm_new_application.grid(row=0, column=1, sticky="nsew")
    fm_new_application.tkraise()

def load_fields(frame):
    lb_company_name = tk.Label(frame, text="Company Name:")
    lb_company_name.grid(row=0, column=0, sticky="sw")
    ent_company_name = tk.Entry(frame)
    ent_company_name.grid(row=0, column=1, sticky="sw")

    lb_position = tk.Label(frame, text="Position:")
    lb_position.grid(row=1, column=0, sticky="we")
    ent_position = tk.Entry(frame)
    ent_position.grid(row=1, column=1, sticky="we")

    dp_resume = load_file_manager(frame, "Resume: ", fileSetup.resumes, 2, "resumes")
    dp_cover = load_file_manager(frame, "Cover Letter: ", fileSetup.cover_letters, 3, "cover_letters")
    btn_template_text = tk.Button(frame, text="TT", command=lambda: template_cover_letter(fileSetup.cover_letters, dp_cover, ent_company_name.get()))
    btn_template_text.grid(row=3, column=3, sticky="we")

    btn_save = tk.Button(frame,text="Save", command=lambda: save_new_application(ent_company_name.get(), ent_position.get(), dp_resume.get(), dp_cover.get()))
    btn_save.grid(row=4, column=1, sticky="we")

def template_cover_letter(directory, dp_cover, company):
    camelCaseCompany = company.replace(" ", "")
    with open(f'{directory}\\{dp_cover.get()}') as cover_letter:
        original_text = cover_letter.read()       
    with open(f'{directory}\\{camelCaseCompany}CoverLetter.txt',"w+") as new_cover_letter:
        # actually replace the text in the {} with company name!
        new_cover_letter.write(original_text + "additional material!!") 
    dp_cover.set(f'{camelCaseCompany}CoverLetter.txt')
    convert_txt_to_pdf(directory, f'{camelCaseCompany}CoverLetter')

def convert_txt_to_pdf(directory, text_file_to_convert):
    pdf = FPDF() 
    pdf.add_page() 
    pdf.set_font("Arial", size = 12) 
    f = open(f'{directory}\\{text_file_to_convert}.txt', "r")
    text = f.read()
    pdf.cell(200, 100, txt = text, ln = 1, align = 'L') 
    f.close()
    pdf.output(f'{fileSetup.pdf_dir}\\{text_file_to_convert}.pdf') 

def load_file_manager(frame, label, directory, row, file):
    lb_file_manager = tk.Label(frame, text=label)
    lb_file_manager.grid(row=row, column=0, sticky="we")
    dp_file_manager = ttk.Combobox(frame, values= os.listdir(directory)) 
    dp_file_manager.grid(row=row, column=1, sticky="we")
    btn_file_link = tk.Button(frame, text="Get Link", command=lambda: get_link(directory, dp_file_manager.get()))
    btn_file_link.grid(row=row, column=2, sticky="we")

    try_load_defaults(dp_file_manager, file)
        
    return dp_file_manager

def get_link(directory, file):
    pyperclip.copy(f'{directory}\\{file}')

def save_new_application(company, position, resume, cover):
    application["company"] = company
    application["position"] = position
    application["resume"] = resume
    application["cover"] = cover
    application["date_applied"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    application["status"] = "applied"
    fileName = f'{fileSetup.saved_applied_jobs}\\{company}.json'
    application_file = open(fileName, 'w')
    application_file.write(json.dumps(application))
    application_file.close()

def try_load_defaults(dropdown, directory):
    with open(f'{fileSetup.currentPath}\\settings.json') as settings_file:
        settings = json.load(settings_file)
        if settings[directory]["default"]:
            dropdown.set(settings[directory]["default"])

def load_snippts():
    # load all the snippits here
    pass

def compose_new_cover_from_selected_snippts():
    # generate a cover letter 
    pass