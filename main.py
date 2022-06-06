import sqlalchemy
from pprint import pprint
engine = sqlalchemy.create_engine('postgresql://postgres:gabs@localhost:5432/home3')
connection = engine.connect()




# Испонители
connection.execute("INSERT INTO musicians VALUES ( 1,'Сектор Газа','Юрий Хой');")
connection.execute("INSERT INTO musicians VALUES ( 2,'Михаил Круг','Миха');")
connection.execute("INSERT INTO musicians VALUES ( 3,'Руки Вверх','Сергей Жуков');")
connection.execute("INSERT INTO musicians VALUES ( 4,'Золотое кольцо','Надежда Кадышева');")
connection.execute("INSERT INTO musicians VALUES ( 5,'Snoop Dogg','Snoop');")
connection.execute("INSERT INTO musicians VALUES ( 6,'Тимати','Тиму́р Ильда́рович Юну́сов ');")
connection.execute("INSERT INTO musicians VALUES ( 7,'Егор Крид','Его́р Никола́евич Була́ткин ');")
connection.execute("INSERT INTO musicians VALUES ( 8,'AC/DC','братья Малькольмы и Ангус Янгам');")

# Жанры
connection.execute("INSERT INTO genre VALUES ( 1,'Шансон');")
connection.execute("INSERT INTO genre VALUES ( 2,'Рок');")
connection.execute("INSERT INTO genre VALUES ( 3,'Народные песни');")
connection.execute("INSERT INTO genre VALUES ( 4,'ПОП-музыка');")
connection.execute("INSERT INTO genre VALUES ( 5,'Рэп');")

# Жанры музыкантов
connection.execute("INSERT INTO genre_musicains VALUES ( 1,1,2);")
connection.execute("INSERT INTO genre_musicains VALUES ( 2,2,1);")
connection.execute("INSERT INTO genre_musicains VALUES ( 6,2,8);")
connection.execute("INSERT INTO genre_musicains VALUES ( 3,3,4);")
connection.execute("INSERT INTO genre_musicains VALUES ( 4,4,3);")
connection.execute("INSERT INTO genre_musicains VALUES ( 7,4,7);")
connection.execute("INSERT INTO genre_musicains VALUES ( 5,5,6);")
connection.execute("INSERT INTO genre_musicains VALUES ( 8,5,5);")

# Альбомы
connection.execute("INSERT INTO albums VALUES ( 1,'Колхозный панк',1991);")
connection.execute("INSERT INTO albums VALUES ( 2,'Жиган-лимон',1994);")
connection.execute("INSERT INTO albums VALUES ( 3,'Маленькие девочки',2001);")
connection.execute("INSERT INTO albums VALUES ( 4,'Течёт ручей',1995);")
connection.execute("INSERT INTO albums VALUES ( 5,'No Limit Top Dogg',1999);")
connection.execute("INSERT INTO albums VALUES ( 6,'Black Star',2020);")
connection.execute("INSERT INTO albums VALUES ( 7,'Холостяк',2019);")
connection.execute("INSERT INTO albums VALUES ( 8,'Back in Black',1980);")

# Треки
connection.execute("""INSERT INTO track VALUES ( 1,'Колхозный панк', '2.38', 1);""")
connection.execute("""INSERT INTO track VALUES ( 2,'Местные','3.50',1);""")
connection.execute("""INSERT INTO track VALUES ( 3,'А сечку жрите сами','2.59',2);""")
connection.execute("""INSERT INTO track VALUES ( 4,'Девочка — пай','2.49',2);""")
connection.execute("""INSERT INTO track VALUES ( 5,'18 Мне Уже','4.07',3);""")
connection.execute("""INSERT INTO track VALUES ( 6,'мой сынок','3.50',3);""")
connection.execute("""INSERT INTO track VALUES ( 7,'Течёт ручей','3.01',4);""")
connection.execute("""INSERT INTO track VALUES ( 8,'Buck Em','2.44',5);""")
connection.execute("""INSERT INTO track VALUES ( 9,'Bitch Please','3.54',5);""")
connection.execute("""INSERT INTO track VALUES ( 10,'В Клубе','4.25',6);""")
connection.execute("""INSERT INTO track VALUES ( 11,'Я и Ты','4.44',6);""")
connection.execute("""INSERT INTO track VALUES ( 12,'Самая самая','3.50',7);""")
connection.execute("""INSERT INTO track VALUES ( 13,'Ревность','3.18',7);""")
connection.execute("""INSERT INTO track VALUES ( 14,'Hells Bells','5.12',8);""")
connection.execute("""INSERT INTO track VALUES ( 15,'Back in Black','4.15',8);""")
connection.execute("""INSERT INTO track VALUES ( 16,'Back','4.1',8);""")

# Сборники
connection.execute("INSERT INTO digets VALUES ( 1,'Лучшие песни Сектор-Газа',2005);")
connection.execute("INSERT INTO digets VALUES ( 2,'Лучшие песни М.Круга',2010);")
connection.execute("INSERT INTO digets VALUES ( 3,'Лучшие песни Руки Вверх',2018);")
connection.execute("INSERT INTO digets VALUES ( 4,'Песни Надежды Кадышевой',1995);")
connection.execute("INSERT INTO digets VALUES ( 5,'Лучшие песни Snoop DOgg',2020);")
connection.execute("INSERT INTO digets VALUES ( 6,'Тимати-Лучшии из',2013);")
connection.execute("INSERT INTO digets VALUES ( 7,'Лучшие песни Крида',2021);")
connection.execute("INSERT INTO digets VALUES ( 8,'AC/DC лучшие на все времена',2001);")

# Состав сборника
connection.execute("INSERT INTO composition_digets VALUES ( 1,1,1);")
connection.execute("INSERT INTO composition_digets VALUES ( 2,1,2);")
connection.execute("INSERT INTO composition_digets VALUES ( 3,2,3);")
connection.execute("INSERT INTO composition_digets VALUES ( 4,2,4);")
connection.execute("INSERT INTO composition_digets VALUES ( 5,3,5);")
connection.execute("INSERT INTO composition_digets VALUES ( 6,3,6);")
connection.execute("INSERT INTO composition_digets VALUES ( 7,4,7);")
connection.execute("INSERT INTO composition_digets VALUES ( 8,5,8);")
connection.execute("INSERT INTO composition_digets VALUES ( 9,5,9);")
connection.execute("INSERT INTO composition_digets VALUES ( 10,6,10);")
connection.execute("INSERT INTO composition_digets VALUES ( 11,6,11);")
connection.execute("INSERT INTO composition_digets VALUES ( 12,7,12);")
connection.execute("INSERT INTO composition_digets VALUES ( 13,7,13);")
connection.execute("INSERT INTO composition_digets VALUES ( 14,8,14);")
connection.execute("INSERT INTO composition_digets VALUES ( 15,8,15);")

# АЛьбомы исполнителей
connection.execute("INSERT INTO musicians_albums VALUES ( 1,1,1);")
connection.execute("INSERT INTO musicians_albums VALUES ( 2,2,2);")
connection.execute("INSERT INTO musicians_albums VALUES ( 3,3,3);")
connection.execute("INSERT INTO musicians_albums VALUES ( 4,4,4);")
connection.execute("INSERT INTO musicians_albums VALUES ( 5,5,5);")
connection.execute("INSERT INTO musicians_albums VALUES ( 6,6,6);")
connection.execute("INSERT INTO musicians_albums VALUES ( 7,7,7);")
connection.execute("INSERT INTO musicians_albums VALUES ( 8,8,8);")
connection.execute("INSERT INTO musicians_albums VALUES ( 9,8,8);")
