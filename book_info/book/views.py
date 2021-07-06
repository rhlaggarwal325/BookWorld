from django.shortcuts import redirect, render
from .models import Book
from django.contrib import messages
from .forms import BookForm, BookSearch

# Create your views here.
def home(request):
    return render(request, 'book/home.html')

def addBook(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Book added successfully ')
            return redirect('search')
    else:
        form = BookForm()
    return render(request, 'book/addbook.html', {'form':form})

def searchBook(request):
    form = BookSearch()
    frst = True
    books = Book.objects.all()
    if request.method == 'POST':
        form = BookSearch(request.POST)
        if form.is_valid():
            result = True
            genre = form.cleaned_data.get("genre")
            language = form.cleaned_data.get("language")
            if language != [] or genre != []:
                if language != [] and genre != []:
                    books = Book.objects.filter(genre__in = genre).filter(language__in=language)
                elif language != []:
                    books = Book.objects.filter(language__in=language)
                elif genre != []:
                    books = Book.objects.filter(genre__in = genre)
            else:
                books = Book.objects.all()
            if books.count() == 0:
                result = False
            return render(request, 'book/search.html', {'form':form,'books':books,'result':result})

    return render(request, 'book/search.html', {'form':form,'books':books,'frst':frst})

def aboutus(request):
    return render(request, 'book/aboutus.html')