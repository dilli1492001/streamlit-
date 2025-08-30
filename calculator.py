import streamlit as st

st.title("calculator")

with st.container(border=True):
    a=st.text_input("Enter  your firsst number ",placeholder="Eg : 25")
    b=st.text_input("Enter your second number ",placeholder="Eg : 30")
    operation = st.radio("Operation",["Add","Sub","Mul","Div"],horizontal=True)
    x=st.button("calculate",type="primary")
    if x:
        if operation == "Add":
            st.header(int(a)+int(b))
        if operation == "Sub":
            st.header(int(a)-int(b))
        if operation == "Mul":
            st.header(int(a)*int(b))
        if operation == "Div":
            st.header(int(a)/int(b))












        

    





      



