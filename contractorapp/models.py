from django.db import models
from homeownerapp.models import*
from mainapp.models import *
# Create your models here.
class ContractorApplication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='applications')
    contractor = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='contractor_applications')
    proposal_text = models.TextField()
    design_file = models.FileField(upload_to='designs/', null=True, blank=True)
    estimated_budget = models.DecimalField(max_digits=12, decimal_places=2)
    estimated_duration = models.IntegerField(help_text="Estimated number of days")
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected')
        ],
        default='pending'
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contractor.name}'s Application for {self.project.projectname}"


class ProgressUpdate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='progress_updates')
    update_text = models.TextField()
    progress_percent = models.PositiveIntegerField()
    image = models.ImageField(upload_to='progress_images/', null=True, blank=True)
    updated_by = models.ForeignKey(UserInfo, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Progress Update ({self.progress_percent}%) for {self.project.projectname}"



