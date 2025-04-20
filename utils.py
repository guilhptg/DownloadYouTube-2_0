import re
import customtkinter as ctk
from tkinter import filedialog

# Auxiliary functions
def sanitize_filename(name):
    """
    Remove caracteres inválidos para nomes de arquivos.
    """
    return re.sub(r'[<>:"/\\|?*]', '', name)

def ask_save_directory():
    """
    Abre um seletor de pasta.
    """
    return ctk.filedialog.askdirectory(title="Escolha a pasta para salvar")

def show_progress(label, percent):
    """
    Atualiza um label de progresso com a porcentagem.
    """
    label.configure(text=f"Progresso: {percent:.2f}%")