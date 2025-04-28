from pytubefix import YouTube
from tkinter import messagebox
from .utils import ask_save_directory, sanitize_filename

def download_video_audio(url, custom_name, use_original_name, format_choice, progress_callback):
    """
    Baixa um vídeo ou áudio do YouTube.
    
    Args:
        url (str): URL do vídeo no YouTube.
        custom_name (str): Nome customizado do arquivo.
        use_original_name (bool): Usa o nome original do vídeo de True.
        formt_choice (int): 1 para áudio, 2 para vídeo.
        progress_callback (function): Atualiza a UI com progresso.
    """
    try:
        save_path = ask_save_directory()
        if not save_path:
            return

        yt = YouTube(url, on_progress_callback=lambda stream, chunck, bytes_remaining:progress_callback(100 - (bytes_remaining/stream.filesize)* 100))

        if use_original_name or not custom_name:
            custom_name = sanitize_filename(yt.title)
            

        # Download Audio
        yt_stream = yt.streams.get_audio_only() if format_choice == 1 else yt.streams.get_highest_resolution()
        extension = '.m4a' if format_choice == 1 else '.mp4'
        if not custom_name.endswith(extension):
            custom_name += extension

        yt_stream.download(output_path=save_path, filename=custom_name)
        messagebox.showinfo('Sucesso', f'{custom_name} baixado com sucesso em {save_path}')
        
        if not yt_stream:
            messagebox.showerror('Erro', 'Nenhum fluxo compatível encontrado.')
            return
        
    except Exception as e:
        messagebox.showerror('Erro', f'Erro ao baixar: {e}')