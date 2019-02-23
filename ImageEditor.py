from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image,ImageFilter,ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
width = 1000#w.winfo_screenwidth()
height = 700#w.winfo_screenheight()
m=1
n=1
main=Tk()
main.title("Image Editor")
main.configure(background='#17202A')#https://htmlcolorcodes.com/color-chart/    for more colors
main.geometry('%sx%s' % (width*m,height*n))
main.resizable(0,0)
"""width = main.winfo_screenwidth()
height = main.winfo_screenheight()
def resize(event):
    global width,height,m,n
    m=event.width/width
    n=event.height/height
    width=event.width
    height=event.height
    print(frame1['width']*m)
    frame1['width']=frame1['width']*m
    frame1['height']=frame1['height']*n
    print("hi"+str(m)+"bye"+str(n))
    print(frame1['width'])
main.bind("<Configure>", resize)"""
"""************************************************************  frame 1 load image file  ***********************************************************"""
frame1=Frame(main,width=200*m,height=95*n,bg='#003333')
frame1.place(x=4*m,y=4*n)
canvas1=Canvas(frame1,width=200,height=95,bg="#003333",highlightthickness=0)
canvas1.place(x=0,y=0)
def load():
    global inputpath,render

    canvas1['bg'] = "#0B5345"
    openImage.config(bg="#0B5345", activeforeground="#0B5345", activebackground="#0B5345")
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    inputpath = filename
    canvas1['bg'] = "#003333"
    openImage.config(bg="#003333", activeforeground="#003333", activebackground="#003333")
    try:
        load = Image.open(inputpath)
        load1=load
        size = 400, 400
        outfile = "C:/Users/HARIPRASAD/Desktop/pythonMiniProject/img.thumbnail"
        load1.thumbnail(size, Image.ANTIALIAS)
        load1.save(outfile, "JPEG")
        render = ImageTk.PhotoImage(load1)
        image1['image'] = render
        image1.place(x=180, y=170)
    except AttributeError:
        image1['fg'] = "#EB984E"
        image1['text'] = "You didn't select any image\nTry again!!"
        image1['image'] = ""
        image1.place(x=200, y=200)
openImage=Button(frame1,text="Open",command=load,bg="#003333",fg="#A2D9CE",activeforeground="#003333",
activebackground="#003333",font=("Helvetica", 12),bd=0)
openImage.place(x=43,y=30)
"""************************************************************  frame 2 edit Image  ***********************************************************"""
frame2=Frame(main,width=200*m,height=497*n,bg='#17202A')
frame2.place(x=4*m,y=102*n)
#crop
canvasc=Canvas(frame2,width=200,height=50,bg="#003333",highlightthickness=0)
canvasc.place(x=0,y=0)
def crop():
    global inputpath
    canvasc['bg'] = "#0B5345"
    trace = 0
    top = Toplevel()
    top.title("Crop Image here...")
    top.geometry("500x500")
    load=Image.open(inputpath)
    load1 = load
    size = 400,600
    outfile = "C:/Users/HARIPRASAD/Desktop/pythonMiniProject/crop.thumbnail"
    load1.thumbnail(size, Image.ANTIALIAS)
    load1.save(outfile, "PNG")
    render = ImageTk.PhotoImage(load1)
    class CanvasEventsDemo:
        x1=0
        y1=0
        x2=0
        y2=0
        def __init__(self, w):
            self.root=w
            canvas = Canvas(self.root,width=600, height=400)
            canvas.place(x=0,y=0)

            canvas.create_image(50,50, image=render, anchor=NW)

            canvas.bind('<ButtonPress-1>', self.onStart)
            canvas.bind('<B1-Motion>', self.onGrow)
            canvas.bind('<Double-1>', self.onClear)
            canvas.bind('<ButtonPress-3>', self.onMove)
            self.canvas = canvas
            self.drawn = None
            self.kinds = [canvas.create_rectangle]

        def onStart(self, event):
            self.shape = self.kinds[0]
            self.kinds = self.kinds[1:] + self.kinds[:1]
            self.start = event
            self.drawn = None

        def onGrow(self, event):
            global x1,y1,x2,y2
            canvas = event.widget
            if self.drawn: canvas.delete(self.drawn)
            objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
            self.x1, self.y1, self.x2, self.y2 = self.start.x, self.start.y, event.x, event.y
            if trace: print(objectId)
            self.drawn = objectId

        def onClear(self, event):
            event.widget.delete('all')

        def onMove(self, event):
            if self.drawn:
                if trace: print(self.drawn)
                canvas = event.widget
                diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
                canvas.move(self.drawn, diffX, diffY)
                self.start = event
    a=CanvasEventsDemo(top)
    def _delete_window():
        print("delete_window")
        try:
            top.destroy()
        except:
            pass

    def _destroy(event):
        global x1,x2,y1,y2,render3,inputpath
        print("i am distroyed")
        print(a.x1, a.y1, a.x2, a.y2)
        #load = Image.open(inputpath)
        if(a.x1!=0 or a.y1!=0 or a.x2!=0 or a.y2!=0):
            img2=load1.crop((a.x1-50, a.y1-50, a.x2-50, a.y2-50))
            img2.save("croped.jpg")
            inputpath="croped.jpg"
            outfile = "C:/Users/HARIPRASAD/Desktop/pythonMiniProject/crop.thumbnail"

            img2.thumbnail(size, Image.ANTIALIAS)
            img2.save(outfile, "JPEG")
            render3 = ImageTk.PhotoImage(img2)
            image1['image'] = render3
            image1.place(relx=0.25, rely=0.25, anchor=CENTER)
            canvasc['bg'] = "#003333"
        else:
            canvasc['bg'] = "#003333"
            pass

    top.protocol("WM_DELETE_WINDOW", _delete_window)
    top.bind("<Destroy>", _destroy)

    button = Button(top, text="Crop", command=top.destroy)
    button.place(x=410,y=410)
    top.mainloop()
