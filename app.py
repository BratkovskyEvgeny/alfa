import streamlit as st
#from streamlit_extras.let_it_rain import rain
from typing import Union
from PIL import Image
import time
from streamlit_player import st_player


#rain(
   # emoji="УКР🔥",
    #font_size=25,
    #falling_speed=5,
    #animation_length="infinite",
#)

st.markdown("<h1 style='text-align: center; '>Итоги нетворкинга</h1>", unsafe_allow_html = True)
st.image('777.JPG')
#st.balloons()
st.write("Хотите узнать итоги? Нажмите на кнопку ниже.")
    


    
if st.button("Жэстачайшая правда о нетворкинге"):
    st.snow()

    st.markdown(f"<h6 style='text-align: justify;'>Довожу до сведения, что нетворкинг продвигается продуктивно, отряд не потерял бойцов, все заряжены на изучение вражеских алгоритмов, чтобы принести пользу банку.Допросы, т.е. опросы, все успешно прошли 🔥🔥🔥. Поэтому ниже специально для нетворкеров песня о тяжелой подготовке.</h6>", unsafe_allow_html=True)
    
        
       
    #st.write('Довожу до сведения, что нетворкинг продвигается продуктивно, отряд не потерял бойцов, все заряжены на изучение вражеских алгоритмов, чтобы принести пользу банку.Допросы, т.е. опросы, все успешно прошли :sunglasses:. Поэтому ниже специально для нетворкеров песня о тяжелой подготовке.')
   
   
     
    time.sleep(3.5)
    st_player("https://soundcloud.com/user-854788030/paul-hertzog-preparation-mp3")
        
        
    
