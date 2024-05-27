from django.urls import path
from . import views
from .views import main, page1, page2, buk, get_m, get_buk_detail_page

urlpatterns = [
    # path('main', main, name = 'main'),
    # path('page1', page1, name= 'page1'),
    # # path('page1/<int:id>/', page1, name= 'page1'),
    # path('page2', page2, name= 'page2'),
    # # path('page2/<int:id>/', page2, name= 'page2'),
    path('', get_m, name='m'),
    path('book/<int:id>/', buk, name='book_n'),
    path('book_detail/<int:buck_id>/', get_buk_detail_page, name='book_detail'),
]
