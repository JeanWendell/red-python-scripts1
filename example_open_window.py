from tkinter import *

window = Tk()

window.geometry("500x500")
window.iconbitmap("icon.ico")

image = Canvas(window, width="500", height="500")
image.place(relx=0, rely=0)

background = PhotoImage(file="photo.png")
image.create_image(300, 500, image = background)
window.mainloop()

