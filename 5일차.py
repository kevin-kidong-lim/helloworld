import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')
st.subheader('This is a subheader with a divider', divider='rainbow')
st.subheader('_Streamlit_ is :blue[cool] :sunglasses:')
# Example 1
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
st.subheader('', anchor='kevin',help='help me', divider='violet')

st.write('Hello, *World!* :sunglasses:')
st.write(1234)
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)
st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['가로', '세로', '아이템'])
c = alt.Chart(df2).mark_circle().encode(
     x='가로', y='세로', size='아이템', color='아이템',
       tooltip=['가로', '세로', '아이템'])
st.write(c)