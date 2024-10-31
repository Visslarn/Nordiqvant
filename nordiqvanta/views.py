from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from .forms import CVUploadForm

def home(request):
    return render (request, 'home.html')

def services(request):
    return render (request, 'services.html')

def about(request):
    return render (request, 'about_us.html')

def success(request):
    return render (request, 'success.html')

def work_for_us(request):
    if request.method == 'POST':
        form = CVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            cv_file = request.FILES['cv']


            email_message = EmailMessage(
                subject=f"CV Submission from {name}",
                body=f"Name: {name}\nEmail: {email}",
                from_email='pontusakibruno@gmail.com',
                to=['applications@nordiqvant.com'],
            )

            email_message.attach(cv_file.name, cv_file.read(), cv_file.content_type)
            email_message.send()

            return redirect('success')

    else:
        form = CVUploadForm()

    return render(request, 'work_for_us.html', {'form': form})
