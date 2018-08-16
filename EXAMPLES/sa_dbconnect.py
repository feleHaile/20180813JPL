#!/usr/bin/env python

from sqlalchemy import create_engine

engine = create_engine(
    'sqlite:///../DATA/presidents.db',
    echo=False
)

# windows: sqlite:///c:\\somewhere\mydatabase.db

conn = engine.connect()

term = 16

s = conn.execute('select * from presidents where termnum = ?', term)

row = s.fetchone()

print(row.lastname)
