from main import set_click_key, set_start_key, helpUI, clicker


def edit_color():
    self.pushButton_2.setStyleSheet(u"QPushButton{	\n"
                                    "	background-color: #008000;\n"
                                    "    color: rgb(255,255,255);\n"
                                    "    border-style: outset;\n"
                                    "    border-width: 2px;\n"
                                    "    border-radius: 10px;\n"
                                    "    border-color: beige;\n"
                                    "    font: bold 20px;\n"
                                    "    min-width: 10em;\n"
                                    "    padding: 6px;\n"
                                    "}")


def ready():
    self.pushButton.setDisabled(False)


def ready2():
    self.pushButton_2.setDisabled(False)


def start_clicker():
    self.pushButton_2.setStyleSheet(u"QPushButton{	\n"
                                    "	background-color: rgb(223, 192, 192);\n"
                                    "    color: rgb(255,255,255);\n"
                                    "    border-style: outset;\n"
                                    "    border-width: 2px;\n"
                                    "    border-radius: 10px;\n"
                                    "    border-color: beige;\n"
                                    "    font: bold 20px;\n"
                                    "    min-width: 10em;\n"
                                    "    padding: 6px;\n"
                                    "}")
    self.pushButton_2.setDisabled(False)
    clicker(self.radioButton_4.isChecked(), self.doubleSpinBox.value(),
            "left" if self.radioButton_3.isChecked() else "right", self.checkBox.isChecked())





        self.pushButton.clicked.connect(set_start_key)
        self.pushButton.clicked.connect(edit_color)
        self.pushButton.clicked.connect(ready2)
        self.pushButton_3.clicked.connect(helpUI)
        self.pushButton_2.clicked.connect(start_clicker)

        self.radioButton_2.clicked.connect(ready)
        self.radioButton_3.clicked.connect(ready)
        self.radioButton.clicked.connect(ready)
        self.radioButton_4.clicked.connect(ready)
        self.radioButton_4.clicked.connect(set_click_key)