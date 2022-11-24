from django.db import models
from wagtail.admin.edit_handlers import FieldPanel

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.search import index
from wagtail_headless_preview.models import HeadlessMixin


class BlogPage(HeadlessMixin, Page):
    body = RichTextField()
    date = models.DateField("Post date")

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body'),
    ]