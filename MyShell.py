import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

t = Topic.objects.get(id=1)

print(t)

entries = t.entry_set.all()

for entry in entries:
    print(entry)

'''

entry = Entry.objects.all()

for t in topics:
    print(f"Topics ID: {t.id}    Topic: {t}")


for e in entry:
    print(f"Topic: {e.topic}    Entry: {e}  Date: {e.date_added}")
'''