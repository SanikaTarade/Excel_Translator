from googletrans import Translator
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import pandas as pd
from googletrans import Translator
import time

def translate_text(text, target_language='en'):
    translator = Translator()
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text if translation else text
    except Exception as e:
        print(f"Error during translation: {e}")
        return text

def translate_excel(input_file_path, output_file_path):
    # Record start time
    start_time = time.time()

    # Read Excel file into a Pandas DataFrame
    df = pd.read_excel(input_file_path)

    # Translate all text in the DataFrame using DataFrame.applymap
    df_translated = df.applymap(lambda x: translate_text(str(x)))

    # Save the translated DataFrame to a new Excel file
    df_translated.to_excel(output_file_path, index=False)

    # Record end time
    end_time = time.time()

    # Print the time it took to translate and save
    elapsed_time = end_time - start_time
    print(f"Translation and saving took {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    # Specify the correct path for your input and output files
    input_file_path = "C:/Users/sanik/AppData/Local/Programs/Python/Python312/Order_Sheet.xls"
    output_file_path = "Translated_Order_Sheet.xls"

    # Call the translation function
    translate_excel(input_file_path, output_file_path)
