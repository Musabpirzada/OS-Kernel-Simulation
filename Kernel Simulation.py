from tkinter import *
import time
from collections import deque
from threading import Semaphore
import math
root = Tk()
root.title("FASTEffos") #OS name
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Set the window size to the screen size
root.geometry(f"{screen_width}x{screen_height}")
global pcbdata, memory_dict,widgets, keyss, fcfs_widgets, short_widgets, keyss_short, Main_memory, memory_list,pages,Process_keys, show_p, lru_save
pcbdata = {}
lru_save = []
widgets = []
show_p = []
keyss = []
fcfs_widgets = []
keyss_short = []
short_widgets = []
memory_list = []
pages = []
Process_keys = []
class Main_Menu:
    def __init__(self, root):
        self.blank_label = Label(root, text='', height=2)
        self.blank_label.pack()
        self.label_title = Label(root, text="OS Kernal Simulation", font="Times 36 italic bold")
        self.label_title.pack()
        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()

        def process_manage():
            self.destroy_elements_main()
            p_m = ProcessManagement()

        self.btn_Process_m = Button(root, text="Process Management", command=process_manage, fg="White", bg="Red")
        self.btn_Process_m.configure(width=50, height=2)
        self.btn_Process_m.pack()

        def memory_manage():
            self.destroy_elements_main()
            mem_m = MemoryManagement()

        self.blank_label2 = Label(root, text='', height=1)
        self.blank_label2.pack()
        self.btn_memory_m = Button(root, text="Memory Management", command=memory_manage, fg="White", bg="Black")
        self.btn_memory_m.configure(width=50, height=2)
        self.btn_memory_m.pack()

        def io_manage():
            self.destroy_elements_main()
            io_m = IO_Management()

        self.blank_label3 = Label(root, text='', height=1)
        self.blank_label3.pack()
        self.btn_io_m = Button(root, text="I/O Management", command=io_manage, fg="White", bg="Blue")
        self.btn_io_m.configure(width=50, height=2)
        self.btn_io_m.pack()

        def synchronization_func():
            self.destroy_elements_main()
            sync = synchronization()

        self.blank_label4 = Label(root, text='', height=1)
        self.blank_label4.pack()
        self.btn_sync = Button(root, text="Synchronization", command=synchronization_func, fg="Black", bg="Green")
        self.btn_sync.configure(width=50, height=2)
        self.btn_sync.pack()

    def destroy_elements_main(self):
        self.label_title.destroy()
        self.blank_label.destroy()
        self.blank_label1.destroy()
        self.blank_label2.destroy()
        self.btn_Process_m.destroy()
        self.blank_label3.destroy()
        self.btn_memory_m.destroy()
        self.btn_io_m.destroy()
        self.btn_sync.destroy()
        self.blank_label4.destroy()
