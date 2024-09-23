from django.shortcuts import render, redirect
from .forms import StudentForm

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scholarship_search')  # Redirect after saving student details
    else:
        form = StudentForm()
    
    return render(request, 'register.html', {'form': form})

def scholarship_search(request):
    # Here, we will later implement the web scraping or API calls to find scholarships
    scholarships = []  # Placeholder
    return render(request, 'scholarships.html', {'scholarships': scholarships})
