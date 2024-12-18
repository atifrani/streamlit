import streamlit as st
from datetime import time, datetime

st.header("Let make diffrents slider examples")

# Exemple 1:

st.subheader("Slider to select your age:")

age = st.slider("How old are you ? ", 0, 100, (20))

st.write("My age is: ", age)

# Exemple 2:

st.subheader("Slider to select age range:")

age_range = st.slider("Select you age range", 0, 100, (20, 50))
st.write ("My age range is: ", age_range)

# example 3:

st.subheader("Slider to select range time")

appointment = st.slider("Schedule your appointment", value=(time(11,30), time(12,45)))
st.write("you're scheduled for: ", appointment)

# Example 4:

st.subheader("Slider to select datetime")

start_time = st.slider("When do you start? ", value= datetime(2024, 12, 18, 12, 28), format="DD/MM/YY - hh:mm")

end_time = st.slider("When do you finish? ", value= datetime(2024, 12, 18, 12, 28), format="DD/MM/YY - hh:mm")


st.write("Start time is : ", start_time)

st.write("End time is : ", end_time)