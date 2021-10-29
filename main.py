import streamlit as st
import hashlib

def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

password = st.sidebar.text_input("Password",type='password')

if check_hashes(password, 'd970990220a1e7e9a1f80ed922d39173e252a34e3739720bbdb55ef3cd9f34b9'):
    dataset_key_selectbox = st.selectbox('Select dataset', ['a', 'b', 'c'])
    na_fraction_selectbox = st.selectbox('Select na_fraction', [0.05, 0.1, 0.15, 0.2, 0.25, 0.3])

    if st.button('Start'):
        "Started!"