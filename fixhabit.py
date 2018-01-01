#!/usr/bin/python3
# pylint: disable=fixme, line-too-long
# Initialize PyQT
from PyQt5.QtCore import QSettings, QTimer, Qt
from PyQt5.QtGui import QCursor, QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QApplication
# The fondamental for working with python
import os, sys, signal, argparse, json
from time import strftime, localtime
from datetime import datetime
from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    # Create settings for the software
    settings = QSettings('Mte90', 'FixHabit')
    settings.setFallbacksEnabled(False)
    path = os.path.dirname(sys.argv[0]) + '/'
    version = '1.0'
    appname = 'FixHabit - ' + version + ' by Mte90'

    def __init__(self, parent=None):
        #http://pythonadventures.wordpress.com/2013/01/10/launch-just-one-instance-of-a-qt-application/
        wid = self.get_pid()
        if_focus = os.popen('xdotool getactivewindow').readlines()
        # hide if the window have focues when executed again
        if if_focus[0] == wid:
            os.system('xdotool windowunmap "' + str(wid) + '"')
            sys.exit()
        # Software already opened
        if wid:
            # Show
            os.system('xdotool windowmap ' + str(wid))
            # get focus
            os.system('xdotool windowactivate ' + str(wid))
            move_under_cursor()
            sys.exit()
        else:
            # Load the ui
            QMainWindow.__init__(self, parent)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            # Set the MainWindow Title
            self.setWindowTitle(self.appname)
            # Connect the function with the signal
            self.ui.remind.clicked.connect(self.openRemind)
            # When the software are closed on console the software are closed
            signal.signal(signal.SIGINT, signal.SIG_DFL)
            # Add hide parameter
            parser = argparse.ArgumentParser()
            parser.add_argument("--hide", help="hide the window at startup", action="store_true")
            args = parser.parse_args()
            self.data = json.load(open(self.path + 'config.json'))
            self.ui.bootTime.setText('Boot time: ' + strftime("%Y-%m-%d %H:%M", localtime()))
            now = datetime.strptime(strftime("%Y/%m/%d", localtime()), "%Y/%m/%d")
            defined = datetime.strptime(self.data['startDate'], "%Y/%m/%d")
            delta = defined - now
            self.ui.bootTime.setStyleSheet("QLabel { color : red; }")
            if delta.days > self.data['congratsTime']:
                self.ui.bootTime.setStyleSheet("QLabel { color : green; }")
            if self.data['remindMe']:
                self.ui.remind.setText('Remind in ' + str(int(self.data['remindMe'])/60) + ' minutes')
                self.openRemind(parent)
            # Show the form
            self.loadTasks()
            self.show()
            if not args.hide:
                move_under_cursor()
            else:
                wid = self.get_pid()
                os.popen('xdotool windowunmap "' + str(wid) + '"')

    def loadTasks(self):
        # get project tasks
        qsubtasks = QStandardItemModel()
        for tasks in self.data['tasks']:
            item = QStandardItem(tasks['label'])
            try:
                if tasks['script']:
                    os.popen(tasks['script'])
            except:
                pass
            check = Qt.Unchecked
            try:
                if tasks['check'] == "true":
                    check = Qt.Checked
            except:
                pass
            item.setCheckState(check)
            item.setCheckable(True)
            # populate the listview
            qsubtasks.appendRow(item)
        self.ui.taskLists.setModel(qsubtasks)

    def get_pid(self):
        wid = os.popen('xdotool search --name "' + self.appname + '"').readlines()
        # Check if multiple rows output
        if len(wid) > 0:
            wid = wid[0]
        return wid

    def openRemind(self, parent):
        self.hide()
        self.timer = QTimer(self)
        self.timer.start(int(self.data['remindMe']) * 1000)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.showWindow)

    def showWindow(self):
        self.show()


def move_under_cursor():
    mouse = QCursor.pos()
    os.system('xdotool getactivewindow windowmove ' + str(mouse.x() - 50) + ' ' + str(mouse.y() - 50))


def main():
    # Start the software
    app = QApplication(sys.argv)
    MainWindow_ = QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow_)
    # Add the close feature at the program with the X
    sys.exit(app.exec_())


# Execute the software
main()
