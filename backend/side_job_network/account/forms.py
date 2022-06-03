from dataclasses import field
from logging import PlaceHolder

from numpy import minimum
from .models import Vacancy
from django.forms import ModelForm, TextInput, Textarea, ModelChoiceField, FileInput

class VacancyForm(ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title', 'image', 'minimum_salary', 'maximum_salary', 'description', 'requirements' ,'country', 'city', 'currency', 'owner']

        widgets={
            'title':TextInput(attrs={'class':'form-control', 
                                    'placeholder':'Title',
                                    }),


            'minimum_salary':TextInput(attrs={'class':'form-control col-md-3', 
                                    'placeholder':'Minimum salary',
                                    'requirment':False
                                    }),


            'maximum_salary':TextInput(attrs={'class':'form-control col-md-3',
                                    'placeholder':'Maximum salary',
                                    'requirment':False 
                                    }),


            'description':Textarea(attrs={'class': 'form-control',
                                        'placeholder':'Description'
                                        }),


            'requirements':Textarea(attrs={'class': 'form-control',
                                        'placeholder':'Requirements'
                                        }),
            

            'currency':TextInput(attrs={'class':'form-control',
                                        'placeholder':'Currency'}),


            'country':TextInput(attrs={'class':'form-control',
                                        'placeholder':'Country'}),


            'city':TextInput(attrs={'class':'form-control',
                                        'placeholder':'City'}),


            'owner':TextInput(attrs={'class':'form-control',
                                        'placeholder':'Owner'})
        }
