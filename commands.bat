.\venv\Scripts\pyside2-designer.exe

.\venv\Scripts\pyside2-uic.exe -o interface.py interface.ui

.\venv\Scripts\pyinstaller.exe .\cuteCerbere.py --name Cerbere --windowed --onefile --clean

pip uninstall enum34