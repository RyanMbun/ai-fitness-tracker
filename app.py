#This logs workouts, views them, and this also quits the application
from data import load_workouts, save_workouts #Pulls in the two functions i wrote in data.py
from datetime import date

# want to log a workout, view workout, quit, print while loop
#Then use input() to ask the user to pick an option, and use if/elif to handle each choice.
# each option can just print something like "coming soon" — except quit, which should actually stop the loop.
while True: # Keeps the app running until the user picks quit
    print("1. Log a workout")
    print("2. View a workout")
    print("3. Quit")

    choice = input("Choose an option: ")
    if choice == '1':
        exercise_name = input("Input the name of your exercise: ")
        while True: #keeps asking for exercise type until they type strength, mobility, or cardio. Once they do, break exits that inner loop and the code continues
            exercise_type = input("Input what type of exercise this is, Strength, Mobility or Cardio: ").lower()
            if exercise_type in ["strength", "mobility", "cardio"]:
                break
            else:
                print("Please choose from one of the three options: strength, mobility, or cardio")
        if exercise_type == "cardio": #cardio doesnt use sets, reps or weights
            minutes = str(input("How many minutes of cardio is this: "))
            workout = {
                "exercise": exercise_name,
                "type": exercise_type,
                "minutes": minutes,
                "date" :  str(date.today())
            }
        else:
            sets = str(input("Input how many sets you are doing for this exercise: "))
            reps = str(input("Input how many reps you are doing for this exercise: "))
            weight = float(input("Input how much weight you are lifting for this exercise: "))
            workout = {
        "exercise" : exercise_name,
        "type" : exercise_type,
        "sets" : sets,
        "reps" : reps,
        "weight" : weight,
        "date" :  str(date.today())
        }
        
        print(workout)
        workouts = load_workouts()
        workouts.append(workout)
        save_workouts(workouts)

#i wanna load the workout and loop thru it printing each one out in a readable way
    elif choice == '2':
        for i in load_workouts():
            if i['type'] == 'cardio':
                print(f"{i['exercise']} | {i['type']} | {i['minutes']} minutes")
            else:
                print(f"{i['exercise']} | {i['type']} | {i['sets']} sets | {i['reps']} reps | {i['weight']} lbs")
    elif choice == '3':
        print("You have quit")
        break
