import streamlit as st 
import base64

def set_bg_hack():
    main_bg = "Untitled design.jpg"
    main_bg_ext = "jpg"
        
    st.markdown(
         f"""
         <style>
         .appview-container {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
         }}
         [data-testid="stHeader"]{{
             background-color: rgba(0,0,0,0);
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    
def header1(text):
    html_temp = f"""
    <h1 style = "color:brown; text_align:center; font-weight: bold;"> {text} </h2>
    </div>
    """   
    st.markdown(html_temp, unsafe_allow_html = True)
    
def header2(text):
    html_temp = f"""
    <h3 style = "color:brown; text_align:center; font-weight: bold;"> {text} </h2>
    </div>
    """   
    st.markdown(html_temp, unsafe_allow_html = True)

def header3(text):
    html_temp = f"""
    <h5 style = "color:brown; text_align:center; font-weight: bold;"> {text} </h2>
    </div>
    """   
    st.markdown(html_temp, unsafe_allow_html = True)
