from polls.models import Person
from polls.dto import PersonDTO


def is_user_ex(user_name):
    try:
        Person.objects.get(user_name=user_name)
    except Person.DoesNotExist:
        return False
    return True


def check_password(user_name, password):
    try:
        Person.objects.get(user_name=user_name)
    except Person.DoesNotExist:
        return False
    person = Person.objects.get(user_name=user_name)
    if person.password == password:
        return True
    return False


def get_detail(user_name):
    person = Person.objects.get(user_name=user_name)

    person_dto = PersonDTO(person.user_name, person.email, person.age)
#    person_dto.user_name = person.user_name
#    person_dto.email = person.email
#   person_dto.age = person.age
    return person_dto


def change_user_name(user_name, name_to_change):
    try:
        Person.objects.get(user_name=user_name)
    except Person.DoesNotExist:
        return False
    person = Person.objects.get(user_name=user_name)
    person.user_name = name_to_change
    person.save()


def set_person(user_name, password, email, age):
    person = Person()
    person.role = 'USER'
    person.user_name = user_name
    person.password = password
    person.email = email
    person.age = age
    return person


def sign_in(person):
    try:
        Person.objects.get(user_name=person.user_name)
    except Person.DoesNotExist:
        person.save()
        return True
    return False


def get_all_person():
    person_list = Person.objects.all()
    list_person = []
    for person in person_list:
        list_person.append(person)
    return list_person


def delete_person(person_id):
    try:
        Person.objects.get(id=person_id)
    except Person.DoesNotExist:
        return False
    person = Person.objects.get(id=person_id)
    person.delete()


def is_admin(user_name):
    person = Person.objects.get(user_name=user_name)
    if person.role == 'ADMIN':
        return True
    return False
