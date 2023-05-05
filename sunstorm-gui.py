import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton, QFileDialog, QGridLayout
from PyQt5.QtCore import Qt

class SunstormGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sunstorm GUI")

        # Create input fields
        self.ipsw_label = QLabel("IPSW Path:")
        self.ipsw_lineedit = QLineEdit()
        self.ipsw_button = QPushButton("Choose IPSW")
        self.ipsw_button.clicked.connect(self.browse_ipsw)

        self.blob_label = QLabel("Blob Path:")
        self.blob_lineedit = QLineEdit()
        self.blob_button = QPushButton("Choose Blob")
        self.blob_button.clicked.connect(self.browse_blob)

        self.kpp_checkbox = QCheckBox("KPP")
        self.restore_radio = QRadioButton("Restore")
        self.boardconfig_label = QLabel("Boardconfig:")
        self.boardconfig_lineedit = QLineEdit()
        self.boot_radio = QRadioButton("Boot")
        self.identifier_label = QLabel("Identifier:")
        self.identifier_lineedit = QLineEdit()
        self.identifier_lineedit.setEnabled(True)
        self.no_baseband_checkbox = QCheckBox("No baseband")

        self.execute_button = QPushButton("Execute")
        self.execute_button.clicked.connect(self.execute_command)

        # Create layout and add widgets
        layout = QGridLayout()
        layout.addWidget(self.ipsw_label, 0, 0)
        layout.addWidget(self.ipsw_lineedit, 0, 1)
        layout.addWidget(self.ipsw_button, 0, 2)
        layout.addWidget(self.blob_label, 1, 0)
        layout.addWidget(self.blob_lineedit, 1, 1)
        layout.addWidget(self.blob_button, 1, 2)
        layout.addWidget(self.kpp_checkbox, 2, 0)
        layout.addWidget(self.restore_radio, 3, 0)
        layout.addWidget(self.boardconfig_label, 4, 0)
        layout.addWidget(self.boardconfig_lineedit, 4, 1)
        layout.addWidget(self.boot_radio, 5, 0)
        layout.addWidget(self.identifier_label, 6, 0)
        layout.addWidget(self.identifier_lineedit, 6, 1)
        layout.addWidget(self.no_baseband_checkbox, 7, 0)
        layout.addWidget(self.execute_button, 8, 1)

        self.setLayout(layout)

    def browse_ipsw(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open IPSW File', '', 'IPSW Files (*.ipsw)')
        if file_path:
            self.ipsw_lineedit.setText(file_path)

    def browse_blob(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open Blob File', '', 'Blob Files (*.shsh2)')
        if file_path:
            self.blob_lineedit.setText(file_path)

    def execute_command(self):
        command = ['sudo', 'python3', './sunstorm.py', '-i', self.ipsw_lineedit.text(), '-t', self.blob_lineedit.text()]
        if self.kpp_checkbox.isChecked():
            command.append('--kpp')
        if self.restore_radio.isChecked():
            command.extend(['-r', '-d', self.boardconfig_lineedit.text()])
        if self.boot_radio.isChecked():
            command.extend(['-b', '-d', self.boardconfig_lineedit.text()])
        if self.identifier_lineedit.isEnabled() and self.identifier_lineedit.text():
            command.extend(['-id', self.identifier_lineedit.text()])
        if self.no_baseband_checkbox.isChecked():
            command.append('--skip-baseband')
        subprocess.run(command)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = SunstormGUI()
    gui.show()
    sys.exit(app.exec_())
