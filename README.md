# Morse Code Streamlit App

![app](https://github.com/harichselvamc/Morsecode_streamlit/assets/90306857/d71d3c0c-89f3-46ec-84e5-9d99a4c45973)

## Overview

This Streamlit application allows users to encode and decode text into Morse code and vice versa. Additionally, it features Morse code detection using a simple Naive Bayes classifier.

## How to Use

1. Visit the live app: [Morse Code Streamlit](https://morsecodeapp.streamlit.app/)
2. Choose between "Encode" and "Decode" operations.
3. Enter the text you want to encode or Morse code you want to decode.
4. Optionally, enable Morse code detection.
5. Click the "Encode" or "Decode" button to see the result.

## Features

- **Encode:** Convert regular text into Morse code.
- **Decode:** Translate Morse code back into regular text.
- **Morse Code Detection:** Utilize a simple Naive Bayes classifier to determine if the input is Morse code or not.

## Usage

To run the app locally, make sure you have Python and Streamlit installed. Clone the repository and run the following commands in your terminal:


    pip install -r requirements.txt
    
    streamlit run app.py


## Open the application in your browser
(by default, it will be available at http://localhost:8501).

## Morse Code Dictionary
The application uses a standard Morse code dictionary for encoding and decoding. 
The dictionary includes mappings for letters A-Z, numbers 0-9, and a space character.

## Machine Learning Morse Code Detection
The application incorporates a simple machine learning model to detect whether the input is in Morse code or not. This feature enhances user experience by automatically selecting the appropriate operation.


Medium Article: 
[medium](https://medium.com/@harichselvamc/learning-morse-code-b71e58a2c9db)
https://medium.com/@harichselvamc/learning-morse-code-b71e58a2c9db
Live Application : (https://morsecodeapp.streamlit.app/)
