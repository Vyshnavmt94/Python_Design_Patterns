import json


class Person(object):
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        database = open("db.txt", "r")
        result = []
        json_list = json.loads(database.read())
        for item in json_list:
            # item = json.loads(item)
            person = Person(item["first_name"], item["last_name"])
            result.append(person)
        return result
