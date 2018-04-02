from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-paypal2', 'url': 'http://pypi.python.org/pypi/django-paypal2/1.0.2'},
	{'name':'django-paypal', 'url': 'http://pypi.python.org/pypi/django-paypal/0.4.1'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-83',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
