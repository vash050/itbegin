from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel

from authapp.models import SiteUser


class HomePage(Page):
    """
    main page
    """
    parent_page_types = []
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    settings_panels = []
    promote_panels = []


class Article(Page):
    """
    model article
    """
    subpage_types = []
    image = models.ForeignKey('wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+')
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('owner', classname="full"),

    ]

    settings_panels = []
    promote_panels = []

    def avatar_or_default(self, default_path="../static/img/news1.png"):
        if self.image:
            return self.image
        return default_path
