from django.db import models




class Images(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField(null=True)
    picture = models.ImageField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True, default=0)
    height = models.IntegerField(null=True, blank=True, default=0)
    parent_picture = models.IntegerField(null=True, blank=True)
     
    
    def __str__(self):
        return str(self.name)


