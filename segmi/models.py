from django.db import models

# Create your models here.
class doctor(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class patient(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    disease = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name

class lab(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    def __str__(self):
        return self.Name

class lab_report(models.Model):
    lab= models.ForeignKey(lab, default=0, on_delete=models.CASCADE)
    patient = models.ForeignKey(patient, default="others", on_delete=models.CASCADE)
    doctor = models.ForeignKey(doctor, default="others", on_delete=models.CASCADE)
    report_img = models.ImageField(upload_to='report_img/', default='default.png')
    segment_img = models.ImageField(upload_to='report_img/', default='default.png')
    report_summary = models.CharField(max_length=500)
    medicines = models.CharField(max_length=500)
    def __str__(self):
        return self.patient.Name

