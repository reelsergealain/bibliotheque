from django import forms
from books.models import Author, Category, Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'category', 'quantity', 'published_date', 'isbn']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
        }
        
    def title_clean(self):
        title = self.cleaned_data['title']
        if len(title) < 10:
            raise forms.ValidationError("Le titre doit comporter au moins 10 caractères")
        return title
    
    def isbn_clean(self):
        isbn = self.cleaned_data['isbn']
        if len(isbn) != 13:
            raise forms.ValidationError("L'ISBN doit comporter 13 caractères")
        return isbn
    
    def quantity_clean(self):
        quantity = self.cleaned_data['quantity']
        if quantity < 1:
            raise forms.ValidationError("La quantité doit être supérieure à 0")
        return quantity