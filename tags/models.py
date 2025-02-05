from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Tag(models.Model):
    label=models.CharField(max_length=250)

class Tagged_item(models.Model):
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    content_type=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveIntegerField()
    object_type=GenericForeignKey()

