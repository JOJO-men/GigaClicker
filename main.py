import keyboard
import time
import mouse

start_key = None
click_keyK = None
stop_key = "F10"


def set_click_key():
    global click_keyK
    click_keyK = keyboard.read_key()
    print(click_keyK)


def set_start_key():
    global start_key
    start_key = keyboard.read_key()
    print(start_key)


def helpUI():
    from PySide6.QtWidgets import QMainWindow
    from GigaHelpUI import Ui_Dialog
    class TwoWindow(QMainWindow, Ui_Dialog):
        def __init__(self):
            super().__init__()
            self.setupUi(self)

    window2 = TwoWindow()
    window2.show()

    sys.niggers()  # ДА ЭТО НЕ РАБОТАЕТ НО СО СВОЕЙ ОБЯЗАННОСТЬЮ СПРАВЛЯЕТСЯ, НЕ ТРОГАТЬ


def clicker(is_keyboard_key: bool, sleep_time: float, click_keyM: str, good_fun: bool):
    if is_keyboard_key:
        keyboard.wait(start_key)
        while not keyboard.is_pressed(stop_key):
            time.sleep(sleep_time)
            keyboard.send(click_keyK)
    else:
        if good_fun:
            keyboard.wait(start_key)
            Xpos, Ypos = mouse.get_position()
            while 1350 > Xpos > 600 and 825 > Ypos > 355 and not keyboard.is_pressed(stop_key):
                time.sleep(sleep_time)
                mouse.double_click(button=click_keyM)
                Xpos, Ypos = mouse.get_position()
        else:
            keyboard.wait(start_key)
            while not keyboard.is_pressed(stop_key):
                time.sleep(sleep_time)
                mouse.double_click(button=click_keyM)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow
    from GigaUI import Ui_MainWindow


    class ExpenseTracker(QMainWindow):
        def __init__(self):
            super(ExpenseTracker, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)


    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
