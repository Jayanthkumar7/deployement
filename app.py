import streamlit as st
import joblib

model_nb = joblib.load('spam-ham')

st.title('spam ham classifier')
ip=st.text_input('enter the text:')
op=model_nb.predict([ip])
if st.button('predict'):
  st.title(op[0])
