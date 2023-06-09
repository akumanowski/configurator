## Configurator 0.01
### Описание
Проект Configurator — это консольное приложение для хранения параметров настройки в базе данных. 
У пользователя есть возможность просматривать и изменять параметры. 
### Структура таблицы Parameter
```
CREATE TABLE Parameter
(
    id     varchar(40)                not null,
    name   varchar(15)                not null,
    val    varchar(200) default '1'   not null,
    typ    varchar(10)  default 'int' not null,
    `desc` text                       null
);
```
### Используемые технологии
```
Python 3.11 - среда выполнения
mariadb 1.1.6 - интерфейс к базе данных MariaDB
peewee 3.16.0 - ORM для доступа к базе данных
python-dotenv 1.00.0 - загрузка переменных окружения из файла .env
uuid 1.30 - универсальные уникальные идентификаторы (RFC 4122)
click 8.1.3 - интерфейс командной строки

```
Это учебный проект, в котором отрабатываются навыки разработки консольного приложения с доступом к базе данных MariaDB.
### Примеры запуска скрипта
#### 1. Добавить новый параметр настройки POWER_LEVEL для хранения минимального уровня заряда батареи

```
# Командная строка:

python configurator.py POWER_LEVEL --mod W --typ int --val 37 --desc "Минимальный уровень заряда батареи"

# Результат работы скрипта:

Добавляем настройку POWER_LEVEL[int]=37 - "Минимальный уровень заряда батареи" в базу данных...
Настройка POWER_LEVEL[int]=37 - "Минимальный уровень заряда батареи" сохранена в базе данных.
```
#### 2. Корректируем параметры настройки POWER_LEVEL для хранения минимального уровня заряда батареи
```
# Командная строка:

python configurator.py POWER_LEVEL --mod W --typ int --val 45 --desc "Минимальный уровень заряда батареи (скорректирован)"

# Результат работы скрипта:

Настройка POWER_LEVEL[int]=37 - "Минимальный уровень заряда батареи" уже хранится в базе данных. Обновляем...
Настройка POWER_LEVEL[int]=45 - "Минимальный уровень заряда батареи (скорректирован)" сохранена в базе данных.
```
#### 3. Читаем параметры настройки POWER_LEVEL
```
# Командная строка:

python configurator.py POWER_LEVEL

# Результат работы скрипта:

Читаем значение настройки: POWER_LEVEL
Настройка POWER_LEVEL[int]=45 - "Минимальный уровень заряда батареи (скорректирован)" найдена в базе данных.
```
#### 4. Читаем параметры настройки POWER_MAX
```
# Командная строка:

python configurator.py POWER_MAX

# Результат работы скрипта:

Читаем значение настройки: POWER_MAX
Ошибка! В базе данных настроек отсутствует POWER_MAX
```
#### 5. Пытаемся прочитать параметры настройки POWER_MAX
```
# Командная строка:

python configurator.py POWER_MAX --mod Rread

# Результат работы скрипта:

Ошибка! Неопознанный режим работы программы: Rread
```
#### 6. Получаем информацию о параметрах запуска скрипта
```
# Командная строка:

python configurator.py --help

# Результат работы скрипта:

Usage: configurator.py [OPTIONS] NAME
  Программа управления базой данных настроек приложения X.
  - значение (должно соответствовать типу данных)
  - краткое описание настройки
Options:
  -m, --mod TEXT   Режим выполнения команды: R - чтение, W - запись.
  -t, --typ TEXT   Задать тип данных параметра настройки.
  -v, --val TEXT   Задать значение параметра настройки.
  -d, --desc TEXT  Задать описание настройки.
  --help           Показать это сообщение и выйти.
```
### Как запустить проект на локальной машине:

Клонировать репозиторий на локальный компьютер и перейти в папку api_final_yatube:

```
git clone https://github.com/akumanowski/configurator.git
```

```
cd configurator
```

Создать виртуальное окружение:

```
python3 -m venv env
```

Активировать виртуальное окружение:
- для Windows
```
env/bin/activate
```
- для Linux
```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Создать файл хранения переменных окружения .env и заполнить его данными:

```
# .env
DATABASE_NAME=db_name
USER=user_name
PASSWORD=password
HOST=localhost
PORT=3306
```

Запустить проект:

```
python3 configurator.py --help
```