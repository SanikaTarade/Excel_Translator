# Excel_Translator
This Python script translates text in an Excel file from Chinese to English using the Google Translate API. The translated content is then saved to a new Excel file.

# Features
1. Reads an Excel file with text in Chinese.
2. Utilizes the Google Translate API to translate each text cell to English.
3. Handles network issues and prints error messages for any translation errors.
4. Measures the time taken for the translation and saving process.

# Requirements
1. Python 3.x
2. pandas library (pip install pandas)
3. googletrans library (pip install googletrans==4.0.0-rc1)

# Usage
1. Specify the correct paths for your input and output Excel files in the script.
2. Run the script using a Python interpreter.

# Important Note
Ensure you have a stable internet connection, and consider checking the status of the Google Translate API. Adjustments may be needed based on network settings or API limitations.
