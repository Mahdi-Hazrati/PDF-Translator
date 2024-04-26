# PDF Translator Developer Documentation



## Overview
This document serves as a comprehensive guide for developers who wish to understand and contribute to the PDF Translator application. PDF Translator is a Python application that enables users to translate the content of PDF files into another language and save the translated content into a Word document. It utilizes various libraries such as PyMuPDF, OpenCV, googletrans, tkinter, and docx for PDF handling, image extraction, translation, GUI creation, and document generation.

## Table of Contents
1. **Dependencies**
2. **File Structure**
3. **Key Components**
    - 3.1 GUI Text Loading
    - 3.2 Image Extraction from PDF
    - 3.3 Text Extraction from PDF
    - 3.4 Text Translation
    - 3.5 Word Document Generation
    - 3.6 GUI Functions
4. **Usage**
5. **Contributing**
6. **License**

## 1. Dependencies
PDF Translator relies on the following Python libraries:
- tkinter: For creating the graphical user interface.
- PyMuPDF: For interacting with PDF files and extracting text and images.
- OpenCV: For image processing and manipulation.
- googletrans: For translating text.
- docx: For creating Word documents.
- numpy: For numerical operations.

## 2. File Structure
The main components of the application are organized as follows:
- **assets/:** Contains GUI text in JSON format and program icon.
- **pdf_translator.py:** Main Python script containing the application logic.

## 3. Key Components

### 3.1 GUI Text Loading
The application loads GUI text from a JSON file located in the `assets/` directory. If the file is found, the contents are loaded into memory to be used for various labels, buttons, and messages in the GUI.

### 3.2 Image Extraction from PDF
Images are extracted from PDF files using PyMuPDF library. Each page of the PDF is scanned for images, and if found, they are extracted and saved as PNG files.

### 3.3 Text Extraction from PDF
Text extraction from PDF files is performed using PyMuPDF library. It iterates through each page of the PDF and retrieves the text content.

### 3.4 Text Translation
Text translation is achieved using the Google Translate API provided by the googletrans library. The original text extracted from the PDF is translated into the desired target language.

### 3.5 Word Document Generation
The translated text and extracted images are combined and saved into a Word document using the docx library.

### 3.6 GUI Functions
Various functions are implemented to handle GUI interactions, such as selecting input and output files, triggering the translation process, displaying error messages, and opening the GitHub repository link.

## 4. Usage
To use the PDF Translator application:
1. Run the `main.py` script.
2. Select the input PDF file containing the content to be translated.
3. Choose the output location and filename for the translated Word document.
4. Click the "Translate" button to start the translation process.
5. Upon completion, a success message will be displayed, and the translated document will be opened.

## 5. Contributing
Contributions to PDF Translator are welcome. To contribute:
1. Fork the repository.
2. Make changes or additions as needed.
3. Submit a pull request with a clear description of the changes.

## 6. License
PDF Translator is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the LICENSE file for more details.
