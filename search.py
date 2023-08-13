import connect
from models import Author, Quote

AUTHORS = Author.objects()
QUOTES = Quote.objects()

def search_by_name(name):
    quote_list = []
    for author in AUTHORS(fullname__contains=name):
        for quote in QUOTES(author__contains=author.id):
            quote_list.append(quote.quote.encode('utf-8'))
    return quote_list
        
            
def search_by_tags(tags):
    tags_list = tags.split(',')
    quote_list = []
    for tag in tags_list:
        for quote in QUOTES(tags__contains=tag.strip()):
            quote_list.append(quote.quote.encode('utf-8'))
    return quote_list


if __name__ == '__main__':
    while True:
        command = input('Input command: ').strip() 
        if command[:5] == "name:":
            arguments = command[6:]
            print(search_by_name(arguments))
        elif command[:5] == "tags:":
            arguments = command[6:]
            print(search_by_tags(arguments))
        elif command[:4] == "exit":
            print('Goodby')
            break
        else:
            print('Command is incorrect! Try again!')
        command = ''