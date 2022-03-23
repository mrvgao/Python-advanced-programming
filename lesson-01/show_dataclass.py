from dataclasses import dataclass


@dataclass
class Person:
    name: str = ""
    age: int = 18
    location: float = 10.0
    weight: float = 20.0


class OldPerson:
    def __init__(self, name="Tom", age=10, location=10.0, weight=20.0):
        self.name = name
        self.age = age
        self.location = location
        self.weight = weight

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, location={self.location}, weight={self.weight})"


person = OldPerson()
print(person)
person.name = "Jack"