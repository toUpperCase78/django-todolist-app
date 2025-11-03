from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# This models.py is an important file to define the models and their attributes and to store information in the database 
# By default, you are using sqlite3.

class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

# Don't forget to execute these commands to register any changes you've made to the database:
# >>> python manage.py makemigrations <app_name>
# >>> python manage.py migrate

# To add some information without HTML pages, use this command:
# >>> python manage.py shell

# Follow these commands to interact with the shell and the models:
# from main.models import Item, ToDoList
# t = ToDoList(name="My List 1")
# t.save()
# ToDoList.objects.all()
# ToDoList.objects.get(id=1)
# ToDoList.objects.get(name="My List 1")
# t.item_set.all()
# t.item_set.create(text="Go to the mall", complete=False)
# t.item_set.get(id=1)
# quit()

# from main.models import Item, ToDoList
# t = ToDoList.objects
# t.all()
# t.filter(name__startswith="My")
# t.filter(name__startswith="Tim")   // empty queryset
# t.filter(id=2)                     // empty queryset
# del_obj = t.get(id=1)
# del_obj.delete()
# t.all()                            // empty queryset
# t1 = ToDoList(name="First list")
# t1.save()
# t2 = ToDoList(name="Second list")
# t2.save()
# ToDoList.objects.all()
# quit()

# from main.models import Item, ToDoList
# ls = ToDoList.objects.get(id=2)
# ls.item_set.all()                  // empty queryset
# ls.item_set.create(text="Item One", complete=False)
# ls.item_set.create(text="Item Two", complete=False)
# ls.item_set.create(text="Item Three", complete=False)
# ls.item_set.all()
# quit()