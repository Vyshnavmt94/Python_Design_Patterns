class DSA():
    """Class for Data Structures and Algorithms"""

    def fee(self):
        return 8000

    def available_batches(self):
        return 5

    def __str__(self):
        return "DSA"


# concrete course
class SDE():
    """Class for Software development Engineer"""

    def fee(self):
        return 10000

    def available_batches(self):
        return 4

    def __str__(self):
        return "SDE"


# concrete course
class STL():
    """class for Standard Template Library of C++"""

    def fee(self):
        return 5000

    def available_batches(self):
        return 7

    def __str__(self):
        return "STL"


# main method
if __name__ == "__main__":
    sde = SDE()  # object for SDE
    dsa = DSA()  # object for DSA
    stl = STL()  # object for STL

    print(f'Name of Course: {sde} and its Fee: {sde.fee()}')
    print(f'Name of Course: {stl} and its Fee: {stl.fee()}')
    print(f'Name of Course: {dsa} and its Fee: {dsa.fee()}')
