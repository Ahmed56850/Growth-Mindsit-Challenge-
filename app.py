# streamlit 
import streamlit as st 

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="⭐")
st.title("Growth Mindset Challenge: Web App With Streamlit")    

st.header("Welcome To My Growth Journey")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla facilisi. Donec vel metus at justo fermentum tincidunt.")

# Quote section 
st.header("Today's Growth Mindset Challenge")
st.write("LIFE IS THE NAME OF LEARNING ")

st.header("What's Your Challenge Today?")
user_input = st.text_input("Describe a Challenge You're Facing:")

# Condition 
if user_input:
    st.success(f"You're Facing: {user_input}. Keep Moving Forward Towards Your Goal!")
else:
    st.warning("Tell us your challenge to get started!")

# Reflecting
st.header("Reflect On Your Learning")
reflection = st.text_area("Type Your Reflections Here:")

if reflection:
    st.success(f"Great Insight! Your Reflection: {reflection}")
else:
    st.info("Reflecting on past experiences helps you grow! Share your difficulties.")    

# Achievements 
st.header("🎉🏆 Celebrate Your Wins!")
achievement = st.text_input("Share Something You've Recently Accomplished:")

if achievement:
    st.success(f"🚀 Amazing! You Achieved: {achievement}")
else:
    st.info("Big or small, every achievement counts! Share one now 😍")    

# Footer 
st.write("---")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")
st.write("** ✍ Created By Ahmed Choru**")


