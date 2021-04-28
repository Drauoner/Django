import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django

django.setup()

from MainApp.models import Topic, Entry

# topics = Topic.objects.all()
# entires = Entry.objects.all()

topic = Topic.objects.get(id=1)
entries = topic.entry_set.order_by("-date_added")

for e in entries:
    print(e)