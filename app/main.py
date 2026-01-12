class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)
    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"]:
            person_list[i].wife = Person.people[people[i]["wife"]]
            continue
        if "husband" in people[i] and people[i]["husband"]:
            person_list[i].husband = Person.people[people[i]["husband"]]

    return person_list
