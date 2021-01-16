import tkinter as tk
import views.statistics as stats
import views.side_menu as sm
import constants.fileSetup as fs

fs.setUpFiles()

window = tk.Tk()
window.title("Placement")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

sm.load_buttons(window)
stats.load_statistics(window)

window.mainloop()