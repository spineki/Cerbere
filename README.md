# Cerbere

A little tool to mute spotify sound when an add replace the music. Uses python 3.
This project is a hobby, so no help is needed ^^

## clone this repository
- open a terminal and place yourself in a repository where you want to store this programm

  `cd my/folder/for/this/program`
- make sure you have installed git, and run
  `git clone https://github.com/spineki/Cerbere.git` 

## Install the dependencies
go to the newly created folder
  `cd Cerbere`

If you want to keep your python dependencies clean, create a virtualenv (to install virtualenv, `pip install virtualenv`)

`virtualenv venv`

then activate it with
- for windows `.\venv\Scripts\activate`
- for linux `source venv/bin/activate`

Finally, for virtualenv or classic python installation, type `pip install -r requirements.txt`

## To run this as a python script:
`python cuteCerbere.py`

## To build it as an exe file,

- if you have a venv, `.\venv\Scripts\pyinstaller.exe .\cuteCerbere.py --name Cerbere --windowed --onefile --clean` or just launch venv_build.bat
- if you don't have a venv, `pyinstaller.exe .\cuteCerbere.py --name Cerbere --windowed --onefile --clean` or just launch build.bat

Your exe is now in the dist folder.


Have Fun!!
