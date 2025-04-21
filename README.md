# 🎬 YouTube Downloader 2.0 — Agora com Estilo e Poder!

Bem-vindo à versão **2.0** do nosso app de download de vídeos do YouTube! 

Este projeto nasceu como uma simples ideia: baixar vídeos do YouTube com o bom e velho `tkinter`. Mas agora... evoluímos!

## 🚀 O que há de novo?

A versão **1.0** era um app básico, feito com `tkinter`, sem firula: você colava o link do vídeo e ele baixava. Só isso. Era funcional, mas... feinho. 😅

Agora, com a **2.0**, tudo mudou:

- Interface moderna com **customtkinter**
- Escolha entre **áudio (.m4a)** ou **vídeo (.mp4)**
- **Nome personalizado** ou título original do vídeo
- Barra de progresso com porcentagem
- Mensagens de sucesso amigáveis (a gente gosta de elogiar quando dá certo )

## 💻 Como usar esse projeto

### Clonando e rodando localmente

1. Clone este repositório:
``` bash
git clone https://github.com/seuusuario/youtube-downloader-2.0.git
cd youtube-downloader-2.0
```

2. Instale os requisitos:

``` bash
Copiar
Editar
pip install -r requirements.txt
```

3. Rode o app:


```bash
Copiar
Editar
python main.py
```
---

4. Funcionalidades

| Função             | Descrição                                              |
|--------------------|--------------------------------------------------------|
| **Baixar Vídeo**       | Qualidade máxima disponível (.mp4)                     |
| **Baixar Áudio**       | Áudio em `.m4a` com qualidade decente                  |
| **Nome Personalizado** | Você escolhe o nome do arquivo                     |
| **Nome Original**      | Usa o título do vídeo como nome automaticamente        |
| **Barra de Progresso** | Veja a mágica acontecer em tempo real ✨          |

---

## 📦 Baixar o Executável `.exe`

Quer usar sem instalar nada? Só baixar o `.exe` e pronto!

1. Vá até a [última release](https://github.com/seu-usuario/seu-repositorio/releases)
2. Baixe o arquivo **`YouTubeDownloader2.0.exe`**
3. Dê dois cliques, cole o link do vídeo, escolha o formato e seja feliz 🎉

⚠️ Recomendamos **rodar como administrador** caso ocorra algum erro com permissões.

---

## 🧠 Como usar como base para seu projeto

Esse projeto está organizado para facilitar estudos e manutenção. Veja os arquivos principais:

- `main.py` → Onde tudo começa (interface principal e lógica de download)
- `config.py` → Configurações gerais (tema, textos, tamanho da janela)
- `ui.py` → Componentes visuais separados
- `helpers.py` → Funções utilitárias (progresso, validações, tratamento de nome)
- `README.md` → Este manual simpático 😊

Se quiser converter para `.exe`, use o [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe) ou `pyinstaller`.

---

## 📚 Feito com

- [Python](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [pytubefix](https://github.com/nficano/pytube) — versão corrigida do `pytube`

---

## 👨‍💻 Autor

Desenvolvido por **Seu Nome**.

Se quiser colaborar, melhorar, reportar bugs ou apenas dar um "salve", fique à vontade para abrir uma **issue** ou mandar um **Pull Request**. 😉

---