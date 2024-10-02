from flask import Blueprint, render_template, request
import logging
import sys
sys.path.append("..")
from functions import search_content

logging.basicConfig(filename='basic.log', level=logging.INFO)  # Для логирования при выполнении поиска

# Создаем новый блюпринт, выбираем имя
main_blueprint = Blueprint('main_blueprint', __name__)  # , template_folder='Homework_12/templates'


@main_blueprint.route("/")  # Главная страница
def main_page():
    logging.info('Открывал главную страницу')
    return render_template('index.html')


@main_blueprint.route('/search')  # Страница поиска поста
def search_page():
    s = request.args.get('s')
    post = search_content(s)
    logging.info('Выполнял поиск')
    return render_template('post_list.html', post=post, s=s)
