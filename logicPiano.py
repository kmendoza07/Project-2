import pygame.mixer
from PyQt6.QtWidgets import *
from guiPiano import *
from pygame import mixer


class Logic(QMainWindow, Ui_MainWindow):

    # WHITE_NOTES = ['C2','D2','E2', 'F2', 'G2', 'A2', 'B2',
    #                'C3','D3','E3', 'F3', 'G3', 'A3', 'B3',
    #                'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
    #                'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5',
    #                'C6']
    #
    # BLACK_NOTES = ['Db2', 'Eb2', 'Gb2', 'Ab2', 'Bb2',
    #                'Db3','Eb3', 'Gb3', 'Ab3', 'Bb3',
    #                'Db4', 'Eb4', 'Gb4', 'Ab4', 'Bb4',
    #                'Db5', 'Eb5', 'Gb5', 'Ab5', 'Bb5']

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        pygame.mixer.init()

        self.record_value = False
        self.stop_value = True
        self.play_value = False

        # self.buttonRecord.clicked.connect(lambda: self.record())
        # self.buttonStop.clicked.connect(lambda: self.stop())

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

    def play_note(self):
        pygame.mixer.music.play()

    def c2_pressed(self):
        pygame.mixer.music.load('C2.wav')
        self.play_note()

    def d2_pressed(self):
        pygame.mixer.music.load('D2.wav')
        self.play_note()

    def e2_pressed(self):
        pygame.mixer.music.load('E2.wav')
        self.play_note()

    def f2_pressed(self):
        pygame.mixer.music.load('F2.wav')
        self.play_note()

    def g2_pressed(self):
        pygame.mixer.music.load('G2.wav')
        self.play_note()

    def a2_pressed(self):
        pygame.mixer.music.load('A2.wav')
        self.play_note()

    def b2_pressed(self):
        pygame.mixer.music.load('B2.wav')
        self.play_note()

    def db2_pressed(self):
        pygame.mixer.music.load('Db2.wav')
        self.play_note()

    def eb2_pressed(self):
        pygame.mixer.music.load('Eb2.wav')
        self.play_note()

    def gb2_pressed(self):
        pygame.mixer.music.load('Gb2.wav')
        self.play_note()

    def ab2_pressed(self):
        pygame.mixer.music.load('Ab2.wav')
        self.play_note()

    def bb2_pressed(self):
        pygame.mixer.music.load('Bb2.wav')
        self.play_note()

    def c3_pressed(self):
        pygame.mixer.music.load('C3.wav')
        self.play_note()

    def d3_pressed(self):
        pygame.mixer.music.load('D3.wav')
        self.play_note()

    def e3_pressed(self):
        pygame.mixer.music.load('E3.wav')
        self.play_note()

    def f3_pressed(self):
        pygame.mixer.music.load('F3.wav')
        self.play_note()

    def g3_pressed(self):
        pygame.mixer.music.load('G3.wav')
        self.play_note()

    def a3_pressed(self):
        pygame.mixer.music.load('A3.wav')
        self.play_note()

    def b3_pressed(self):
        pygame.mixer.music.load('B3.wav')
        self.play_note()

    def db3_pressed(self):
        pygame.mixer.music.load('Db3.wav')
        self.play_note()

    def eb3_pressed(self):
        pygame.mixer.music.load('Eb3.wav')
        self.play_note()

    def gb3_pressed(self):
        pygame.mixer.music.load('Gb3.wav')
        self.play_note()

    def ab3_pressed(self):
        pygame.mixer.music.load('Ab3.wav')
        self.play_note()

    def bb3_pressed(self):
        pygame.mixer.music.load('Bb3.wav')
        self.play_note()

    def c4_pressed(self):
        pygame.mixer.music.load('C4.wav')
        self.play_note()

    def d4_pressed(self):
        pygame.mixer.music.load('D4.wav')
        self.play_note()

    def e4_pressed(self):
        pygame.mixer.music.load('E4.wav')
        self.play_note()

    def f4_pressed(self):
        pygame.mixer.music.load('F4.wav')
        self.play_note()

    def g4_pressed(self):
        pygame.mixer.music.load('G4.wav')
        self.play_note()

    def a4_pressed(self):
        pygame.mixer.music.load('A4.wav')
        self.play_note()

    def b4_pressed(self):
        pygame.mixer.music.load('B4.wav')
        self.play_note()

    def db4_pressed(self):
        pygame.mixer.music.load('Db4.wav')
        self.play_note()

    def eb4_pressed(self):
        pygame.mixer.music.load('Eb4.wav')
        self.play_note()

    def gb4_pressed(self):
        pygame.mixer.music.load('Gb4.wav')
        self.play_note()

    def ab4_pressed(self):
        pygame.mixer.music.load('Ab4.wav')
        self.play_note()

    def bb4_pressed(self):
        pygame.mixer.music.load('Bb4.wav')
        self.play_note()

    def c5_pressed(self):
        pygame.mixer.music.load('C5.wav')
        self.play_note()

    def d5_pressed(self):
        pygame.mixer.music.load('D5.wav')
        self.play_note()

    def e5_pressed(self):
        pygame.mixer.music.load('E5.wav')
        self.play_note()

    def f5_pressed(self):
        pygame.mixer.music.load('F5.wav')
        self.play_note()

    def g5_pressed(self):
        pygame.mixer.music.load('G5.wav')
        self.play_note()

    def a5_pressed(self):
        pygame.mixer.music.load('A5.wav')
        self.play_note()

    def b5_pressed(self):
        pygame.mixer.music.load('B5.wav')
        self.play_note()

    def db5_pressed(self):
        pygame.mixer.music.load('Db5.wav')
        self.play_note()

    def eb5_pressed(self):
        pygame.mixer.music.load('Eb5.wav')
        self.play_note()

    def gb5_pressed(self):
        pygame.mixer.music.load('Gb5.wav')
        self.play_note()

    def ab5_pressed(self):
        pygame.mixer.music.load('Ab5.wav')
        self.play_note()

    def bb5_pressed(self):
        pygame.mixer.music.load('Bb5.wav')
        self.play_note()

    def c6_pressed(self):
        pygame.mixer.music.load('C6.wav')
        self.play_note()
    # def load_music(self):
    #     for i in self.WHITE_NOTES:
    #         pygame.mixer.music.load(f'{i}.wav')
    #     for i in self.BLACK_NOTES:
    #         pygame.mixer.music.load(f'{i}.wav')
    #
    # def c2_pressed(self):
    #     #playsound("audioPianoNotes/C2.wav")
    #     # if self.record_value == True:
    #     #     with open('music_sheet.txt', 'a') as music_sheet:
    #     #         music_sheet.write('C2')
    #
    # def record(self):
    #     if self.record_status == False:
    #         self.record_status = True
    #         self.stop_value = False
    #     else:
    #         self.record_status = False
    #         self.stop_value = True
    #
    # def stop(self):
    #     if self.stop_value == True:
    #         self.stop_value = False
    #         self.play_value = True
    #     else:
    #         self.stop_value = True
    #         self.play_value = False
    #
    # def music_sheet(self):
    #     while self.record_status == True:
    #         with open('music_sheet.txt', 'w') as music_sheet:
    #             pass
    #
