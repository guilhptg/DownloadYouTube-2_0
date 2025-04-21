import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from utils import show_progress, ask_save_directory
from downloader import download_video_audio

# Interface Gráfica
# Window Settings

def run_app():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("dark-blue") # Color and Themes - Dark Blue
    ctk.set_widget_scaling(1.2)  # aumenta tamanho dos widgets
    ctk.set_window_scaling(1.1)  # aumenta tamanho da janela

    app = ctk.CTk()
    app.geometry('800x600')
    app.title('Download YouTube 2.0')


    # Elementos da interface
    # --- URL ---
    ctk.CTkLabel(app, text='Link do YouTube: ', font=('Arial', 20)).pack(pady=10)
    url_entry = ctk.CTkEntry(app, width=400)
    url_entry.pack(pady=10, padx=10)

    # --- Nome do arquivo ---
    ctk.CTkLabel(app, text='Nome do arquivo (sem extensão):', font=('Arial', 20)).pack(pady=10)
    filename_entry = ctk.CTkEntry(app, width=350)
    filename_entry.pack(pady=10)

    # --- Checkbox para nome original ---
    use_original_title = ctk.StringVar(value="on")
    checkbox = ctk.CTkCheckBox(app, text="Nome original do Vídeo", variable=use_original_title, onvalue="on", offvalue="off")
    checkbox.pack(padx=10, pady=10)

    # --- Radio: vídeo ou áudio ---
    radio_var = tk.IntVar(value=2)
    radio_frame = ctk.CTkFrame(app)
    radio_frame.pack(pady=10, padx=20)

    ctk.CTkLabel(app, text='Escolha qual formato deseja baixar')
    ctk.CTkRadioButton(radio_frame, text="Audio", variable= radio_var, value=1).pack(padx=20, pady=15, side=tk.LEFT)
    ctk.CTkRadioButton(radio_frame, text="Vídeo", variable= radio_var, value=2).pack(padx=20, pady=15)


    # --- Label progresso ---
    progress_label = ctk.CTkLabel(app, text=f'Progresso: 0%', width=350)
    progress_label.pack(padx=10, pady=10)


    # --- Botão baixar ---
    def handle_download():
        download_video_audio(
            url=url_entry.get(),
            custom_name=filename_entry.get(),
            use_original_name=(use_original_title.get() == 'on'),
            format_choice=radio_var.get(),
            progress_callback=lambda percent: show_progress(progress_label, percent)
        )
        
    ctk.CTkButton(app, text="Baixar", command=handle_download, hover_color=('blue', 'green')).pack(pady=10)
    ctk.CTkButton(app, text="Sair", command=app.destroy, hover_color=('red', 'black'), fg_color='red').pack(pady=10)


    # TODO "about"



    # Loop de aplicação
    app.mainloop()
