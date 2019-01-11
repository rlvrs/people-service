"""
This is the people module and supports all the REST actions for the
PEOPLE collection
"""
import app.utils.utils as utils

from app.people.model.people import People
from app.people.model.person import Person

# Data to serve with our API
PEOPLE = People()
PEOPLE.add_person(Person(fname="Doug", lname="Farrell", tstamp=utils.get_timestamp()))
PEOPLE.add_person(Person(fname="Kent", lname="Brockman"))
PEOPLE.add_person(Person(fname="Bunny", lname="Easter"))


def read_all() -> People:
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        sorted list of people
    """
    # create the list of people from our data
    return PEOPLE
    #return [PEOPLE[key].to_json() for key in sorted(PEOPLE.keys())]


def get_person_by_last_name(lname: str) -> Person:
    """
    This function responds to a request for /api/people/{lname}
    with the user with the corresponding last name.
    :return:        The user with the corresponding lastname.
    """
    return PEOPLE.get_person_by_lname(lname)
