import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from PyQt5 import uic, QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from time import sleep



class MainWindow(QMainWindow):
	"""docstring for MainWindow"""
	def __init__(self):
		super(MainWindow, self).__init__()
		uic.loadUi('webbrowser.ui', self)
		self.btnGO.clicked.connect(self.onClick)

	def onClick(self):
		print('btnGO pressed.')
		print(self.edtURL.text())
		self.webEngineView.load(QUrl.fromUserInput(self.edtURL.text()))

if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec())