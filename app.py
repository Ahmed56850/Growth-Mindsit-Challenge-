 #streamlit 
import streamlit as st 
# import pandas as pd
# import os 
# from io import BytesIO 

st.set_page_config(page_title= "Growth Mindset Challenge" , project_page_icon = "⭐")
st.title("Growth Mindset Challenge: Web App With Streamlit")    

st.header("Well To My Growth Journey")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Donec vel metus at justo fermentum tincidunt.")

#quote section 
st.header("Today Growth Mindset Challenge")
st.write("LIFE IS THE NAME OF LEARING ")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Decribe a Challenge You're Facing; ")

#condition 
if user_input:
    st.success(f"You're Facing: {user_input}. Keep Forwar Towords Your Goal")
else:
    st.warning("Tell As Your Challenge To Get Started!")

#reflexing
st.header("Reflect On Your Learning")
reflection = st.text_area("Type Your Reflectiions Here:")

if reflection:
    st.success(f"Great Insight Your Reflection: {reflection}")
else:
    st.info("Reflecting On Past Experience Help You Grow! Share Your Defeculties ")    

#acheivements 
st.header(f"🎉🏆Celebrate Your Wins!")
acheivment = st.text_input("Share Somting You've Recently Accomplished:")

if acheivment:
    st.success(f"🚀Amazing! You Acheived: {acheivment}")
else:
    st.info("Big Or Small , Every Achievment Counts! Share One Now 😍")    

#footer 
st.write("- - -")
st.write("🚀Keep Beleving In Your Self .Growth Is A Journey, Not A Destination! 🌟")
st.write("** ✍ Created By Ahmed Choru**")


