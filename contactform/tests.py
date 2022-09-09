from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from . import views


# Create your tests here.

# View Tests


class TestUrls(SimpleTestCase):

    def test_form_url(self):
        url = reverse('form')
        self.assertEquals(resolve(url).func, views.form)

    def test_form_url(self):
        url = reverse('board')
        self.assertEquals(resolve(url).func.view_class, views.HomePage)


# Model Tests

# View Tests
