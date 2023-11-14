import streamlit as st
from streamlit_extras.let_it_rain import rain
from typing import Union
from PIL import Image
import time
from streamlit_player import st_player


rain(
    emoji="ALFA🔥",
    font_size=25,
    falling_speed=5,
    animation_length="infinite",
)

st.markdown("<h1 style='text-align: center; '>Мини-презентация :)</h1>", unsafe_allow_html = True)
st.image('2.JPG')
#st.balloons()
st.write("Хотите узнать вкратце обо мне? Нажмите кнопку ниже.")
    


    
if st.button("Краткая биография"):
    st.snow()
    st.image('1.JPG')
        
       
    st.write('Всем привет ! Вкратце обо мне: несостоявшийся патологоанатом, создаю модельки для минимизации кредитного риска и не только, люблю двухтактные мотоциклы и тяжелую музыку (black/melodic death/progressive/heavy metal :sunglasses:').
   
   
     
    time.sleep(3.5)
    st_player("https://soundcloud.com/dursunakyz/dark-tranquillity-miserys-crown")
        
        
    
