from model import Person
import view


def showall():
    db_list = Person.get_all()
    return view.showall(db_list=db_list)


def start():
    view.startview()
    user_input = input()
    if user_input == "y":
        return showall()
    return view.endview()


if __name__ == "__main__":
    start()
