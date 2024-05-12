import tkinter as tk
import time

def atualizar_relogio():
    tempo_atual = time.strftime('%H:%M:%S')
    label_relogio.config(text=tempo_atual)
    root.after(1000, atualizar_relogio)

root = tk.Tk()
root.title("Relógio")

# Cria um rótulo para exibir o tempo
label_relogio = tk.Label(root, font=('calibri', 40, 'bold'), bg='white')
label_relogio.pack(padx=20, pady=20)

atualizar_relogio()

root.mainloop()