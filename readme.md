# Django scrapper






## To run this project
Locally:
$python manage.py runserver

default port is set on 8000
to change
$python manage.py runserver 8080




## Python Shell commands
>>>p = Properties.objects
>>> p.all()

>>>p.filter(name_startswith="somth")
>>>p.filter(id=1)
>>> p.filter(id=323) => will return and empty QuerySet []

To delete
>>> del_object = p.get(id=1)
>>> del_object.delete()


Create a Property List
>>> p1 = Properties(name="First property list")
>>> p1.save()

Create an item
pt = Properties.objects.get(id=2)
pt.item_set.create(text="First Property", complete=False)
# Create a login

python manage.py createsuperuser