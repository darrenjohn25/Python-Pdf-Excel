from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
root = Tk()
root.title("Tkinter Eg")
def open():
    global root.filename
    root.filename = filedialog.askopenfilename()
    my_label = Label(root,text=root.filename).pack()   
    # my_image = ImageTk.PhotoImage(Image.open(root.filename))
    # my_image_label = Label(image=my_image).pack()
def convertxl():
    my_label = Label(root,text=root.filename).pack()
    df = tabula.read_pdf(root.filename, lattice = True)[1]
    df.columns = df.columns.str.replace('\r', ' ')
    data = df.dropna()
    data.to_excel('data.xlsx')
my_btn = Button(root,text="Open File",command=open).pack()
my_btn = Button(root,text="Convert to Excel",command=convertxl).pack()
root = mainloop()