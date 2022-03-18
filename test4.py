from email.mime import image
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
    root.after(175, scroll_bg)

count = 0
def ChangeDog():
    global count
    count = (count + 1) % 4
    canvas.create_image(240, 200, image = img_dog[count], tag = "DOG")
    root.after(175, ChangeDog)

root = tkinter.Tk()
root.title("screen scroll")
canvas = tkinter.Canvas(width = 480, height = 300)
canvas.pack()
img_bg = tkinter.PhotoImage(file = "image/park.png")
img_dog = [tkinter.PhotoImage(file = "image/dog0.png"), tkinter.PhotoImage(file = "image/dog1.png"), tkinter.PhotoImage(file = "image/dog2.png"), tkinter.PhotoImage(file = "image/dog3.png")]

scroll_bg()
ChangeDog()

root.mainloop()