from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': ' Your Class', 'aria-label': 'Todo',
                                      'aria-describedby': 'add-btn', 'autocomplete': 'off'})
                           )


# 'pattern':'[A-Za-z1-3]+' means that there are only letters and digits from 1-3 allowed in the CharField, no special characters, no umlauts/vowels


class TodoFormSecond(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': ' Your Class', 'aria-label': 'Todo',
                                      'aria-describedby': 'add-btn', 'autocomplete': 'off'})
                           )
