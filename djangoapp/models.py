from django.db import models

# Create your models here.


class News(models.Model):# basaga model
    title = models.CharField(max_length=500,verbose_name="Mavzu") #textni miqdorini belgilash max_length
    content = models.TextField(blank=True, null=True, verbose_name="Sarlavha") # null=True textni bo'sh qoldirsayam bo'ladi , blank=Ture
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Kirish vaqti")# ma'lumot qo'shgan paytizni qo'shib ketadi, yozib ketadi
    updated_at=models.DateTimeField(auto_now=True, verbose_name="O'zgarish vaqti")#oxirgi update ni yozib ketadi , update qilib yozib ketadi
    photos=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True , verbose_name="Rasm")#chislosi bilan saralab ketadi (blank=True bunda rasm qo'shmasaham bo'ladi)
    is_bool=models.BooleanField(verbose_name="bool") #default=True
    category=models.ForeignKey('Category',on_delete=models.CASCADE) # agar Category class bu classdan tepada bo'lsa qo'shtirnoqni yozmaymiz ,on_delete bu categoriyadagi narsani o'chirseyz qolgan barcha joydan o'chib ketadi , ma'lumotlar 
    views=models.IntegerField(default=0,verbose_name="Ko'rinishlar")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Ma'lumot"
        verbose_name_plural="Ma'lumotlar"
        ordering=['created_at']

class Category(models.Model):
    title=models.CharField(max_length=150)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Kategoriya"
        verbose_name_plural="Kategoriyalar"


class Counts(models.Model):
    category=models.CharField(max_length=150,verbose_name='Categoriya')
    counts=models.IntegerField(max_length=10,verbose_name='contentlar soni')
    
    def __str__(self):
        return self.category
    
    class Meta:
        verbose_name="Kategoriya counter"
        verbose_name_plural="Kategoriyalar counters"