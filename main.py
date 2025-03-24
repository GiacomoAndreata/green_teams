import tkinter as tk
import pyautogui
import time
import threading

# Variabili globali
paused = False
start_time = None
elapsed_time = 0

# Funzione per simulare la pressione del tasto SCROLLLOCK ogni 5 minuti
def simulate_key():
    while True:
        if not paused:
            pyautogui.press('scrolllock')  # Simula la pressione del tasto ScrollLock
            time.sleep(300)  # Attende 5 minuti prima di ripetere
        else:
            time.sleep(1)  # Dorme per 1 secondo quando in pausa

# Funzione per avviare il timer
def start_timer():
    global start_time, elapsed_time
    start_time = time.time() - elapsed_time  # Riprende o avvia il cronometro
    update_timer()

# Funzione per aggiornare il timer sull'interfaccia
def update_timer():
    global elapsed_time
    if not paused:
        elapsed_time = time.time() - start_time
    minutes, seconds = divmod(int(elapsed_time), 60)
    time_str = f"{minutes:02}:{seconds:02}"
    timer_label.config(text=time_str)
    if not paused:
        timer_label.after(1000, update_timer)  # Aggiorna ogni secondo

# Funzione per mettere in pausa o riprendere
def toggle_pause():
    global paused, start_time
    if paused:
        paused = False
        start_time = time.time() - elapsed_time  # Riprende da dove era
        pause_button.config(text="Pausa", bg="#f4511e")  # Cambia il testo e il colore del pulsante
        start_timer()  # Avvia il timer se riprende
    else:
        paused = True
        pause_button.config(text="Riprendi", bg="#34b7f1")  # Cambia il testo e il colore del pulsante per pausa

# Creazione dell'interfaccia grafica
root = tk.Tk()
root.title("Green Teams")

# Blocco della dimensione della finestra
root.geometry("300x250")  # Dimensioni fisse
root.resizable(False, False)  # Disabilita il ridimensionamento della finestra

# Colori di sfondo moderni
root.config(bg="#2c3e50")

# Aggiunta del frame per il timer
frame = tk.Frame(root, bd=5, relief="solid", padx=20, pady=20, bg="#34495e")
frame.pack(pady=20)

# Timer Label
timer_label = tk.Label(frame, font=("Helvetica", 24), width=10, height=2, bg="black", fg="white")
timer_label.pack()

# Pulsante per mettere in pausa o riprendere
pause_button = tk.Button(root, text="Pausa", bg="#f4511e", font=("Helvetica", 14), relief="flat", command=toggle_pause, width=15)
pause_button.pack(pady=10)

# Avvio del thread per simulare la pressione del tasto ScrollLock
thread = threading.Thread(target=simulate_key, daemon=True)
thread.start()

# Avvio del timer immediatamente all'inizio
start_timer()

# Avvio dell'interfaccia grafica
root.mainloop()
