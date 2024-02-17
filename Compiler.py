# Autor: Christopher Gabriel Pedraza Pohlenz

# Compilador para crear un ejecutable del updater de NAEVYS

import PyInstaller.__main__

PyInstaller.__main__.run(["main.py", "--onefile"])
