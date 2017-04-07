from django.core.management.base import BaseCommand
import requests
from bs4 import BeautifulSoup
from ...models import Talk


class Command(BaseCommand):

    help = "Loads talks from pycon.it"

    def handle(self, *args, **options):
        html = requests.get("https://www.pycon.it/p3/schedule/pycon8/").content
        soup = BeautifulSoup(html, "html.parser")
        h3s = soup.find_all(
            lambda t: t.name == "h3" and t.get("class") == ["name"])
        for h3 in h3s:
            if h3.a is not None:
                Talk.objects.get_or_create(name=h3.a.get_text())
