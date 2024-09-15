import os
import django
from quotes.models import Tag, Quote
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()


def jsonl_to_db(filepath):
#    util to migrate jsonl to db
    try:
        with open(filepath, 'r') as file:
            for line in file:
                record = json.loads(line.strip())
                quote_text = record.get('quote')
                author_name = record.get('author', 'Unknown')
                tags_list = record.get('tags', [])

                quote, created = Quote.objects.update_or_create(quote=quote_text, author=author_name)
                for tag_name in tags_list:
                    tag, created = Tag.objects.get_or_create(tag=tag_name)
                    if tag not in quote.tags.all():
                        quote.tags.add(tag)
                quote.save()
    except Exception as e:
        print('Error Message', e)


jsonl_to_db('./utils/quotes.jsonl')


