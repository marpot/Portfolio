from django.test import TestCase
import models
import pytest
# Create your tests here.

class AboutTestCase(TestCase):
    def setUp(self):
        models.About.objects.create(short_description="opis", description = "rozległy opis", )
