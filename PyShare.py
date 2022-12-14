import time
from tkinter import *
from tkinter import ttk
from PIL import Image 
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import socket
import os
import subprocess
dirName='Received'
if not os.path.exists(dirName):
        os.mkdir(dirName)
        folders = ['songs', 'videos', 'documents','photos']
        for folder in folders:
                os.mkdir(os.path.join(dirName, folder))
else:    
        pass


#*********************************************************************************************************************************
root = Tk()
root.geometry('900x500')
root.iconbitmap('icons/icon.ico')
root.title("PyShare")
imagelist = []
for i in range(1,41):
        a="icons/"+str(i)+".png"
        imagelist+=[a]

# extract width and height info
photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()
canvas = Canvas(width=width, height=height)
canvas.pack()

# create a list of image objects
giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)

# loop through the gif image objects for a while
for k in range(0, 1):
    for gif in giflist:
        canvas.delete(ALL)
        canvas.create_image(0,0,anchor=NW, image=gif)
        canvas.update()
        time.sleep(0.1)
time.sleep(2)
root.destroy()
root.mainloop()




#**********************************************************************************************************************************

class mainwindow:

    def __init__(self, master):
        self.master = master
        self.master.iconbitmap('icons/icon.ico')
        self.master.title("PyShare")
        self.master.geometry("800x700")
        self.master.configure(background = "azure2");
        self.k = Label(self.master ,text = "PyShare",foreground="cadetBlue",font=('Helvetica',30, 'bold'),background = "azure2").grid(row = 2,column =2 ,padx=5,pady=5)
        self.width = 120
        self.height = 120
        self.img = Image.open("icons/icon.jpg")
        self.img = self.img.resize((self.width,self.height), Image.ANTIALIAS)
        self.photoImg =  ImageTk.PhotoImage(self.img)
        self.k1 = Label(self.master ,background = "white",text = "PyShare",image=self.photoImg)
        self.k1.grid(row = 0,column = 2,padx=5,pady=5)
        self.width = 120
        self.height = 120
        self.img1 = Image.open("icons/send.png")
        self.img1 = self.img1.resize((self.width,self.height), Image.ANTIALIAS)
        self.photoImg1 =  ImageTk.PhotoImage(self.img1)
        self.b=Button(self.master,width=500,height=100,background = "white",image=self.photoImg1,command=self.send)
        self.b.grid(row = 8,column = 2,padx=150,pady=5)
        self.width = 120
        self.height = 120
        self.img2 = Image.open("icons/rcv.png")
        self.img2 = self.img2.resize((self.width,self.height), Image.ANTIALIAS)
        self.photoImg2 =  ImageTk.PhotoImage(self.img2)
        self.b1=Button(self.master,width=500,height=100,background = "white",image=self.photoImg2,command=self.recieve)
        self.b1.grid(row = 10,column = 2,padx=5,pady=5)
        self.width = 120
        self.height = 120
        self.img3 = Image.open("icons/local.png")
        self.img3 =self.img3.resize((self.width,self.height), Image.ANTIALIAS)
        self.photoImg3 =  ImageTk.PhotoImage(self.img3)
        self.b2=Button(self.master,width=500,height=100,background = "white",image=self.photoImg3,command=self.local)
        self.b2.grid(row = 11,column = 2,padx=5,pady=5)

        self.ct1= Label(self.master ,background = "azure2",foreground="thistle4",font=('Helvetica',15, 'bold'))
        self.ct1.grid(row = 3,column = 2,padx=5,pady=5)
        self.name()

        self.width = 50
        self.height = 50
        self.img5 = Image.open("icons/exit.jpg")
        self.img5 = self.img5.resize((self.width,self.height), Image.ANTIALIAS)
        self.photoImg5 =  ImageTk.PhotoImage(self.img5)
        self.b4=Button(self.master,width=50,height=50,background = "white",image=self.photoImg5,command=self.master.destroy)
        self.b4.grid(row = 12,column = 2,padx=5,pady=50)
      

    def recieve(self):
        self.master.withdraw()
        self.r = Toplevel(self.master)
        br= Recieve(self.r)

    def send(self):
        self.master.withdraw()
        self.s = Toplevel(self.master)
        bs = Send(self.s)

    def local(self):
        self.master.withdraw()
        self.l=Toplevel(self.master)
        bl=Local(self.l)
        
    def name(self):
        results = subprocess.check_output(["netsh", "wlan", "show", "network"])
        results = results.decode("ascii")
        results = results.replace("\r","")
        ls = results.split("\n")
        ls = ls[4]
        a=(str(ls))
        r=(str(a[9:]))
        self.ct1["text"]="CONNECTED TO: "+r
        

