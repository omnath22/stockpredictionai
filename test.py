import streamlit as st
import pandas as pd
import utils as utl
from streamlit_option_menu import option_menu

# NOTE: This must be the first command in your app, and must be set only once
st.set_page_config(initial_sidebar_state="collapsed",layout="wide",page_title="yourfinancebuddy")


st.markdown("""<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <a class="navbar-brand" href="#">YourFinanceBuddy</a>
  <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">Star Performer</a>
      </li>
    </ul>
      <a target="_self" href="login"><button class="btn btn-outline-info my-2 my-sm-0">Login / Sign Up</button></a>
  </div>
</nav>""",unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)
    # Loading CSS





# with col3:
#     st.write(f'''
#     <a target="_self" href="login">
#         <button>
#             Login/Register
#         </button>
#     </a>
#     ''',
#     unsafe_allow_html=True
# )

# col1, col2, col3,col4 = st.columns(4)

# with col3:

#     st.write("""
#             # Stock Prediction Ai
            
#             Shown are the stock closing price
#             """)


st.markdown("""<h1 style="text-align:center;font-weight:700">Stay ahead of the Market</h1>""",unsafe_allow_html=True)
col1,col2,col3,col4,col5 = st.columns(5)
with col3:
    st.text_input("Enter Stock Ticker")
    # tickersymbol = 'GOOGL'

    # tickerdata = yf.Ticker(tickersymbol)

    # tickerof = tickerdata.history(period='1d',start='2010-5-31', end='2020-5-31')

    # st.line_chart(tickerof.Close)
    # st.line_chart(tickerof.Volume)
st.markdown('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">', unsafe_allow_html=True)
st.markdown('<script type="text/javascript" src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>',unsafe_allow_html=True)
st.markdown('<style>.css-qri22k{display:none} .css-ilrupz{gap:0rem} .css-1x4jpr0{gap:0} </style>', unsafe_allow_html=True)
st.markdown("""
    <style>footer{visibility:hidden;}
            #MainMenu{visibility:hidden;}
            header{visibility:hidden;}
            .css-9s5bis {display: none;}
            .css-18e3th9{padding-top:0;padding-left:0;padding-right:0}

    </style>
    """, unsafe_allow_html=True)
