#Program by Eric Meier
#8/8/2019
import tkinter as tk
from tkinter import *
from tkinter import ttk 
import zipfile
from tkinter import filedialog
from zipfile import ZipFile
import os
from tkinter import messagebox
import pyAesCrypt
import base64

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

root = tk.Tk()

var = StringVar()

def zipper():
    filez = filedialog.askopenfilenames(parent=root,title='Choose a file')
    test = len(filez)
    file_list = root.tk.splitlist(filez)
    if filez == '':
        test2 = 'false'
    elif test < 2:
        #cont
        file = file_list[0]
        full_path = os.path.dirname(file)
        filename = os.path.basename(file)
        trimfiled = filename[:-4]
        with ZipFile(full_path + '/' + trimfiled + '.zip','w') as zip:
            zip.write(file)
            l.insert(1,trimfiled)
            var.set(full_path)
    elif test > 1:
        #multiple
        for x in range(0,test):
            file = file_list[x]
            full_path = os.path.dirname(file)
            filename = os.path.basename(file)
            trimfiled = filename[:-4]
            with ZipFile(full_path + '/' + trimfiled + '.zip','w') as zip:
                zip.write(file)
                l.insert(x+1,trimfiled)
                var.set(full_path)

def unzipper():
    filez = filedialog.askopenfilenames(parent=root,title='Choose a file')
    test = len(filez)
    file_list = root.tk.splitlist(filez)
    if filez == '':
        test2 = 'false'
    elif test < 2:
        #cont
        file = file_list[0]
        full_path = os.path.dirname(file)
        filename = os.path.basename(file)
        strlen = len(filename)
        File_Name = filename[0:(strlen-4)]
        New_Folder = full_path + '/' + File_Name
        os.mkdir(New_Folder)
        with ZipFile(file,'r') as zip:
            zip.extractall(New_Folder)
            l.insert(1,File_Name)
            var.set(full_path)
    elif test > 1:
        #multiple
        for x in range(0,test):
            file = file_list[0]
            full_path = os.path.dirname(file)
            filename = os.path.basename(file)
            strlen = len(filename)
            File_Name = filename[0:(strlen-4)]
            New_Folder = full_path + '/' + File_Name
            os.mkdir(New_Folder)
            with ZipFile(full_path + '/' + filename + '.zip','w') as zip:
                zip.extract(file)
                l.insert(x+1,File_Name)
                var.set(full_path)

def About():
    messagebox.showinfo("About", "This app was made by Eric Meier.")

def Help():
    messagebox.showinfo("Help", "Zip and unzip can be used with either "
    "one or several files. If multiple folders are selected to be zipped, each will be zipped into their "
    "own folder. Unzipping will unzip the folders into their own folders.")

def Encrypt():
    filez = filedialog.askopenfilenames(parent=root,title='Choose a file')
    test = len(filez)
    file_list = root.tk.splitlist(filez)
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    password = input("Enter the password")
    if filez == '':
        test2 = 'false'
    elif test < 2:
        #cont
        file = file_list[0]
        full_path = os.path.dirname(file)
        file_out = full_path + ".aes"
        # encrypt
        pyAesCrypt.encryptFile(full_path, file_out, password, bufferSize)
    elif test > 1:
        #multiple
        for x in range(0,test):
            file = file_list[x]
            full_path = os.path.dirname(file)
            file_out = full_path + ".aes"
            # encrypt
            pyAesCrypt.encryptFile(full_path, file_out, password, bufferSize)

def Decrypt():
    filez = filedialog.askopenfilenames(parent=root,title='Choose a file')
    test = len(filez)
    file_list = root.tk.splitlist(filez)
    # encryption/decryption buffer size - 64K
    bufferSize = 64 * 1024
    password = input("Enter the password")
    if filez == '':
        test2 = 'false'
    elif test < 2:
        #cont
        file = file_list[0]
        full_path = os.path.dirname(file)
        file_out = full_path + ".aes"
        # encrypt
        pyAesCrypt.decryptFile(file_out, full_path, password, bufferSize)
    elif test > 1:
        #multiple
        for x in range(0,test):
            file = file_list[x]
            full_path = os.path.dirname(file)
            file_out = full_path + ".aes"
            # decrypt
            pyAesCrypt.decryptFile(file_out, full_path, password, bufferSize)

w = root.winfo_reqwidth()
h = root.winfo_reqheight()

# get screen width and height
ws = int(root.winfo_screenwidth()/2 - w/2) # width of the screen
hs = int(root.winfo_screenheight()/3 - h/3) # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry("400x400+{}+{}".format(ws,hs))

labelframe = ttk.LabelFrame(root)
labelframe.pack(side = LEFT, fill="both")#, expand="yes")

L1 = ttk.Button(labelframe, text='Unzip', command=unzipper)
L1.pack(side = TOP, expand=True, fill='both')
L2 = ttk.Button(labelframe, text='Zip', command=zipper)
L2.pack(side = TOP, expand=True, fill='both')
L3 = ttk.Button(labelframe, text='Encrypt', command=Encrypt)
L3.pack(side = BOTTOM, expand=True, fill='both')
L3 = ttk.Button(labelframe, text='Decrypt', command=Decrypt)
L3.pack(side = BOTTOM, expand=True, fill='both')

#scroll bar for the list box that shows selected files
scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)
#Right frame for the list box and slider
right_frame = ttk.LabelFrame(root)#tk.Frame(root, bg = 'lime')
right_frame.pack(side = tk.BOTTOM, expand = True, fill = tk.BOTH)
l = Listbox(right_frame, height=10, yscrollcommand = scrollbar.set)
l.pack(side = RIGHT, expand=True, fill='both')

#menu bar with the help and about buttons
menubar = Menu(root)
menubar.add_command(label="Help", command=Help)
menubar.add_command(label="About", command=About)
root.config(menu=menubar)

top_frame = ttk.Frame(root)
top_frame.pack(side = TOP, fill = tk.BOTH)# expand = True, fill = tk.BOTH)
#Path of directory user selected
label = Label(top_frame, textvariable=var, anchor=W, bg="white", bd=1, relief="solid")
label.pack(side=tk.TOP, expand = True, fill = tk.BOTH)


currentDirectory = os.path.dirname(os.path.realpath(__file__))
tempFile = currentDirectory + "\ZipperIcon.ico"
# = self.label.setPixmap(QtGui.QPixmap(resource_path("Multifolder2withlockV2tan_lock.png")))
root.wm_title('Z-Zip')
root.wm_iconbitmap(tempFile) #ico file goes here

root.mainloop()

