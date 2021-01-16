from constants import fileSetup
import tkinter as tk
import os
import json 

def load_application(frame, filename, application):
    fm_job = tk.Frame(frame, relief=tk.RAISED, bd=3)
    lb_company = tk.Label(fm_job, text=application["company"], font=("arial bold", 18))
    lb_company.grid(row=0, column=0, sticky="nw")

    lb_position = tk.Label(fm_job, text=application["position"])
    lb_position.grid(row=1, column=0, sticky="nw")

    lb_resume = tk.Label(fm_job, text=f'resume: {application["resume"]}')
    lb_resume.grid(row=2, column=0, sticky="nw")

    lb_cover = tk.Label(fm_job, text=f'Cover Letter: {application["cover"]}')
    lb_cover.grid(row=3, column=0, sticky="nw")

    date_applied = tk.Label(fm_job, text=application["date_applied"])
    date_applied.grid(row=0, column=2, sticky="nw")

    status = tk.Label(fm_job, text=application["status"])
    status.grid(row=4, column=1, sticky="nw")
    return fm_job 

def load_applications(window):
    fm_applications = tk.Frame(window)
    index = 0
    for file_name in os.listdir(fileSetup.saved_applied_jobs):
        with open(f'{fileSetup.saved_applied_jobs}\\{file_name}') as application_file:
            application = json.load(application_file)
        load_application(fm_applications, file_name, application).grid(row=index, column=0, sticky="nsew")
        index += 1

    fm_applications.grid(row=0, column=1, sticky="nsew")
