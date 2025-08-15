from django import forms
from mainapp.models import UserInfo
from .models import Project


class ProjectForm(forms.ModelForm):
    ADDITIONAL_ROOM_CHOICES = [
        ('puja_room', 'Puja Room'),
        ('study_room', 'Study Room'),
        ('guest_room', 'Guest Room'),
        ('store_room', 'Store Room'),
        ('home_theater', 'Home Theater'),
        ('gym', 'Home Gym'),
    ]

    OUTDOOR_AREA_CHOICES = [
        ('balcony', 'Balcony'),
        ('terrace_garden', 'Terrace Garden'),
        ('lawn', 'Lawn'),
        ('veranda', 'Veranda'),
        ('parking_space', 'Parking Space'),
        ('swimming_pool', 'Swimming Pool'),
    ]

    additional_rooms = forms.MultipleChoiceField(
        choices=ADDITIONAL_ROOM_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Additional Rooms'
    )

    outdoor_areas = forms.MultipleChoiceField(
        choices=OUTDOOR_AREA_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Outdoor Areas'
    )

    class Meta:
        model = Project
        fields = [
            'projectname',  'budget', 
            'duration',  'location', 
            'plot_size', 'house_type', 'num_floors', 'basement', 'parking_required',
            'bedrooms', 'bathrooms', 'kitchen_each_floor',
            'preferred_material', 'construction_style', 'solar_panel', 
            'design_reference', 'special_requirements',
            'additional_rooms', 'outdoor_areas'
        ]
        widgets = {
            'projectname': forms.TextInput(attrs={'class': 'form-control'}),
	    'budget': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            
            'plot_size': forms.TextInput(attrs={'class': 'form-control', 'id': 'plot_size'}),
            'house_type': forms.Select(attrs={'class': 'form-control'}),
            'num_floors': forms.TextInput(attrs={'class': 'form-control', 'id': 'num_floors'}),
            'basement': forms.Select(attrs={'class': 'form-control', 'id': 'basement'}),
            'parking_required': forms.Select(attrs={'class': 'form-control'}),
            
            'bedrooms': forms.Select(attrs={'class': 'form-control', 'id': 'bedrooms'}),
            'bathrooms': forms.TextInput(attrs={'class': 'form-control', 'id': 'bathrooms'}),
            'kitchen_each_floor': forms.Select(attrs={'class': 'form-control'}),
            
            'preferred_material': forms.Select(attrs={'class': 'form-control'}),
            'construction_style': forms.Select(attrs={'class': 'form-control'}),
            
            'design_reference': forms.URLInput(attrs={'class': 'form-control'}),
            'special_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

        labels = {
            'projectname': 'Project Name',
            'description': 'Description',
            'duration': 'Duration (days)',
            'budget': 'Budget (₹)',
            'location': 'Location',
            'requirement_file': 'Project Requirement File',

            'plot_size': 'Plot Size (e.g., 30x40)',
            'house_type': 'Type of House',
            'num_floors': 'Number of Floors',
            'basement': 'Do you want a basement?',
            'parking_required': 'Parking Required',
            'bedrooms': 'Number of Bedrooms',
            'bathrooms': 'Number of Bathrooms',
            'kitchen_each_floor': 'Kitchen on Each Floor?',
            'additional_rooms': 'Additional Rooms',
            'outdoor_areas': 'Outdoor Areas',
            'preferred_material': 'Preferred Construction Material',
            'construction_style': 'Preferred Construction Style',
            'solar_panel': 'Include Solar Panel Setup?',
            'design_reference': 'Design Reference Link',
            'special_requirements': 'Special Requirements',
        }

    def clean_additional_rooms(self):
        return self.cleaned_data['additional_rooms']

    def clean_outdoor_areas(self):
        return self.cleaned_data['outdoor_areas']



















