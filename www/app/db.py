from mongoengine import Document, ObjectIdField, StringField, BinaryField
from mongoengine import BooleanField, EmailField, DateTimeField, IntField

import settings

ENGLISH = "english"
GERMAN = "german"
SPANISH = "spanish"
RUSSIAN = "russian"

class Request(Document):
    meta = {'collection': "requests", 'indexes': ['email', 'moment']}

    # def __init__(self):
    #     moment =

    # id = ObjectIdField(primary_key=True)
    moment = DateTimeField(required=True) # fixme: default=now
    name = StringField(required=True)
    email = EmailField(required=True)
    source_lang = StringField(required=True, regex="{}|{}|{}|{}".format(ENGLISH, GERMAN, SPANISH, RUSSIAN))
    dest_lang = StringField(required=True, regex="{}|{}|{}|{}".format(ENGLISH, GERMAN, SPANISH, RUSSIAN))
    file = BinaryField(required=True, max_bytes=settings.MAX_UPLOAD_FILE_SIZE)
    file_name = StringField(required=True)
    phone_number = StringField(default="")
    comment = StringField(default="")


class Message(Document):
    meta = {'collection': "messages", 'indexes': ['email', 'moment']}

    id = ObjectIdField(primary_key=True)
    moment = DateTimeField(required=True) # fixme: default=now
    name = StringField(required=True)
    email = EmailField(required=True)
    message = StringField(required=True)
