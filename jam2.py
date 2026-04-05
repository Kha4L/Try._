import tkinter as tk
from time import strftime


def update_waktu():
    waktu_sekarang = strftime('%H:%M:%S')
    label_jam.config(text=waktu_sekarang)
    
    
    tanggal_sekarang = strftime('%A, %d %B %Y')
    label_tanggal.config(text=tanggal_sekarang)
    
    
    label_jam.after(1000, update_waktu)


window = tk.Tk()
window.title("Jam Digital")
window.geometry("500x250")
window.resizable(False, False)


window.config(bg="#2C3E50")

label_judul = tk.Label(
    window,
    text="JAM-Jaman",
    font=("Arial", 16, "bold"),
    bg="#2C3E50",
    fg="#ECF0F1"
)
label_judul.pack(pady=20)


label_jam = tk.Label(
    window,
    font=("Digital-7", 60, "bold"),  
    bg="#2C3E50",
    fg="#3498DB"
)
label_jam.pack()


label_tanggal = tk.Label(
    window,
    font=("Arial", 18),
    bg="#2C3E50",
    fg="#ECF0F1"
)
label_tanggal.pack(pady=10)

label_footer = tk.Label(
    window,
    text="Waktu indonesia bagian barat (WIB)",
    font=("Arial", 10),
    bg="#2C3E50",
    fg="#95A5A6"
)
label_footer.pack(side="bottom", pady=10)

update_waktu()


window.mainloop()
