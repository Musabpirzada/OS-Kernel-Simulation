from tkinter import *
root = Tk()
root.title("FASTEffos") #OS name
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the window size to the screen size
root.geometry(f"{screen_width}x{screen_height}")

class Main_Menu:
    def __init__(self, root):
        self.blank_label = Label(root, text='', height=2)
        self.blank_label.pack()
        self.label_title = Label(root, text="OS Kernal Simulation", font="Times 36 italic bold")
        self.label_title.pack()
        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()

class ProcessManagement:
    def __init__(self):
        self.blank_label = Label(root, text='', height=1)
        self.blank_label.pack()

        self.label_title = Label(root, text="Process Management log", font="Times 24 bold")
        self.label_title.pack()
        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()
root.mainloop()