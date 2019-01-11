"""
This is the people module and supports all the ReST actions for the
PEOPLE collection
"""

from app.people.db import people_db


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    # create the list of people from our data.
    return people_db.read_all().to_json()


def get_person_by_last_name(lname):
    """
    This function responds to a request for /api/people/{lname}
    with the person with the given last name.

    :param lname:   the last name of the required person.
    :return:        person with the given last name.
    """
    return people_db.get_person_by_last_name(lname).to_json()
