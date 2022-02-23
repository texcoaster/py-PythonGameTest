import tkinter

x = 0
speed = 5
def scroll_bg():
    global x
    x = x + speed
    if x == 480:
        x = 0
    canvas.delete("BG")
    canvas.create_image(x - 240, 150, image = img_bg, tag = "BG")
    canvas.create_image(x + 240, 150, image = img_bg, tag = "BG")
    root.after(50, scroll_bg)

root = tkinter.Tk()
root.title("screen scroll")
canvas = tkinter.Canvas(width = 480, height = 300)
canvas.pack()
img_bg = tkinter.PhotoImage(file = "test/park.png")
scroll_bg()
root.mainloop()