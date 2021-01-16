import tkinter as tk
from .statistics import load_statistics
from .new_application import load_new_application
from .applications import load_applications
from .settings import load_settings

def load_buttons(window):
    fr_side_menu = tk.Frame(window, relief=tk.RAISED, bd=2)

    bt_stats = tk.Button(fr_side_menu, text="Statistics", command=lambda: load_statistics(window))
    bt_new_application = tk.Button(fr_side_menu, text="New Application", command=lambda: load_new_application(window))
    bt_applications = tk.Button(fr_side_menu, text="All Applications", command=lambda: load_applications(window))
    bt_manage_resumes = tk.Button(fr_side_menu, text="Manage application Defaults", command=lambda: load_settings(window))

    bt_stats.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    bt_new_application.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
    bt_applications.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
    bt_manage_resumes.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

    fr_side_menu.grid(row=0, column=0, sticky="ns", padx=5, pady=5)