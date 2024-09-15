from django.shortcuts import render
from .models import UserTag, Tag, Quote
import random

# Create your views here.

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