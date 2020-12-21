# Cerbere

A little tool to mute spotify sound On windows when an ad replaces the music. Uses python 3.
This project is a hobby, so no help is needed ^^

<p align="center">
  <img src="https://raw.githubusercontent.com/spineki/Cerbere/master/app_look.png" />
</p>

## Who to Get it?

### Download the executable
This is the simplest way. Go to the right, `Release` section, choose the newest version and download the exectuable. Double click it and it works!

### Get the files
- Open a terminal and place yourself in a repository where you want to store this programm

  `cd my/folder/for/this/program`
- make sure you have installed git, and run
  `git clone https://github.com/spineki/Cerbere.git`
- (I you don't have git, simply click the green upper-right button on this page -> Code -> download zip and unzip it in your folder)

### Install the dependencies
Go to the newly created folder
  `cd Cerbere`
  or open your file explorer and open the newly created folder

- If you are not familiar with command line, that's fine! Just double click on `install.bat` to install the needed dependencies. A new virtualenv folder named 'venv' will be created in the folder with the needed dependencies, you can go to the next section
- - I you want to manage the installation by yourself, you can create a virtualenv \
open a terminal\
enter the folder `cd Cerbere`\
`virtualenv venv` then `venv\Scripts\activate` to activate it\
  - Finally, for virtualenv or classic python installation,\
    Just type `pip install -r requirements.txt` to install the dependencies.\
    Eventually, type `pip uninstall enum34` to uninstall this librariy that may harm the code.


### To run this as a python script:
`python cerbere.py`

### To build it as an exe file,
Maybe you don't want to open Python everytime and just be able to double click it like a regular program.


- if you are not familiar with command line, just double click on `buid.bat`
- If you want to manage it by yourself,
  - Activate your virtualenv if you need to,\
  make sure to have __pyinstaller__ library installed (`pip install pyinstaller`) and then enter\
  `.\venv\Scripts\pyinstaller.exe .\cerbere.py --name Cerbere --windowed --onefile --clean --add-data "mini_shiba.png;." --add-data "round_button.png;."` or just launch build.bat




Your exe is now in the dist folder. You can place it anywhere you want in your pc and use it as a tradition exe programm.


## How to Use it?

Double click on the exe.The program window will appear:
  - The silence button allows you to toogle the sound (example, spotify had a glitch an the sound is now muted during the musics. Just click on "Silence" button and it will work properly again
  - The percentage: It's the percentage of the volume allowed to spotify: 100% = sound up, 0%= sound down
  - A text at the center showing that there is an ad ("pub", in french) or the music and artist name.


## Incoming improvement
  - Add other languages ( Displayed info are in french until now)
  - Clean up the code and files tree


<p align="center">
  <img src="https://raw.githubusercontent.com/spineki/Cerbere/master/mini_shiba.png" width="200" height="200" />
</p>

Have Fun!!
