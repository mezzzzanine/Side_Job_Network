from dataclasses import field

from numpy import minimum
from .models import Vacancy
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'minimum_salary', 'maximum_salary', 'description', 'publication_time']

        widgets={
            'title':TextInput(attrs={'class':'form-control', 
                                    'placeholder':'Title'
                                    }),
            'minimum_salary':TextInput(attrs={'class':'form-control', 
                                    'placeholder':'Minimum salary'
                                    }),
            'maximum_salary':TextInput(attrs={'class':'form-control',
                                    'placeholder':'Maximum salary' 
                                    }),
            'description':Textarea(attrs={'class': 'form-control',
                                        'placeholder':'Description'
                                        }),
            'publication_time':DateTimeInput(attrs={'class':'form-control', 
                                                    'placeholder':'Publication time'
                                                    })
        }
