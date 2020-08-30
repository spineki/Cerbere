# import de l'interface

from PySide2 import QtCore, QtWidgets
from interface import Ui_MainWindow

from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume

# détection de spotify
import sys
import time
from threading import Thread  # pour lire l'état courant de spotify
import win32gui
try:
    # pour simuler l'utilisation des touches de son
    from pynput.keyboard import Key, Controller, Listener, KeyCode


except Exception as e:
    print("bibliothèque pynput manquante, essayez de taper: \n pip install pynput")
    print(str(e))


class mywindow(QtWidgets.QMainWindow):

    last = ""
    mute = 173
    keyboard = Controller()
    dernierTemps = time.clock()
    pasDeTemps = 1  # s
    last_music = ""
    current = ""
    message = "recherche de spotify..."

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # connexion des boutons aux actions
        self.ui.pushButton_silence.clicked.connect(self.flip_sound)
        self.ui.pushButton_valider.clicked.connect(self.validTouche)
        self.ui.pushButton_changer_touche_son.clicked.connect(self.paramSon)

        # lancement de la tâche périodique
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def update(self):
        # on lance un thread d'analyse de la page spotify
        # print("analyse...")
        # Thread(target=self.worker).start()
        self.worker()

    def worker(self):
        # print("worker lancé")
        # ce thread taff en arrière plan
        infos = self.get_info_windows()
        # infos=["une musique", "un musicien talentueux"]
        current = infos[1]
        messageAAfficher = ""
        if current == "Nothing playing":  # si il y a une pub
            if self.last_music != "Nothing playing":  # si il y avait une musique juste avant
                # on vient de passer à une pub
                # self.flip_sound()  # on éteint le son
                self.setSoundLevel(0.0)
                self.last_music = "Nothing playing"  # on note que c'est une pub
            messageAAfficher = "En cours: PUB! argh"
            # si c'est toujours une pub. Bahhh on ne change rien

        else:
            # si on est sur une musique:
            if self.last_music == "Nothing playing":  # si on avait une pub avant
                # self.flip_sound()  # on remet le son
                self.setSoundLevel(1.0)
                self.last_music = current  # on note la musique actuelle

            elif self.last_music != current:  # si l'on vient juste de changer de musique
                self.last_music = current

            messageAAfficher = "En cours:\n" + infos[1] + "\nde " + infos[0]

        self.ui.label_musique_en_cours.setText(messageAAfficher)

    def setSoundLevel(self, soundLevel: int):
        print("setSoundLevel", soundLevel)
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)

            if session.Process and session.Process.name() == "Spotify.exe":
                print("volume.GetMasterVolume(): %s" %
                      volume.GetMasterVolume())
                volume.SetMasterVolume(soundLevel, None)

    def flip_sound(self):
        # print("tentative de couper le son")
        """coupe le son s'il est ouvert, le rouvre s'il est fermé"""

        self.keyboard.press(KeyCode(self.mute))
        time.sleep(0.05)
        self.keyboard.release(KeyCode(self.mute))

    def paramSon(self):
        self.ui.pushButton_changer_touche_son.setText(
            "Taper sur\nla touche mute")
        Thread(target=self.ecouteTouche).start()

    def ecouteTouche(self):
        def on_press(key):
            if key == Key.enter:
                self.ui.pushButton_changer_touche_son.setText(
                    "Changer Touche Son?")
                return False
            self.last = str('{0}'.format(key))[1:-1]
            self.ui.lineEdit_code_touche.setText(self.last)

        with Listener(on_press=on_press) as listener:
            listener.join()

    def validTouche(self):
        self.ui.pushButton_changer_touche_son.setText("Changer Touche Son?")
        temp = self.mute
        try:
            self.mute = int(self.ui.lineEdit_code_touche.text())
        except:
            self.mute = temp

    def get_info_windows(self):

        windows = []
        # on cherche sur les anciennes version de spotify le titre SpotifyMAinWindow
        windows.append(win32gui.GetWindowText(
            win32gui.FindWindow("SpotifyMainWindow", None)))

        # sur les versions plus récentes, on
        # on utilise EnumHandler pour EnumWindows puis on vide la liste si besoin
        def find_spotify_uwp(hwnd, windows):
            text = win32gui.GetWindowText(hwnd)
            if win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and len(text) > 0:
                windows.append(text)

        win32gui.EnumWindows(find_spotify_uwp, windows)

        while windows.count != 0:
            try:
                text = windows.pop()
            except:
                return "Error", "Nothing playing"
            try:
                artist, track = text.split(" - ", 1)
                return artist, track
            except:
                pass


app = QtWidgets.QApplication(sys.argv)
mainWin = mywindow()
mainWin.show()
returns = app.exec_()

sys.exit(returns)
