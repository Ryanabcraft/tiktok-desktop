#!/usr/bin/env python3
"""TikTok Desktop — abre o TikTok no navegador em modo app."""
from browser_launcher import detect_browser, launch_url
import sys
import json
import os
import webbrowser
from urllib.request import urlopen
from urllib.error import URLError

URL = "https://www.tiktok.com"
VERSION = "1.1.0"
REPO = "Ryanabcraft/tiktok-desktop"


def check_update():
    """Verifica no GitHub se há versão mais nova. Retorna (nova_versão, url) ou None."""
    try:
        req = urlopen(f"https://api.github.com/repos/{REPO}/releases/latest", timeout=5)
        data = json.loads(req.read().decode())
        latest = data.get("tag_name", "").lstrip("v")
        url = data.get("html_url", "")
        if latest and latest != VERSION:
            return latest, url
    except (URLError, json.JSONDecodeError, OSError):
        pass
    return None


def msgbox(title, text, buttons=0):
    if sys.platform == "win32":
        import ctypes
        return ctypes.windll.user32.MessageBoxW(0, text, title, buttons)
    print(f"{title}: {text}")
    return 0


def main():
    # Auto-update em background
    update = check_update()
    if update:
        new_ver, url = update
        resp = msgbox(
            "Atualização disponível",
            f"TikTok Desktop v{new_ver} disponível!\n\n"
            f"Sua versão: v{VERSION}\n\n"
            "Deseja baixar a nova versão?",
            4  # MB_YESNO
        )
        if resp == 6:  # IDYES
            webbrowser.open(url)
            return

    browser = detect_browser()
    if not browser:
        msg = (
            "Nenhum navegador encontrado!\n\n"
            "Instale Chrome, Edge, Brave, Firefox, Opera ou Vivaldi."
        )
        msgbox("TikTok Desktop", msg)
        sys.exit(1)

    launch_url(URL, browser)


if __name__ == "__main__":
    main()
