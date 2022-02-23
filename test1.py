import tkinter

def key_down(e):
    key_c = e.keycode
    Label1["text"] = "KeyCode . " + str(key_c)
    key_s = e.keysym
    Label2["text"] = "KeySym . " + str(key_s)

root = tkinter.Tk()
root.geometry("1000x600")
root.title("키 입력")

root.bind("<KeyPress>", key_down)

fnt = ("Segoe Script", 30)

Label1 = tkinter.Label(text = "KeyCode", font = fnt)
Label1.place(x = 0, y = 0)
Label2 = tkinter.Label(text = "KeySym", font = fnt)
Label2.place(x = 0, y = 80)

root.mainloop()