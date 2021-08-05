"""
Написать программу с использованием библиотеки SQLAlchemy, которая:

1. Создаёт на сервере базу данных для какой-нибудь игры;
2. Создаёт в этой базе таблицу игроков, где для каждого игрока определён:
    2.1. Ник
    2.2. Уровень
    2.3. Сила
    2.4. Ловкость
    2.5. Интеллект
    2.6. И/или любые другие игровые параметры;
3. Наполняет таблицу данными (от 10 строк);
4. Делает выборку/группировку по условию, основанному на игровых параметрах.

В личный кабинет загрузить .py файл с исходным ходом программы.
"""

from sqlalchemy import create_engine, Column, Integer, String, or_, and_, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

import os


'''1. Создаёт на сервере базу данных для какой-нибудь игры;'''

# Using environment variable to hide connection info
psql_connect = os.environ.get('POSTGRESQL_CONNECT')
engine = create_engine(psql_connect, echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

'''2. Создаёт в этой базе таблицу игроков'''
class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    level = Column(Integer)
    strength = Column(Integer)
    agility = Column(Integer)
    intelligence = Column(Integer)

# Base.metadata.create_all(engine)


'''3. Наполняет таблицу данными (от 10 строк);'''
# adding one to test
# player1 = Player(name='Garry', level=3, strength=22, agility=34, intelligence=8)
# session.add(player1)

# adding the other 9
# session.add_all( [
#     Player(name='Gamer', level=5, strength=15, agility=20, intelligence=5),
#     Player(name='Fiorenze', level=90, strength=90, agility=73, intelligence=10),
#     Player(name='Elwira', level=79, strength=78, agility=21, intelligence=100),
#     Player(name='Kelsy', level=55, strength=33, agility=73, intelligence=92),
#     Player(name='Cheater', level=99, strength=99, agility=99, intelligence=99),
#     Player(name='Hartwell', level=61, strength=6, agility=89, intelligence=43),
#     Player(name='Noob', level=1, strength=1, agility=1, intelligence=1),
#     Player(name='Clarice', level=33, strength=22, agility=25, intelligence=8),
#     Player(name='Dniren', level=96, strength=77, agility=27, intelligence=42),
# ])

# session.commit()

# printing out our players
# players = session.query(Player)
# for player in players:
#     print(f'{player.name}: lvl. {player.level}')

'''4. Делает выборку/группировку по условию, основанному на игровых параметрах.'''

# level > 50
# players = session.query(Player).filter(Player.level>50)
# for player in players:
#     print(player.name, player.level)

# Name contains 'a' and strength between 10 and 80
# players = session.query(Player).filter(and_(Player.name.like('%a%'), (Player.strength.between(10, 80))))
# for player in players:
#     print(f'Name: {player.name} | Strength: {player.strength}')

# session.add(Player(name='Test', level=0, strength=0, agility=0, intelligence=0))
# session.commit()


# Bannning the cheater
# session.query(Player).filter(Player.name=='Cheater').update({
#     Player.name: 'Banned',
#     Player.level: 0,
#     Player.strength: 0,
#     Player.agility: 0,
#     Player.intelligence: 0,
# })
# session.commit()

# delete a player
# session.query(Player).filter(Player.name=='Test').delete(synchronize_session=False)
# session.commit()