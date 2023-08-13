from models import Author, Quote
import json
import connect


def load_authors(file):
    with open(file, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    
    for author in json_data:
        Author(
            fullname=author["fullname"],
            born_date=author["born_date"],
            born_location=author["born_location"],
            description=author["description"]
        ).save()
    
        
def load_quotes(file):
    with open(file, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
    authors = Author.objects()
    
    for quote in json_data:
        list_id = []
        for author in authors:
            if quote['author'] == author.fullname:
                list_id.append(author.id)
        Quote(
            tags=quote["tags"],
            author=list_id,
            quote=quote["quote"]
        ).save()


if __name__ == '__main__':
    load_authors('data/authors.json')
    load_quotes('data/quotes.json')