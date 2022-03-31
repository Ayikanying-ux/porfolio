from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.conf import settings
# Create your views here.
def homepage(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        form_data = {
            'fname': fname,
            'lname': lname,
            'email': email,
            'message': message,
        }
        message = '''
        From:\n\t\t{}\n
        Email:\n\t\t{}\n
        message:\n\t\t{}\n
        '''.format(form_data["fname"], form_data["email"], form_data["message"])

        send_mail('You have got an email!', message, email, [settings.RECIPIENT_ADDRESS])
        return redirect("home:homepage")
    return render(request, 'personal/home.html')
