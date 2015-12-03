"""
Check PyPI for new releases of packages
"""

import xmlrpclib
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#import datetime.datetime
import argparse
import sys

Base = declarative_base()
engine = create_engine('sqlite:///packages.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class Package(Base):

    __tablename__ = 'packages'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    latest_version = Column(String(10))

    pypi = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')

    def find_latest_version(self):
        try:
            version = self.pypi.package_releases(self.name)[0]
        except IndexError:
            return None
        else:
            return version

    def check_for_update(self):
        print('Polling for %s' % self.name)
        latest = self.find_latest_version()
        if self.latest_version != latest:
            self.latest_version = latest
            session.add(self)
            session.commit()
        else:
            False

# Create the table
Base.metadata.create_all(engine)

# List of current packages
packages = session.query(Package)
# Add a package to the DB
def add_package(package):
    package_names = [p.name for p in packages]
    if package not in package_names:
        package = Package(name=package)
        session.add(package)
        session.commit()

# Setup program arguments
parser = argparse.ArgumentParser(description='Monitor Python packages from PyPI')
parser.add_argument('--requirements',
                    dest='requirements',
                    type=str, nargs='+',
                    help='Path to a requirements file',
                    default=None)
parser.add_argument('--list',
                    action='store_true',
                    help='Currently monitored pacakges',
                    default=False)

args = parser.parse_args()
if args.requirements:
    for r in args.requirements:
        with open(r) as f:
            for package in f:
                if not package.startswith('#'):
                    package = package.rstrip('\n')
                    index = len(package)
                    if '==' in package:
                        index = min(index, package.find('=='))
                    if '>=' in package:
                        index = min(index, package.find('>='))
                    if '<=' in package:
                        index = min(index, package.find('<='))
                    if '>' in package:
                        index = min(index, package.find('>'))
                    if '<' in package:
                        index = min(index, package.find('<'))
                    package_name = package[:index].strip()
                    print('Addding %s for monitoring' % package_name)
                    add_package(package_name)
elif args.list:
    for p in packages:
        print(p.name + ' ' + str(p.latest_version))
    sys.exit(0)

for package in session.query(Package):
    current_version = package.latest_version
    updated = package.check_for_update()
    if updated:
        print('Current version: %s, New version: %s' % (current_version, updated))
