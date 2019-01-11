from app.people.model.people import People
from app.people.model.person import Person

person1 = Person(fname="Doug", lname="Farrell", tstamp="20122030")
person2 = Person(fname="Doug", lname="Farrell")
person3 = Person(fname="Doug", lname="Farrell", tstamp="20122030")
person4 = Person(fname="Kent", lname="Farrell")
person5 = Person(fname="Doug", lname="Brockman")


def test_people_size():
    people = People()

    prev_size = people.size()
    people.add_person(person1)
    curr_size = people.size()

    assert prev_size + 1 == curr_size


def test_people_get():
    people = People()

    prev_found_person1 = people.get_person(person1)
    people.add_person(person1)
    curr_found_person1 = people.get_person(person1)

    assert prev_found_person1 != person1
    assert curr_found_person1 == person1


def test_people_remove():
    people = People()

    people.add_person(person1)
    prev_found_person1 = people.get_person(person1)
    people.remove_user(person1)
    curr_found_person1 = people.get_person(person1)

    assert prev_found_person1 == person1
    assert curr_found_person1 != person1
