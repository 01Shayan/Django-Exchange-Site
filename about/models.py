from django.db import models

class About(models.Model):
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True, help_text="Google Maps coordinates (latitude,longitude)")
    
    show_address = models.BooleanField(default=True)
    show_email = models.BooleanField(default=True)
    show_phone = models.BooleanField(default=True)
    show_whatsapp = models.BooleanField(default=True)
    show_location = models.BooleanField(default=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "about"
        
    def __str__(self):
        return "About Page Configuration"
