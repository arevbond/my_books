import wikipedia

def dowloand_book_desc(title, author):
    wikipedia.set_lang('ru')
    try:
        information = wikipedia.page(f'Произведение {title}')
        return information.content.split('\n\n')[0]
    except:
        pass

