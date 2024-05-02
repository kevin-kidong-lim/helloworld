import streamlit as st 

st.header("st.button")
if st.button('say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')