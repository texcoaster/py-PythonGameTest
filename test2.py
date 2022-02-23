import tkinter
import datetime

def time_now():
    d = datetime.datetime.now()
    t = "{0}-{1}-{2} / {3}:{4}:{5}".format(d.year, d.month, d.day, d.hour, d.minute, d.second)
    label["text"] = t
    root.after(100, time_now)

root = tkinter.Tk()
root.geometry("700x100")
root.title("clock")

label = tkinter.Label(font = ("Times New Roman", 60))
label.pack()

time_now()

root.mainloop()