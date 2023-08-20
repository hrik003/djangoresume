from turtle import title
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from .forms import contactForm
from certification.models import Certification
from django.core.mail import EmailMultiAlternatives, send_mail
import datetime
from interest.models import Interest
from workflow.models import Workflow
from skill.models import Skill
from education.models import Education
from experience.models import Experience
from personalInfo.models import PersonalInfo

def HomePage(request):
    certData = Certification.objects.all()
    interestData = Interest.objects.all()
    workflowData = Workflow.objects.all()
    skillData = Skill.objects.all()
    educationData = Education.objects.all().order_by('-from_date')
    experienceData = Experience.objects.all().order_by('-from_date')
    personalData = PersonalInfo.objects.all()

    data = {
        'title' : 'Arijit Resume',
        'certData' : certData,
        'interestData' : interestData,
        'workflowData' : workflowData,
        'skillData' : skillData,
        'educationData' : educationData,
        'experienceData' : experienceData,
        'personalData' : personalData,
    }

    return render(request, 'index.html', data)