from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=255)

class Rule(models.Model):
    name1 = models.ForeignKey(Name, on_delete=models.CASCADE, related_name='name1_rules')
    name2 = models.ForeignKey(Name, on_delete=models.CASCADE, related_name='name2_rules')
