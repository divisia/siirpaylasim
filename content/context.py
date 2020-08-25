from datetime import date, timedelta
from .models import Entry
from django.contrib.contenttypes.models import ContentType
from pinax.likes.models import Like

interval = timedelta(weeks=1)
selected = {'count': -1, 'last_update': date.today()}

def get_entry_with_most_likes(after=None, before=None):
    if selected['count'] > 0 and ((selected['last_update'] + interval) > date.today()):
        return selected
    qs = Entry.objects.all()
    if after:
        qs = qs.filter(created_at__gte=after)
    if before:
        qs = qs.filter(created_at__lte=before)
    
    for entry in qs:
        count = Like.objects.filter(
            receiver_content_type=ContentType.objects.get_for_model(entry),
            receiver_object_id=entry.pk,
        ).count()
        if count > selected['count']:
            selected['pk'] = entry.pk
            selected['count'] = count
            selected['entry'] = entry

    return selected
    

def HighlightedEntry(request):
    return {
        'selected': get_entry_with_most_likes(after=date.today()-interval),
    }