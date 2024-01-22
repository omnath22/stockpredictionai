import streamlit as st

st.set_page_config(page_title="yourfinancebuddy")
st.markdown('<style>.css-qri22k{display:none} </style>', unsafe_allow_html=True)
st.markdown("""
    <style>
        section[data-testid="stSidebar"][aria-expanded="true"]{
            display: none;
        }
            #MainMenu{visibility:hidden;}
            footer{visibility:hidden;}
            header{visibility:hidden;}
    </style>
    """, unsafe_allow_html=True)
col1,col2,col3 = st.columns(3)
with col2:
    st.title('Login Page')
email = st.text_input('Email Address')
password = st.text_input('Password', type='password')


col4,col5,col6 = st.columns([4,4,1])
with col4:
    st.markdown(
    """Don't have an account Signup <a target="_self" href="register">Here</a>""", unsafe_allow_html=True,
)
with col6:
    st.button('Login')

