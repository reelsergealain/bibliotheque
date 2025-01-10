from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Auteurs'
    
    
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Catégories"
    
class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.title} ({self.quantity})"
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'Livres'