# this file define all site logic actions like registration new user etc.

from django.contrib.auth.models import User
from ..models import NormalUser
from ..exceptions.FormExceptions import InputError

def createUser(inputPersonalData):
    dataContainer = __parseData(inputPersonalData)

    user = User.objects.create_user(username=dataContainer['username'], email=dataContainer['email'], password=dataContainer['password'])
    user.is_active = True  # TODO change it to false when email confirmation will be done
    user.first_name = dataContainer['name']
    user.last_name = dataContainer['surname']
    user.save

    # TODO data don't want save into table with additonal info... FIX IT
    normalUserData = NormalUser
    normalUserData.birth_date = dataContainer['birthday']
    normalUserData.event_paid = False
    normalUserData.sex = dataContainer['sex']
    normalUserData.telephone = dataContainer['telephone']

    #normalUserData.save()  # TODO perhaps it coudn't work becasue we need to perform user.save() firstly


def __parseData(personDetails):
    dataContainer = {}

    dataContainer['username'] = personDetails.get('username')
    dataContainer['password'] = personDetails.get('password')
    dataContainer['password2'] = personDetails.get('password2')
    dataContainer['name'] = personDetails.get('name')
    dataContainer['surname'] = personDetails.get('surname')
    dataContainer['sex'] = personDetails.get('sex')
    dataContainer['birthday'] = personDetails.get('birthday')
    dataContainer['email'] = personDetails.get('email')
    dataContainer['telephone'] = personDetails.get('telephone')
    dataContainer['team'] = personDetails.get('team')

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

    if( not dataContainer['password'] == dataContainer['password2']):
        raise InputError(msg='passwords are not equal!')

    # TODO write another validations (for example for birthday -> maybe there are some libraries)
    return dataContainer
