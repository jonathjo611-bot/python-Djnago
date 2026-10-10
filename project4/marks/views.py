from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm
from .models import Student


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")     # go to the list page after saving
    else:
        form = StudentForm()
    return render(request, "marks/1.html", {"form": form})


def student_list(request):
    students = Student.objects.order_by("roll_no")
    count = students.count()
    if count:
        class_avg = round(sum(s.percentage() for s in students) / count, 2)
    else:
        class_avg = 0
    return render(request, "marks/2.html", {"students": students, "class_avg": class_avg})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":        # deleting must be a POST, never a plain link
        student.delete()
    return redirect("list")