class ProcessManagement:
    def __init__(self):
        self.blank_label = Label(root, text='', height=1)
        self.blank_label.pack()
        self.label_title = Label(root, text="Process Management log", font="Times 24 bold")
        self.label_title.pack()
        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()

        def create_process():
            self.destroy_elements()
            cc = Create()
        self.create_process = Button(root, text="Create Process", command=create_process, fg="Black", bg="#E74C3C")
        self.create_process.configure(width=50, height=2)
        self.create_process.pack()
        self.blank_label2 = Label(root, text='', height=1)
        self.blank_label2.pack()

        def destroy_process():
            self.destroy_elements()
            dp = destroyProcess()
        self.destroy_process = Button(root, text="Destroy Process", command=destroy_process, fg="Black", bg="#EB984E")
        self.destroy_process.configure(width=50, height=2)
        self.destroy_process.pack()
        self.blank_label3 = Label(root, text='', height=1)
        self.blank_label3.pack()

        def suspend_process():
            self.destroy_elements()
            sp = suspendprocess()
        self.suspend_process = Button(root, text="Suspend Process", command=suspend_process, fg="Black", bg="#EB984E")
        self.suspend_process.configure(width=50, height=2)
        self.suspend_process.pack()
        self.blank_label4 = Label(root, text='', height=1)
        self.blank_label4.pack()

        def resume_process():
            self.destroy_elements()
            rp = resume_process_block()

        self.resume_process = Button(root, text="Resume Process", command=resume_process, fg="Black", bg="#EB984E")
        self.resume_process.configure(width=50, height=2)
        self.resume_process.pack()
        self.blank_label5 = Label(root, text='', height=1)
        self.blank_label5.pack()

        def change_process_priority():
            self.destroy_elements()
            cpp = process_priority_change()

        self.process_priority = Button(root, text="Change Process Priority", command=change_process_priority, fg="Black", bg="#EB984E")
        self.process_priority.configure(width=50, height=2)
        self.process_priority.pack()
        self.blank_label7 = Label(root, text='', height=1)
        self.blank_label7.pack()

        def dispatch_process():
            self.destroy_elements()
            das = dispatch_and_scheduling()

        self.dispatchPro = Button(root, text="Dispatch Process", command=dispatch_process, fg="Black", bg="#EB984E")
        self.dispatchPro.configure(width=50, height=2)
        self.dispatchPro.pack()
        self.blank_label8 = Label(root, text='', height=1)
        self.blank_label8.pack()

        def show_process():
            self.destroy_elements()
            sp = Show_Processes()

        self.ShowPro = Button(root, text="Show Processes", command=show_process, fg="Black", bg="#EB984E")
        self.ShowPro.configure(width=50, height=2)
        self.ShowPro.pack()

        def back_main():
            self.destroy_elements()
            mm = Main_Menu(root)

        self.blank_label6 = Label(root, text='', height=2)
        self.blank_label6.pack()
        self.back_to_main = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow', command=back_main)
        self.back_to_main.configure(bd=2)
        self.back_to_main.pack()

    def destroy_elements(self):
        self.label_title.destroy()
        self.blank_label1.destroy()
        self.blank_label.destroy()
        self.create_process.destroy()
        self.destroy_process.destroy()
        self.suspend_process.destroy()
        self.resume_process.destroy()
        self.process_priority.destroy()
        self.blank_label2.destroy()
        self.blank_label3.destroy()
        self.blank_label4.destroy()
        self.blank_label5.destroy()
        self.blank_label7.destroy()
        self.dispatchPro.destroy()
        self.ShowPro.destroy()
        self.blank_label8.destroy()
        self.back_to_main.destroy()
        self.blank_label6.destroy()
