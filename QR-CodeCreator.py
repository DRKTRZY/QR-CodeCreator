from tkinter import filedialog
from PIL import ImageTk, Image
import tkinter.messagebox
import tkinter as tk
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

def create_qrcode(versions):
        qr = qrcode.QRCode(version=versions, box_size=10, border=5)
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
        create_qrcode(version.get())

def creator_link(url):
    webbrowser.open_new(url)

def click(value):
    test_label = tk.Label(window, text=value)
    test_label.place(x=300,y=330)

# Labels, Buttons, Entry & More
version = tk.IntVar()
qr_code_image_src = Image.open("qrcode1version.png")
qr_code_image_src = qr_code_image_src.resize((int(qr_code_image_src.width / 3.27), int(qr_code_image_src.height / 3.27)))
qr_code_image_v1 = ImageTk.PhotoImage(qr_code_image_src)
qr_code_image = tk.Label(window, image=qr_code_image_v1,width=72,height=72)
qr_code_image.place(x=100,y=147)
qr_code_image_src_v20 = ImageTk.PhotoImage(Image.open("qrcodev20s.png"))
qr_code_image_v20 = tk.Label(window, image=qr_code_image_src_v20,width=90,height=90)
qr_code_image_v20.place(x=275,y=140)
radio_button_v1 = tk.Radiobutton(window,bg="#424242", selectcolor="White", activebackground="#424242",activeforeground="white", cursor="hand2", variable=version,value=1,)
radio_button_v1.place(x=185,y=170)
radio_button_v2 = tk.Radiobutton(window,bg="#424242", selectcolor="White",activebackground="#424242",activeforeground="white", cursor="hand2",variable=version,value=10,)
radio_button_v2.place(x=375,y=170)
data = tk.StringVar()
data_entry = tk.Entry(window,width=70,textvariable=data)
data_entry.place(x=50,y=50)
data_label = tk.Label(window,text="Enter the Link",font=("Bahnschrift", 14),bg="#424242",fg="white")
data_label.place(x=190,y=20)
creator = tk.Label(window, text="Creator: DRKTRZY", fg="#d3d3d3", cursor="hand2", font=("Bahnschrift 8 underline"))
creator.place(x=400, y=280)
creator.configure(bg="#3f3f3f")
creator.bind("<Button-1>", lambda e: creator_link("https://github.com/DRKTRZY"))
custom_button(188,80,"Create QR-Code","white","#424242",create)

# Mainloop
window.mainloop()