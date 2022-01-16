
import tkinter as tk
import download
def urlal():
    url=text.get("1.0","end-1c")
    download.urll(url)
    tk._exit()
window=tk.Tk()
text=tk.Text(window)
text.pack()
buton =tk.Button(window,text="Müziğe çevir",command=lambda: urlal())

buton.pack()
window.mainloop()