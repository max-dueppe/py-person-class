class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        if people[i].get("wife"):
            person_list[i].wife = Person.people[people[i]["wife"]]
            continue
        if people[i].get("husband"):
            person_list[i].husband = Person.people[people[i]["husband"]]
    return person_list
