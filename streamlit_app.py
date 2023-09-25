import streamlit as st

st.header('st.button')

if st.button('Say Hello'):
    st.write('Howzit')
else:
    st.write('Goodbye')