b=Button(canvasc,text="Crop",command=crop,bg="#003333",fg="#A2D9CE",activeforeground="#003333",activebackground="#003333",font=("Helvetica", 12),bd=0)
b.place(relx=0.33, rely=0.5, anchor=CENTER)

#Rotate
canvasr=Canvas(frame2,width=200,height=100,bg="#003333",highlightthickness=0)
canvasr.place(x=0,y=54)
rvar=IntVar()
def rotate():
    global render4,inputpath
    theta=rvar.get()
    size=400,400
    load=Image.open(inputpath)
    load = load.rotate(theta)
    outfile = "C:/Users/HARIPRASAD/Desktop/pythonMiniProject/rotate.thumbnail"
    load.thumbnail(size, Image.ANTIALIAS)
    load.save(outfile, "JPEG")
    render4= ImageTk.PhotoImage(load)
    image1.config(image=render4)
    image1.place(relx=0.25, rely=0.25, anchor=CENTER)
    load.save("rotate.jpg")
    inputpath="rotate.jpg"
r1=Radiobutton(canvasr,text="180",variable=rvar,value=180,bg="#003333",fg="#996633",activeforeground="#003333",activebackground="#003333",font=("Helvetica", 12),bd=0)
r2=Radiobutton(canvasr,text="90",variable=rvar,value=90,bg="#003333",fg="#996633",activeforeground="#003333",activebackground="#003333",font=("Helvetica", 12),bd=0)
r3=Radiobutton(canvasr,text="60",variable=rvar,value=60,bg="#003333",fg="#996633",activeforeground="#003333",activebackground="#003333",font=("Helvetica", 12),bd=0)
r1.place(x=10,y=0)
r2.place(x=70,y=0)
r3.place(x=120,y=0)
rotate180=Button(canvasr,text="Rotate",command=rotate,bg="#003333",fg="#A2D9CE",activeforeground="#003333",activebackground="#003333",font=("Helvetica", 12),bd=0)
rotate180.place(x=40,y=30)

#Enhancement
canvasE=Canvas(frame2,width=200,height=220,bg="#003333",highlightthickness=0)
canvasE.place(x=0,y=158)
menub=Menubutton(canvasE,text="Enhance",bg="#003333",fg="#A2D9CE",activeforeground="#003333",activebackground="#003333",font=("Helvetica", 12),bd=0)
menub.menu  =  Menu ( menub, tearoff = 0 )
menub["menu"]  =  menub.menu
Enoption = IntVar()
def EnhanceFun():
    global inputpath,render4
    print(inputpath)
    im1 = Image.open(inputpath)
    im1.save("Enhance.jpg",dpi=(300,300))
    im=Image.open("Enhance.jpg")
    if(Enoption.get()==1):
        im= im.filter(ImageFilter.DETAIL)
    elif(Enoption.get()==2):
        im=im.filter(ImageFilter.SHARPEN)
    elif(Enoption.get()==3):
        im = im.filter(ImageFilter.SMOOTH)
    elif(Enoption.get() == 4):
        im = im.filter(ImageFilter.SMOOTH_MORE)
    elif(Enoption.get() == 5):
        im = im.filter(ImageFilter.EDGE_ENHANCE)
    elif (Enoption.get() == 6):
        im = im.filter(ImageFilter.BLUR)
    elif(Enoption.get() == 7):
        im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    elif(Enoption.get()==8):
        im = im.filter(ImageFilter.EMBOSS)
    elif(Enoption.get() == 9):
        im = im.filter(ImageFilter.FIND_EDGES)
    elif(Enoption.get()==10):
        im = im.filter(ImageFilter.CONTOUR)
    im.save("Enhance.jpg")
    inputpath = "Enhance.jpg"
    outfile = "C:/Users/HARIPRASAD/Desktop/pythonMiniProject/Enhance.thumbnail"
    size=400,400
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile, "PNG")
    render4 = ImageTk.PhotoImage(im)
    image1['image'] = render4
    image1.place(relx=0.25, rely=0.25, anchor=CENTER)


