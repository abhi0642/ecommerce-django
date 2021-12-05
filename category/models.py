from django.db import models

# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=40,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.CharField(max_length=700,blank=True)
    cat_image=models.ImageField(upload_to='photoes/category',blank=True)

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Catogories'

    def __str__(self):
        return self.category_name
