# blog-platform

## Короткий опис проекту.
Цей проект був створений на **Python 3.11.2** з використанням фреймворку **Django 5.1.4**, **Bootstrap** та **SQLite**. Це блог-платформа на якій користувачі зареєструватися, створити, редагувати та видаляти свої пости. 
___
## Як запустити проект ?
Для того щоб встановити усі необхідні файли та запустити цей проект, треба виконати декілька простих кроків:
1. Скопіюйте репозиторій
```bash
https://github.com/Fantom245/blog-platform.git
```
2. Перейдіть у папку проекту
```bash
cd blog_platform
```
3. Створіть віртуальне середовище:
```bash
python -m venv venv
venv/Script/activate (для Windows)
source venv/bin/activate (on macOS)
```
4. Встановіть усі залежності
```bash
pip install -r requirements.txt
```
5. Виконайте міграції бази данних
```bash
python manage.py migrate
```
6. Запустіть локальний сервер
```bash
python manage.py runserver
```
___
## Автор проекту
Цей проект був зроблений мною, Гиркало Максимом, для демонстрації моїх навичок роботи з **Django** та базами даних. Проект розроблений самостійно, використовуючи офіційну документацію та навчальні ресурси. Це був мій перший Django проект тому тут реалізовано все, що я знаю на данний момент.
