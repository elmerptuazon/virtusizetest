from django.test import TestCase
from webaccessread.models import WebAccessRead

class WebAccessReadTestCase(TestCase):
    def setUp(self):
        WebAccessRead.objects.create(link="http://www.python.org", word="python", count=166)

    def test_animals_can_speak(self):
        lion = WebAccessRead.objects.get(link="http://www.python.org")
        word = WebAccessRead.objects.get(word="python")
        count = WebAccessRead.objects.get(count=166)