class Send :
    def __init__(self, master):
        self.master=master
        self.master.iconbitmap('icons/icon.ico')
        self.master.title("Sender")
        self.master.geometry("800x700")
        self.master.configure(background = "azure2");
        self.k = Label(self.master ,text = "PyShare",foreground="cadetBlue",font=('Helvetica',30, 'bold'),background = "azure2").grid(row = 2,column =2 ,padx=5,pady=5)

        self.width = 120
        self.height = 120
        self.img = Image.open("icons/icon.jpg")
        self.img = self.img.resize((self.width,self.height), Image.ANTIALIAS)
        self.photoImg =  ImageTk.PhotoImage(self.img)


        self.k1 = Label(self.master ,background = "white",text = "PyShare",image=self.photoImg)
        self.k1.grid(row = 0,column = 2,padx=350,pady=5)

        self.dip = Label(self.master ,text = "IP Adress: ",foreground="black",font=('Helvetica',15, 'bold'),background = "azure2").grid(row = 3,column =2 ,padx=5,pady=5)

        self.b=Button(self.master,width=10,height=1,background = "white",text="Show IP",command=self.getip)
        self.b.grid(row = 6,column = 2,padx=150,pady=5)

        self.ipa = Label(self.master ,background = "azure2",foreground="red4",font=('Helvetica',25, 'bold'))
        self.ipa.grid(row = 7,column = 2,padx=5,pady=5)

        self.b=Button(self.master,width=14,height=2,background = "white",text="Select file",command=self.sendinit)
        self.b.grid(row = 8,column = 2,padx=150,pady=5)

        self.wt1 = Label(self.master ,background = "azure2",foreground="black",text="File Name")
        self.wt1.grid(row = 9,column = 2,padx=5,pady=5)

        self.wt2 = Label(self.master ,background = "azure2",foreground="SpringGreen4")
        self.wt2.grid(row = 10,column = 2,padx=5,pady=5)

        self.wt3 = Label(self.master ,background = "azure2",foreground="black",text="File Path")
        self.wt3.grid(row = 11,column = 2,padx=5,pady=5)

        self.wt4 = Label(self.master ,background = "azure2",foreground="SpringGreen4",)
        self.wt4.grid(row = 12,column = 2,padx=5,pady=5)

        self.dn1= Label(self.master ,background = "azure2",foreground="Green2",font=('Helvetica',15, 'bold'))
        self.dn1.grid(row = 13,column = 2,padx=5,pady=5)

        self.b1=Button(self.master,width=10,height=1,background = "white",text="BACK",command=self.BACK)
        self.b1.grid(row = 14,column = 2,padx=150,pady=5)
        
    def getip(self):
        c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        c.connect(("8.8.8.8", 80))
        self.addr=(c.getsockname()[0])
        self.ipa["text"]=str(self.addr)
        c.close()
            

    def sendinit(self):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.bind(('',9999))
        s.listen(1)
        c,self.addr=s.accept()
        Tk().withdraw()
        filename = askopenfilename()
        file_info = os.stat(filename)
        f=open(filename,'br')
        name = (os.path.basename(filename))
        self.wt2["text"]=name
        self.wt4["text"]=filename
        c.send(name.encode())
        f.seek(0)
        for i in f:
                c.send(i)
        self.dn1["text"]="File Transfer Complete !!"
        s.close()
        
    def BACK(self):
        self.master.withdraw()
        self.b = Toplevel(self.master)
        b= mainwindow(self.b)               
        
