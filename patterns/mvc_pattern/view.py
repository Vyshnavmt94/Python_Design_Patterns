from model import Person


def startview():
    print("MVC Example")
    print("List all in db? [y/n]")


def endview():
    print("GoodBye!")


def showall(db_list):
    print(f"The DB has total {len(db_list)} users")
    for item in db_list:
        print(item.name())
