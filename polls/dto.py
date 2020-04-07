from django.db import models


# remove modes.model
class PersonDTO(models.Model):
    def __init__(self, user_name, email, age, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = email
        self.user_name = user_name
        self.age = age

    def set_name(self, name):
        pass

    def set_email(self, email):
        pass

    def set_age(self, age):
        pass

    def as_json(self):
        return dict(
            input_user=self.user_name,
            email=self.email, age=self.age,
        )
