from django import forms


class TodoForm(forms.Form):
    text=forms.CharField(max_length=40,
        widget=forms.TextInput(
        attrs={'class' : 'form-control', 'placeholder' : ' Your Class', 'aria-label' : 'Todo', 'aria-describedby' : 'add-btn', 'pattern':'[A-Za-z ]+', 'autocomplete': 'off'})
    )

  #'pattern':'[A-Za-z ]+' means that there are only letters allowed in the CharField, no digits, no special characters, no umlauts/vowels


class TodoFormSecond(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': ' Your Class', 'aria-label': 'Todo',
                                      'aria-describedby': 'add-btn', 'pattern': '[A-Za-z ]+', 'autocomplete': 'off'})
                           )