import tkinter
root = tkinter.Tk()
root.title("미로표시")
canvas = tkinter.Canvas(width = 800, height = 560, bg = "gray")
canvas.pack()
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 1, 0, 1]
]

for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] == 1:
            canvas.create_rectangle(x * 80, y * 80, x * 80 + 80, y * 80 + 80, fill = "white")
root.mainloop()