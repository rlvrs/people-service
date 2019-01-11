import jsonpickle
from typing import List, Any, Optional

from app.people.model.person import Person

PersonList = List[Person]


class People(PersonList):
    person_list = None

    def __init__(self) -> None:
        self.person_list = []

    def size(self):
        return len(self.person_list)

    def add_person(self, person: Person) -> None:
        self.person_list.append(person)

    def get_person(self, person: Person) -> Optional[Any]:
        for p in self.person_list:
            if p == person:
                return p
        return None

    def get_person_by_lname(self, lname: str) -> Optional[Any]:
        for p in self.person_list:
            if p.last_name == lname:
                return p
        return None

    def remove_user(self, person: Person) -> None:
        self.person_list.remove(person)

    def to_json(self):
        return jsonpickle.encode(self.person_list, unpicklable=False)
