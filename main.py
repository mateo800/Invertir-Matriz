import sys
from PySide6.QtWidgets import (
    QApplication,  # app principal
    QWidget,       # ventana base
    QLabel,        # etiqueta de texto o imagen
    QPushButton,   # botón
    QLineEdit,     # campo de texto (una línea)
    QVBoxLayout,   # layout vertical
    QHBoxLayout,   # layout horizontal
)
app = QApplication(sys.argv)
from PySide6.QtCore import Qt
from fractions import Fraction
#**********************************************************

# INTERFAZ
pantalla = QWidget()
pantalla.setWindowTitle("INVERTIR MATRICES")
pantalla.setFixedSize(300,330)
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

L2 = QLabel("")
L2.setStyleSheet("""
    color: black;
    font-weight: bold;
    text-align: center;
    font-size : 10px;
    padding: 5px;
""")

layout_f1 = QHBoxLayout()
layout_f2 = QHBoxLayout()
layout_f3 = QHBoxLayout()

a11 = QLineEdit()
a11.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 12px")
a11.setFixedSize(85, 55)
a11.setMaxLength(8)
a11.setAlignment(Qt.AlignCenter)

a12 = QLineEdit()
a12.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 12px")
a12.setFixedSize(85, 55)
a12.setMaxLength(8)
a12.setAlignment(Qt.AlignCenter)

a13 = QLineEdit()
a13.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 12px")
a13.setFixedSize(85, 55)
a13.setMaxLength(8)
a13.setAlignment(Qt.AlignCenter)

a21 = QLineEdit()
a21.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 12px")
a21.setFixedSize(85, 55)
a21.setMaxLength(8)
a21.setAlignment(Qt.AlignCenter)

a22 = QLineEdit()
a22.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 12px")
a22.setFixedSize(85, 55)
a22.setMaxLength(8)
a22.setAlignment(Qt.AlignCenter)

a23 = QLineEdit()
a23.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 12px")
a23.setFixedSize(85, 55)
a23.setMaxLength(8)
a23.setAlignment(Qt.AlignCenter)

a31 = QLineEdit()
a31.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 12px")
a31.setFixedSize(85, 55)
a31.setMaxLength(8)
a31.setAlignment(Qt.AlignCenter)

a32 = QLineEdit()
a32.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 12px")
a32.setFixedSize(85, 55)
a32.setMaxLength(8)
a32.setAlignment(Qt.AlignCenter)

a33 = QLineEdit()
a33.setStyleSheet("background-color: lightgray; font-weight: bold; font-size: 12px")
a33.setFixedSize(85, 55)
a33.setMaxLength(8)
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
layout_principal.addWidget(L2)

pantalla.setLayout(layout_principal)
#**********************************************************

#INVERTIR
def invertir():
    try: 
        if int(a11.text()) == 5  or int(a12.text()) == 5 or int(a13.text()) == 5 or int(a21.text()) == 5 or int(a22.text()) == 5 or int(a23.text()) == 5 or int(a31.text()) == 5 or int(a32.text()) == 5 or int(a33.text()) == 5:
            pass

        determinante = 1
        L2.setText("")

        t11 = int(a11.text())
        t12 = int(a12.text())
        t13 = int(a13.text())
        t21 = int(a21.text())
        t22 = int(a22.text())
        t23 = int(a23.text())
        t31 = int(a31.text())
        t32 = int(a32.text())
        t33 = int(a33.text())

        determinante = (t11 * t22 * t33) + (t12 * t23 * t31) + (t13 * t21 * t32) - (t31 * t22 * t13) - (t32 * t23 * t11) - (t33 * t21 * t12)
        
        if determinante == 0:
            L2.setText(f"Esta matriz no es invertible")
        else:
            cof11 = (t22 * t33) - (t32 * t23) 
            cof12 = ( (t21 * t33) - (t31 * t23) ) * -1
            cof13 = (t21 * t32) - (t31 * t22) 
            cof21 = ( (t12 * t33) - (t32 * t13) ) * -1 
            cof22 = (t11 * t33) - (t31 * t13) 
            cof23 = ( (t11 * t32) - (t31 * t12) ) * -1
            cof31 = (t12 * t23) - (t22 * t13) 
            cof32 = ( (t11 * t23) - (t21 * t13) ) * -1
            cof33 = (t11 * t22) - (t21 * t12) 

            r11 = cof11 / determinante
            r12 = cof21 / determinante
            r13 = cof31 / determinante
            r21 = cof12 / determinante
            r22 = cof22 / determinante
            r23 = cof32 / determinante
            r31 = cof13 / determinante
            r32 = cof23 / determinante
            r33 = cof33 / determinante

            a11.setText(str(Fraction(r11).limit_denominator()))
            a11.setReadOnly(True)

            a12.setText(str(Fraction(r12).limit_denominator()))
            a12.setReadOnly(True)

            a13.setText(str(Fraction(r13).limit_denominator()))
            a13.setReadOnly(True)

            a21.setText(str(Fraction(r21).limit_denominator()))
            a21.setReadOnly(True)

            a22.setText(str(Fraction(r22).limit_denominator()))
            a22.setReadOnly(True)

            a23.setText(str(Fraction(r23).limit_denominator()))
            a23.setReadOnly(True)

            a31.setText(str(Fraction(r31).limit_denominator()))
            a31.setReadOnly(True)

            a32.setText(str(Fraction(r32).limit_denominator()))
            a32.setReadOnly(True)

            a33.setText(str(Fraction(r33).limit_denominator()))
            a33.setReadOnly(True)

            btn_invertir.setEnabled(False)
            L2.setText(f"Matriz invertida")

    except Exception as e:
        L2.setText(f"Solo puedes poner numeros enteros \nY debes llenar todos los espacios")

#**********************************************************
btn_invertir.clicked.connect(invertir)
pantalla.show()
app.exec()