.\venv\Scripts\python.exe -m pip install pyinstaller
.\venv\Scripts\python.exe -m pip  uninstall enum34
.\venv\Scripts\pyinstaller.exe .\cerbere.py --name Cerbere --windowed --onefile --clean --add-data "mini_shiba.png;." --add-data "round_button.png;."

