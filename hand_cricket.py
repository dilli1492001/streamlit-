import streamlit, random

if not streamlit.session_state.get("score"):
    streamlit.session_state.score=0

streamlit.title("Hand Cricket Game")
cols=streamlit.columns([1,1])
with cols[1]:
    b=streamlit.button("Play Now",use_container_width=True,type="primary")
    with streamlit.container(border=True):
        streamlit.write("system 🎾")
        c=random.randrange(1,7)
        streamlit.header(c)
with cols[0]:
    a=streamlit.text_input("Enter number ",label_visibility="collapsed",placeholder="Enter number between 1 to 6")
    if a and (int(a)<1 or int(a)>6):
        streamlit.toast("Enter a number between 1 to 6")
        a=0
    with streamlit.container(border=True):
        streamlit.write("user 🏏")
        if b :
            streamlit.header(a)
            if int(a)!=c:
                streamlit.session_state.score+=int(a)
            else:
                streamlit.toast(f"You are out , Score :{streamlit.session_state.score}")
        else: 
            streamlit.header(0)
with streamlit.container(border=True):
    streamlit.header(streamlit.session_state.score)


