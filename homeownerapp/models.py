from django.db import models
from mainapp.models import UserInfo
#create your models here

class Project(models.Model):
    projectname = models.CharField(max_length=255)

    homeowner = models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name='project_homeowner')
    contractor = models.ForeignKey(UserInfo,on_delete=models.SET_NULL,null=True, blank=True,related_name='project_contractor')
    
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField(help_text="Estimated number of days", null=True, blank=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2)
    
    progress = models.PositiveIntegerField(default=0, help_text="Completion percentage")

    location = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('planned', 'Planned'),
            ('designing_phase', 'Designing Phase'),
            ('awaiting_approval', 'Awaiting Approval'),
            ('under_construction', 'Under Construction'),
            ('delayed', 'Delayed'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='planned'
    )
    
    plot_size = models.CharField(max_length=50, blank=True)
    
    HOUSE_TYPES = [
        ('duplex', 'Duplex'),
        ('bungalow', 'Bungalow'),
        ('villa', 'Villa'),
        ('independent_floor', 'Independent Floor'),
        ('flat', 'Modern Flat'),
    ]
    house_type = models.CharField(max_length=50, choices=HOUSE_TYPES, blank=True)

    num_floors = models.CharField(max_length=10, blank=True) 
    basement = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')], blank=True)

    PARKING_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('covered', 'Covered Parking'),
        ('open', 'Open Parking')
    ]
    parking_required = models.CharField(max_length=20, choices=PARKING_CHOICES, blank=True)

    bedrooms = models.CharField(max_length=10, choices=[
        ('1bhk', '1 BHK'),
        ('2bhk', '2 BHK'),
        ('3bhk', '3 BHK'),
        ('4+', '4+ BHK')
    ], blank=True)

    bathrooms = models.CharField(max_length=10, blank=True) 
    kitchen_each_floor = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')], blank=True)

    additional_rooms = models.JSONField(blank=True, null=True)  
    outdoor_areas = models.JSONField(blank=True, null=True)

    MATERIAL_CHOICES = [
        ('bricks', 'Red Bricks'),
        ('aac', 'AAC Blocks'),
        ('fly_ash', 'Fly Ash Bricks'),
        ('concrete', 'Concrete Blocks'),
        ('not_sure', 'Not Sure')
    ]
    preferred_material = models.CharField(max_length=50, choices=MATERIAL_CHOICES, blank=True)

    STYLE_CHOICES = [
        ('modern', 'Modern'),
        ('traditional', 'Traditional'),
        ('contemporary', 'Contemporary'),
        ('minimalist', 'Minimalist'),
        ('not_decided', 'Not Decided')
    ]
    construction_style = models.CharField(max_length=50, choices=STYLE_CHOICES, blank=True)

    solar_panel = models.BooleanField(default=False)

    design_reference = models.URLField(blank=True, null=True)
    special_requirements = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.projectname} ({self.status})"




















