import tkinter as tk
from tkinter import messagebox
import random

# Variables globales
player = "X"
game_over = False
score_X = 0
score_0 = 0
modo_pc = False  

# Comprueba el ganador
def ganador():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

# Limpia el tablero al encontrar un ganador manteniendo el puntaje
def limpiar_tablero():
    global player, game_over
    game_over = False
    player = "X"
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col]["bg"] = "#7e3232"

# Registra los clicks de los jugadores
def button_click(row, col):
    global player, game_over, score_X, score_0
    if buttons[row][col]["text"] == "" and not game_over:
        buttons[row][col]["text"] = player
        buttons[row][col]["bg"] = "#957435" if player == "X" else "#c69c4c"
        if ganador():
            if player == "X":
                score_X += 1
            else:
                score_0 += 1
            actualizar_puntaje()
            messagebox.showinfo(title="3 en raya", message=f"Jugador {player} gana!")
            limpiar_tablero()
        elif all(buttons[row][col]["text"] != "" for row in range(3) for col in range(3)):
            messagebox.showinfo(title="3 en raya", message="Empate")
            limpiar_tablero()
        else:
            player = "0" if player == "X" else "X"
            if modo_pc and player == "0":
                computadora_juega()

# Registra los clicks de la PC
def computadora_juega():
    global game_over, player
    if not game_over:
        vacios = [(r, c) for r in range(3) for c in range(3) if buttons[r][c]["text"] == ""]
        if vacios:
            row, col = random.choice(vacios)  
            buttons[row][col]["text"] = "0"
            buttons[row][col]["bg"] = "#455A64"
            if ganador():
                messagebox.showinfo(title="3 en raya", message="Computadora gana!")
                limpiar_tablero()
            elif all(buttons[r][c]["text"] != "" for r in range(3) for c in range(3)):
                messagebox.showinfo(title="3 en raya", message="Empate")
                limpiar_tablero()
            else:
                player = "X"

# Reinicia el puntaje a 0
def reset():
    global score_X, score_0
    score_X = 0
    score_0 = 0
    actualizar_puntaje()
    limpiar_tablero()

def actualizar_puntaje():
    label_score["text"] = f"X: {score_X} | 0: {score_0}"

# Funcion para seleccionar el modo de juego
def seleccionar_modo(modo):
    global modo_pc
    modo_pc = modo
    limpiar_tablero()

# Interfaz de la aplicación        
root = tk.Tk()
root.title("3 en raya")
root.geometry("400x550")
root.config(bg="#7e3232") 

# Estilo para el marco de puntaje
score_frame = tk.Frame(root, bg="#7e3232")
score_frame.pack(pady=10)
label_score = tk.Label(score_frame, text="X: 0 | 0: 0", font="normal 15 bold", bg="#7e3232", fg="white")
label_score.pack()

# Estilo para los botones de selección de modo
mode_frame = tk.Frame(root, bg="#7e3232") 
mode_frame.pack(pady=10)
btn_vs_pc = tk.Button(mode_frame, text="Versus PC", font="normal 10 bold", command=lambda: seleccionar_modo(True),
                      bg="#c69c4c", fg="white", bd=1)  
btn_vs_pc.grid(row=0, column=0, padx=10)

btn_vs_player = tk.Button(mode_frame, text="Versus Player", font="normal 10 bold", command=lambda: seleccionar_modo(False),
                          bg="#c69c4c", fg="white", bd=1) 
btn_vs_player.grid(row=0, column=1, padx=10)

# Estilo para el tablero
frame = tk.Frame(root, bg="#7e3232", bd=1, relief="solid")
frame.pack(pady=20)

buttons = [[tk.Button(frame, text="", font="normal 20 bold", width=5, height=2, bg="#7e3232", fg="white",
                      command=lambda row=row, col=col: button_click(row, col))
            for col in range(3)] for row in range(3)]

for row in range(3):
    for col in range(3):
        buttons[row][col].grid(row=row, column=col, padx=10, pady=10)

# Estilo para el boton de reiniciar
reset_button = tk.Button(root, text="Reiniciar", font="normal 15 bold", command=reset, bg="#7e3232", fg="white")
reset_button.pack(pady=10)

root.mainloop()
