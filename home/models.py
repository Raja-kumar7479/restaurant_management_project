from django.db import models
classnMenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)
    class Meta:
        verbaose_name = "Menu_Category"
        verbaose_name_plural ="Menu_category"
        ordering =["name"]
    def __str__(self):
        return self.name
