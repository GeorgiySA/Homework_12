from flask import Blueprint, render_template, request
import logging
import sys
sys.path.append("..")
from functions import new_post


logging.basicConfig(filename='basic.log', level=logging.INFO)  # Для логирования при загрузке файла

loader_blueprint = Blueprint('loader_blueprint', __name__)  # Создаем новый блюпринт, выбираем имя

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}  # Допустимые расширения изображения


def is_filename_allowed(filename):  # Проверка типа расширения загруженного файла
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


@loader_blueprint.route('/post')  # Реализует страничку "добавить пост"
def post_page_post():
    return render_template('post_form.html')


@loader_blueprint.route('/post', methods=['POST'])  # Загружает файл в папку
def upload_page():
    try:
        picture = request.files.get('picture')
        filename = picture.filename
        if is_filename_allowed(filename):
            content = request.form.get('content')
            picture.save(f'./uploads/images/{filename}')
            new_post(f'./uploads/images/{filename}', content)
            return render_template('post_uploaded.html', content=content, filename=filename)
        else:
            logging.info('Ошибка с расширением файла')
            return 'Ошибка с расширением файла'
    except:
        logging.error('Oшибка загрузки')
        return 'Oшибка загрузки'