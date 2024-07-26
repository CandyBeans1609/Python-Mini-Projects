## Secret Code Language

The Python program allows users to encode and decode messages using a simple secret code language. 
It modifies words based on their length and shuffles characters to obfuscate the original message. 
The program consists of two main functions: encode and decode, which transform the text in different ways depending on word length.

<br>

<p align="center">
    <img src="https://github.com/user-attachments/assets/ac96304f-5705-422d-8d32-441b25360d65">
    
</p>

<br>

## 🌟 Explanation

- **Character List**: A list of characters `characters` is created to be used for encoding. This list includes all lowercase letters from the English alphabet.
  
- **Encoding Function (encode)**:
  - For words longer than 3 characters:
    - The word is transformed by moving its first character to the end.
    - Characters from the `characters` list are randomly shuffled, and a sequence of 3 characters is taken both before and after the word.
    - These sequences are added to the beginning and end of the modified word.
  - For words 3 characters or shorter:
    - The word is reversed.
  
- **Decoding Function (decode)**:
  - For words longer than 3 characters:
    - The first and last 3 characters (which were added during encoding) are removed.
    - The remaining part of the word is reversed to recover the original word.
  - For words 3 characters or shorter:
    - The word is reversed to recover the original word.
  
- **Encoding Process**:
  - User inputs a message, which is split into words.
  - Each word is encoded using the `encode` function.
  - The encoded words are joined to form the encoded sentence, which is then printed.

- **Decoding Process**:
  - User inputs an encoded message, which is split into words.
  - Each word is decoded using the `decode` function.
  - The decoded words are joined to form the decoded sentence, which is then printed.

<br>

## ⚙️ Prerequisites

- **Basic Python Knowledge**: Understanding of Python syntax, functions, and basic programming concepts.
- **String Manipulation**: Familiarity with string operations such as slicing, reversing, and joining.
- **Lists and Random Module**: Knowledge of working with lists and using the `random` module for shuffling elements.
- **User Input Handling**: Ability to handle and process user input using `input()` and `split()` methods.

<br>

## 🛠️ How to Run

### To encode text :

```python3
  python3 encode.py
```

### To decode text :

```python3
  python3 decode.py
```

<br>

## 📺 Output

![image](https://github.com/user-attachments/assets/13d2dc8e-b64c-44fb-bdd8-5bbb26894a60)

<br>

## 📜 Conclusion

This program effectively demonstrates a simple method for encoding and decoding messages using character manipulation and random shuffling. 
It works well for encoding longer words with additional characters for obfuscation and reverses shorter words directly. 
This method is basic and not secure for serious encryption but provides a fun way to encode and decode messages for casual use.

<br>

## 👻 Author

[Akanksha Kanade](https://github.com/CandyBeans1609)
<br>
[Atharva Baikar](https://github.com/DarkGuardian641)
