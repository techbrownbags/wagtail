""" STREAM FIELDS LIVE HERE"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional  text')

    class Meta: #noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title & Text"


class RichtextBlock(blocks.RichTextBlock):
    """rich ext with features"""

    class Meta: #noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "FULL RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """rich ext with out features"""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link"
        ]

    class Meta: #noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "SIMPLE RichText"


class CardBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text='Card title')
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40 )),
                ("text", blocks.CharBlock(required=True, max_length=200 )),
                ("button_page", blocks.PageChooserBlock(required=False, )),
                ("button_url", blocks.URLBlock(required=False, help_text="If a button page is selected that will be used first"))
            ]
        )
    )

    class Meta: #noqa
        template = "streams/card_block.html"
        icon = "edit"
        label = "Staff Cards"


class LinkStructValue(blocks.StructValue):
    """ additional logic for urls"""

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        url = None
        if button_page:
            url = button_page.url
        elif button_url:
            url = button_url
        return url


    def title(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        title = None
        if button_page:
            title = button_page.title
        elif button_url:
            title = self.get('button_title')
            if not title:
                title = button_url
        return title

class ButtonBlock(blocks.StructBlock):
    """An external and internal URL"""

    button_page = blocks.PageChooserBlock(required=False,
                                          help_text='If selected this url will be used first')
    button_url = blocks.URLBlock(required=False,
                                 help_text='If selected this url will be used last')
    button_title = blocks.CharBlock(required=False, help_text='Overrides default title')

    class Meta: #noqa
        template = "streams/button_block.html"
        icon = "olaceholder"
        label = "Single Button"
        value_class = LinkStructValue