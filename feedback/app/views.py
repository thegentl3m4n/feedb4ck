from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.

# homepage
def home(request):
    email_recieve_on = 'gamer.vish7@gmail.com'
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        dept = request.POST.get('name_of_dept', '')
        subject = request.POST.get('feedback_subject', '')
        feedback_msg = request.POST.get('feedback_msg', '')

        message = "Name: "+name+"\n"+"Email: "+email+"\n"+"Department: "+dept+"\n"+"Subject: "+subject+"\n"+"Message: "+feedback_msg+"\n"           # message with email in it
        message_without_email = "Name: "+name+"\n"+"Department: "+dept+"\n"+"Subject: "+subject+"\n"+"Message: "+feedback_msg+"\n"                  # message without email
        mail_subject = "Feedback from " + name

        if name and dept and subject and feedback_msg:
            if email:
                try:
                    send_mail(mail_subject,
                        message,
                        settings.EMAIL_HOST_USER,
                        [email_recieve_on],
                        fail_silently=False
                    )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('app/thanks/')
            else:
                try:
                    send_mail(mail_subject,
                        message_without_email,
                        settings.EMAIL_HOST_USER,
                        [email_recieve_on],
                        fail_silently=False
                    )
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('app/thanks/')

        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, 'app/home.html')

# thanks response
def thanks(request):
    return render(request, 'app/thanks.html')
