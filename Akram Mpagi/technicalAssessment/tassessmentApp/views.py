from django.shortcuts import render
from django.shortcuts import redirect
from .models import appForm
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       course = request.POST['course']
       entry_scheme = request.POST['entry_scheme']
       intake = request.POST['intake']
       sponsorship = request.POST['sponsorship']
       gender = request.POST['gender']
       date_of_birth = request.POST['date_of_birth']
       residence = request.POST['residence']
       

       customer = appForm.objects.create(first_name=first_name, last_name=last_name, course=course,  entry_scheme=entry_scheme, intake=intake, sponsorship=sponsorship, gender=gender, date_of_birth=date_of_birth, residence=residence)
       customer.save()
       messages.success(request, 'Form has been Submitted Successfully!')
       return redirect('index') 

    else:
        return render(request, 'tassessmentApp/index.html', {})
