#==============================================================================
#                              Converter App - PyQt5 
#==============================================================================



# importing Libraries 
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from gui import Ui_Form as Ui_MainWindow 
from controller import conversions
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from index import Ui_Splash
from PyQt5.QtCore import QTimer



class run(QMainWindow , Ui_Splash):
    def __init__(self , parent=None):
        super(run,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)# Set UI properties
        self.progress()# Call the progressor function
        self.prog.setMaximum(100)# Set the maximum 
        self.prog.setValue(0)# Set the initial state of the 
        timer = QTimer(self)
        timer.timeout.connect(self.progress)
        timer.start(50)# Setting the timer with a frequency of 50 milliseconds
        # Connect the finished signal to open the AppWindow
    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()
    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()
        

    def progress(self):
        # Increase the booster value once
        self.prog.setValue(self.prog.value() + 1)
        # If the booster value reaches 99
        if self.prog.value() == 99:
            self.close()
            # Show other Window
            self.openApp = AppWindow()
            self.openApp.show()
        



class AppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)#Set Ui Properties
        self.selectFileButton.clicked.connect(self.select_file)# Connect the file selection button to the select_file function
        self.convertButton.clicked.connect(self.perform_conversion)
        self.selected_file = ''# Define the selected_file variable
        self.exit.clicked.connect(self.exit_btn)
        self.mini.clicked.connect(self.mini_btn)

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File")
        if file_name:
            self.selected_file = file_name
            self.filePathLabel.setText(file_name)

    def perform_conversion(self):
        conversion_type = self.conversionComboBox.currentText()
        if not self.selected_file:
            QMessageBox.warning(self, "Error", "Please select a file first!")
            return
        
        
        try:
            if conversion_type == "PDF to Word":
                # Define the output file path for the converted Word document
                output_file = 'output/converted_' + os.path.basename(self.selected_file).split('.')[0] + '.docx'
                conversions.pdf_to_word(self.selected_file, output_file)
                # Call the pdf_to_word function to convert the selected PDF file to Word
            elif conversion_type == "Word to PDF":
                output_file = conversions.word_to_pdf(self.selected_file)
                # Call the word_to_pdf function to convert the selected Word file to PDF
            elif conversion_type == "Excel to Word":
                output_file = 'output/converted_' + os.path.basename(self.selected_file).split('.')[0] + '.docx'
                conversions.xl_to_word(self.selected_file, output_file)
            elif conversion_type == "Image to PDF":
                output_file = 'output/converted_' + os.path.basename(self.selected_file).split('.')[0] + '.pdf'
                conversions.image_to_pdf(self.selected_file)
            elif conversion_type == "Image Text Extract":
                output_file = 'output/extracted_' + os.path.basename(self.selected_file).split('.')[0] + '.txt'
                conversions.image_text_extractor(self.selected_file, output_file)

            # Set the status label to indicate successful conversion
            self.statusLabel.setText("Conversion successful!")
        except Exception as e:
            # If an error occurs during conversion, display an error message
            self.statusLabel.setText(f"Error: {e}")
            
            
    def mini_btn(self):


        QMainWindow.showMinimized(self)
    

    def exit_btn(self):
        sys.exit(0)
            
            
            
            
    def mousePressEvent(self, evt):
    # Store the current mouse position when the mouse button is pressed
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
    # Calculate the difference between the current mouse position and the stored position
        delta = QPoint(evt.globalPos() - self.oldPos)
    # Move the window by adjusting its x and y coordinates
        self.move(self.x() + delta.x(), self.y() + delta.y())
    # Update the stored mouse position
        self.oldPos = evt.globalPos()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = run()  # Create an instance of the run class (First Running Window)
    window.show()  # Show the window
    sys.exit(app.exec_())  # Start the application event loop

