import sys
from PySide6.QtWidgets import (
    QApplication,  # app principal
    QWidget,       # ventana base
    QLabel,        # etiqueta de texto o imagen
    QPushButton,   # botón
    QLineEdit,     # campo de texto (una línea)
    QVBoxLayout,   # layout vertical
    QHBoxLayout   # layout horizontal
)
app = QApplication(sys.argv)
from PySide6.QtCore import Qt

#**********************************************************

# INTERFAZ
pantalla = QWidget()
pantalla.setWindowTitle("INVERTIR MATRICES")
pantalla.setFixedSize(300,300)
pantalla.setStyleSheet("background-color: lightgreen")

layout_principal = QVBoxLayout()
layout_p1 = QVBoxLayout()


L1 = QLabel("INVERTIR MATRIZ")
L1.setStyleSheet("""
    color: black;
    font-weight: bold;
    text-align: center;
    font-size : 15px;
    padding: 5px;
""")
L1.setAlignment(Qt.AlignCenter)
L1.setFixedSize(275,40)

layout_f1 = QHBoxLayout()
layout_f2 = QHBoxLayout()
layout_f3 = QHBoxLayout()

a11 = QLineEdit()
a11.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 20px")
a11.setFixedSize(85, 55)
a11.setAlignment(Qt.AlignCenter)

a12 = QLineEdit()
a12.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 20px")
a12.setFixedSize(85, 55)
a12.setAlignment(Qt.AlignCenter)

a13 = QLineEdit()
a13.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 20px")
a13.setFixedSize(85, 55)
a13.setAlignment(Qt.AlignCenter)

a21 = QLineEdit()
a21.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 20px")
a21.setFixedSize(85, 55)
a21.setAlignment(Qt.AlignCenter)

a22 = QLineEdit()
a22.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 20px")
a22.setFixedSize(85, 55)
a22.setAlignment(Qt.AlignCenter)

a23 = QLineEdit()
a23.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 20px")
a23.setFixedSize(85, 55)
a23.setAlignment(Qt.AlignCenter)

a31 = QLineEdit()
a31.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 20px")
a31.setFixedSize(85, 55)
a31.setAlignment(Qt.AlignCenter)

a32 = QLineEdit()
a32.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 20px")
a32.setFixedSize(85, 55)
a32.setAlignment(Qt.AlignCenter)

a33 = QLineEdit()
a33.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 20px")
a33.setFixedSize(85, 55)
a33.setAlignment(Qt.AlignCenter)

layout_f1.addWidget(a11)
layout_f1.addWidget(a12)
layout_f1.addWidget(a13)

layout_f2.addWidget(a21)
layout_f2.addWidget(a22)
layout_f2.addWidget(a23)

layout_f3.addWidget(a31)
layout_f3.addWidget(a32)
layout_f3.addWidget(a33)

layout_p1.addLayout(layout_f1)
layout_p1.addLayout(layout_f2)
layout_p1.addLayout(layout_f3)

btn_invertir = QPushButton("INVERTIR")
btn_invertir.setStyleSheet("background-color: lightblue; font-weight: bold; font-size: 15px")
btn_invertir.setFixedSize(275,40)

layout_principal.addWidget(L1)
layout_principal.addLayout(layout_p1)
layout_principal.addWidget(btn_invertir)

pantalla.setLayout(layout_principal)
#**********************************************************

#INVERTIR




#**********************************************************
pantalla.show()
app.exec()