class MemoryManagement:
    def __init__(self):
        self.blank_label2 = Label(root, text='', height=1)
        self.blank_label2.pack()
        self.label_title = Label(root, text="Memory Management Block", font="Times 24 bold")
        self.label_title.pack()
        self.blank_label1 = Label(root, text='', height=2)
        self.blank_label1.pack()
        self.pagesize_l = Label(root, text='Enter Page Size: ')
        self.pagesize_l.pack()
        self.page_s_in = Entry(root, width=20)
        self.page_s_in.pack()
        self.blank_label = Label(root, text='', height=1)
        self.blank_label.pack()
        self.submit = Button(root, text="Submit", command=self.paging)
        self.submit.configure(width=50, height=2)
        self.submit.pack()
        self.blank_label3 = Label(root, text='', height=1)
        self.blank_label3.pack()
        self.lruimpl = Button(root, text="Implement LRU", command=self.LRU)
        self.lruimpl.configure(width=50, height=2)
        self.lruimpl.pack()
        self.blank_label4 = Label(root, text='', height=1)
        self.blank_label4.pack()
        self.back_to_main = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow',command=self.back_to_m)
        self.back_to_main.configure(bd=2)
        self.back_to_main.pack()
    def destroy_elements_for_paging(self):
        self.blank_label2.destroy()
        self.blank_label1.destroy()
        self.blank_label.destroy()
        self.pagesize_l.destroy()
        #self.label_title.destroy()
        self.page_s_in.destroy()
        self.blank_label3.destroy()
        self.lruimpl.destroy()
        self.submit.destroy()
        self.back_to_main.destroy()
        self.blank_label4.destroy()
    def back_to_m(self):
        self.blank_label2.destroy()
        self.blank_label1.destroy()
        self.blank_label.destroy()
        self.pagesize_l.destroy()
        self.label_title.destroy()
        self.page_s_in.destroy()
        self.blank_label3.destroy()
        self.lruimpl.destroy()
        self.submit.destroy()
        self.back_to_main.destroy()
        self.blank_label4.destroy()
        mm = Main_Menu(root)
    def paging(self):
        self.page_size = int(self.page_s_in.get())
        for key in pcbdata.keys():
            Process_keys.append(key)
        for key, value in pcbdata.items():
            memory_dict[key] = value[4]
        for value in memory_dict.values():
            memory_list.append(value)
        self.process_size = list(map(int, memory_list))
        for i in self.process_size:
            self.no_of_pages = i // self.page_size
            if i % self.page_size != 0:
                self.no_of_pages += 1
            pages.append(self.no_of_pages)
        for keys, i in zip(memory_dict.keys(), pages):
            for j in range(i):
                self.show_pages = Label(root, text='Process '+ keys+' :'+' Page: '+ str(j))
                self.show_pages.pack()
                show_p.append(self.show_pages)

        self.destroy_elements_for_paging()
        self.back_to_main = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow',command=self.back_to_ma)
        self.back_to_main.configure(bd=2)
        self.back_to_main.pack()

    def back_to_ma(self):
        for items in show_p:
            items.destroy()
        self.back_to_main.destroy()
        self.label_title.destroy()
        m = Main_Menu(root)
    def LRU(self):
        # self.framel = Label(root, text='Enter Frame Number: ')
        # self.framel.pack()
        self.framesize = Entry(root, width=20)
        self.process_string = [1, 2, 1, 3, 4, 2, 4, 3, 1, 2]
        q = deque()
        for i in range(len(self.process_string)):
            if len(q) == 4:
                q.popleft()
            q.append(self.process_string[i])
            self.listofq = str(list(q))
            self.lruprint = Label(root, text=self.listofq)
            self.lruprint.pack()
            lru_save.append(self.lruprint)
        self.destroy_elements_for_paging()
        self.back_to_main = Button(root, text="BACK", font='Times 16 bold', fg='Black', bg='Yellow',command=self.back_to_mai)
        self.back_to_main.configure(bd=2)
        self.back_to_main.pack()
    def back_to_mai(self):
        for items in lru_save:
            items.destroy()
        self.back_to_main.destroy()
        self.label_title.destroy()
        m = Main_Menu(root)
class IO_Management:
    def __init__(self):
        self.manage_label = Label(root, text="I/O Management Block")
        self.manage_label.pack()
class synchronization:
    def __init__(self):
        pass
class Create:
    def __init__(self):
        self.registers = ['ACC', 'MDR', 'MAR', 'CIR']
        self.selected_register = StringVar()
        self.selected_register.set('ACC')
        self.selected_value = StringVar()
        self.options = ['Ready']
        self.selected_value.set('Ready')
        self.blank_label5 = Label(root, text='', height=3)
        self.blank_label5.pack()
        self.idl = Label(root, text='Enter ID:')
        self.idl.pack()
        self.id = Entry(root, width=20)
        self.id.pack()
        self.blank_label = Label(root, text='', height=1)
        self.blank_label.pack()
class destroyProcess:
    def __init__(self):
        pass
class suspendprocess:
    def __init__(self):
        pass
class resume_process_block:
    def __init__(self):
        pass
class process_priority_change:
    def __init__(self):
        pass
class dispatch_and_scheduling:
    def __init__(self):
        pass
class Show_Processes:
    def __init__(self):
        pass

m_m = Main_Menu(root)
root.mainloop()