# Full path and name to your csv file
csv_filepathname="/home/drapek/HDD/projects/indywidual/example_data/example_usernames.csv"
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

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

for row in dataReader:
    if row[0] != 'first_name':  # Ignore the header row, import everything else
        user = User.objects.create_user(first_name=row[0], last_name=row[1], email=row[2], password=row[4], username=row[5])
