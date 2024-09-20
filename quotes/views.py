from django.shortcuts import render
from .models import UserTag, Tag, Quote
import random, json
from django.http import HttpResponse

# Create your views here.

def load_quotes(request):
    filepath = 'static/quotes.jsonl'
#    function to migrate jsonl to db
    try:
        with open(filepath, 'r') as file:
            i = 0
            for line in file:
                record = json.loads(line.strip())
                quote_text = record.get('quote')
                author_name = record.get('author', 'Unknown')
                tags_list = record.get('tags', [])
                i = i+1
                quote, created = Quote.objects.update_or_create(quote=quote_text, author=author_name)
                for tag_name in tags_list:
                    tag, created = Tag.objects.get_or_create(tag=tag_name)
                    if tag not in quote.tags.all():
                        quote.tags.add(tag)
                quote.save()
                print('quote saved ',i)
            print('Total saved quote = ',i)
    except Exception as e:
        print('Error Message', e)

def get_random_quote(user):
    user_tags = UserTag.objects.filter(user=user).values_list('tag', flat=True)
    if not user_tags:
        return None
    random_tag = random.choice(user_tags)

    tag_quotes = Quote.objects.filter(tags__id = random_tag)
    if not tag_quotes:
        return None
    random_quote = random.choice(tag_quotes)

    return random_quote



def quotes(request):
    quote = get_random_quote(request.user)
    return render(request, 'quotes.html', {'quote': quote})