from django.contrib import admin
from django.urls import path

from djangoapp.views import add_catagory,GetNew,get_category,CreateNews,delete,delete_news,get_one,search, index

urlpatterns=[
    path('',index,name='home'),
    # path('',HomeNews.as_view,name='home'),
    # path('/category/<int:category_id>/',get_category,name='category'),
    # path('add_news/',add_news,name='add_news'),
    path('add_category/',add_catagory,name="add_category"),
    
    path('new/<int:news_id>/', GetNew.as_view(), name="new"),
    path('category/<int:category_id>/', get_category, name="category"),
    path('add_news/', CreateNews.as_view(), name="add_news"),
    path('delete/', delete, name="delete"),
    path('delete_news/<int:new_id>/', delete_news, name="delete_news"),
    # path('onenews/<int:pk>/', GoOne.as_view(), name="get_one"),
    path('onenews/<int:get_id>/', get_one, name="get_one"),
    path('get/',search,name='get_search')
    

]