class Recieve:

    def __init__(self, master):
        self.master=master
        self.master.iconbitmap('icons/icon.ico')
        self.master.title("Reciever")
        self.master.geometry("800x700")
        self.master.configure(background = "azure2");
        self.k = Label(self.master ,text = "PyShare",foreground="cadetBlue",font=('Helvetica',30, 'bold'),background = "azure2").grid(row = 2,column =2 ,padx=5,pady=5)

        self.width = 120
        self.height = 120
        self.img = Image.open("icons/icon.jpg")
        self.img = self.img.resize((self.width,self.height), Image.ANTIALIAS)
        self.photoImg =  ImageTk.PhotoImage(self.img)

        self.k1 = Label(self.master ,background = "white",text = "PyShare",image=self.photoImg)
        self.k1.grid(row = 0,column = 2,padx=350,pady=5)


        self.k2=Label(self.master ,text = "Enter IP",foreground="black",background = "azure2",font=('Helvetica',15, 'bold'))
        self.k2.grid(row = 4,column =2 ,padx=5,pady=5)

        self.a1 = Entry(self.master,width=30)
        self.a1.grid(row = 5,column = 2,padx=5,pady=5)


        self.b=Button(self.master,width=20,height=1,background = "white",text="Start Recieving",command=self.recieveinit)
        self.b.grid(row = 6,column = 2,padx=150,pady=5)

        self.p1 = Label(self.master ,background = "azure2",foreground="black",text = "File Name")
        self.p1.grid(row = 7,column = 2,padx=5,pady=5)

        self.fp = Label(self.master ,background = "azure2",foreground="SpringGreen4")
        self.fp.grid(row = 8,column = 2,padx=5,pady=5)

        self.fn =Label(self.master ,background = "azure2",foreground="Green2",font=('Helvetica',15, 'bold'))
        self.fn.grid(row = 9,column = 2,padx=5,pady=5)

        self.b1=Button(self.master,width=10,height=1,background = "white",text="Back",command=self.BACK)
        self.b1.grid(row = 11,column = 2,padx=150,pady=5)


    def recieveinit(self):
        self.addr1=self.a1.get()
        s = socket.socket()
        s.connect((self.addr1, 9999))
        fname = s.recv(10000)
        self.fp["text"]=(fname.decode())
        if os.path.splitext(fname.decode())[1] == ".mp3":
                f=open('Received/songs/'+fname.decode(),'bw')
        elif os.path.splitext(fname.decode())[1] == ".mp4":
                f=open('Received/videos/'+fname.decode(),'bw')
        elif os.path.splitext(fname.decode())[1] == ".jpg":
                f=open('Received/photos/'+fname.decode(),'bw')
        elif os.path.splitext(fname.decode())[1] == ".png":
                f=open('Received/photos/'+fname.decode(),'bw')
        else:
                f=open('Received/documents/'+fname.decode(),'bw')
        x=s.recv(100000)
        while(x):
                f.write(x)
                x = s.recv(100000)
        self.fn["text"]="File Transfer Complete !!"
        f.close()

        
    def BACK(self):
        self.master.withdraw()
        self.b = Toplevel(self.master)
        b= mainwindow(self.b)

