from __future__ import unicode_literals
from django.db import models
class Dojo(models.Model):
	name = models.CharField(max_length=255)
	city = models.CharField(max_length=255)
	state = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)


class Ninja(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	dojo = models.ForeignKey(Dojo, models.SET_NULL, related_name="ninjas", blank=True, null=True)