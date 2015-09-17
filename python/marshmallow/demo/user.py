import datetime as dt

class User(object):

        def __init__(self, name, email):
                self.name = name
                self.email = email
                self.created_at = dt.datetime.now()

        def __repr__(self):
                return 'User: {0} {1}'.format(self.name, self.email)

