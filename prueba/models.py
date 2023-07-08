# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Mes(models.Model):
    nombre = models.CharField(primary_key=True, max_length=255)
    numero = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mes'

class Manga(models.Model):
    # Definición de campos
    mangaid=models.IntegerField()
    name = models.CharField(primary_key=True)
    type = models.CharField()
    score= models.FloatField()
    startyear=models.IntegerField()

    class Meta:
        db_table = 'manga'  

class Anime(models.Model):
    # Definición de campos
    name = models.CharField(primary_key=True)
    type = models.CharField()
    score= models.FloatField()
    startyear= models.IntegerField()   

    class Meta:
        db_table = 'anime'  


class Author(models.Model):
    # Definición de campos
    mangaid=models.IntegerField()
    firstname=models.CharField(primary_key=True)
    lastname=models.CharField()
    art=models.IntegerField()
    story=models.IntegerField()

    class Meta:
        db_table = 'author' 

class Genre2(models.Model):
    # Definición de campos 
    mangaid=models.IntegerField()
    genre=models.CharField(primary_key=True)

    class Meta:
        db_table = 'genre2' 

class Allmangas(models.Model):
    # Definición de campos
    name = models.CharField(primary_key=True)
    type = models.CharField()
    score= models.FloatField()
    startyear=models.IntegerField()
    firstname=models.CharField()
    lastname=models.CharField()
    genre=models.CharField()
    


    class Meta:
        db_table = 'allmangas'		

class Filtroanime(models.Model):
    # Definición de campos
    animename=models.CharField(primary_key=True)
    manganame=models.CharField()

    class Meta:
        db_table = 'filtroanime' 