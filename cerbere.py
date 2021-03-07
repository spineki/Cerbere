import os
import sys
import tkinter as tk
import osascript  # Graphics


if sys.platform  == "win32":
    import win32gui  # getting spotify windows music title
    from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume  # manage sound
if sys.platform == "darwin":
    import osascript
    from AppKit import NSApp, NSWorkspace
    from Quartz import (
        CGWindowListCopyWindowInfo,
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID,
        kCGWindowListOptionAll
    )


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class App(tk.Frame):

    parent = None
    pushButton_silence = None
    label_current_music = None
    label_image = None
    label_percent = None

    verification_time_step = 1000  # ms
    last_music = ""
    current = ""
    soundStateOn = True

    message = "recherche de spotify..."

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.setupUi()
        self.pushButton_silence.config(command=self.flipSound)
        self.label_current_music.after(
            self.verification_time_step, self.update)
        # trick to deal with window initialisation problem
        self.setSoundLevel(0.0)
        self.setSoundLevel(1.0)

    def setupUi(self):
        # Silence Button
        self.pushButton = tk.Button(self.parent, text='Button text!', bg='#6b6b6b', fg="#FFFFFF", border="0", font=(
            'arial', 12, 'normal'))
        self.pushButton.place(
            anchor=tk.NW,  bordermode=tk.INSIDE, x=10, y=20, width=114,  height=51)  # (, , 111, 51)

        # Image Dog Button
        self.button_image = tk.PhotoImage(
            file=resource_path("round_button.png"))
        self.pushButton_silence = tk.Button(self.parent, text='Button text!', bg='#6b6b6b', fg="#FFFFFF", border="0", font=(
            'arial', 12, 'normal'), image=self.button_image)
        self.pushButton_silence.place(
            anchor=tk.NW,  bordermode=tk.INSIDE, x=10, y=20, width=114,  height=51)  # (, , 111, 51)

        # Current Music label
        self.label_current_music = tk.Label(self.parent, text='En cours: PUB! argh ', bg='#000000',
                                            fg="#FFFFFF", anchor="nw", justify=tk.LEFT, font=('Times New Roman', 10, 'underline'))
        self.label_current_music.place(
            anchor=tk.NW, bordermode=tk.INSIDE, x=130, y=20, width=200, height=70)

        # Shiba Image
        self.dog_img = tk.PhotoImage(file=resource_path("mini_shiba.png"))
        self.label_image = tk.Label(
            self.parent, image=self.dog_img, bg="#000000")
        self.label_image.place(anchor=tk.NW, bordermode=tk.INSIDE, x=330, y=0)

        # Percentage label
        self.label_percent = tk.Label(self.parent, text='100%', bg='#000000', fg="#FFFFFF",
                                      anchor="nw", justify=tk.LEFT, font=('Times New Roman', 10, 'normal'))
        self.label_percent.place(
            anchor=tk.NW, bordermode=tk.INSIDE, x=360, y=8)

    def update(self):
        # on lance un thread d'analyse de la page spotify
        infos = self.getInfoWindows()
        current = infos[1]
        message_to_display = ""

        nothing_playing_keyword = "Nothing playing"

        if current == nothing_playing_keyword:  # si il y a une pub
            if self.last_music != nothing_playing_keyword:  # si il y avait une musique juste avant
                # on vient de passer à une pub
                self.setSoundLevel(0.0)  # on éteint le son
                self.last_music = nothing_playing_keyword  # on note que c'est une pub
            message_to_display = "En cours: PUB! argh"
            # si c'est toujours une pub. Bahhh on ne change rien

        else:
            # si on est sur une musique:
            if self.last_music == nothing_playing_keyword:  # si on avait une pub avant
                self.setSoundLevel(1.0)  # on remet le son
                self.last_music = current  # on note la musique actuelle

            elif self.last_music != current:  # si l'on vient juste de changer de musique
                self.last_music = current
            else:
                # we are still in the same musique, nothing to do
                pass

            message_to_display = "En cours:\n" + infos[1] + "\nde " + infos[0]

        self.label_current_music.config(text=message_to_display)
        self.label_current_music.after(1000, self.update)

    def setSoundLevel(self, soundLevel: int):
        if sys.platform == "win32":
            self.setSoundLevelWindows(soundLevel)
        if sys.platform == "darwin":
            self.setSoundLevelDarwin(soundLevel)
 
    def setSoundLevelWindows(self, soundLevel: int):
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)

            if session.Process and session.Process.name() == "Spotify.exe":
                volume.SetMasterVolume(soundLevel, None)
                self.label_percent.config(
                    text=str(int(100 * soundLevel)) + "%")
                if (soundLevel == 0):
                    self.soundStateOn = False
                else:
                    self.soundStateOn = True

    def setSoundLevelDarwin(self, soundLevel: int):
        self.label_percent.config(text=str(int(20 * soundLevel)) + "%")

        osascript.run("set volume output volume " + str(int(20 * soundLevel)))

        if (soundLevel == 0):
            self.soundStateOn = False
        else:
            self.soundStateOn = True

    def flipSound(self):
        """coupe le son s'il est ouvert, le rouvre s'il est fermé"""

        if self.soundStateOn:
            self.setSoundLevel(0.0)
        else:
            self.setSoundLevel(1.0)

    def getInfoWindows(self):
        if sys.platform == "win32":
            return self.getInfoWindowsWindows()
        if sys.platform == "darwin":
            return self.getInfoWindowsDarwin()

    def getInfoWindowsWindows(self):

        windows = []
        # on cherche sur les anciennes version de spotify le titre SpotifyMainWindow
        windows.append(win32gui.GetWindowText(
            win32gui.FindWindow("SpotifyMainWindow", None)))

        # sur les versions plus récentes, on
        # on utilise EnumHandler pour EnumWindows puis on vide la liste si besoin
        def findSpotifyUwp(hwnd, windows):
            text = win32gui.GetWindowText(hwnd)
            if win32gui.GetClassName(hwnd) == "Chrome_WidgetWin_0" and len(text) > 0:
                windows.append(text)

        win32gui.EnumWindows(findSpotifyUwp, windows)

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

    def getInfoWindowsDarwin(self):
        # on cherche sur les anciennes version de spotify le titre Spotify
        options = kCGWindowListOptionAll
        windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
        #result = osascript.run("""set appName to "Spotify" \n if application appName is running then \n tell application "Spotify" \n set c to current track \n return {(artist of c), (album of c)} \n end tell \n else \n return "not running" \n end if""")

        for window in windowList:
            if window["kCGWindowOwnerName"] == "Spotify":
                (error_code, current_track, other) = osascript.run("""tell application "Spotify" \n set c to current track \n return {(artist of c), (album of c)} \n end tell""")
                if current_track == ",":
                    return ("Error", "Nothing playing")
                else:
                    try:
                        artist, track = current_track.split(",", 1)
                        return (artist.strip(), track.strip())
                    except Exception as e:
                        return ("Error", "Nothing playing")
        



#  ------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()

    # This is the section of code which creates the main window
    root.geometry('420x90')
    root.configure(background='#000000')
    root.title('Cerbère')
    app = App(parent=root)
    app.mainloop()
