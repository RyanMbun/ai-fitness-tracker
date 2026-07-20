import streamlit as st
from data import load_workouts, save_workouts
from datetime import date
import google.generativeai as genai
import os

st.title("Fitness Tracker") #gives a title to my web page
tab1, tab2, tab3 = st.tabs(["Log Workouts", "View Workouts", "AI Workout Plan"])
with tab1:
    exercise_name = st.text_input("Input the name of your exercise: ")
    exercise_type = st.selectbox(
        "What type of exercise is this?",
        ("Strength", "Mobility", "Cardio")
    )
    if exercise_type == "Cardio": # EDITED: moved inputs above the button so variables exist before button is clicked
        minutes = st.number_input("How many minutes?")
    else:
        sets = st.number_input("Sets: ")
        reps = st.number_input("Reps: ")
        weight = st.number_input("Weight (lbs): ")
    if st.button("Log Workout"): # EDITED: fixed indentation so everything below is inside the button block
        if exercise_type == "Cardio": # EDITED: added cardio dictionary inside the button block
            workout = {
                "exercise": exercise_name,
                "type": exercise_type,
                "minutes": minutes,
                "date": str(date.today())
            }
        else: # EDITED: fixed indentation on else block and its dictionary
            workout = {
                "exercise": exercise_name,
                "type": exercise_type,
                "sets": sets,
                "reps": reps,
                "weight": weight,
                "date": str(date.today())
            }
        workouts = load_workouts() # EDITED: moved inside button block so it only runs on click
        workouts.append(workout)
        save_workouts(workouts)
        st.success("Workout logged!")
with tab2:
    st.write("Workout History:")
    for i in load_workouts():
        if i['type'].lower() == 'cardio': #Checks what type workout was logged
            st.write(f"{i['exercise']} | {i['type']} | {i['minutes']} minutes | {i['date']}")
        else:
            st.write(f"{i['exercise']} | {i['type']} | {i['sets']} sets | {i['reps']} reps | {i['weight']} lbs | {i['date']}")
with tab3:
    goal = st.selectbox("What is your fitness goal?", ("Build Muscle", "Lose Weight", "Improve Endurance"))
    days = st.selectbox("How many days per week can you work out?", (1, 2, 3, 4, 5, 6, 7))
    experience = st.selectbox("What is your experience level?", ("Beginner", "Intermediate", "Advanced"))
    if st.button("Generate Plan"):
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(f"Create a {days} day per week workout plan for someone who wants to {goal.lower()}. Their experience level is {experience}. Format it clearly by day.")
        st.write(response.text)
            