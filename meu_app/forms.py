from django import forms

class ProdutoForm(forms.Form):
    nome = forms.CharField(max_length=100)
    descricao = forms.CharField(widget=forms.Textarea, required=False)
    preco = forms.DecimalField(max_digits=10, decimal_places=2)
    quantidade = forms.IntegerField(initial=0)
