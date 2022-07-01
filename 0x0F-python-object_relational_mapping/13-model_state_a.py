#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a from the database hbtn_0e_6_usa
takes 3 arguments: mysql username, mysql password and database name
"""

import sys

from sqlalchemy.orm.session import Session
from sqlalchemy.sql.expression import false
from model_state import Base, State
from sqlalchemy import create_engine


def delete_astate():
    """ defining func """

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = Session(engine)

    for state in session.query(State):
        if 'a' in state.name:
            session.delete(state)
            session.commit()


if __name__ == '__main__':
    delete_astate()
