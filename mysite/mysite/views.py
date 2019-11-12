from django.shortcuts import render

def index(request):
    """View function for home page of site"""
    context = {
            'test_var': 'test'

    }
    return render(request, 'index.html', context=context) 
