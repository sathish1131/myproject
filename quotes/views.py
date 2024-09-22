from django.shortcuts import render
from .models import UserTag, Tag, Quote
import random, json
from django.http import JsonResponse

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
    user_tags = UserTag.objects.filter(user=user).values_list('tag__id', flat=True)
    all_quotes = Quote.objects.all()
    random_quote = "Failed to fetch quotes"
    if user_tags:
        random_tag = random.choice(user_tags)
        if random_tag:
            tag_quotes = Quote.objects.filter(tags__id = random_tag)
            if tag_quotes:
                random_quote = random.choice(tag_quotes)
            else:
                return ('Quotes not present for selected Category')
        else:
            return ('Categories not Correct')
    else:
        random_quote = random.choice(all_quotes)
    
    return random_quote

def save_tags(request):
    if request.method == 'POST':
        selected_tags = request.POST.getlist('tags[]')
        user = request.user
        UserTag.objects.filter(user=user).delete()
        for tag_name in selected_tags:
            tag, created = Tag.objects.get_or_create(tag=tag_name)
            tag.save()
            usertag, created = UserTag.objects.update_or_create(user=user, tag=tag)
            usertag.save()
        return JsonResponse({'status': 'success'})
    
def quotes(request):
    user = request.user
    quote = get_random_quote(user)
    tags = Tag.objects.all()
    existing_tags = UserTag.objects.filter(user=user).values_list('tag__tag', flat=True)
    return render(request, 'quotes.html', {'quote': quote, 'tags': tags, 'existing_tags': list(existing_tags)})