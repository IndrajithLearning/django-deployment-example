import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")

import django 
django.setup()

import random
from first_app.models import AccessReocrd,Topic,WebPage
from faker import Faker

fakegen = Faker()
topic = ["Search","Social","Market","Economic","Sports"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t

def populate(n=5):

    for entry in range(n):

        top = add_topic()

        fake_url = fakegen.url()
        fake_data = fakegen.date()
        fake_name = fakegen.company()

        webpg = WebPage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]

        acc =  AccessReocrd.objects.get_or_create(name=webpg,date=fake_data)[0]


if __name__ == "__main__":
    print("Poluating!!!")
    populate(n=25)
    print("Population Done!!!")