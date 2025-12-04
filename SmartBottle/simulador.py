import tkinter as tk
from tkinter import messagebox
import time
import random
import threading
import requests

# ----------------------------------------------------
# CONFIG BLYNK
# ----------------------------------------------------
BLYNK_TOKEN = "Ex5IaN0U91NpBo-rOx1QsHyev9atFO9z"
BASE_URL = f"https://blynk.cloud/external/api/update?token={BLYNK_TOKEN}"

# ----------------------------------------------------
# VARIÁVEIS GLOBAIS
# ----------------------------------------------------
meta = 2000              # meta total do dia
nivel_atual = 2000       # água restante na garrafa
total_consumido = 0      # quanto já bebeu
simulando = False
TEMP_LIMITE = 40         # temperatura alta
TEMPO_INATIVIDADE = 10   # segundos sem mudar nível
ultimo_nivel = 2000
timer_inatividade = 0

# ----------------------------------------------------
# FUNÇÃO DE ENVIO PARA O BLYNK
# ----------------------------------------------------
def enviar(pin, valor):
    try:
        requests.get(f"{BASE_URL}&{pin}={valor}")
    except:
        pass

# ----------------------------------------------------
# DEFINIR META
# ----------------------------------------------------
def definir_meta():
    global meta, nivel_atual, total_consumido, timer_inatividade

    try:
        valor = int(entry_meta.get())
        if valor <= 0:
            raise Exception()

        meta = valor
        nivel_atual = meta
        total_consumido = 0
        timer_inatividade = 0

        atualizar_interface()

        enviar("V1", 100)            # nível %
        enviar("V2", meta)           # nível ml
        enviar("V9", 0)              # consumido ml
        enviar("V4", 0)              # meta atingida OFF

        messagebox.showinfo("Meta atualizada", f"Meta diária definida para {meta} ml.")

    except:
        messagebox.showerror("Erro", "Digite um valor válido para a meta.")

# ----------------------------------------------------
# ADICIONAR +200 ML
# ----------------------------------------------------
def adicionar_agua():
    global nivel_atual

    nivel_atual += 200
    if nivel_atual > meta:
        nivel_atual = meta

    atualizar_envio()
    atualizar_interface()

# ----------------------------------------------------
# REPOR ÁGUA
# ----------------------------------------------------
def repor_agua():
    global nivel_atual, total_consumido, timer_inatividade

    nivel_atual = meta
    total_consumido = 0
    timer_inatividade = 0

    atualizar_envio()
    atualizar_interface()

    enviar("V4", 0)
    enviar("V5", 0)
    enviar("V6", 0)
    enviar("V9", 0)

# ----------------------------------------------------
# INICIAR SIMULAÇÃO
# ----------------------------------------------------
def iniciar_simulacao():
    global simulando
    if simulando:
        return

    simulando = True
    threading.Thread(target=loop_simulacao, daemon=True).start()

# ----------------------------------------------------
# LOOP DE SIMULAÇÃO
# ----------------------------------------------------
def loop_simulacao():
    global nivel_atual, total_consumido, ultimo_nivel, timer_inatividade

    while simulando:
        time.sleep(1)

        # Simular consumo
        consumo = random.randint(80, 160)
        antes = nivel_atual
        nivel_atual -= consumo

        if nivel_atual < 0:
            nivel_atual = 0

        bebido = antes - nivel_atual
        if bebido > 0:
            total_consumido += bebido

        # Temperatura
        temperatura = 0 if nivel_atual == 0 else round(random.uniform(20, 45), 1)

        enviar("V0", temperatura)

        # INATIVIDADE
        if nivel_atual == ultimo_nivel:
            timer_inatividade += 1
        else:
            timer_inatividade = 0

        ultimo_nivel = nivel_atual

        enviar("V6", 255 if timer_inatividade >= TEMPO_INATIVIDADE else 0)

        # TEMPERATURA ALTA
        enviar("V5", 255 if temperatura >= TEMP_LIMITE else 0)

        # META ATINGIDA
        if total_consumido >= meta:
            enviar("V4", 255)

        atualizar_envio()
        atualizar_interface()

# ----------------------------------------------------
# ENVIO PARA BLYNK
# ----------------------------------------------------
def atualizar_envio():
    # nível %
    percent = int((nivel_atual / meta) * 100)

    enviar("V1", percent)
    enviar("V2", nivel_atual)
    enviar("V9", total_consumido)

# ----------------------------------------------------
# ATUALIZA A INTERFACE
# ----------------------------------------------------
def atualizar_interface():
    label_nivel["text"] = f"{nivel_atual} ml restantes"
    label_total["text"] = f"{total_consumido} ml consumidos"


# ----------------------------------------------------
# INTERFACE MODERNA (Tkinter)
# ----------------------------------------------------
root = tk.Tk()
root.title("SmartBottle")
root.geometry("360x540")
root.configure(bg="#F0F2F5")

# Título
titulo = tk.Label(root, text="SMART BOTTLE", font=("Arial", 22, "bold"), fg="#2A4D69", bg="#F0F2F5")
titulo.pack(pady=10)

# CARD META
card_meta = tk.Frame(root, bg="white", highlightbackground="#DDD", highlightthickness=1)
card_meta.pack(pady=10, padx=20, fill="x")

tk.Label(card_meta, text="Meta diária (ml):", font=("Arial", 12, "bold"), bg="white").pack(pady=5)

entry_meta = tk.Entry(card_meta, font=("Arial", 12), width=10, justify="center")
entry_meta.insert(0, "2000")
entry_meta.pack(pady=5)

tk.Button(card_meta, text="Definir Meta", bg="#2196F3", fg="white",
          font=("Arial", 10, "bold"), command=definir_meta).pack(pady=8)

# CARD STATUS
card_status = tk.Frame(root, bg="white", highlightbackground="#DDD", highlightthickness=1)
card_status.pack(pady=10, padx=20, fill="x")

label_nivel = tk.Label(card_status, text="2000 ml restantes", font=("Arial", 12), bg="white", fg="#2A4D69")
label_nivel.pack(pady=5)

label_total = tk.Label(card_status, text="0 ml consumidos", font=("Arial", 12), bg="white", fg="#2A4D69")
label_total.pack(pady=5)

# BOTÕES
tk.Button(root, text="INICIAR SIMULAÇÃO", bg="#4CAF50", fg="white",
          font=("Arial", 12, "bold"), width=25, command=iniciar_simulacao).pack(pady=10)

tk.Button(root, text="ADICIONAR +200 ml", bg="#2196F3", fg="white",
          font=("Arial", 12, "bold"), width=25, command=adicionar_agua).pack(pady=5)

tk.Button(root, text="REPOR ÁGUA", bg="#FF9800", fg="white",
          font=("Arial", 12, "bold"), width=25, command=repor_agua).pack(pady=5)

root.mainloop()
