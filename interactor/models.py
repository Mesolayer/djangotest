from django.db import models

class Friends(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length = 100, default = "")
    website = models.TextField(max_length = 200,  default = "")
    LOR_contact = models.CharField(max_length = 100,  default = "")
    ext_contact = models.CharField(max_length = 100,  default = "")
    materials_rec = models.TextField(max_length = 200,  default = "")
    notes = models.TextField(max_length = 500,  default = "")
    plans = models.TextField(max_length = 500,  default = "")

    def __str__(self):
        return self.name


