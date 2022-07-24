import streamlit as st
def calculate(a,b):
  try:
    ans=a/b
    st.write("""Ans is """+ str(ans))
  except:
    st.write("Denomitor can't be 0")
st.write("""
# Division of 2 numbers
# """)
a=st.number_input("Numerator")
b=st.number_input("Denominator")
st.button("Calculate", on_click=calculate(a,b))
