import datetime


# creating a Class
class User:
    """This class define the user object
    used in this example"""

    # init method (function inside a class)
    # sometimes called constructor
    # this method is called each time an instance of the object is created
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday  # yyyy-mm-dd

        # Method to split first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years"""
        today = datetime.date.today()
        print(today)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[5:7])
        dd = int(self.birthday[8:10])
        date_of_birth = datetime.date(yyyy, mm, dd)
        age_days = (today - date_of_birth).days
        age_years = age_days / 365
        return int(age_years)


user = User("David Bowie", "1947-01-08")

print(user.name)
print(user.first_name)
print(user.last_name)
print(user.birthday)
print(user.age())

print(user.__dict__)  # shows all the fields in a class
