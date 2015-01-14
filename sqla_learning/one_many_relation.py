from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# demo one to many relationship, reverse side one to many
# http://docs.sqlalchemy.org/en/rel_0_9/orm/basic_relationships.html#many-to-one

engine = create_engine('sqlite:///onemany.db')
Base = declarative_base()

class Member(Base):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    # If a parent record is removed, remove the corresponding
    # child record
    # http://docs.sqlalchemy.org/en/latest/orm/cascades.html
    books = relationship('Book', back_populates='member',
                         cascade = 'all, delete-orphan')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Book(Base):
    __tablename__ = 'book'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    isbn = Column(String)
    member_id = Column(Integer, ForeignKey('member.id'))
    member = relationship('Member', back_populates='books')
    
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

# create tables
Base.metadata.create_all(engine)
# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Populate
member = Member('John', 'Doe')
book = Book('Do not write your first program', 'AB-78-CD')
book.member = member
session.add(book)

member = Member('Jane', 'Allen')
book = Book('You must write your first program', 'AB-78-CE')
member.books.append(book)
session.add(member)

session.commit()

# query and print
res = session.query(Member).all()
for member in res:
    print member.first_name, member.last_name , [book.title for book in member.books]

# query and print
res = session.query(Book).all()
for book in res:
    issued_by = session.query(Member).filter(Member.id == book.member.id).one()
    print book.title, book.isbn, '%s %s' % (issued_by.first_name, issued_by.last_name)

# Remove a record
record = session.query(Member).filter(Member.first_name == 'Jane').all()
for r in record:
    session.delete(r)
session.flush()
# query and print
res = session.query(Member).all()
for member in res:
    print member.first_name, member.last_name , [book.title for book in member.books]
# query and print
res = session.query(Book).all()
for book in res:
    issued_by = session.query(Member).filter(Member.id == book.member.id).one()
    print book.title, book.isbn, '%s %s' % (issued_by.first_name, issued_by.last_name)
