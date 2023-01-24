from django.shortcuts import render

# Create your views here.
def say_hello(request, *args, **kwargs):
    # return render(request, 'hello.html')
    return render(request, 'hello.html', {'name': 'Satya'})
