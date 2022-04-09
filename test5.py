from email.mime import image
import tkinter

key = ""
def key_down(e):
    global key
    key = e.keysym
    print(key)
def key_up(e):
    global key
    key = ""

root = tkinter.Tk()
root.title("미로표시")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
canvas = tkinter.Canvas(width = 800, height = 560, bg = "gray")
canvas.pack()

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

my = 1
mx = 1

def main_proc():
    global my, mx
    if key == "Up" and maze[my-1][mx] == 0:
        my = my - 1
    if key == "Down" and maze[my+1][mx] == 0:
        my = my + 1
    if key == "Left" and maze[my][mx-1] == 0:
        mx = mx - 1
    if key == "Right" and maze[my][mx+1] == 0:
        mx = mx + 1

    if maze[my][mx] == 0:
        maze[my][mx] = 2
    if maze[my][mx] == 2:
        canvas.create_rectangle(mx * 80, my * 80, mx * 80 + 80, my * 80 + 80, fill = "pink")
    
    # canvas.coords("MYCHR", mx * 80 + 40, my * 80 + 40)
    canvas.delete("MYCHR")
    canvas.create_image(mx * 80 + 40, my * 80 + 40, image = img, tag = "MYCHR")
    root.after(100, main_proc)

img = tkinter.PhotoImage(file = "image/mini_2.png")

for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80, fill = "white")

canvas.create_image(mx * 80 + 40, my * 80 + 40, image = img, tag = "MYCHR")

main_proc()

root.mainloop()