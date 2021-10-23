from django.db import models

# Create your models here.


class Event:
    id: int
    image: str
    deadline: str
    title: str
    description: str

    def __init__(self, title, deadline):
        self.title = title
        self.deadline = deadline
