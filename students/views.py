"""
student app views
"""
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import StudentRecord
from .forms import AddRecord
from django.http import HttpResponse
import datetime
import csv


# Create your views here.
def home(request):
    """home page view function"""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "logged In Successfully")
            return redirect("dashboard")
        messages.success(request, "You must have an account to login")
        return redirect("home")
    return render(request, "home.html", {})


def dashboard(request):
    """dashboard view function"""
    if request.user.is_authenticated:
        records = StudentRecord.objects.all().values()
        return render(request, "dashboard.html", {"records": records})
    messages.success(request, "You must be logged in to access the dashboard")
    return redirect("home")


def logout_user(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("home")


def edit_record(request, pk):
    if request.user.is_authenticated:
        current_record = StudentRecord.objects.get(id=pk)
        form = AddRecord(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated Successfully!")
            return redirect("dashboard")
        return render(request, "edit_record.html", {"form": form})
    messages.success(request, "You must be logged in to edit a record")
    return redirect("home")


def add_record(request):
    if request.user.is_authenticated:
        form = AddRecord(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Added Successfully!")
            return redirect("dashboard")
        return render(request, "add_record.html", {"form": form})
    messages.success(request, "You must be logged in to edit a record")
    return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        current_record = StudentRecord.objects.get(id=pk)
        current_record.delete()
        messages.success(request, "Record deleted successfully")
        return redirect("dashboard")
    messages.success(request, "You must be logged in to edit a record")
    return redirect("home")


def view_record(request, pk):
    if request.user.is_authenticated:
        student_record = StudentRecord.objects.get(id=pk)
        return render(request, "record.html", {"student_record": student_record})
    messages.success(request, "You must be logged in to edit a record")
    return redirect("home")


def export_csv(request):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = (
        "attachment; filename " + str(datetime.datetime.now()) + ".csv"
    )
    writer = csv.writer(response)
    writer.writerow(["first_name", "last_name", "email", "course", "gpa"])

    records = StudentRecord.objects.all().values()

    for record in records:
        writer.writerow(
            [
                record.first_name,
                record.last_name,
                record.email,
                record.course,
                record.gpa,
            ]
        )
        return response
