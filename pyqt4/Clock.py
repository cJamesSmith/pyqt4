import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = 'Alert!'
    if len(sys.argv) < 2:
        raise(ValueError)
    hours, mins = sys.argv[1].split(':')
    due = QTime(int(hours), int(mins))
    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = ' '.join(sys.argv[2:])
except ValueError:
    message = 'Usage: alert.pyw HH:MM [optional message]'# 24hr clock

while QTime.currentTime() < due:
    time.sleep(20)
    lable = QLabel('<font color=red size=72><b>' + message + '</b></font>')
    lable.setWindowTitle('Alert!')
    lable.show()
    QTimer.singleShot(60, app.quit)
    app.exec_()