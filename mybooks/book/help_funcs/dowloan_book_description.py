import wikipedia

def dowloand_book_desc(title, author):
    wikipedia.set_lang('ru')
    information = wikipedia.page(f'Книга {title}')
    return information.content.split('\n\n')[0]

