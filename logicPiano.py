import pygame.mixer
from PyQt6.QtWidgets import *
from guiPiano import *


class Logic(QMainWindow, Ui_MainWindow):
    """
    A class describing the functions of the piano app
    """

    def __init__(self) -> None:
        """
        Method that creates that calls other methods upon an action being detected on an app.
        """
        super().__init__()
        self.setupUi(self)

        pygame.mixer.init()

        self.C2.clicked.connect(lambda: self.c2_pressed())
        self.D2.clicked.connect(lambda: self.d2_pressed())
        self.E2.clicked.connect(lambda: self.e2_pressed())
        self.F2.clicked.connect(lambda: self.f2_pressed())
        self.G2.clicked.connect(lambda: self.g2_pressed())
        self.A2.clicked.connect(lambda: self.a2_pressed())
        self.B2.clicked.connect(lambda: self.b2_pressed())
        self.Db2.clicked.connect(lambda: self.db2_pressed())
        self.Eb2.clicked.connect(lambda: self.eb2_pressed())
        self.Gb2.clicked.connect(lambda: self.gb2_pressed())
        self.Ab2.clicked.connect(lambda: self.ab2_pressed())
        self.Bb2.clicked.connect(lambda: self.bb2_pressed())

        self.C3.clicked.connect(lambda: self.c3_pressed())
        self.D3.clicked.connect(lambda: self.d3_pressed())
        self.E3.clicked.connect(lambda: self.e3_pressed())
        self.F3.clicked.connect(lambda: self.f3_pressed())
        self.G3.clicked.connect(lambda: self.g3_pressed())
        self.A3.clicked.connect(lambda: self.a3_pressed())
        self.B3.clicked.connect(lambda: self.b3_pressed())
        self.Db3.clicked.connect(lambda: self.db3_pressed())
        self.Eb3.clicked.connect(lambda: self.eb3_pressed())
        self.Gb3.clicked.connect(lambda: self.gb3_pressed())
        self.Ab3.clicked.connect(lambda: self.ab3_pressed())
        self.Bb3.clicked.connect(lambda: self.bb3_pressed())

        self.C4.clicked.connect(lambda: self.c4_pressed())
        self.D4.clicked.connect(lambda: self.d4_pressed())
        self.E4.clicked.connect(lambda: self.e4_pressed())
        self.F4.clicked.connect(lambda: self.f4_pressed())
        self.G4.clicked.connect(lambda: self.g4_pressed())
        self.A4.clicked.connect(lambda: self.a4_pressed())
        self.B4.clicked.connect(lambda: self.b4_pressed())
        self.Db4.clicked.connect(lambda: self.db4_pressed())
        self.Eb4.clicked.connect(lambda: self.eb4_pressed())
        self.Gb4.clicked.connect(lambda: self.gb4_pressed())
        self.Ab4.clicked.connect(lambda: self.ab4_pressed())
        self.Bb4.clicked.connect(lambda: self.bb4_pressed())

        self.C5.clicked.connect(lambda: self.c5_pressed())
        self.D5.clicked.connect(lambda: self.d5_pressed())
        self.E5.clicked.connect(lambda: self.e5_pressed())
        self.F5.clicked.connect(lambda: self.f5_pressed())
        self.G5.clicked.connect(lambda: self.g5_pressed())
        self.A5.clicked.connect(lambda: self.a5_pressed())
        self.B5.clicked.connect(lambda: self.b5_pressed())
        self.Db5.clicked.connect(lambda: self.db5_pressed())
        self.Eb5.clicked.connect(lambda: self.eb5_pressed())
        self.Gb5.clicked.connect(lambda: self.gb5_pressed())
        self.Ab5.clicked.connect(lambda: self.ab5_pressed())
        self.Bb5.clicked.connect(lambda: self.bb5_pressed())

        self.C6.clicked.connect(lambda: self.c6_pressed())

    def play_note(self) -> None:
        """
        Method that plays audio file
        """
        pygame.mixer.music.play()

    def c2_pressed(self) -> None:
        """
        Method that plays the C2 file when the C2 key is clicked
        """
        pygame.mixer.music.load('C2.wav')
        self.play_note()

    def d2_pressed(self) -> None:
        """
        Method that plays the D2 file when the D2 key is clicked
        """
        pygame.mixer.music.load('D2.wav')
        self.play_note()

    def e2_pressed(self) -> None:
        """
        Method that plays the E2 file when the E2 key is clicked
        """
        pygame.mixer.music.load('E2.wav')
        self.play_note()

    def f2_pressed(self) -> None:
        """
        Method that plays the F2 file when the F2 key is clicked
        """
        pygame.mixer.music.load('F2.wav')
        self.play_note()

    def g2_pressed(self) -> None:
        """
        Method that plays the G2 file when the G2 key is clicked
        """
        pygame.mixer.music.load('G2.wav')
        self.play_note()

    def a2_pressed(self) -> None:
        """
        Method that plays the A2 file when the A2 key is clicked
        """
        pygame.mixer.music.load('A2.wav')
        self.play_note()

    def b2_pressed(self) -> None:
        """
        Method that plays the B2 file when the B2 key is clicked
        """
        pygame.mixer.music.load('B2.wav')
        self.play_note()

    def db2_pressed(self) -> None:
        """
        Method that plays the Db2 file when the DB2 key is clicked
        """
        pygame.mixer.music.load('Db2.wav')
        self.play_note()

    def eb2_pressed(self) -> None:
        """
        Method that plays the Eb2 file when the Eb2 key is clicked
        """
        pygame.mixer.music.load('Eb2.wav')
        self.play_note()

    def gb2_pressed(self) -> None:
        """
        Method that plays the Gb2 file when the Gb2 key is clicked
        """
        pygame.mixer.music.load('Gb2.wav')
        self.play_note()

    def ab2_pressed(self) -> None:
        """
        Method that plays the Ab2 file when the Ab2 key is clicked
        """
        pygame.mixer.music.load('Ab2.wav')
        self.play_note()

    def bb2_pressed(self) -> None:
        """
        Method that plays the Bb2 file when the Bb2 key is clicked
        """
        pygame.mixer.music.load('Bb2.wav')
        self.play_note()

    def c3_pressed(self) -> None:
        """
        Method that plays the C3 file when the C3 key is clicked
        """
        pygame.mixer.music.load('C3.wav')
        self.play_note()

    def d3_pressed(self) -> None:
        """
        Method that plays the D3 file when the D3 key is clicked
        """
        pygame.mixer.music.load('D3.wav')
        self.play_note()

    def e3_pressed(self) -> None:
        """
        Method that plays the E3 file when the E3 key is clicked
        """
        pygame.mixer.music.load('E3.wav')
        self.play_note()

    def f3_pressed(self) -> None:
        """
        Method that plays the F3 file when the F3 key is clicked
        """
        pygame.mixer.music.load('F3.wav')
        self.play_note()

    def g3_pressed(self) -> None:
        """
        Method that plays the G3 file when the G3 key is clicked
        """
        pygame.mixer.music.load('G3.wav')
        self.play_note()

    def a3_pressed(self) -> None:
        """
        Method that plays the A3 file when the A3 key is clicked
        """
        pygame.mixer.music.load('A3.wav')
        self.play_note()

    def b3_pressed(self) -> None:
        """
        Method that plays the B3 file when the B3 key is clicked
        """
        pygame.mixer.music.load('B3.wav')
        self.play_note()

    def db3_pressed(self) -> None:
        """
        Method that plays the Db3 file when the Db3 key is clicked
        """
        pygame.mixer.music.load('Db3.wav')
        self.play_note()

    def eb3_pressed(self) -> None:
        """
        Method that plays the Eb3 file when the Eb3 key is clicked
        """
        pygame.mixer.music.load('Eb3.wav')
        self.play_note()

    def gb3_pressed(self) -> None:
        """
        Method that plays the Gb3 file when the Gb3 key is clicked
        """
        pygame.mixer.music.load('Gb3.wav')
        self.play_note()

    def ab3_pressed(self) -> None:
        """
        Method that plays the Ab3 file when the Ab3 key is clicked
        """
        pygame.mixer.music.load('Ab3.wav')
        self.play_note()

    def bb3_pressed(self) -> None:
        """
        Method that plays the Bb3 file when the Bb3 key is clicked
        """
        pygame.mixer.music.load('Bb3.wav')
        self.play_note()

    def c4_pressed(self) -> None:
        """
        Method that plays the C4 file when the C4 key is clicked
        """
        pygame.mixer.music.load('C4.wav')
        self.play_note()

    def d4_pressed(self) -> None:
        """
        Method that plays the D4 file when the D4 key is clicked
        """
        pygame.mixer.music.load('D4.wav')
        self.play_note()

    def e4_pressed(self) -> None:
        """
        Method that plays the E4 file when the E4 key is clicked
        """
        pygame.mixer.music.load('E4.wav')
        self.play_note()

    def f4_pressed(self) -> None:
        """
        Method that plays the F4 file when the F4 key is clicked
        """
        pygame.mixer.music.load('F4.wav')
        self.play_note()

    def g4_pressed(self) -> None:
        """
        Method that plays the G4 file when the G4 key is clicked
        """
        pygame.mixer.music.load('G4.wav')
        self.play_note()

    def a4_pressed(self) -> None:
        """
        Method that plays the A4 file when the A4 key is clicked
        """
        pygame.mixer.music.load('A4.wav')
        self.play_note()

    def b4_pressed(self) -> None:
        """
        Method that plays the B4 file when the B4 key is clicked
        """
        pygame.mixer.music.load('B4.wav')
        self.play_note()

    def db4_pressed(self) -> None:
        """
        Method that plays the Db4 file when the Db4 key is clicked
        """
        pygame.mixer.music.load('Db4.wav')
        self.play_note()

    def eb4_pressed(self) -> None:
        """
        Method that plays the Eb4 file when the Eb4 key is clicked
        """
        pygame.mixer.music.load('Eb4.wav')
        self.play_note()

    def gb4_pressed(self) -> None:
        pygame.mixer.music.load('Gb4.wav')
        self.play_note()

    def ab4_pressed(self) -> None:
        """
        Method that plays the Ab4 file when the Ab4 key is clicked
        """
        pygame.mixer.music.load('Ab4.wav')
        self.play_note()

    def bb4_pressed(self) -> None:
        """
        Method that plays the Bb4 file when the Bb4 key is clicked
        """
        pygame.mixer.music.load('Bb4.wav')
        self.play_note()

    def c5_pressed(self) -> None:
        """
        Method that plays the C5 file when the C5 key is clicked
        """
        pygame.mixer.music.load('C5.wav')
        self.play_note()

    def d5_pressed(self) -> None:
        """
        Method that plays the D5 file when the D5 key is clicked
        """
        pygame.mixer.music.load('D5.wav')
        self.play_note()

    def e5_pressed(self) -> None:
        """
        Method that plays the E5 file when the E5 key is clicked
        """
        pygame.mixer.music.load('E5.wav')
        self.play_note()

    def f5_pressed(self) -> None:
        """
        Method that plays the F5 file when the F5 key is clicked
        """
        pygame.mixer.music.load('F5.wav')
        self.play_note()

    def g5_pressed(self) -> None:
        """
        Method that plays the G5 file when the G5 key is clicked
        """
        pygame.mixer.music.load('G5.wav')
        self.play_note()

    def a5_pressed(self) -> None:
        """
        Method that plays the A5 file when the A5 key is clicked
        """
        pygame.mixer.music.load('A5.wav')
        self.play_note()

    def b5_pressed(self) -> None:
        """
        Method that plays the B5 file when the B5 key is clicked
        """
        pygame.mixer.music.load('B5.wav')
        self.play_note()

    def db5_pressed(self) -> None:
        """
        Method that plays the Db5 file when the Db5 key is clicked
        """
        pygame.mixer.music.load('Db5.wav')
        self.play_note()

    def eb5_pressed(self) -> None:
        """
        Method that plays the Eb5 file when the Eb5 key is clicked
        """
        pygame.mixer.music.load('Eb5.wav')
        self.play_note()

    def gb5_pressed(self) -> None:
        """
        Method that plays the Gb5 file when the Gb5 key is clicked
        """
        pygame.mixer.music.load('Gb5.wav')
        self.play_note()

    def ab5_pressed(self) -> None:
        """
        Method that plays the Ab5 file when the Ab5 key is clicked
        """
        pygame.mixer.music.load('Ab5.wav')
        self.play_note()

    def bb5_pressed(self) -> None:
        """
        Method that plays the Bb5 file when the Bb5 key is clicked
        """
        pygame.mixer.music.load('Bb5.wav')
        self.play_note()

    def c6_pressed(self) -> None:
        """
        Method that plays the C6 file when the C6 key is clicked
        """
        pygame.mixer.music.load('C6.wav')
        self.play_note()
