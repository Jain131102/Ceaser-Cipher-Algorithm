import streamlit as st


class CaesarCipher:
    """Encrypts and decrypts text using the Caesar Cipher."""

    def __init__(self):
        """Initializes the CaesarCipher class with empty attributes."""
        self.plain_text = ""  # Stores the plain text input
        self.key_value = ""  # Stores the key value input
        self.result = ""  # Stores the encrypted or decrypted text

    def encrypt(self):
        """Encrypts the plain text using the Caesar Cipher."""
        if not self.plain_text or not self.key_value:
            # Check for empty input fields
            st.warning("Please enter both plain text and key value.")
            return

        try:
            key = int(self.key_value)  # Convert key value to integer
            encrypted_text = ""  # Initialize empty string for encrypted text

            for char in self.plain_text:
                if char.isalpha():  # Check if character is alphabetic
                    shift = (ord(char.lower()) - 97 + key) % 26  # Calculate shift
                    encrypted_text += chr(shift + 97).upper() if char.isupper() else chr(shift + 97)  # Shift and append character
                else:
                    encrypted_text += char  # Append non-alphabetic characters

            self.result = encrypted_text  # Store encrypted text in result
        except ValueError:
            st.error("Key value must be an integer.")  # Handle invalid key value

    def decrypt(self):
        """Decrypts the plain text using the Caesar Cipher."""
        if not self.plain_text or not self.key_value:
            # Check for empty input fields
            st.warning("Please enter both plain text and key value.")
            return

        try:
            key = int(self.key_value)  # Convert key value to integer
            decrypted_text = ""  # Initialize empty string for decrypted text

            for char in self.plain_text:
                if char.isalpha():  # Check if character is alphabetic
                    shift = (ord(char.lower()) - 97 - key) % 26  # Calculate shift
                    decrypted_text += chr(shift + 97).upper() if char.isupper() else chr(shift + 97)  # Shift and append character
                else:
                    decrypted_text += char  # Append non-alphabetic characters

            self.result = decrypted_text  # Store decrypted text in result
        except ValueError:
            st.error("Key value must be an integer.")  # Handle invalid key value

    def clear(self):
        """Clears the input fields and result."""
        self.plain_text = ""
        self.key_value = ""
        self.result = ""

    def learn(self):
        """Displays information about the Caesar Cipher."""
        learn_text = """
        ### What is Caesar Cipher Technique?

        The Caesar cipher is a simple encryption technique that was used by Julius Caesar to send secret messages to his allies. It works by shifting the letters in the plaintext message by a certain number of positions, known as the 'shift' or 'key'.

        The Caesar Cipher technique is one of the earliest and simplest methods of encryption techniques. It's simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter with a fixed number of positions down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on. The method is apparently named after Julius Caesar, who used to communicate with his officials.

        **Formulas:**
        - Encryption: En(x) = (x + n) mod 26
        - Decryption: Dn(x) = (x - n) mod 26
        """
        st.markdown(learn_text)


def main():
    cipher = CaesarCipher()

    # Set Streamlit page configuration
    st.set_page_config(
        page_title="Caesar Cipher App",
        page_icon=":lock:",
        layout="wide",
    )

    st.title('Caesar Cipher Algorithm')

    st.write("""
        Welcome to the Caesar Cipher App! 
        Use this tool to see how Caesar Cipher Algorithm works.
    """)

    # Custom CSS for styling
    st.markdown("""
        <style>
        /* Global styles */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }

        /* Specific element styling */
        .stTitle {
            font-size: 24px;
            font-weight: bold;
            color: #333;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
        }
        .stTextInput > div > div > input, .stTextArea > div > div > textarea {
            border-radius: 5px;
            border: 1px solid #ccc;
            padding: 10px;
            font-size: 16px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Input fields for plain text and key value
    col1, col2 = st.columns([3, 1])
    with col1:
        cipher.plain_text = st.text_area(
            "Plain Text", cipher.plain_text, placeholder="Enter a plain text", height=100)
    with col2:
        cipher.key_value = st.text_input(
            "Key Value", cipher.key_value, placeholder="Enter an integer")

    # Buttons for encrypt, decrypt, clear, and learn actions
    col1, col2, col3, col4 = st.columns([2, 2, 2, 2])
    with col1:
        if st.button("Encrypt"):
            cipher.encrypt()
    with col2:
        if st.button("Decrypt"):
            cipher.decrypt()
    with col3:
        if st.button("Clear"):
            cipher.clear()
    with col4:
        if st.button("Learn"):
            cipher.learn()

    # Display the result
    if cipher.result:
        st.subheader("Result:")
        st.write(cipher.result)


if __name__ == "__main__":
    main()
