# autotest_framework

## Шаблон для автоматизации тестирования на Python

### Шаги
1. Склонировать проект `git clone https://github.com/dimkor/autotest_framework.git`
2. Установить все зависимости `pip install -r requirements.txt`
3. Запустить тесты `python -m pytest`
4. Сгенерировать отчет `allure generate allure-files -o allure-report`
5. Открыть отчет `allure open allure-report`

### Стек:
- pytest
- selenium
- webdriver manager
- requests
- _sqlalchemy_
- allure
- configparser
- json
- urllib

### Структура:
- ./test - тесты
- ./pages - описание страниц
- ./api - хелперы для работы с API
- ./testdata - провайдер тестовых данных
    - test_data.json

### Полезные ссылки
- [Подсказка по markdown](https://www.markdownguide.org/cheat-sheet/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)