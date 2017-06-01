from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class Kalkulator(QWidget):
    def __init__(self, parent=None):
        super(Kalkulator, self).__init__(parent)
        self.interfejs()

    def interfejs(self):
        label1 = QLabel("Liczba 1:")
        label2 = QLabel("Liczba 2:", self)
        labelWynik = QLabel("Wynik:", self)

        ukladT = QGridLayout()
        ukladT.addWidget(label1, 0, 0)
        ukladT.addWidget(label2, 0, 1)
        ukladT.addWidget(labelWynik, 0, 2)

        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.setReadOnly(True)
        self.wynikEdt.setToolTip("Wpisz <b>liczby</b> i wybierz działanie...")

        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 1, 2)
        dodajBtn = QPushButton("Dodaj", self)
        odejmijBtn = QPushButton("Odejmij", self)
        dzielBtn = QPushButton("Podziel", self)
        mnozBtn = QPushButton("Pomnoz", self)
        koniecBtn = QPushButton("Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)

        self.setLayout(ukladT)

        koniecBtn.clicked.connect(self.koniec)
        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        mnozBtn.clicked.connect(self.dzialanie)
        dzielBtn.clicked.connect(self.dzialanie)

        self.setWindowIcon(QIcon('kalkulator.png'))
        self.liczba1Edt.setFocus()
        self.setGeometry(500, 500, 800, 400)
        self.setWindowTitle("Prosty kalkulator")
        self.show()

    def koniec(self):
        self.close()

    def closeEvent(self, event):
        odp = QMessageBox.question(self, "Komunikat", "Czy na pewno koniec?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def dzialanie(self):
        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = float(self.liczba2Edt.text())
            wynik = ""

            if nadawca.text() == "Dodaj":
                wynik = liczba1 + liczba2
            elif nadawca.text() == "Odejmij":
                wynik = liczba1 - liczba2
            elif nadawca.text() == "Pomnoz":
                wynik = liczba1 * liczba2
            elif nadawca.text() == "Podziel":
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(self, "Błąd", "Nie można dzielić przez zero!")
                    return
            else:
                pass

            self.wynikEdt.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    okno = Kalkulator()
    sys.exit(app.exec_())
