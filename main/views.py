from django.shortcuts import render

from main.models import Avtor, Book, Review


def get():
    avtors = Avtor.objects.all()
    books = Book.objects.all()
    # for i in avtors:
    #     print(i, i.book_set.all())
    #     print('---------')
    context = {
        'avtors': avtors,
        'books': books,
    }
    return context


def page1(request):
    context = get()
    return render(request, 'page1.html', context)


def page2(request):
    context = get()
    return render(request, 'page2.html',context)


def main(request):
    context = get()
    return render(request, 'main.html',context)





def get_m(request):
    avtors = Avtor.objects.all()
    books = Book.objects.all()
    context = {
        'avtors': avtors,
        'books': books,
    }
    return render(request, 'm.html', context)

def buk(request,id):
  avtors = Avtor.objects.all()
  book = Book.objects.filter(autor_id=id)
  context = {
      'avtors': avtors,
      'books': book,
      'id':id,
             }
  return render(request, 'book.html', context)
def get_buk_detail_page(request,buck_id):
    book = Book.objects.get(id=buck_id)

    context = {
        'book':book,
    }
    return render(request, 'book_detail.html', context)