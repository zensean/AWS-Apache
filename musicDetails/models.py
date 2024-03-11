from django.db import models

# Create your models here.

class Activity(models.Model):
    version=models.TextField()
    UID=models.TextField(default='')
    titil=models.TextField(default='')
    category=models.TextField(default='')
    showUnit=models.TextField(default='')
    descriptionFilterHtml=models.TextField(default='')
    discountInfo=models.TextField(default='')
    imageURL=models.TextField(default='')
    masterUnit=models.TextField(default='')
    subUnit=models.TextField(default='')
    supportUnit=models.TextField(default='')
    otherUnit=models.TextField(default='')
    webSales=models.TextField(default='')
    sourceWebPromote=models.TextField(default='')
    comment=models.TextField(default='')
    editModifyDate=models.TextField(default='')
    sourceWebName=models.TextField(default='')
    startDate=models.TextField(default='')
    endDate=models.TextField(default='')
    hitRate=models.TextField(default='')

class Performance(models.Model):
    time=models.TextField(default='')
    location=models.TextField(default='')
    locationName=models.TextField(default='')
    onSales=models.TextField(default='')
    latitude=models.TextField(default='')
    longitude=models.TextField(default='')
    Price=models.TextField(default='')
    endTime=models.TextField(default='')