class Local:
        def __init__(self, master):
            self.master=master
            self.master.iconbitmap('icons/icon.ico')
            self.master.title("Local Files")
            self.master.geometry("800x700")
            self.master.configure(background = "azure2")
            self.k = Label(self.master ,text = "PyShare",foreground="cadetBlue",font=('Helvetica',30, 'bold'),background = "azure2").grid(row = 2,column =2 ,padx=5,pady=5)
            self.width = 120
            self.height = 120
            self.img = Image.open("icons/icon.jpg")
            self.img = self.img.resize((self.width,self.height), Image.ANTIALIAS)
            self.photoImg =  ImageTk.PhotoImage(self.img)


            self.k1 = Label(self.master ,background = "white",text = "PyShare",image=self.photoImg)
            self.k1.grid(row = 0,column = 2,padx=5,pady=5)

            self.width = 120
            self.height = 120
            self.img1 = Image.open("icons/photos.png")
            self.img1 = self.img1.resize((self.width,self.height), Image.ANTIALIAS)
            self.photoImg1 =  ImageTk.PhotoImage(self.img1)

            self.b=Button(self.master,width=500,height=100,background = "white",image=self.photoImg1,command=self.photo)
            self.b.grid(row = 8,column = 2,padx=150,pady=5)

            self.width = 120
            self.height = 120
            self.img2 = Image.open("icons/songs.png")
            self.img2 = self.img2.resize((self.width,self.height), Image.ANTIALIAS)
            self.photoImg2 =  ImageTk.PhotoImage(self.img2)


            self.b1=Button(self.master,width=500,height=100,background = "white",image=self.photoImg2,command=self.songs)
            self.b1.grid(row = 10,column = 2,padx=5,pady=5)

            self.width = 120
            self.height = 120
            self.img3 = Image.open("icons/videos.png")
            self.img3 = self.img3.resize((self.width,self.height), Image.ANTIALIAS)
            self.photoImg3 =  ImageTk.PhotoImage(self.img3)


            self.b2=Button(self.master,width=500,height=100,background = "white",image=self.photoImg3,command=self.vid)
            self.b2.grid(row = 11,column = 2,padx=5,pady=5)

            self.width = 120
            self.height = 120
            self.img4 = Image.open("icons/documents.png")
            self.img4 = self.img4.resize((self.width,self.height), Image.ANTIALIAS)
            self.photoImg4 =  ImageTk.PhotoImage(self.img4)


            self.b2=Button(self.master,text="Songs",width=500,height=100,background = "white",image=self.photoImg4,command=self.docs)
            self.b2.grid(row = 12,column = 2,padx=5,pady=5)

            self.b3=Button(self.master,width=10,height=1,background = "white",text="BACK",command=self.BACK)
            self.b3.grid(row = 14,column = 2,padx=150,pady=5)

        def BACK(self):
                self.master.withdraw()
                self.b = Toplevel(self.master)
                b= mainwindow(self.b)
        def songs(self):
            root = Tk()
            root.geometry("800x700")
            l = Listbox(root, height=800,width=600)
            l.grid(column=0, row=0)
            s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
            s.grid(column=1, row=0)
            l['yscrollcommand'] = s.set
            ttk.Sizegrip().grid(column=1, row=1)
            root.grid_columnconfigure(0, weight=1)
            root.grid_rowconfigure(0, weight=1)
            for filename in os.listdir("./Received/songs/"):
                l.insert(END, filename)
            root.mainloop()

        def docs(self):
            root = Tk()
            root.geometry("800x700")
            l = Listbox(root, height=800,width=600)
            l.grid(column=0, row=0)
            s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
            s.grid(column=1, row=0)
            l['yscrollcommand'] = s.set
            ttk.Sizegrip().grid(column=1, row=1)
            root.grid_columnconfigure(0, weight=1)
            root.grid_rowconfigure(0, weight=1)
            for filename in os.listdir("./Received/documents/"):
                l.insert(END, filename)
            root.mainloop()

        def vid(self):
            root = Tk()
            root.geometry("800x700")
            l = Listbox(root, height=800,width=600)
            l.grid(column=0, row=0)
            s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
            s.grid(column=1, row=0)
            l['yscrollcommand'] = s.set
            ttk.Sizegrip().grid(column=1, row=1)
            root.grid_columnconfigure(0, weight=1)
            root.grid_rowconfigure(0, weight=1)
            for filename in os.listdir("./Received/videos/"):
                l.insert(END, filename)
            root.mainloop()


        def photo(self):
            root = Tk()
            root.geometry("800x700")
            l = Listbox(root, height=800,width=600)
            l.grid(column=0, row=0)
            s = ttk.Scrollbar(root, orient=VERTICAL, command=l.yview)
            s.grid(column=1, row=0)
            l['yscrollcommand'] = s.set
            ttk.Sizegrip().grid(column=1, row=1)
            root.grid_columnconfigure(0, weight=1)
            root.grid_rowconfigure(0, weight=1)
            for filename in os.listdir("./Received/photos/"):
                l.insert(END, filename)
            root.mainloop()




if __name__ == '__main__':
    root = Tk()
    b = mainwindow(root)
    root.mainloop()
