from tkinter import *
import datetime

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.master = master
        self.init_window()
    def init_window(self):
        self.pack(fill=BOTH, expand=1)
        self.count = 0
        self.text = Label(self, text="", bg="black")
        self.text.configure(foreground="white")
        self.text.pack()
        self.update_label()

    def client_exit(self):
        exit()

    def update_label(self):
        if self.count < 1000:
            left = int((datetime.date(2021, 7, 30) - datetime.date.today()).days)
            todayHour = int(datetime.datetime.now().strftime("%H"))
            todayMinute = int(datetime.datetime.now().strftime("%M"))
            todaySec = int(datetime.datetime.now().strftime("%S"))
            toShow =str(left) + " days " + str(23 - todayHour) + " hours " + str( 59 - todayMinute ) + " min " + str(59 - todaySec) + " sec"
            self.text.configure(text = toShow)
            self.text.after(1000, self.update_label)
root = Tk()
root.geometry("200x20+1200+1000")
app = Window(root)
root.wm_attributes('-type', 'splash')
root.attributes("-alpha", 0.6)
root.wm_attributes("-topmost", 1)
root.mainloop()
