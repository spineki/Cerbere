./venv/bin/python -m pip install pyinstaller
./venv/bin/python -m pip uninstall enum34
./venv/bin/pyinstaller ./cerbere.py --name Cerbere --windowed --clean --add-data "mini_shiba.png:." --add-data "round_button.png:." --add-data "icon.ico:." --icon "icon.ico"

