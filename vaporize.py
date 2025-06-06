import tkinter as tk
import os
import threading
from time import sleep

def spoof_mac(logbox):
    try:
        os.system("ifconfig eth0 down")
        os.system("macchanger -r eth0")
        os.system("ifconfig eth0 up")
        logbox.insert(tk.END, "[+] MAC FALSIFICADO\n")
    except:
        logbox.insert(tk.END, "[x] FALHA NO SPOOF DE MAC\n")

def iniciar_tor(logbox):
    try:
        logbox.insert(tk.END, "[...] SUBINDO TOR...\n")
        os.system("service tor start")
        sleep(5)
        logbox.insert(tk.END, "[+] TOR ATIVADO - TÚNEL NO INFERNO OK\n")
    except:
        logbox.insert(tk.END, "[x] TOR FALHOU... TU TÁ NU\n")

def abrir_terminal_proxy(logbox):
    try:
        logbox.insert(tk.END, "[*] INICIANDO TERMINAL CAMUFLADO COM PROXYCHAINS\n")
        os.system("gnome-terminal -- proxychains bash")
    except:
        logbox.insert(tk.END, "[x] NÃO FOI POSSÍVEL ABRIR O TERMINAL\n")

def limpar_rastro(logbox):
    try:
        os.system("bleachbit -c system.cache system.clipboard system.recent_documents bash.history")
        os.system("history -c && unset HISTFILE")
        logbox.insert(tk.END, "[+] LIMPEZA GERAL FEITA. TU É LENDÁRIO\n")
    except:
        logbox.insert(tk.END, "[x] FALHA NA LIMPEZA\n")

def executar_sequencia(logbox):
    spoof_mac(logbox)
    iniciar_tor(logbox)
    abrir_terminal_proxy(logbox)

def executar(func, logbox):
    threading.Thread(target=func, args=(logbox,)).start()

# GUI
app = tk.Tk()
app.title("VAPORIZE GHOST + TOR + TERMINAL - by LEK DO BLACK ᴾᴿᴼ")
app.geometry("500x480")
app.configure(bg="black")

tk.Label(app, text="PAINEL FANTASMA SUPREMO", bg="black", fg="lime", font=("Courier", 14)).pack(pady=10)

btn1 = tk.Button(app, text="MAC + TOR + TERMINAL", bg="darkred", fg="white", font=("Courier", 12),
                 command=lambda: executar(executar_sequencia, logbox))
btn1.pack(pady=10, fill=tk.X, padx=40)

btn2 = tk.Button(app, text="LIMPAR RASTROS", bg="darkblue", fg="white", font=("Courier", 12),
                 command=lambda: executar(limpar_rastro, logbox))
btn2.pack(pady=10, fill=tk.X, padx=40)

logbox = tk.Text(app, bg="black", fg="lime", height=12)
logbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

app.mainloop()
