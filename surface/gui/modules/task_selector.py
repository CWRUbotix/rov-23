from PyQt5.QtWidgets import QWidget, QComboBox, QHBoxLayout, QLabel

class TaskSelector(QWidget):
    def __init__(self):
        super().__init__()

        layout: QHBoxLayout = QHBoxLayout()

        ## Add 'Task: ' label ##
        label: QLabel = QLabel()
        label.setText('Task: ')
        layout.addWidget(label)

        ## Add dropdown ##
        # Create PyQt element
        self.comboBox: QComboBox = QComboBox()
        self.comboBox.addItem('Manual Control')
        self.comboBox.addItem('Auto Docking')
        self.comboBox.addItem('Coral Modeling')
        layout.addWidget(self.comboBox)

        # Connect signals
        self.comboBox.currentIndexChanged.connect(self.userChangedTask)

        self.setLayout(layout)
    
    def userChangedTask(self, i: int):
        print(f'Task changed to: {self.comboBox.currentText()} at {self.comboBox.currentIndex()}')
