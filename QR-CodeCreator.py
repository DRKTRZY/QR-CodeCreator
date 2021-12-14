import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox
import ttk
import qrcode
import webbrowser

# Display
window = tk.Tk()
window.geometry("500x300+500+300")
window.resizable(0,0)
window.title("QR-CodeCreator")
window.iconbitmap('icon.ico')
window.configure(bg="#424242")

# Functions
def custom_button(x,y,text,bcolor,fcolor,downloader):

    def on_enter(e):
        create_button["background"]=bcolor
        create_button["foreground"]=fcolor

    def on_leave(e):
        create_button["background"]=fcolor
        create_button["foreground"]=bcolor

    create_button = tk.Button(window, text=text, font="Bahnschrift",fg=bcolor, bg=fcolor,border=0,activeforeground=fcolor,activebackground=bcolor,padx=2, command=downloader)
    create_button.bind("<Enter>", on_enter)
    create_button.bind("<Leave>", on_leave)
    create_button.place(x=x, y=y)

def create_qrcode():
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        data_qrcode = str(data.get())
        qr.add_data(data_qrcode)
        qr.make(fit=True)
        img = qr.make_image(fill="black", back_color="white")
        img.save(filedialog.asksaveasfilename(initialdir="/", title="Select Directory", defaultextension=".png", filetypes=(
            ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif'))))
        data_entry.delete(0, tk.END)
def create():
    if data.get() == "":
        tkinter.messagebox.showerror("Error","Please enter a link")
    else:
        create_qrcode()

def creator_link(url):
    webbrowser.open_new(url)

# Labels, Buttons, Entry
data = tk.StringVar()
data_entry = tk.Entry(window,width=70,textvariable=data)
data_entry.place(x=50,y=50)
data_label = tk.Label(window,text="Enter the Link",font=("Bahnschrift", 14,"bold"),bg="#424242",fg="white")
data_label.place(x=190,y=20)
creator = tk.Label(window, text="Creator: DRKTRZY", fg="#d3d3d3", cursor="hand2", font=("Bahnschrift 8 underline"))
creator.place(x=400, y=280)
creator.configure(bg="#3f3f3f")
creator.bind("<Button-1>", lambda e: creator_link("https://github.com/DRKTRZY"))
custom_button(188,80,"Create QR-Code","white","#424242",create)

# Mainloop
window.mainloop()