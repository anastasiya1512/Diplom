# Diplom
Diplom_Project
Этот проект представляет собой автоматизированный тестовый фреймворк на базе pytest, selenium и allure для проверки API и UI веб-приложения Кинопоиск.

Используемые библиотеки
pytest

selenium

allure-pytest

requests

webdriver-manager

flake8

Возможности
API тестирование публичного REST API UI тестирование через Selenium WebDriver Генерация отчетов с помощью Allure Структурированная архитектура (Page Object Model)

Структура проекта
Pages:

settings.py # Настройки проекта (BASE_URL, API ключ и т.д.)

search_page.py # PageObject для страницы поиска

movie_page.py # PageObject для страницы фильма

main_page.py # Базовый класс страницы

Test

test_api.py # API тесты

test_ui.py # UI тесты

Шаблон для автоматизации тестирования на python
Шаги
Склонировать проект - 'git clone https://github.com/RuslanErg/Diplom_project.git'
Установить зависимости - 'pip3 install > -r requirements.txt'
Запустить все тесты (UI + API) - 'python -m pytest --alluredir=allure-results allure server allure-results'
Запустить только UI: 'python -m pytest test/test_ui.py --alluredir=allure-results'
Запустить только API: 'python -m pytest test/test_api.py --alluredir=allure-results'
Полезные ссылки
[Гайд по Markdown] (https://www.markdownguide.org/basic-syntax/)
[Генератор файлов .gitignore] (https://www.toptal.com/developers/gitignore.)
[Про pip freez] (https://pip.pypa.io/en/stable/cli/pip_freeze/)
