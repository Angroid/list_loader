from tkinter import *
from tkinter import filedialog
from subprocess import call
from sys import platform


# open file dialog function
def browse():
    file_path = filedialog.askopenfilename()
    return file_path


# call to system's wget
def dl():
    curr_os = platform
    if curr_os == "win32":
        call(["wget", "-c", "-i", browse()], shell=True)
    else:
        call(["wget", "-c", "-i", browse()])


# create application window
root = Tk()
root.wm_title("List Loader")
root.minsize(width=500, height=100)
root.maxsize(width=500, height=100)
theLabel = Label(root, text="Choose a .txt file containing a list of URL's")
theLabel.pack()
dl_btn = Button(root, width=15, height=2, text="Choose & Download", command=dl)
dl_btn.pack()
root.mainloop()




