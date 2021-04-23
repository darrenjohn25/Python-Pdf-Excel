from tkinter import *
import tabula
from PIL import Image, ImageTk
from tkinter import filedialog
root = Tk()
canvas= Canvas(root,width=500,height=300)
canvas.pack()
root.title("Python Pdf-Excel")
logo = ImageTk.PhotoImage(Image.open(r('Urlof anyimage')
canvas.create_image(30,30,anchor=NW,image=logo)
def open():
    global root.filename
    root.filename = filedialog.askopenfilename()
    my_label = Label(root,text=root.filename).pack()   
def convertxl():
    my_label = Label(root,text=root.filename).pack()
    destination=filedialog.asksaveasfilename(defaultextension=".xlsx")                                 
    df = tabula.read_pdf(root.filename, lattice = True)[1]
    df.columns = df.columns.str.replace('\r', ' ')
    data = df.dropna()
    data.to_excel(destination)
my_btn = Button(root,text="Open File",command=open).pack(side=LEFT)
mybtn = Button(root,text="Convert to Excel",command=convertxl).pack(side=LEFT)
root = mainloop()
