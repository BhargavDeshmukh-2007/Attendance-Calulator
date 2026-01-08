#Import neeeded libraies
import pandas as pd
import math

#Criteria for attendance
REQUIRED_ATTENDANCE = 80

#Create clsss to find classes needed to attend to fullfil requirement
def classes_needed(total, attended):
    if total == 0:
        return 0

    attendance = (attended / total) * 100
    if attendance >= REQUIRED_ATTENDANCE:
        return 0

    target = REQUIRED_ATTENDANCE / 100
    x = ((target * total) - attended) / (1 - target)  #Formula to calculate classes needed
    return max(0, math.ceil(x))

#This class is the base class it takes all the input needed and checks conditions to find errors
def calc(subject):
    cls = int(input(f"Total number of classes for {subject}: "))
    att = int(input(f"How many classes have you attended in {subject}?: "))

    if att > cls or cls <= 0:
        attendance = None
        needed = None
        result = "Error in numbers"
    else:
        attendance = round((att / cls) * 100, 2)  #Formula to calculate attendance
        needed = classes_needed(cls, att)

        if attendance >= REQUIRED_ATTENDANCE:
            result = "You're qualified for the sem end!!"
        else:
            result = f"Attend next {needed} classes to reach 80%"

    return {
        'Subject': subject,
        'Total_Classes': cls,
        'Attended_Classes': att,
        'Attendance_%': attendance,
        'Classes_Needed': needed,
        'Result': result
    }

#This is a loop which runs until all classes are given input using keyword "stop" will stop the loop
records = []

while True:
    print()
    sub = input("Enter subject (or 'stop' to finish): ")
    print()
    if sub.lower() == 'stop':
        break

    record = calc(sub)
    records.append(record)

#Create a dataframe to display result
df = pd.DataFrame(records)

print("\n--- Attendance Report ---\n")
print(df.to_string(index=False))
