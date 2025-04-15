from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import filedialog
from pytubefix import *
from pytubefix.cli import on_progress



# def on_progress(stream, chunk, bytes_remaining):
#     total_size = stream.filesize
#     bytes_downloaded = total_size - bytes_remaining
#     percent = (bytes_downloaded / total_size) * 100
#     progress_label.config(text=f"Progresso: {percent:.2f}%")


def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Erro", "Por favor, insira um link do YouTube.")
        return

    save_path = filedialog.askdirectory(title="Escolha a pasta para salvar o arquivo")
    if not save_path:
        messagebox.showerror("Erro", "Por favor, escolha uma pasta para salvar o arquivo.")
        return

    custom_name = filename_entry.get().strip()
    if not custom_name:
        messagebox.showerror("Erro", "Por favor, insira um nome para o arquivo.")
        return

    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        if format_var.get() == "video":
            stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()
        elif format_var.get() == "audio":
            stream = yt.streams.filter(only_audio=True).first()
        else:
            messagebox.showerror("Erro", "Escolha um formato válido.")
            return

        if not stream:
            messagebox.showerror("Erro", "Nenhum fluxo compatível encontrado.")
            return

        stream.download(output_path=save_path, filename=custom_name)
        messagebox.showinfo("Sucesso", f"'{custom_name}' foi baixado com sucesso em {save_path}!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao baixar o vídeo: {e}")


# Window Settings

# Color and Themes - Dark Blue
ctk.set_default_color_theme("dark-blue") 

# Appearence Mode - Default
ctk.set_appearance_mode("system")

# Uncomment to deactivete automatic scaling mode
# customtkinter.deactivate_automatic_dpi_awareness()

# customtkinter.set_widget_scaling(float_value)  # widgrootet dimensions and text size
# customtkinter.set_window_scaling(float_value)  # window geometry dimensions




# Crate APP
app = ctk.CTk()

# Tamanho janela principal
app.geometry('600x600')

# Title
app.title('Download YouTube 2.0')

# Input do Link do YouTube
label_link = ctk.CTkLabel(app, text='Link do YouTube: ', font=('Arial', 20))
label_link.pack(pady=10)


def down_test():
    url = url_entry.get()
    yt = YouTube(url=url, on_progress_callback=on_progress)
    video_title = yt.title
    ys = yt.streams.get_audio_only()
    ys.download()

# Campo para inserção do link
url_entry = ctk.CTkEntry(app, width=350)
url_entry.pack(padx=10, pady=10)


botao_baixar = ctk.CTkButton(app, text='Baixar', command=down_test)
botao_baixar.pack(padx=10, pady=10)



# ctk.CTkLabel(app, text="Formato disponivel:").pack(padx=10, pady=10)

# Botão fechar aplicativo
botao_sair = ctk.CTkButton(app, text='Sair', command=app.destroy)
botao_sair.pack(pady=10)


# TODO "about"



# Loop de aplicação
app.mainloop()
