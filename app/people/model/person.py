import jsonpickle
import app.utils.utils as utils


class Person:
    first_name = None
    last_name = None
    timestamp = None

    def __init__(self, fname: str, lname: str, tstamp: str= utils.get_timestamp()) -> None:
        self.first_name = fname
        self.last_name = lname
        self.timestamp = tstamp

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Person):
            return self.first_name == other.first_name and self.last_name == other.last_name

        return False

    def to_json(self):
        return jsonpickle.encode(self, unpicklable=False)
