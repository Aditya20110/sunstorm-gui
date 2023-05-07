import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QRadioButton, QLineEdit, QPushButton, QFileDialog
import subprocess

class SunstormGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sunstorm GUI")
        self.setGeometry(100, 100, 400, 300)

        self.ipsw_label = QLabel("IPSW Path:", self)
        self.ipsw_label.setGeometry(10, 10, 100, 30)

        self.ipsw_path = QLineEdit(self)
        self.ipsw_path.setGeometry(120, 10, 180, 30)

        self.ipsw_button = QPushButton("Browse", self)
        self.ipsw_button.setGeometry(310, 10, 80, 30)
        self.ipsw_button.clicked.connect(self.select_ipsw)

        self.blob_label = QLabel("Blob Path:", self)
        self.blob_label.setGeometry(10, 50, 100, 30)

        self.blob_path = QLineEdit(self)
        self.blob_path.setGeometry(120, 50, 180, 30)

        self.blob_button = QPushButton("Browse", self)
        self.blob_button.setGeometry(310, 50, 80, 30)
        self.blob_button.clicked.connect(self.select_blob)

        self.kpp_checkbox = QCheckBox("KPP", self)
        self.kpp_checkbox.setGeometry(10, 100, 100, 30)

        self.restore_radio = QRadioButton("Restore", self)
        self.restore_radio.setGeometry(120, 100, 100, 30)
        self.restore_radio.toggled.connect(self.restore_toggled)

        self.boot_radio = QRadioButton("Boot", self)
        self.boot_radio.setGeometry(230, 100, 100, 30)

        self.boardconfig_label = QLabel("BoardConfig:", self)
        self.boardconfig_label.setGeometry(10, 150, 100, 30)

        self.boardconfig = QLineEdit(self)
        self.boardconfig.setGeometry(120, 150, 150, 30)

        self.identifier_label = QLabel("Identifier:", self)
        self.identifier_label.setGeometry(10, 190, 100, 30)

        self.identifier = QLineEdit(self)
        self.identifier.setGeometry(120, 190, 150, 30)
        self.identifier.setEnabled(False)

        self.baseband_checkbox = QCheckBox("No Baseband", self)
        self.baseband_checkbox.setGeometry(10, 230, 150, 30)

        self.generate_button = QPushButton("Start!", self)
        self.generate_button.setGeometry(120, 260, 150, 30)
        self.generate_button.clicked.connect(self.generate_command)

    def select_ipsw(self):
        options = QFileDialog.Options()
        ipsw_path, _ = QFileDialog.getOpenFileName(self, "Select IPSW", "", "IPSW Files (*.ipsw)", options=options)
        if ipsw_path:
            self.ipsw_path.setText(ipsw_path)

    def select_blob(self):
        options = QFileDialog.Options()
        blob_path, _ = QFileDialog.getOpenFileName(self, "Select Blob", "", "Blob Files (*.shsh2)", options=options)
        if blob_path:
            self.blob_path.setText(blob_path)

    def restore_toggled(self, checked):
        self.identifier.setEnabled(not checked)

    def generate_command(self):
        ipsw = self.ipsw_path.text()
        blob = self.blob_path.text()
        command = "sudo python3 sunstorm.py -i {} -t {}".format(ipsw, blob)

        if self.kpp_checkbox.isChecked():
            command += " --kpp"

        if self.restore_radio.isChecked():
            boardconfig = self.boardconfig.text()
            command += " -r -d {}".format(boardconfig)
        elif self.boot_radio.isChecked():
            boardconfig = self.boardconfig.text()
            command += " -b -d {} -id {}".format(boardconfig, self.identifier.text())

        if self.baseband_checkbox.isChecked():
            command += " --skip-baseband"

        print(command)  # Replace with the code to execute the command
        subprocess.call(command, shell=True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SunstormGUI()
    window.show()
    sys.exit(app.exec_())
