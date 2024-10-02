import json


def load_json():  # Записывает посты в файл posts.json
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def search_content(form):  # Поиск постов по ключу
    return [i for i in load_json() if form.lower() in i['content'].lower()]


def new_post(pic, content):  # Передача нового поста для записи в файл
    list_ = load_json()
    list_.append({'pic': pic, 'content': content})
    with open('posts.json', 'w') as file:
        json.dump(list_, file, ensure_ascii=False)
