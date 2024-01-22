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

col1,col2,col3 = st.columns([2,3,1])
with col2:
    st.title('Register Page')
name = st.text_input('Name')
email = st.text_input('Email Address')
password = st.text_input('Password', type='password')
reenterpassword = st.text_input('Confirm Password', type='password')

col4,col5,col6 = st.columns([4,3,1])
with col4:
    st.markdown(
    """Already have an account Login <a target="_self" href="login">Here</a>""", unsafe_allow_html=True,
)
with col6:
    st.button('Register')


