from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# demo many to many relationship
# http://docs.sqlalchemy.org/en/rel_0_9/orm/basic_relationships.html#many-to-many

engine = create_engine('sqlite:///manymany.db')
Base = declarative_base()

# Association table linking the two tables
# Also see: http://docs.sqlalchemy.org/en/rel_0_9/orm/basic_relationships.html#association-object
member_club_mapping = Table('member_club_mapping', Base.metadata,
                            Column('member_id', Integer, ForeignKey('member.id')),
                            Column('club_id', Integer, ForeignKey('club.id')))

class Member(Base):
    
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    clubs = relationship('Club', back_populates='members',
                         secondary=member_club_mapping)
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Club(Base):
    __tablename__ = 'club'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    members = relationship('Member', back_populates='clubs',
                           secondary=member_club_mapping)
    def __init__(self, name):
        self.name = name

# create tables
Base.metadata.create_all(engine)
# create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Populate
member1 = Member('John', 'Doe')
club1 = Club('Club dub')
club1.members.append(member1)
session.add(club1)

club2 = Club('Club dub dub')
club2.members.append(member1)
session.add(club2)

club3 = Club('Club dub step')
session.add(club3)

member2 = Member('Jane', 'Allen')
member2.clubs.extend([club1, club2])
session.add(member2)

session.commit()

# query and print Member
res = session.query(Member).all()
for member in res:
    print member.first_name, member.last_name , [club.name for club in member.clubs]

# query and print Club
res = session.query(Club).all()
for club in res:
    print club.name, [(member.first_name, member.last_name) for member in club.members]

print 'After removing members with first name: Jane'
# Remove a record 
record = session.query(Member).filter(Member.first_name == 'Jane').all()
for r in record:
    session.delete(r)

session.commit()

# query and print Member
res = session.query(Member).all()
for member in res:
    print member.first_name, member.last_name , [club.name for club in member.clubs]

# query and print
res = session.query(Club).all()
for club in res:
    print club.name, [(member.first_name, member.last_name) for member in club.members]

print 'After removing the club, Club dub'
# Remove a record 
record = session.query(Club).filter(Club.name == 'Club dub').all()
for r in record:
    session.delete(r)

session.commit()

# query and print Member
res = session.query(Member).all()
for member in res:
    print member.first_name, member.last_name , [club.name for club in member.clubs]

# query and print
res = session.query(Club).all()
for club in res:
    print club.name, [(member.first_name, member.last_name) for member in club.members]
