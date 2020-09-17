# Cerbere

A little tool to mute spotify sound On windows when an ad replaces the music. Uses python 3.
This project is a hobby, so no help is needed ^^

<p align="center">
  <img src="https://raw.githubusercontent.com/spineki/Cerbere/master/app_look.png" />
</p>

## Who to Get it? 
### Get the files
- open a terminal and place yourself in a repository where you want to store this programm

  `cd my/folder/for/this/program`
- make sure you have installed git, and run
  `git clone https://github.com/spineki/Cerbere.git` 
- (I you don't have git, simply click the green upper-right button on this page -> Code -> download zip)

### Install the dependencies
Go to the newly created folder
  `cd Cerbere`

If you want to keep your python dependencies clean, create a virtualenv (to install virtualenv, `pip install virtualenv`)

`virtualenv venv`

then activate it with
- for windows `.\venv\Scripts\activate`

Finally, for virtualenv or classic python installation, type `pip install -r requirements.txt`to install all required libraries

### To run this as a python script:
`python cuteCerbere.py`

### To build it as an exe file,

- if you have a venv, `.\venv\Scripts\pyinstaller.exe .\cuteCerbere.py --name Cerbere --windowed --onefile --clean` or just launch venv_build.bat
- if you don't have a venv, `pyinstaller.exe .\cuteCerbere.py --name Cerbere --windowed --onefile --clean` or just launch build.bat

Your exe is now in the dist folder. You can place it anywhere you want in your pc and use it as a tradition exe programm.


## Who to Use it?

Double click on the exe.The program window will appear:
  - The silence button allows you to toogle the sound (example, spotify had a glitch an the sound is now muted during the musics. Just click on "Silence" button and it will work properly again
  - The percentage: It's the percentage of the volume allowed to spotify: 100% = sound up, 0%= sound down
  - A text at the center showing that there is an ad ("pub", in french) or the music and artist name.


## Incoming improvement
  - Add other languages ( Displayed info are in french until now)
  - Clean up the code and files tree


<p align="center">
  <img src="https://raw.githubusercontent.com/spineki/Cerbere/master/shiba.png" width="200" height="200" />
</p>

Have Fun!!
