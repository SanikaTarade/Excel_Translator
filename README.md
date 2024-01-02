# Excel_Translator
This Python script translates text in an Excel file from Chinese to English using the Google Translate API. The translated content is then saved to a new Excel file.

# Features
Reads an Excel file with text in Chinese.
Utilizes the Google Translate API to translate each text cell to English.
Handles network issues and prints error messages for any translation errors.
Measures the time taken for the translation and saving process.

# Requirements
Python 3.x
pandas library (pip install pandas)
googletrans library (pip install googletrans==4.0.0-rc1)

# Usage
Specify the correct paths for your input and output Excel files in the script.
Run the script using a Python interpreter.

# Important Note
Ensure you have a stable internet connection, and consider checking the status of the Google Translate API. Adjustments may be needed based on network settings or API limitations.
