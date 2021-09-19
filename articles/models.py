from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page

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
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('owner', classname="full"),
    ]

    settings_panels = []
    promote_panels = []
