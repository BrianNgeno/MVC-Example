from django.db import models

# Create your models here.


    
class HomeInfo(models.Model):
    title= models.CharField(max_length=100)
    time_created = models.DateField(auto_now_add=True)
    publisher = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    content =  models.TextField()

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title
    
    def save_info(self):
        self.save()

    def del_info(self):
        self.delete()
