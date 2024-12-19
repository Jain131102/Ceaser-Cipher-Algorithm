# Caesar Cipher App

This is a Streamlit application that implements the Caesar Cipher algorithm for encryption and decryption.

## How it Works

The Caesar Cipher is a simple yet classic encryption technique. It works by shifting each letter in a message by a specific number of positions (called the key) along the alphabet. For example, with a key of 3, "hello" would become "khoor."

This app provides a user-friendly interface for:

* **Encrypting plain text:** Enter your message and the key value, and the app will display the encrypted text.
* **Decrypting encrypted text:** Enter the encrypted text and the key value, and the app will display the original message.
* **Learning about Caesar Cipher:** Get a detailed explanation of the algorithm and its formulas.

## Features

* **Streamlit Integration:** Leverages Streamlit for a clean and interactive user interface.
* **Input Validation:** Ensures user input is in the correct format (plain text and integer key).
* **Error Handling:** Provides informative messages in case of invalid input.
* **Customizable Appearance:** Uses basic CSS styling to enhance the app's look and feel.

## Running the App

1. **Prerequisites:** 
Ensure you have Python (version 3.6 or later) and Streamlit installed. 
```bash
pip install python streamlit
```
2. **Clone or Download the Repository:** 
Access the code for this app from your preferred source control system or download the files directly.
```bash
git clone https://github.com/Jain131102/Ceaser-Cipher-Algorithm.git
``` 
3. **Run the application:** 
Navigate to the directory containing the Python script nd execute it .
```bash
cd Ceaser-Cipher-Algorithm
streamlit run app.py
```

## Additional Notes

* This implementation focuses on the core functionality of Caesar Cipher. More advanced encryption methods exist with stronger security properties.
* The provided CSS is basic and can be further customized for a more refined user experience.

I hope this Caesar Cipher App provides you with a valuable and informative tool for basic encryption and decryption tasks.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).

