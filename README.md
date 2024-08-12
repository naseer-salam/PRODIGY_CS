# Caesar Cipher GUI

This is a simple Python application with a graphical user interface (GUI) that allows users to encrypt and decrypt text using the Caesar Cipher algorithm. The GUI is built using the `tkinter` library.

## Features
- **Encrypt Text**: Input text and apply a Caesar Cipher to encrypt the message with a specified shift value.
- **Decrypt Text**: Input encrypted text and decrypt it using the same shift value.
- **Copy to Clipboard**: Easily copy the encrypted or decrypted message to your clipboard for use elsewhere.

## Prerequisites
- Python 3.x

## Installation

1. **Clone the repository:**
    ```sh
    https://github.com/naseer-salam/PRODIGY_CS_01
    cd PRODIGY_CS_01
    ```

2. **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application:**
    ```sh
    python CC.py
    ```

2. **Encrypt/Decrypt Text:**
    - Enter the text you want to encrypt or decrypt.
    - Enter the shift value (a positive integer).
    - Click the "Encrypt" or "Decrypt" button to process the text.
    - The result will be displayed below the buttons.
    - Click "Copy to Clipboard" to copy the result for easy use elsewhere.

## Example

- **Encrypting "Hello, World!" with a shift of 3:**
    - Input: `Hello, World!`
    - Shift: `3`
    - Output: `Khoor, Zruog!`

- **Decrypting "Khoor, Zruog!" with a shift of 3:**
    - Input: `Khoor, Zruog!`
    - Shift: `3`
    - Output: `Hello, World!`

## Author
    Naseer 
