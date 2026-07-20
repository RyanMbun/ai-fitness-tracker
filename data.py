import json

def load_workouts():
    with open("workouts.json", "r") as f:
        return json.load(f)
    
def save_workouts(workouts):
    with open("workouts.json", "w") as f:
        json.dump(workouts, f)

workouts = load_workouts()
print(workouts)

workouts.append({
    "exercise": "bench press",
    "type": "strength",
    "sets": 3,
    "reps": 8,
    "weight": 135,
    "date": "2026-05-19"
})
save_workouts(workouts)
print("saved!")

#This saves and load workouts frm json file
#We used a JSON file because it's the simplest way to save data permanently without setting up anything extra.
