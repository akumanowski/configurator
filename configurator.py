# Configurator - консольное приложение, предназначенное для получения и
# изменения определенной настройки. Для хранения параметров используется
# СУБД MariaDB.
from peewee import *
import os
from dotenv import load_dotenv
from playhouse.mysql_ext import MariaDBConnectorDatabase
import uuid
import click

load_dotenv()

DATABASE_NAME = os.getenv('DATABASE_NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))

db = MariaDBConnectorDatabase(DATABASE_NAME, user=USER, password=PASSWORD,
                              host=HOST, port=PORT)


class Parameter(Model):
    id = UUIDField(null=False, primary_key=True, default='')
    name = CharField(max_length=15, null=False, default='')
    val = CharField(max_length=200, null=False, default='1')
    typ = CharField(max_length=10, null=False, default='int')
    desc = TextField()

    class Meta:
        database = db
        order_by = ('id',)


def create_table():
    user_choice = input("Вы уверены, что хотите очистить все данные "
                        "в таблице хранения настроек?(y/N)")
    if user_choice == 'y':
        Parameter.create_table()


@click.command()
@click.argument('name')
@click.option('--mod', '-m', default='R',
              help='Режим выполнения команды: R - чтение, W - запись.')
@click.option('--typ', '-t', default='string',
              help='Задать тип данных параметра настройки.')
@click.option('--val', '-v', default='',
              help='Задать значение параметра настройки.')
@click.option('--desc', '-d', default='',
              help='Задать описание настройки.')
@click.help_option('--help', help='Показать это сообщение и выйти.')
def parameter(name, typ, val, desc, mod):
    """
        Программа управления базой данных настроек приложения X.

        NAME - имя настройки. Программа позволяет читать значение и параметры
        настроек, а также записывать новые и изменять старые.
        Каждая настройка имеет следующие характеристики:

        - тип данных (string, int, float, bool)

        - значение (должно соответствовать типу данных)

        - краткое описание настройки
        """
    if mod in ['W', 'w', 'write']:
        param = None
        if Parameter.select().where(Parameter.name == name).count() > 0:
            param = Parameter.get(Parameter.name == name)
        if param is not None:
            click.echo(f'Настройка {param.name}'
                       f'[{param.typ}]={param.val} - "{param.desc}"'
                       f' уже хранится в базе данных. Обновляем...')
            param.typ = typ
            param.val = val
            param.desc = desc
            param.save()
        else:
            click.echo(f'Добавляем настройку {name}'
                       f'[{typ}]={val} - "{desc}" в базу данных...')
            param = Parameter.create(id=uuid.uuid4(), name=name,
                                     typ=typ, val=val, desc=desc)
        click.echo(f'Настройка {param.name}'
                   f'[{param.typ}]={param.val} - "{param.desc}"'
                   f' сохранена в базе данных.')
    elif mod in ['R', 'r', 'read']:
        click.echo(f'Читаем значение настройки: {name}')
        param = None
        if Parameter.select().where(Parameter.name == name).count() > 0:
            param = Parameter.get(Parameter.name == name)
        if param is None:
            click.echo(f'Ошибка! В базе данных настроек отсутствует {name}')
        else:
            click.echo(f'Настройка {param.name}'
                       f'[{param.typ}]={param.val} - "{param.desc}"'
                       f' найдена в базе данных.')
    else:
        click.echo(f'Ошибка! Неопознанный режим работы программы: {mod}')


if __name__ == '__main__':
    parameter()
