#!/usr/bin/env python
'''
Populate some Director/Movie records
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sa_movie_models import Director, Movie

ALTMAN_MOVIES = [
    ('Nashville', 1975),
    ("Cookie's Fortune", 1999),
    ('Gosford Park', 2001),
    ('M*A*S*H', 1970),
]

HITCHCOCK_MOVIES = [
    ('Rear Window', 1954),
    ('Psycho', 1960),
    ('The Lady Vanishes', 1938)
]

def main():
    session = setup()
    add_director(session, 'Robert', 'Altman', ALTMAN_MOVIES)
    add_director(session, 'Alfred', 'Hitchcock', HITCHCOCK_MOVIES)
    session.commit()

    session.close()

def setup():
    engine = create_engine(
        'sqlite:///../DATA/movies.db',
        echo=False
    )
    SESSION = sessionmaker(bind=engine)
    return SESSION()

def add_director(session, first_name, last_name, movies):

    d = Director(first_name, last_name)
    
    for movie_name, year in movies:
        m = Movie(movie_name, year)
        d.movies.append(m)
    
    session.add(d)

if __name__ == '__main__':
    main()
