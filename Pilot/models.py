from django.db import models

# Create your models here.
class FileData(models.Model):
    store_name=models.CharField(max_length=50)
    store_number=models.SmallIntegerField()
    jsocver=models.CharField(max_length=10)
    RHEL_version=models.CharField(max_length=10)
    bridge_count=models.SmallIntegerField()
    progressrjbridge_GB=models.CharField(max_length=10)
    retailjstaticdata_UK=models.CharField(max_length=10)
    commonutilities_GB=models.CharField(max_length=10)
    callcentreinstore_GB=models.CharField(max_length=10)
    storeserver_GB=models.CharField(max_length=10)
    storeprogresscode_GB=models.CharField(max_length=10)
    socrates_GB=models.CharField(max_length=10)
    rjsoabridge_GB=models.CharField(max_length=10)
    socratesContainer=models.CharField(max_length=10)
    socratesBroker=models.CharField(max_length=10)
    ccApp=models.CharField(max_length=10)
    sgmb=models.CharField(max_length=10)
    mysqld=models.CharField(max_length=10)
    backoffice=models.CharField(max_length=10)
    httpd =models.CharField(max_length=10)
    progress_to_rj_bridge =models.CharField(max_length=10)
    rj_to_soa_bridge =models.CharField(max_length=10)
    Deployment_type=models.CharField(max_length=10)
    Store_type=models.CharField(max_length=10)


    '''
    >>> import csv
>>>  import os
  File "<console>", line 1
    import os
    ^
IndentationError: unexpected indent
>>> import os
>>> path="C:\\Users\\s.thirugnanam\\Desktop\\djangoproject\\Postdepl_check_project"
>>> os.chdir(path)
>>> from Pilot.models import FileData
>>> with open('checks.csv') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...             p = FileData(store_name=row['store_name'], store_number=row['store_number'], jsocver=row['jsocver'],RHEL_version=row['RHEL_version'],bridge_count=row['bridge_count'],progressrjbridge_GB=row['progressrjbridge_GB'], retailjstaticdata_UK=row['retailjstaticdata_UK'],commonutilities_GB=row['commonutilities_GB'],callcentreinstore_GB=row['callcentreinstore_GB'], storeserver_GB=row['storeserver_GB'],storeprogresscode_GB=row['storeprogresscode_GB'],socrates_GB=row['socrates_GB'], rjsoabridge_GB=row['rjsoabridge_GB'],socratesContainer=row['socratesContainer '],socratesBroker=row['socratesBroker '],ccApp=row['ccApp '],sgmb=row['sgmb '],mysqld=row['mysqld '],backoffice=row['backoffice '],httpd=row['httpd '],progress_to_rj_bridge=row['progress_to_rj_bridge '],rj_to_soa_bridge =row['rj_to_soa_bridge '],Deployment_type=row['Deployment_type'],Store_type=row['Store_type'])
...             p.save()
...
>>> exit()

'''

    
