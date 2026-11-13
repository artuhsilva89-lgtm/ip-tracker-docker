from django.db import models

class IP_Tracker(models.Model):
    
    STATUS_CHOICES = (
        ('active', 'Ativo'),
        ('inactive', 'Inativo'),
        ('manutencao', 'Manutencao'),
        ('reservado', 'Reservado'),
    )
    
    address = models.CharField(max_length = 50)
    vlan = models.CharField(max_length = 20)
    device = models.CharField(max_length = 30)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES)
    
    def __str__(self):
        return self.device
