import tkinter as tk
from constants import fileSetup
import os 

statistics_data = []

def set_statistics():
    statistics_data = []
    statistics_data.append({"name": "Total application count", "value":len(os.listdir(fileSetup.saved_applied_jobs))})
    statistics_data.append({"name": "Total unique resumes", "value":len(os.listdir(fileSetup.saved_applied_jobs))})
    statistics_data.append({"name": "Total unique cover letters", "value":len(os.listdir(fileSetup.saved_applied_jobs))})
    statistics_data.append({"name": "Job application rate", "value":len(os.listdir(fileSetup.saved_applied_jobs))})
    return statistics_data


def add_stat(stat_frame, name, value):
    fr_stat = tk.Frame(stat_frame)
    lb_name = tk.Label(fr_stat, text=name)
    lb_value = tk.Label(fr_stat, text=value)
    lb_value.grid(row=0, column=0)
    lb_name.grid(row=1, column=0)
    return fr_stat
    
def loop_through_stats(fm_statistics, statistics):
    i = 0
    irow = 0
    icol = 0 
    while i < len(statistics):
        stat = statistics[i]
        fr_stat = add_stat(fm_statistics, stat["name"], stat["value"])
        fr_stat.grid(row=irow, column=icol, sticky="ns")
        i += 1
        icol += 1
        if i >= len(statistics):
            break
        stat = statistics[i]
        fr_stat = add_stat(fm_statistics, stat["name"], stat["value"])
        fr_stat.grid(row=irow, column=icol, sticky="ns")
        irow += 1 
        icol = 0
        i += 1

def load_statistics(window):
    fm_statistics = tk.Frame(window)
    loop_through_stats(fm_statistics, set_statistics())
    fm_statistics.grid(row=0, column=1, sticky="nsew")