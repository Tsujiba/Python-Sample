import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

"""
#############################################################################
SQLAlchemyはMySQLやSQLiteはラッパーする（O/Rマッパー）
　・DBMSの変更した時にも影響がでにくい
　・オブジェクト志向でSQL分を書かずに、データベースを操作できる　
#############################################################################

"""
# echo=TrueでSQL分がコンソールに表示される
# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
# engine = sqlalchemy.create_engine('sqlite:///sqlite_test2.db', echo=True)
engine = sqlalchemy.create_engine('mysql+pymysql://root:tsujiba@localhost/test_mysql_database', echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Tsujiba')
session.add(p1)
p2 = Person(name='Kagawa')
session.add(p2)
p3 = Person(name='Nakano')
session.add(p3)
session.commit()

p4 = session.query(Person).filter_by(name='Tsujiba').first()
p4.name = 'Tsujiba2'
session.add(p4)
session.commit()

p5 = session.query(Person).filter_by(name='Kagawa').first()
session.delete(p5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
    







