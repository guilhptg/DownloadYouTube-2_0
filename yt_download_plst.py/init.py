import os
import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix.exceptions import VideoUnavailable


# ========== Funções Utilitárias ==========

def obter_titulo(url):
    try:
        return YouTube(url).title
    except Exception as e:
        print("Erro ao obter título:", e)
        return None


def ajustar_nome_arquivo(nome, extensao):
    return nome if nome.lower().endswith(extensao) else nome + extensao


def nome_valido(nome):
    """Remove caracteres inválidos para nomes de arquivos."""
    import re
    return re.sub(r'[\\/*?:"<>|]', "", nome)


def show_on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percent = (bytes_downloaded / total_size) * 100
    progress_label.configure(text=f"Progresso: {percent:.2f}%")
    progress_bar.set(percent / 100)
    app.update_idletasks()


# ========== Função Principal de Download ==========

def download_yt():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira um link do YouTube.")
        return

    save_path = ctk.filedialog.askdirectory(title='Escolha a pasta para salvar o arquivo')
    if not save_path:
        messagebox.showerror("Erro", "Por favor, escolha uma pasta para salvar o arquivo.")
        return

    custom_name = filename_entry.get().strip()
    use_original_name = checkbox.get() == 'on'

    # Obtém o nome do vídeo se checkbox estiver marcado ou nome não preenchido
    if use_original_name or not custom_name:
        titulo = obter_titulo(url)
        if not titulo:
            messagebox.showerror('Erro', 'Não foi possível obter o título do vídeo.')
            return
        custom_name = titulo

    custom_name = nome_valido(custom_name)  # remove caracteres inválidos

    try:
        botao_baixar.configure(state="disabled")
        yt = YouTube(url, on_progress_callback=show_on_progress)
    except VideoUnavailable:
        messagebox.showerror("Erro", "Vídeo indisponível.")
        botao_baixar.configure(state="normal")
        return
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao processar o vídeo: {e}")
        botao_baixar.configure(state="normal")
        return

    # Determina formato
    if radio_var.get() == 1:
        ys = yt.streams.get_audio_only()
        file_extension = '.wav'
    else:
        ys = yt.streams.get_highest_resolution()
        file_extension = '.mp4'

    if not ys:
        messagebox.showerror('Erro', 'Nenhum fluxo compatível encontrado.')
        botao_baixar.configure(state="normal")
        return

    custom_name = ajustar_nome_arquivo(custom_name, file_extension)

    try:
        ys.download(output_path=save_path, filename=custom_name)

        label_frame = ctk.CTkFrame(app)
        label_frame.pack(pady=20, padx=20)
        ctk.CTkLabel(
            label_frame,
            text=f"'{custom_name}'\nBaixado com sucesso em:\n{save_path}",
            font=('Arial', 18)
        ).pack(pady=20, padx=20)
    except Exception as e:
        messagebox.showerror('Erro', f"Erro ao baixar: {e}")
        print("Erro de download:", e)
    finally:
        botao_baixar.configure(state="normal")
        progress_label.configure(text="Progresso: 0%")
        progress_bar.set(0)


# ========== Interface ==========

ctk.set_default_color_theme("dark-blue")
ctk.set_appearance_mode("system")

app = ctk.CTk()
app.geometry('800x600')
app.title('Download YouTube 2.0')

# Entrada do link
ctk.CTkLabel(app, text='Link do YouTube:', font=('Arial', 20)).pack(pady=10)
url_entry = ctk.CTkEntry(app, width=350)
url_entry.pack(padx=10, pady=10)

# Nome do arquivo
ctk.CTkLabel(app, text='Nome do arquivo (sem extensão):', font=('Arial', 20)).pack(pady=10)
filename_entry = ctk.CTkEntry(app, width=350)
filename_entry.pack(pady=10)

# Checkbox nome original
check_var = ctk.StringVar(value="on")
checkbox = ctk.CTkCheckBox(app, text="Nome original do Vídeo", variable=check_var, onvalue="on", offvalue="off")
checkbox.pack(padx=10, pady=10)

# Formato: áudio ou vídeo
radio_var = tk.IntVar(value=1)
ctk.CTkLabel(app, text='Escolha qual formato deseja baixar').pack()

radio_frame = ctk.CTkFrame(app)
radio_frame.pack(pady=10, padx=20)

ctk.CTkRadioButton(radio_frame, text="Áudio", variable=radio_var, value=1).pack(padx=20, pady=15, side=tk.LEFT)
ctk.CTkRadioButton(radio_frame, text="Vídeo", variable=radio_var, value=2).pack(padx=20, pady=15)

# Progresso
progress_label = ctk.CTkLabel(app, text='Progresso: 0%', width=350)
progress_label.pack(padx=10, pady=5)

progress_bar = ctk.CTkProgressBar(app, width=350)
progress_bar.pack(pady=5)
progress_bar.set(0)

# Botões
botao_baixar = ctk.CTkButton(app, text='Baixar', command=download_yt)
botao_baixar.pack(padx=10, pady=10)

botao_sair = ctk.CTkButton(app, text='Sair', command=app.destroy, fg_color='red')
botao_sair.pack(pady=10)

# Loop
app.mainloop()
