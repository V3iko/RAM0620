import tkinter as tk
import math
from PIL import Image, ImageTk, ImageDraw


aken = tk.Tk()
aken.title("Rotary Telefon")
aken.geometry("600x800")

canvas = tk.Canvas(aken, width=600, height=800, bg="white")
canvas.pack()

valitud_numbrid = []
max_numbrid = 8 # mitu numbrit korraga kuvatakse

numbrid = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
cx, cy = 300, 400
r = 150
algus_nurk = None
offset = 0
pealmine_ketas = None
stopper_nurk = 68 # Stopperi nurk
numbri_algnurk = 0 # Vajalik numbri tuvastamiseks
max_delta = 280 # Piirab ketta liikumist paremale

def joonista_staatiline():
    # Suur hall ketas
    canvas.create_oval(100, 200, 500, 600, fill="gray", outline="black")
    # Stopper joon
    canvas.create_line(325, 443, 403, 572, fill="black", width=5, tags="visuaalid")
    # Suvalised visuaalid
    canvas.create_oval(250, 350, 350, 450, fill="forest green", outline="black", tags="visuaalid")
    canvas.create_rectangle(150, 80, 450, 120, fill="white", outline="black", width=2)
    # Telefoni number (kirjutatakse üle)
    canvas.create_text(300, 100, text="", font=("Arial", 24), fill="black", tags="ekraan")
    canvas.create_text(300, 65, text="Valitud number:", font=("Arial", 16), fill="black")

def testimine():
    print(f"stopper nurk: {math.degrees(math.atan2(572 - cy, 403 - cx)):.1f}")
    print(f"offset: {offset}")
    pass



def joonista_pealmine(offset=0):
    global pealmine_ketas
    pilt = Image.new("RGBA", (600,800), (0,0,0,0))
    draw = ImageDraw.Draw(pilt)

    #ketas
    draw.ellipse([100,200,500,600], fill=(28,77,45,255), outline=(0,0,0,255))

    #Tühjad augud numbrite kohal
    for i in range(10):
        nurk = math.radians(i*28 + 90 + offset)
        x = cx + r * math.cos(nurk)
        y = cy + r * math.sin(nurk)
        draw.ellipse([x-21, y-21, x+21, y+21], fill=(0,0,0,0))

    pealmine_pilt = ImageTk.PhotoImage(pilt)
    canvas.create_image(0,0, anchor="nw", image=pealmine_pilt, tags="pealmine")
    canvas.foto = pealmine_pilt
    canvas.tag_raise("visuaalid")

def uuenda_pealmist(offset=0):
    canvas.delete("pealmine")
    joonista_pealmine(offset)

def joonista_numbrid():
    # Numbrid + augud, joonistatakse iga kord üle
    canvas.delete("numbrid")
    for i, num in enumerate(numbrid):
        nurk = math.radians(i*28 + 90)
        x = cx + r * math.cos(nurk)
        y = cy + r * math.sin(nurk)

        canvas.create_oval(x-20, y-20, x+20, y+20, fill="black", tags="numbrid")
        canvas.create_text(x, y, text=num, font=("Arial", 20), fill="white", tags="numbrid")

def tagasi_kerimine():
    global offset
    if abs(offset) < 4:
        offset = 0
        uuenda_pealmist(offset)
        return
    elif offset > 0:
        offset -= 4
    elif offset < 0:
        offset += 4
    uuenda_pealmist(offset)
    aken.after(5, tagasi_kerimine)

def hiir_alla(event):
    global algus_nurk
    global numbri_algnurk

    dx = event.x - cx
    dy = event.y - cy
    algus_nurk = math.degrees(math.atan2(dy, dx))

    for i, num in enumerate(numbrid):
        nurk = math.radians(i*28+90 + offset)
        x = cx + r * math.cos(nurk)
        y = cy + r * math.sin(nurk)

        # Kui hiir on selle numbri lähedal
        kaugus = math.sqrt((event.x - x) ** 2 + (event.y - y) ** 2)
        if kaugus < 25:
            numbri_algnurk = math.degrees(math.radians(i*28+90))
            print(f"Valitud number: {num}")

def hiir_liigub(event):
    global algus_nurk, offset
    dx = event.x - cx
    dy = event.y - cy
    praegune = math.degrees(math.atan2(dy, dx))
    delta = algus_nurk - praegune

    while delta < 0:
        delta += 360
    while delta > 360:
        delta -= 360

    # Arvutame valitud numbri nurga
    numbri_nurk = (numbri_algnurk - delta) % 360

    if numbri_nurk > stopper_nurk and 0 < delta < max_delta :
        offset = -delta
        uuenda_pealmist(offset)

    #print(f"delta: {delta}")

def hiir_ules(event):
    for i, num in enumerate(numbrid):
        nurk = (i * 28 + 90 + offset) % 360
        #print(f"Number {num}: nurk {nurk:.1f}")
        if abs(nurk-68) < 5:
            valitud_numbrid.append(str(num))
            ekraani_uuendamine()
            # print(valitud_numbrid)
    tagasi_kerimine()
    # print(f"Asukoht: x={event.x}, y={event.y}")  # Koordinaatide kuvamine

def ekraani_uuendamine():
    if len(valitud_numbrid) > max_numbrid:
        nähtav = "..." + "".join(valitud_numbrid[-max_numbrid:])
    else:
        nähtav = "".join(valitud_numbrid)
    canvas.itemconfig("ekraan", text=nähtav)

def kustuta():
    if len(valitud_numbrid) > 0:
        valitud_numbrid.pop()
        ekraani_uuendamine()

nupp = tk.Button(aken, text="⌫", command=kustuta,
                 bg="white", fg="black", font=("Arial", 20, "bold"),
                 relief="flat", padx=15, pady=8, cursor="hand2")
nupp.place(x=350, y=700)

canvas.bind("<ButtonPress-1>", hiir_alla)    # hiir vajutatakse alla
canvas.bind("<B1-Motion>", hiir_liigub)      # hiir liigub hoides
canvas.bind("<ButtonRelease-1>", hiir_ules)  # hiir lastakse lahti

joonista_staatiline()
joonista_numbrid()
joonista_pealmine()

aken.mainloop()