menub.menu.add_checkbutton ( label="DETAIL",
                          variable=Enoption,command=EnhanceFun,onvalue=1,offvalue=0)
menub.menu.add_checkbutton ( label="SHARPEN",
                          variable=Enoption,command=EnhanceFun,onvalue=2,offvalue=0)
menub.menu.add_checkbutton ( label="SMOOTH",
                          variable=Enoption,command=EnhanceFun,onvalue=3,offvalue=0)
menub.menu.add_checkbutton ( label="SMOOTH_MORE",
                          variable=Enoption,command=EnhanceFun,onvalue=4,offvalue=0)
menub.menu.add_checkbutton ( label="EDGE_ENHANCE",
                          variable=Enoption,command=EnhanceFun,onvalue=5,offvalue=0)
menub.menu.add_checkbutton ( label="BLUR",
                          variable=Enoption,command=EnhanceFun,onvalue=6,offvalue=0)
menub.menu.add_checkbutton ( label="EDGE_ENHANCE_MORE",
                          variable=Enoption,command=EnhanceFun,onvalue=7,offvalue=0)
menub.menu.add_checkbutton ( label="EMBOSS",
                          variable=Enoption,command=EnhanceFun,onvalue=8,offvalue=0)
menub.menu.add_checkbutton ( label="FIND_EDGES",
                          variable=Enoption,command=EnhanceFun,onvalue=9,offvalue=0)
menub.menu.add_checkbutton ( label="CONTOUR",
                          variable=Enoption,command=EnhanceFun,onvalue=10,offvalue=0)

menub.place(x=40,y=4)

#ColorFilter
canvasF=Canvas(frame2,width=200,height=118,bg="#003333",highlightthickness=0)
canvasF.place(x=0,y=382)
def open_image(path):
  newImage = Image.open(path)
  return newImage
def save_image(image, path):
  image.save(path, 'png')
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image
def get_pixel(image, i, j):
  width, height = image.size
  if i > width or j > height:
    return None
  pixel = image.getpixel((i, j))
  return pixel
def convert_grayscale(image,r,g,b):
  width, height = image.size
  new = create_image(width, height)
  pixels = new.load()
  for i in range(width):
    for j in range(height):
      pixel = get_pixel(image, i, j)
      red = pixel[0]
      green = pixel[1]
      blue = pixel[2]
      level=(red * r) + (green * g) + (blue * b)
      pixels[i, j] = (int(level), int(level), int(level))
  return new

def convert_primary(image):
  width, height = image.size
  new = create_image(width, height)
  pixels = new.load()
  for i in range(width):
    for j in range(height):
      pixel = get_pixel(image, i, j)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]
      if red > 127:
        red = 255
      else:
        red = 0
      if green > 127:
        green = 255
      else:
        green = 0
      if blue > 127:
        blue = 255
      else:
        blue = 0
      pixels[i, j] = (int(red), int(green), int(blue))
  return new

def filterFun(self):
    global inputpath,render5,optn,option
    original = open_image(inputpath)
    original.save("Enhance.jpg")
    original=open_image("Enhance.jpg")
    if(optn.get()=="Original"):
        im=original
    elif (optn.get() == "Gray1"):
        im = convert_grayscale(original, 0.350, 0.350, 0.350)
    elif (optn.get() == "Gray2"):
        im = convert_grayscale(original, 0.700, 0.100, 0.850)
    elif (optn.get() == "Gray3"):
        im= convert_grayscale(original, 0.100, 0.100, 0.850)
    elif (optn.get() == "Primary"):
        im = convert_primary(original)
    elif (optn.get() == "Gray4"):
        im = convert_grayscale(original, 1.0, 1.0, 0.850)
    else:
        im=original

    im.save("filter.jpg")
    inputpath = "filter.jpg"
    outfile = "C:/Users/HARIPRASAD/Desktop/pythonMiniProject/filter.thumbnail"
    size = 400, 400
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile, "PNG")
    render5 = ImageTk.PhotoImage(im)
    image1['image'] = render5
    image1.place(relx=0.25, rely=0.25, anchor=CENTER)
    opb.config(state=NORMAL)
    option.place(x=400,y=500)


   # blackAndWhiteImage = original.convert("1")
    #blackAndWhiteImage.save("3.png")
