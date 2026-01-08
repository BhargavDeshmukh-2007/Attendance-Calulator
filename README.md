# Attendance-Calulator
This simple code helps the user to track their attendance and how many more classes are required to be attended to full fill the criteria. This project is beneficial for college students as attendance plays a vital part in their academic results

---

## Features

- Calculates attendance percentage for each subject
- Determines eligibility based on minimum attendance requirement (80%)
- Computes the minimum number of future classes required to meet the criteria
- Displays results in a tabular format using pandas DataFrames

---

## How It Works

For each subject, the user provides:
- Total number of classes conducted
- Number of classes attended

The program calculates:
- Attendance percentage
- Qualification status
- Number of additional classes required to reach 80% attendance (if applicable)

The required number of classes is calculated using a mathematical formula and
rounded up to the nearest whole number to ensure accuracy.

---

## Example Output

| Subject | Total_Classes | Attended_Classes | Attendance_% | Classes_Needed | Result |
|--------|---------------|------------------|--------------|----------------|--------|
| Physics | 25 | 18 | 72.0 | 7 | Attend next 7 classes |
| Maths | 20 | 17 | 85.0 | 0 | Qualified |

---

## Requirements

- Python 3.x
- pandas

## Limitations
-The program currently works for a single student
-Input is taken via the command line
-Data is not persisted after program termination


## Future Improvements
-Support for multiple students
-Export results to CSV or Excel
-Persistent data storage
-Basic user interface
-Learning Outcome


##This project helped reinforce:
-Python function design
-Error handling and input validation
-Mathematical problem-solving
-Data representation using pandas DataFrames
