from mongoengine import Document, StringField, BooleanField


class Contact(Document):
    fullname = StringField(max_length=64)
    email = StringField(max_length=64)
    logic_field = BooleanField(
        default=False
    )