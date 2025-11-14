from pyscript import document, display


def general_weighted_average(e):
    """
    This function runs when the user clicks the "Calculate GWA" button.
    It collects the inputs, computes the weighted average, and prints the results.
    """

    # 1. CLEAR OLD OUTPUT
    # This ensures that new results replace old ones.
    document.getElementById("student_info").innerText = ""
    document.getElementById("summary").innerText = ""
    document.getElementById("output").innerText = ""

    # 2. GET STUDENT NAME FROM HTML INPUTS
    first = document.getElementById("first_name").value
    last = document.getElementById("last_name").value

    # 3. GET GRADES FROM INPUT BOXES
    # Convert each grade to float so Python can calculate properly.
    science = float(document.getElementById("science").value)
    math = float(document.getElementById("math").value)
    english = float(document.getElementById("english").value)
    filipino = float(document.getElementById("filipino").value)
    ict = float(document.getElementById("ict").value)
    pe = float(document.getElementById("pe").value)

    # 4. LISTS OF SUBJECT NAMES + GRADES
    subjects = ["Science", "Math", "English", "Filipino", "ICT", "PE"]
    grades = [science, math, english, filipino, ict, pe]

    # 5. SUBJECT WEIGHTS (UNITS)
    # These represent how important each subject is in the GWA.
    weights = [5, 5, 5, 3, 2, 1]

    # 6. COMPUTE THE WEIGHTED AVERAGE
    # Multiply each grade by its weight → add all → divide by total units.
    weighted_sum = sum(grades[i] * weights[i] for i in range(6))
    total_units = sum(weights)
    gwa = weighted_sum / total_units

    # 7. DISPLAY THE STUDENT'S FULL NAME
    display(f"Name: {first} {last}", target="student_info")

    # 8. DISPLAY SUMMARY OF GRADES PER SUBJECT
    summary = "Grade Summary: "
    for i in range(6):
        # Format: Subject: Grade
        summary += f"{subjects [i]}: {grades[i]: .0f}"
    display(summary, target="summary")

    # 9. DISPLAY FINAL GENERAL WEIGHTED AVERAGE
    # {:.2f} means → show only 2 decimal places
    display(f"Your General Weighted Average is: <b>{gwa:.2f}</b>", target="output")
33