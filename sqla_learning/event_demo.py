from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.event import listen
from sqlalchemy import event
import threading

engine = create_engine('sqlite:///posts.db')
Base = declarative_base()

class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    hits = Column(Integer)

    def __init__(self, title, hits = 0):
        self.title = title
        self.hits = hits

@event.listens_for(Stats.hits, 'set')
def got_hit(instance, value, oldvalue, initiator):
    print('{0} Hits: {1}'.format(instance.title, value))

# create tables
Base.metadata.create_all(engine)
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
post = Stats('A new post', 0)
session.add(post)
session.commit()
res = session.query(Stats).filter(Stats.title=='A new post').first()
# called by each thread
def update_hit():
    res.hits += 1

for i in range(10):
    t = threading.Thread(target=update_hit)
    t.daemon = True
    t.start()

session.commit()
