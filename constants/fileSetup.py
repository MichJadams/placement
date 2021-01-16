import os
import json

currentPath = "C:\\Users\\mjada\\source\\repos\\placement\\saved_files"
saved_applied_jobs = currentPath + "\\applied_jobs"
resumes = currentPath + "\\resumes"
cover_letters = currentPath + "\\cover_letters"
settings_file = currentPath + "\\settings.json"
pdf_dir = currentPath + "\\pdfs"
snippits_dir = currentPath + "\\snippits"

empty_defaults = {
    "resumes": {
        "default": False
    },
    "cover_letters": {
        "default": False
    },
    "snippits": {}
}

def setUpFiles():
    create_saved_files_dir()
    create_cover_dir()
    create_resume_dir()
    create_applied_jobs_dir()
    create_settings_file()
    create_pdf_dir()
    create_snippits_dir()

def create_saved_files_dir():
    try:    
        os.chdir(currentPath)
    except:
        os.makedirs(currentPath)
        
def create_cover_dir():
    try:    
        os.chdir(cover_letters)
    except:
        os.makedirs(cover_letters)

def create_resume_dir():
    try:    
        os.chdir(resumes)
    except:
        os.makedirs(resumes)

def create_applied_jobs_dir():
    try:    
        os.chdir(saved_applied_jobs)
    except:
        os.makedirs(saved_applied_jobs)

def create_snippits_dir():
    try:    
        os.chdir(snippits_dir)
    except:
        os.makedirs(snippits_dir)

def create_settings_file():
    if not os.path.exists(settings_file):
        f = open(settings_file,"w+")
        f.write(json.dumps(empty_defaults))
        f.close()

def create_pdf_dir():
    try:    
        os.chdir(pdf_dir)
    except:
        os.makedirs(pdf_dir)
