from django.shortcuts import render


def view1(request):
    # Hardcoded data, sent to the template through a context dictionary
    name = "Jonath Kumar"
    roll_no = "KU2027-001"
    department = "Data Science & Chemistry"
    university = "Krea University"
    year = 4
    cgpa = 8.0
    email = "jonath@example.com"
    skills = ["Python", "Django", "Data Analysis", "Chemistry"]

    context = {
        "name": name,
        "roll_no": roll_no,
        "department": department,
        "university": university,
        "year": year,
        "cgpa": cgpa,
        "email": email,
        "skills": skills,
    }
    return render(request, "student/1.html", context)
