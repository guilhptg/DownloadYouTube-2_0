from setuptools import setup, find_packages

setup(
    name='youtube_downloader',
    version='2.0',
    packages=find_packages,
    install_point={
        'console_scripts': [
            'youtube-downloader = youtube_downloader.main:run_app',
        ]
    },
    author='Guilherme Portugal',
    description='Aplicativo para baixar vídeos e músicas do YouTube com interface gráfica'
)