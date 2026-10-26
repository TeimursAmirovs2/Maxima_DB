import tkinter as tk
from tkinter import ttk

from funkcijas import (
    add_client,
    add_order
)

def addFromWindow():

    name = name_input.get()
    surname = surname_input.get()

    print(name)
    print(surname)

    add_client(name, surname)

    name_input.delete(0, tk.END)
    surname_input.delete(0, tk.END)

    result.config(text= "Klients Pievienots")

#veidojam logu
window = tk.Tk()
window.title("MaXima datubāze")
window.geometry("1000x800")

#veidojam cilnes
tabs = ttk.Notebook(window)
tabs.pack(fill= "both", expand= True)

product_tab = ttk.Frame(tabs)
client_tab = ttk.Frame(tabs)

#pievieojam cilnes logam
tabs.add(product_tab, text="Preces")
tabs.add(client_tab, text="Klienti")

#virsraksts
header = tk.Label(
    product_tab,
    text="Veikala datubāze",
    font=("Arial", 20, "bold")
)
header.pack(pady = 20)


#klienta bloks
client_block = tk.LabelFrame(
    product_tab,
    text="Pieveinot klientu",
    padx= 10,
    pady= 10
)
client_block.pack(fill="x", padx= 20, pady= 10)

tk.Label(client_block, text="Vārds").pack()
name_input = tk.Entry(client_block, width= 60)
name_input.pack(pady= 5)

tk.Label(client_block, text="Uzvārds").pack()
surname_input = tk.Entry(client_block, width= 60)
surname_input.pack(pady= 5)

client_button = tk.Button(client_block, text= "Pievienot klientu", command=addFromWindow)
client_button.pack(pady=5)

result = tk.Label(
    client_block, text= "", fg="green"
)
result.pack(pady=5)


#Produkta logs
product_block = tk.LabelFrame(
    window,
    text="Pieveinot preci",
    padx= 10,
    pady= 10
)
product_block.pack(fill="x", padx= 20, pady= 10)

tk.Label(product_block, text="Nosaukums").pack()
product_name_input = tk.Entry(product_block, width= 60)
product_name_input.pack(pady= 5)

tk.Label(product_block, text="Cena").pack()
price_input = tk.Entry(product_block, width= 60)
price_input.pack(pady= 5)

product_button = tk.Button(product_block, text= "Pievienot preci")
product_button.pack(pady=5)


#Pasutijuma logs
order_block = tk.LabelFrame(
    window,
    text="Pieveinot pasūtījumu",
    padx= 10,
    pady= 10
)
order_block.pack(fill="x", padx= 20, pady= 10)

tk.Label(order_block, text="Klienta ID").pack()
klient_input = tk.Entry(order_block, width= 60)
klient_input.pack(pady= 5)

tk.Label(order_block, text="Preces ID").pack()
product_input = tk.Entry(order_block, width= 60)
product_input.pack(pady= 5)

order_button = tk.Button(order_block, text= "Pievienot pasūtījumu")
order_button.pack(pady=5)



window.mainloop()