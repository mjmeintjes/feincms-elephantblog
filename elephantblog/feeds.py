from django.conf import settings
from django.contrib.syndication.views import Feed

from feincms.translations import short_language_code

from models import Entry

import settings

class EntryFeed(Feed):
    title = settings.BLOG_TITLE
    link = '/blog/'
    description = settings.BLOG_DESCRIPTION
    
    def items(self):
        if 'translations' in Entry._feincms_extensions:
            return Entry.objects.active().filter(language=short_language_code).order_by('-published_on')
        else:
            return Entry.objects.active().order_by('-published_on')
        
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        content = u''.join(c.render() for c in item.content.main)
        return content