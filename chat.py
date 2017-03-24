from datetime import date
people = [{ "name": 'Tim', "year": 1988 },
{ "name": 'Mike', "year": 1986 },
{ "name": 'Bob', "year": 1970 },
{ "name": 'Tony', "year": 1982 }]

def olderThan(person, age):
    current_year = date.today().year
    return current_year - person["year"] > age

old_people = [person for person in people if olderThan(person, 33) ]
print(old_people)
