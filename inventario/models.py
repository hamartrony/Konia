from django.db import models
import uuid


class Item(models.Model):

    nome = models.CharField(max_length=255, unique=True)
    data_criacao = models.DateField(auto_now_add=True)
