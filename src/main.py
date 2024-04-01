import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLCDNumber, QLabel

from components.lexica import MyLexer
from components.parsers import MyParser
from components.translator import MyTranslator

class MainWindow(QMainWindow):

    # Do this for intellisense
    button_0:QPushButton
    button_1:QPushButton
    button_2:QPushButton
    button_3:QPushButton
    button_4:QPushButton
    button_5:QPushButton
    button_6:QPushButton
    button_7:QPushButton
    button_8:QPushButton
    button_9:QPushButton
    button_plus:QPushButton
    button_multiply:QPushButton
    button_lp:QPushButton
    button_rp:QPushButton
    button_equal:QPushButton
    button_clear:QPushButton
    input_text:QLineEdit
    output_lcd:QLCDNumber
    pre_notation:QLabel
    post_notation:QLabel

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("components/main.ui", self)

        #### Binding button to function ####
        self.button_0.clicked.connect(lambda: self.push("0"))
        self.button_1.clicked.connect(lambda: self.push("1"))
        self.button_2.clicked.connect(lambda: self.push("2"))
        self.button_3.clicked.connect(lambda: self.push("3"))
        self.button_4.clicked.connect(lambda: self.push("4"))
        self.button_5.clicked.connect(lambda: self.push("5"))
        self.button_6.clicked.connect(lambda: self.push("6"))
        self.button_7.clicked.connect(lambda: self.push("7"))
        self.button_8.clicked.connect(lambda: self.push("8"))
        self.button_9.clicked.connect(lambda: self.push("9"))
        
        self.button_plus.clicked.connect(lambda: self.push("+"))
        self.button_multiply.clicked.connect(lambda: self.push("*"))

        self.button_lp.clicked.connect(lambda: self.push("("))
        self.button_rp.clicked.connect(lambda: self.push(")"))

        self.button_equal.clicked.connect(self.push_equal)
        self.button_clear.clicked.connect(self.push_clear)

    def push(self, text:str):
        current_text:str = self.input_text.text()
        self.input_text.setText(f"{current_text}{text}")
    
    def push_equal(self):
        lexer = MyLexer()
        parser = MyParser()
        input_text = self.input_text.text()
        if not input_text:
            result = 0
            self.pre_notation.clear()
            self.post_notation.clear()
        else:
            result = parser.parse(lexer.tokenize(input_text))
            translator = MyTranslator()
            prefix, postfix = translator.translate(input_text)
            self.pre_notation.setText(prefix)
            self.post_notation.setText(postfix)
        self.output_lcd.display(result)

    def push_clear(self):
        self.input_text.setText("")
        self.output_lcd.display(0)
        self.pre_notation.setText("")
        self.post_notation.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()