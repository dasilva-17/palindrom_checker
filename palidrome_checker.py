
import streamlit as st

def is_palindrome(text):
  
    cleaned_text = '.'.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]


st.title("Palindrome Checker")


text =st.text_input("Enter a word or phrase to check:")


if st.button("Check if palindrome"):
    if text:
        if is_palindrome(text):
            st.success(f'"{text}" is a palindrome!')
        else:
            st.error(f'"{text}" is NOT a problem.')
    else:
        st.warning("Please enter a valid word or phrase.")