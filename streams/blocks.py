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