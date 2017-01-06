# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from ..models import NormalUser
from ..exceptions.FormExceptions import InputError
from ..exceptions.UserActions import InvalidPassword
import datetime


def createUser(inputPersonalData):
    dataContainer = __parseData(inputPersonalData, "register")

    user = User.objects.create_user(username=dataContainer['username'], email=dataContainer['email'], password=dataContainer['password'])
    user.is_active = True  # TODO change it to false when email confirmation will be done
    user.first_name = dataContainer['name']
    user.last_name = dataContainer['surname']
    user.save()

    normalUserData = NormalUser(user=user, birth_date=dataContainer['birthday'], event_paid=False,
                                telephone=dataContainer['telephone'], team_name=dataContainer['team'])

    normalUserData.sex = dataContainer['sex']
    normalUserData.save()

def readUserData(user_id):
    dataContainer = {}

    user = User.objects.get(id=user_id)
    user_additional_info = NormalUser.objects.get(user=user)

    dataContainer['username'] = user.username
    dataContainer['password'] = None
    dataContainer['password2'] = None
    dataContainer['name'] = user.first_name
    dataContainer['surname'] = user.last_name
    dataContainer['sex'] = user_additional_info.sex
    dataContainer['email'] = user.email
    dataContainer['telephone'] = user_additional_info.telephone
    dataContainer['team'] = user_additional_info.team_name
    dataContainer['birthday'] = user_additional_info.birth_date

    dataContainer['info__event_paid'] = user_additional_info.event_paid
    dataContainer['info__event_photo_user_id'] = user_additional_info.event_photo_user_id

    return dataContainer

def updateUserData(inputPostData):
    dataContainer = __parseData(inputPostData, "update")

    user = User.objects.get(username=dataContainer['username'])

    if dataContainer['password'] is not None:
        old_password = inputPostData.get('old_password')
        if not user.check_password(old_password):
            raise InvalidPassword(msg="Nie można zmienić hasła, ponieważ stare hasło jest niepoprawne!")
        user.set_password(dataContainer['password'])


    user.first_name = dataContainer['name']
    user.last_name = dataContainer['surname']
    user.email = dataContainer['email']

    user_additional_info = NormalUser.objects.get(user=user)
    user_additional_info.sex = dataContainer['sex']
    user_additional_info.birth_date = dataContainer['birthday']
    user_additional_info.telephone = dataContainer['telephone']
    user_additional_info.team_name = dataContainer['team']

    user.save()
    user_additional_info.save()

def __parseData(personDetails, action_type):
    dataContainer = {}

    dataContainer['username'] = personDetails.get('username')
    dataContainer['password'] = personDetails.get('password')
    dataContainer['password2'] = personDetails.get('password2')
    dataContainer['name'] = personDetails.get('name')
    dataContainer['surname'] = personDetails.get('surname')
    dataContainer['sex'] = personDetails.get('sex')
    dataContainer['email'] = personDetails.get('email')
    dataContainer['telephone'] = personDetails.get('telephone')
    dataContainer['team'] = personDetails.get('team')
    # It must be compatible with form
    dataContainer['birthday'] = personDetails.get('birthday')

    if action_type == "register":
        # check required fileds
        if( not dataContainer['username'] or
            not dataContainer['password'] or
            not dataContainer['password2'] or
            not dataContainer['name'] or
            not dataContainer['surname'] or
            not dataContainer['sex'] or
            not dataContainer['birthday']
                ):
            raise InputError(msg='not every required filed is set')

    if action_type == "update":
        # check required fileds
        if (
                not dataContainer['name'] or
                not dataContainer['surname'] or
                not dataContainer['sex'] or
                not dataContainer['birthday']
            ):
            raise InputError(msg='not every required filed is set')

    if( dataContainer['password'] is not None):
        if( not dataContainer['password'] == dataContainer['password2']):
            raise InputError(msg='passwords are not equal!')

    # TODO write another validations (for example for birthday -> maybe there are some libraries)
    return dataContainer
