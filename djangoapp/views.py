from django.shortcuts import render , redirect
from django.urls import reverse_lazy

# Create your views here.

from django.views.generic import DetailView , CreateView , ListView

from djangoapp.models import News , Category , Counts
from .forms import NewsForm , CategoryForm , SearchForm


def index(request):
    news=News.objects.all()
    # categories=Category.objects.all()
    
    category=Category.objects.all()
    categories=Counts.objects.all()
    
    if len(category)!=len(categories):
        count_item(request)
    
    content={
        "news":news,
        "title":"Ma'lumotlar",
        "categories":categories,
        "category":category
        # 'news':posts,
        
    }
    
    return render(request,'HTML/news_list.html',context=content)


# class HomeNews(ListView):
#     model=News
#     template_name='HTML/news_list.html'
#     context_object_name="news"
    
#     def get_queryset(self):
#         return News.objects.filter(is_bool=True)


def get_category(request,category_id):
    news=News.objects.filter(category=category_id)
    # categories=Category.objects.all()
    # category=News.objects.get(pk=category_id)
    category=Category.objects.all()
    categories=Counts.objects.all()
    
    if len(category)!=len(categories):
        count_item(request)
    
    content={
        "news":news,
        "title":"Ma'lumotlar",
        "categories":categories,
        "category":category
        
    }
    
    return render(request,'HTML/category_list.html',context=content)

# def add_news(request):
#     if request.method=="POST":
#         form= NewsForm(request.POST)
#         if form.is_valid():
#             News.objects.create(**form.cleaned_data)
#             news=form.save()
#             return redirect("home")
#     else:
#         form= NewsForm()
#     content={
#         "form":form
        
#     }
    
#     return render(request,'HTML/add_news.html',context=content)

def add_catagory(request):
    if request.method=="POST":
        form=CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("add_news")
    else:
        form=CategoryForm()
        content={
            "form":form
        }
    
    return render(request,'HTML/add_category.html',context=content)



class CreateNews(CreateView):
    form_class=NewsForm
    template_name='HTML/add_news.html'
    success_url=reverse_lazy('home')


class GetNew(DetailView):
    model=News
    context_object_name='item'
    pk_url_kwarg='news_id'
    template_name='HTML/news.html'

def delete_news(request,new_id):
    new=News.objects.get(pk=new_id)
    new.delete()
    return redirect('home')

def go_home(request):
    return redirect('home')


def delete(request):
    news=News.objects.all()
    categories=Category.objects.all()
    
    content={
        'news':news,
        'title':"Ma'lumotlar",
        'categories':categories
    }
    return render(request,'HTML/delete.html',context=content)

def search(request):
    
    categories=Category.objects.all()
    # search = request.POST['search']
    search_post = request.GET.get('search')
    
    if search_post:
        posts = News.objects.filter(title__icontains=search_post)
    else:    # If not searched, return default posts    
        posts = News.objects.all().order_by("-created_at")

    content={
        'searchs':posts,
        "title":"Ma'lumotlar",
        "categories":categories,
        # "news":news,  
    }
    if len(posts)==0:
        return render(request,'HTML/return_null.html')
    else:
        return render(request,'HTML/search_list.html',context=content)


# def search(request):
#     if request.method=='POST':
#         search = request.POST['search']
#         posts = News.objects.filter(title__contains=search)
        
#         content={
#         'searchs':posts,
#         "title":"Ma'lumotlar",
#         # "news":news,  
#     }
        
#     else:    # If not searched, return default posts    
#         posts = News.objects.all().order_by("-created_at")

#         content={
#             'searchs':posts,
#             "title":"Ma'lumotlar",
#             # "news":news,  
#         }
#     if len(posts)==0:
#         return render(request,'HTML/return_null.html')
#     else:
#         return render(request,'HTML/search_list.html',context=content)



# from rest_framework import filters

# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title', 'content']


# class GoOne(ListView):
#     model = News
#     context_object_name = 'items'
#     pk_url_kwarg='get_id'
#     template_name = "HTML/goone.html"
#     def get_queryset(self):
#         return News.objects.filter(is_bool=True)
    
    
def get_one(request,get_id):
    news=News.objects.filter(pk=get_id)
    
    content={
        "one_news":news,
        "title":"Ma'lumotlar",
    }
    
    return render(request,'HTML/goone.html',context=content)


# def searchh(request):
#     languages = News.objects.all()
#     return render(request,'inc/nav.html',{"languages":languages})

# from django.db.models import Q 

# def search(request):
#     search_post = request.GET.get('search')
    
#     if search_post:
#         posts = News.objects.filter(Q(title__icontains=search_post) | Q(content__icontains=search_post))
#     else:    # If not searched, return default posts    
#         posts = News.objects.all().order_by("-created_at")
    
#     return render(request,{'posts':posts})



def count_item(request):
    summ=Category.objects.all()
    
    for id in range(1,len(summ)+1):
        cats=Category.objects.filter(pk__in=[id])
        # print("**************************************************")
        # print(cats)
        count=News.objects.filter(category__in=cats).count()
        print(count)
        
        # for i in cats:  #update
        #     for item in range(id,id+1):
        #         new=Counts.objects.get(pk=item)
        #         new.category=i.title
        #         new.counts=count
        #         new.save()
        
        for item in cats:
            
            data=Counts(category=item,counts=count)
            data.save()
    return data