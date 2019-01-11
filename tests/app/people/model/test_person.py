from app.people.model.person import Person


def test_person_equality():
    person1 = Person(fname="Doug", lname="Farrell", tstamp="20122030")
    person2 = Person(fname="Doug", lname="Farrell")
    person3 = Person(fname="Doug", lname="Farrell", tstamp="20122030")

    assert person1 == person2
    assert person1 == person3


def test_person_inequality():
    person1 = Person(fname="Doug", lname="Farrell", tstamp="20122030")
    person4 = Person(fname="Kent", lname="Farrell")
    person5 = Person(fname="Doug", lname="Brockman")

    assert person1 != person4
    assert person1 != person5
