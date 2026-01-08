# Import needed libraries
import pandas as pd
import math

# Criteria for attendance
REQUIRED_ATTENDANCE = 80

# Calculate classes needed to reach 80%
def classes_needed(total, attended):
    if total == 0:
        return 0

    attendance = (attended / total) * 100
    if attendance >= REQUIRED_ATTENDANCE:
        return 0

    target = REQUIRED_ATTENDANCE / 100
    x = ((target * total) - attended) / (1 - target)  # Formula to calculate classes needed
    return max(0, math.ceil(x))

# Function to validate integer input
def get_int_input(prompt):
    while True:
        val = input(prompt)
        if val.isdigit():  # Checks if input is numeric
            return int(val)
        else:
            print("Invalid number. Please enter a valid integer.")

# Function to validate subject name
def get_subject_input(prompt):
    while True:
        val = input(prompt).strip()
        if any(c.isalpha() for c in val):  # Must contain at least one letter
            return val
        else:
            print("Invalid subject name. Must contain letters.")

# Main calculation function
def calc(subject):
    cls = get_int_input(f"Total number of classes for {subject}: ")
    att = get_int_input(f"How many classes have you attended in {subject}?: ")

    # Check logical error
    while att > cls:
        print("Attended classes cannot be greater than total classes.")
        att = get_int_input(f"Re-enter classes attended for {subject}: ")

    attendance = round((att / cls) * 100, 2)
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

# Loop to take multiple subjects
records = []

while True:
    print()
    sub = get_subject_input("Enter subject (or 'stop' to finish): ")
    print()
    if sub.lower() == 'stop':
        break

    record = calc(sub)
    records.append(record)

# Create a dataframe to display result
df = pd.DataFrame(records)

print("\n--- Attendance Report ---\n")
print(df.to_string(index=False))