def setOptionMenu():
    global optn,option
    opb.config(state=DISABLED)
    optn = StringVar(frame2)
    optn.set('GreyFiters')
    choices = ['Original', 'Gray1', 'Gray2', 'Gray3', 'Primary', 'Gray4']
    option = OptionMenu(canvasF, optn, *choices, command=filterFun)

    option['menu'].config(bg='#003333')
    option['menu'].config(fg="#996633")
    option['menu'].config(activeforeground="#003333")
    option['menu'].config(activebackground="#003333")
    option['menu'].config(font=("Helvetica", 12))
    option['menu'].config(bd=0)
    option.place(x=2, y=2)
opb=Button(canvasF,text="GrayFliters",command=setOptionMenu,bg="#003333",fg="#1ABC9C",activeforeground="#003333",activebackground="#003333",font=("Helvetica", 12),bd=0)
opb.place(x=35,y=45)
"""************************************************************   frame Image open file  ***********************************************************"""
frameImage=Frame(main,width=789*m,height=692*n)
frameImage.place(x=208*m,y=4*n)
canvas2=Canvas(frameImage,width=789,height=692,bg="#1C2833",highlightthickness=0)
canvas2.place(x=0,y=0)

#viewWindow.create_image(0, 0, anchor=CENTER, image=imageFile, tags="bg_img")
image1 = Label(frameImage, text="No image!!",font=("Helvetica", 12),fg="#99A3A4",bg="#1C2833")
image1.place(x=250,y=250)

#zoom

def zoom(self):
    global inputpath,render2
    try:
        print(var.get())
        if(var.get()==-50):
            size=50,50
        elif(var.get() ==-40):
             size=100,100
        elif(var.get() ==-30):
            size=200,200
        elif(var.get() ==-20):
            size=250,250
        elif(var.get() == -10):
            size=300,300
        elif (var.get() == 0):
            size = 400, 400
        elif (var.get() == 10):
            size = 450, 450
        elif (var.get() == 20):
            size = 500, 500
        elif (var.get() == 30):
            size = 550, 550
        elif (var.get() == 40):
            size = 600, 600
        elif (var.get() == 50):
            size = 650, 650
        load1 = Image.open(inputpath)
        outfile = "C:/Users/HARIPRASAD/Desktop/pythonMiniProject/Zoom.thumbnail"
        load1.thumbnail(size, Image.ANTIALIAS)
        load1.save(outfile, "JPEG")
        render2 = ImageTk.PhotoImage(load1)
        image1["image"]=render2
        image1.place(relx=0.25, rely=0.25, anchor=CENTER)
        #place(x=x1, y=y1)
    except:
        print("not possible to zoom")

def zoomIn():
    try:
        x=int(scale.get())+10
        scale.set(x)
        zoom()
    except TypeError:
        pass
def zoomOut():
    try:
        x=int(scale.get())-10
        scale.set(x)
        zoom()
    except TypeError:
        pass
var = IntVar()
#zoomInImage=PhotoImage("C:/Users/HARIPRASAD/Desktop/pythonMiniProject/plus.png")
#zoomOutImage=PhotoImage("C:/Users/HARIPRASAD/Desktop/pythonMiniProject/minus.png")
zoomInB=Button(frameImage,text="+",command=zoomIn,bg="#336666")
scale = Scale( frameImage, variable = var,from_=50,to=-50,resolution=10,command=zoom,troughcolor="#0B5345",bd=0,showvalue=0)
zoomOutB=Button(frameImage,text="-",command=zoomOut,bg="#336666")
zoomInB.place(x=769,y=200)
scale.place(x=768,y=228)
zoomOutB.place(x=769,y=335)


"""************************************************************  frame 3 save file     ***********************************************************"""
frame3=Frame(main,width=200*m,height=95*n,bg='#003333')
frame3.place(x=4*m,y=602*n)
def save():
    global inputpath
    im=Image.open(inputpath)
    filename=filedialog.askdirectory()
    path2=filename+"/edited.png"
    im.save(path2)
saveImage = Button(frame3, text="Destination", command=save,bg="#003333",fg="#1ABC9C",activeforeground="#003333",activebackground="#003333",font=("Helvetica", 12),bd=0)
saveImage.place(x=40, y=50)


"""************************************************************       End               ***********************************************************"""
main.mainloop()
