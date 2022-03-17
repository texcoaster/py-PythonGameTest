import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym
    print(key)
def key_up(e):
    global key
    key = ""

cx = 400
cy = 300
def main_proc():
    global cx, cy
    if key == "Up":
        cy = cy - 20
    if key == "Down":
        cy = cy + 20
    if key == "Left":
        cx = cx - 20
    if key == "Right":
        cx = cx + 20
    canvas.coords("MYCHR", cx, cy)
    root.after(100, main_proc)

root = tkinter.Tk()
root.title("Move Character")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width = 800, height = 600, bg = "lightgreen")
canvas.pack()
img = tkinter.PhotoImage(file = "image/mini.png")
canvas.create_image(cx, cy, image = img, tag = "MYCHR")

main_proc()

root.mainloop()