from django import forms

"""                                  - Describing the class TodoForm -

The input is limited to 40 letters. The class is form-control and the placeholder is 'Enter your class here'. 
Autocomplete is set on 'off' to avoid distraction while entering a class. 
The attribute 'pattern':'[A-Za-z1-3:-/ ]+' means that there are only letters, digits from 1-3 and whitespaces allowed in the CharField,
no special characters nor umlauts/vowels.
Only '-:/' are allowed as special characters oriented on the module description of FIW. Which special characters are allowed is 
written in the description on the [...]_semester.html sites.
"""


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': ' Enter your class here',
                                      'autocomplete': 'off', 'pattern': '[A-Za-z1-3:-/ ]+'})
                           )


# 'pattern':'[A-Za-z1-3 ]+' means that there are only letters, digits from 1-3 and whitespaces allowed in the CharField, no special characters, no umlauts/vowels
# Only -:/ are allowed as special characters. I oriented on the module description of FIW.

class TodoFormSecond(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': ' Your Class', 'aria-label': 'Todo',
                                      'aria-describedby': 'add-btn', 'autocomplete': 'off', 'pattern': '[A-Za-z1-3 ]+'})
                           )
