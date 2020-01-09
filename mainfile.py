import sys

from PyQt5.QtCore import QRect, QPoint
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui_file import Ui_MainWindow
from ui_file2 import Ui_MainWindow2
from ui_file3 import Ui_MainWindow3

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sqlite3
import random
from PyQt5 import QtGui


class MainWindow(QMainWindow, Ui_MainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openfunction)

    def openfunction(self):
        self.second_form = SecondWindow(self)
        self.second_form.show()





class SecondWindow(QMainWindow, Ui_MainWindow2):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.closefunction)
        self.pushButton_2.clicked.connect(self.openfunction1)
        self.pushButton_4.clicked.connect(self.openfunction2)
        self.pushButton_3.clicked.connect(self.openfunction3)

    def closefunction(self):
        self.close()

    def openfunction1(self):
        self.second_form = ThirdWindow(self)
        self.second_form.show()
        self.close()


    def openfunction2(self):
        self.third_form = ToweroneWindow(self)
        self.third_form.show()
        self.close()

    def openfunction3(self):
        self.fourth_form = TronWindow(self)
        self.fourth_form.show()
        self.close()


class ThirdWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton.clicked.connect(self.closefunction)
        self.pushButton_2.clicked.connect(self.openfunction1)
        self.pushButton_3.clicked.connect(self.openfunction2)


        pixmap = QPixmap('Podzemele_11-1180x664.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)


    def closefunction(self):
        self.close()

    def openfunction1(self):
        self.second_form = ForthWindow(self)
        self.second_form.show()
        self.close()

    def openfunction2(self):
        self.second_form = FifthWindow(self)
        self.second_form.show()
        self.close()





class ForthWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton.clicked.connect(self.closefunction)
        self.pushButton_2.clicked.connect(self.openfunction1)
        self.pushButton_3.clicked.connect(self.openfunction2)
        pixmap = QPixmap('cropped-metal-and-stone-spiral-staircase-1024x614.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''С каждым шагом вы спускаетесь всё ниже и ниже. И вдруг начинаете слышать голоса. 
        Это голоса узников замка, которые заключены в подземельях. Вы можете спасти их. Но Стоит ли это делать? ''')
        self.pushButton_2.setText('Спасти')
        self.pushButton_3.setText('Подняться наверх')
        self.flag = True


    def closefunction(self):
        self.close()

    def openfunction1(self):
        self.second_form = SixWindow(self)
        self.second_form.show()
        self.close()

    def openfunction2(self):
        self.second_form = SevenWindow(self)
        self.second_form.show()
        self.close()


class FifthWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.closefunction)
        self.pushButton_2.clicked.connect(self.openfunction1)
        self.pushButton_3.clicked.connect(self.openfunction2)
        pixmap = QPixmap('qwert.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Перед вами Развилка. Куда пойдёте?''')
        self.pushButton_2.setText('Налево')
        self.pushButton_3.setText('Направо')
        self.flag = True

    def closefunction(self):
        self.close()

    def openfunction1(self):
        self.second_form = ForthWindow(self)
        self.second_form.show()
        self.close()

    def openfunction2(self):
        self.second_form = NewWindow(self)
        self.second_form.show()
        self.close()



class SixWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.closefunction)
        self.pushButton_2.clicked.connect(self.openfunction1)
        self.pushButton_3.clicked.connect(self.openfunction2)
        pixmap = QPixmap('565184067a7e2_DSC05695.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Они вам очень благодарны. Узники рассказали вам, что хозяин замка 
очень жесток и просто так вам не выбраться. Бежать с ними?''')
        self.pushButton_2.setText('Да')
        self.pushButton_3.setText('Нет')

    def closefunction(self):
        self.close()

    def openfunction1(self):
        self.second_form = EWindow(self)
        self.second_form.show()
        self.close()

    def openfunction2(self):
        self.second_form = NWindow(self)
        self.second_form.show()
        self.close()


class SevenWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.openfunction1)
        self.pushButton_2.clicked.connect(self.openfunction2)
        pixmap = QPixmap('3261190647_05e748b932_o.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Они в ярости. Вам приходится убежать и вы поднимаетесь наверх, перед вами двери тронного зала.''')
        self.pushButton_2.setText('Остаться')
        self.pushButton_3.setText('Бежать из замка')

    def closefunction(self):
        self.close()

    def openfunction1(self):
        self.second_form = TWindow(self)
        self.second_form.show()
        self.close()

    def openfunction2(self):
        self.second_form = TronWindow(self)
        self.second_form.show()
        self.close()


class EWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.closefunction)
        self.pushButton_2.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.closefunction)
        pixmap = QPixmap('499176_pole_razrushennyj-zamok_tuchi_pejzazh_4000x2500_www.Gde-Fon.com.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Вы сбежали вместе с заключенными из замка. они спасли вам жизнь.
Вы решили никогда больше не возвращиться в тот замок. И правильно сделали.''')
        self.pushButton_2.setText('Завершить')
        self.pushButton_3.setText('Завершить')

    def closefunction(self):
        self.close()

class NWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pushButton.clicked.connect(self.closefunction)
        self.pushButton_2.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.closefunction)
        pixmap = QPixmap('1441290094_dungeon-cave-hydra.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Очень жаль. Ведь позже в подземелье вам вас укусила змея и вы мучительно погибли.''')
        self.pushButton_2.setText('Завершить')
        self.pushButton_3.setText('Завершить')

    def closefunction(self):
        self.close()

class ToweroneWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.openfunction1)
        self.pushButton_3.clicked.connect(self.openfunction2)
        pixmap = QPixmap('preview.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''В башне Дракон охраняет принцессу. Вы можете сразиться с драконом или спусться в тронный зал''')
        self.pushButton_2.setText('Сразиться')
        self.pushButton_3.setText('Бежать')

    def openfunction1(self):
        self.second_form = PrinWindow(self)
        self.second_form.show()
        self.close()

    def openfunction2(self):
        self.second_form = StWindow(self)
        self.second_form.show()
        self.close()


class TWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.closefunction)
        pixmap = QPixmap('unnamed.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Вы сбежали из замка. На этом квест завершён.''')
        self.pushButton_2.setText('Завершить')
        self.pushButton_3.setText('Завершить')

    def closefunction(self):
        self.close()

class PrinWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.openfunction1)
        self.pushButton_3.clicked.connect(self.openfunction2)
        pixmap = QPixmap('the-alluring-charm-of-15th-century-antique-elm-chests-31-BI1.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Вы победили дракона. Перед вами открылась тайная комната. В ней стоит очень странный сундук.''')
        self.pushButton_2.setText('Открыть')
        self.pushButton_3.setText('Уйти')

    def closefunction(self):
        self.close()

    def openfunction1(self):
        self.second_form = TrWindow(self)
        self.second_form.show()
        self.close()

    def openfunction2(self):
        self.second_form = TronWindow(self)
        self.second_form.show()
        self.close()

class StWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.closefunction)
        pixmap = QPixmap('i.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Вы бежали вниз по скользкой лестнице и упали.
очень жаль но вам не удалось выбраться живым из замка.''')
        self.pushButton_2.setText('Завершить')
        self.pushButton_3.setText('Завершить')

    def closefunction(self):
        self.close()

class TrWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.closefunction)
        pixmap = QPixmap('rare-horror-movies.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Вы открыли Сундук, я он оказался полон сокровищами.
Но всё не так просто, ведь сундук, кроме дракона охранял скелет, он убивает вас. Лучше бы вы бежали.''')
        self.pushButton_2.setText('Завершить')
        self.pushButton_3.setText('Завершить')

    def closefunction(self):
        self.close()


class TronWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.openfunction1)
        self.pushButton_3.clicked.connect(self.openfunction2)
        pixmap = QPixmap('8c7d7a5090d9c5ee07f6ba86e061ac4e.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''После всех испытаний вы попали в тронный зал. Там вас уже ждёт король со своей стражей.
Он наслышен о ваших приключениях и просит вас об услуге.''')
        self.pushButton_2.setText('Помочь королю')
        self.pushButton_3.setText('Отказать')

    def closefunction(self):
        self.close()

    def openfunction1(self):
        self.second_form = HelpWindow(self)
        self.second_form.show()
        self.close()

    def openfunction2(self):
        self.second_form = PrisonWindow(self)
        self.second_form.show()
        self.close()


class HelpWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.openfunction1)
        self.pushButton_3.clicked.connect(self.openfunction2)
        pixmap = QPixmap('22.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Вы решили помочь королю. Он просит спасти его дочь. Она заколдована.
Чтобы ее вылечить нужно приготовить зелье. Вы умеете?''')
        self.pushButton_2.setText('Да')
        self.pushButton_3.setText('Нет')

    def closefunction(self):
        self.close()

    def openfunction1(self):
        self.second_form = ZWindow(self)
        self.second_form.show()
        self.close()

    def openfunction2(self):
        self.second_form = EndWindow(self)
        self.second_form.show()
        self.close()


class PrisonWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.closefunction)
        pixmap = QPixmap('prison_by_gregmks-d30mry0.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Очень жаль. Король не любит отказов. Вас схватили и отправили в темницу.
Завтра на рассвете вы будете казнены.''')
        self.pushButton_2.setText('Завершить')
        self.pushButton_3.setText('Завершить')

    def closefunction(self):
        self.close()

class ZWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.closefunction)
        pixmap = QPixmap('happy-end.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Вам повезло. Вы спасаете принцессу. Король отдаёт её вам в жёны
и вы наследник всего королевства!''')
        self.pushButton_2.setText('Завершить')
        self.pushButton_3.setText('Завершить')

    def closefunction(self):
        self.close()


class EndWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.closefunction)
        pixmap = QPixmap('24869_1054353600.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Король в ярости, из-за того, что вы его подвели.
Вас выгнали из замка, но вы хотя бы живы.''')
        self.pushButton_2.setText('Завершить')
        self.pushButton_3.setText('Завершить')

    def closefunction(self):
        self.close()

class NewWindow(QMainWindow, Ui_MainWindow3):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.flag = False
        self.pushButton_2.clicked.connect(self.closefunction)
        self.pushButton_3.clicked.connect(self.closefunction)
        pixmap = QPixmap('2294958-8XPU3.jpg')
        cw, ch = 641, 551
        iw = pixmap.width()
        ih = pixmap.height()

        if iw / cw < ih / ch:
            pixmap = pixmap.scaledToWidth(cw)
            hoff = (pixmap.height() - ch) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(0, hoff), QPoint(cw, pixmap.height() - hoff))
            )

        elif iw / cw > ih / ch:
            pixmap = pixmap.scaledToHeight(ch)
            woff = (pixmap.width() - cw) // 2
            pixmap = pixmap.copy(
                QRect(QPoint(woff, 0), QPoint(pixmap.width() - woff, ch))
            )
        self.label.setPixmap(pixmap)
        self.textEdit.setText('''Ой, а тут ловушка. Вас поймали стражи замка. Теперь бежать уже не получиться.''')
        self.pushButton_2.setText('Завершить')
        self.pushButton_3.setText('Завершить')

    def closefunction(self):
        self.close()
app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec_())
