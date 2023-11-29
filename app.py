import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Morse code dictionary
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/'
}

def encode(text):
    return ' '.join(morse_code_dict[char] if char.upper() in morse_code_dict else char for char in text)

def decode(morse_code):
    morse_code_reverse_dict = {value: key for key, value in morse_code_dict.items()}
    return ''.join(morse_code_reverse_dict[code] if code in morse_code_reverse_dict else code for code in morse_code.split())

def is_morse_code(text):
    # CountVectorizer is used to convert Morse code into a bag-of-words representation
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 1))
    X = vectorizer.fit_transform([text])

    # Training a simple Naive Bayes classifier
    clf = MultinomialNB()
    y = [1]  # 1 indicates Morse code, 0 would indicate non-Morse code
    clf.fit(X, y)

    # Predicting whether the input is Morse code or not
    prediction = clf.predict(X)

    return prediction[0] == 1

# Streamlit app
st.title('Morse Code Encoder and Decoder with ML')

# Choose between Encode and Decode
operation = st.radio('Choose operation:', ['Encode', 'Decode'])

# Input text
input_text = st.text_area(f'Enter text to {operation.lower()}:', 'Hello, World!')

# Checkbox for Morse code detection
ml_enabled = st.checkbox('Enable Morse Code Detection', True)

# Button to encode or decode
if st.button(f'{operation}'):
    if ml_enabled and is_morse_code(input_text):
        decoded_result = decode(input_text)
        st.success(f'Decoded Text: {decoded_result}')
    elif operation == 'Encode':
        encoded_result = encode(input_text.upper())
        st.success(f'Encoded Morse Code: {encoded_result}')
    elif operation == 'Decode':
        decoded_result = decode(input_text)
        st.success(f'Decoded Text: {decoded_result}')

