from django.shortcuts import render, HttpResponse
from . import forms
from .models import Book
from django.contrib.auth.decorators import login_required



def HomePage(request):
    return render(request, 'library/home.html')



@login_required
def index(request):
    books = Book.objects.all()
    context = {'books': books}

    return render(request, 'library/index.html', context)



@login_required
def DisplayBook(request):
    if request.method == 'POST':
        data = request.POST.get('BookPath')
        with open(data, 'rb') as pdf:
            response = HttpResponse(pdf.read() ,content_type='application/pdf')
            response['Content-Disposition'] = f'inline;filename={data}'
            return response
    else:
        return HttpResponse('Error 404')


@login_required
def Search(request):
    print('excutec')
    query = request.GET.get('q')
    print(query)
    context = Book.objects.filter(title__icontains=query)
    context = {'books': context}
    return render(request, 'library/index.html', context)



