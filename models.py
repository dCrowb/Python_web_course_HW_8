from mongoengine import Document, StringField, ListField, ReferenceField, CASCADE



class Author(Document):
    fullname = StringField(max_length=64)
    born_date = StringField(max_length=32)
    born_location = StringField(max_length=64)
    description = StringField()
    

class Quote(Document):
    tags = ListField(max_length=16)
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField(max_length=256)
