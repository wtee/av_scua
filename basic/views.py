from django.shortcuts import render

# Create your views here.
def home_page(request):
    '''
        Home Page located in templates/basic/home.html
    '''
    return render(request, 'basic/home.html')
