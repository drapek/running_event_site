# Full path and name to your csv file
csv_filepathname="/home/drapek/HDD/projects/indywidual/example_data/example_usernames_additonal_info.csv"
# # Full path to your django project directory
your_djangoproject_home="/home/drapek/HDD/projects/indywidual/RunningTemplate/MainSite"
#

import sys,os
import django


sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()

from django.contrib.auth.models import User
import csv
from UserAccount.models import NormalUser

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'user_id':  # Ignore the header row, import everything else
        user = User.objects.get(id=row[0])

        additional_user_info = NormalUser(user=user)
        additional_user_info.sex = row[1]
        additional_user_info.birth_date = row[2]
        additional_user_info.telephone = row[3]
        additional_user_info.team_name = row[4]
        additional_user_info.save()