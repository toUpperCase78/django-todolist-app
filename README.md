# Django To-Do-List App

**The fully-functional to-do-list application with Python Django**

## Overview

This to-do-list project was created with **Python** language and **Django** framework (v5.1.1), which enables to simulate the well-known **to-do-list** application.

To carry out this project into runnable condition at the most reasonable level, I benefited from [this YouTube video](https://www.youtube.com/watch?v=sm1mokevMWk), teaching Django with various aspects and took more than 3 hours to complete.

Thanks to the video for elaborating the necessary components about Django, this project features these things below:

* SQLite3 Database
* Admin Dashboard
* Templates & Custom HTML
* Simple & Custom Forms
* Sidebar
* Bootstrap CSS
* User Registration
* Login, Logout & User Authentication
* User Specific Pages

Later on, I continued working on this project, such as providing richer UI, enabling item deletion from to-do lists, more robust user registry, and login / logout procedure.

_Hopefully, this will pave the way for creating web applications using Python & Django with other popular libraries alongside, for unique user experience and interactions and being alternative to other web frameworks such as React, TypeScript, etc._

## Screenshots

![Django To-Do-List](Screenshots/django_todolist(4).png)

![Django To-Do-List](Screenshots/django_todolist(6).png)

![Django To-Do-List](Screenshots/django_todolist(7).png)

More screenshots can be found in the _Screenshots_ folder.

## Usage

* Get all the folders `main`, `register`, `todolist_project` and files `db.sqlite3`, `manage.py` into a root folder (e.g. `todolist_project`) and run the command `python manage.py runserver` to start a development server. In your favorite browser, go to `http://localhost:8000` to view the main page.

* First of all, it is recommended to register yourself by clicking on `REGISTER` button (or the text in the sidebar) and enter the necessary information: `Username`, `First name`, `Last name`, `Email`, `Password`, `Password confirmation`. Then, login by using your credentials.

* After successful login, you'll be able to create a new to-do list. To do so, click `Create New To-Do List` button, then specify the name for your new to-do list in the input text and click `Create New List` button. As you're redirected to the available To-Do Lists page, you should see the newly created list, with the name and an ID number on the left.

* Next, click on the button that is related to your new to-do list. To add a new item for this list, enter something in the input text and click on `Add New Item` button. Upon the addition, the new item must be listed on the screen. You can continue adding more items in this way... Notice that every item has its own ID number on the left.

* As you added several items for your to-do list, try clicking on the small boxes on the leftmost side to mark that item as **checked**, and click on `Save Item Status` button to save their check status. Moreover, there are `X` buttons on the right side for each item and clicking on it will delete the specific item from the list.

* Besides, you can view your profile by clicking on `View User Profile` button in the main page (or `Profile` text in the sidebar). There you can find the details about the currently logged in user with useful information, and available permissions.

* Lastly, try clicking on `Admin` text on the sidebar to access the administration panel, but make sure the user has the necessary permissions.

## Pre-Defined Users

There are total of 5 users registered in this project beforehand with different permissions:

* **YigitNewday** (as seen above) is the **superuser**; has all the permissions in the admin page and is able to change all the to-do-lists and items inside, as well as the users.
* **Damon863** is another user with **staff** permission; he's able to access the admin page, but does not have the ability to change everything.
* The rest of the users are **Andrew984**, **Betty725** and **Charlie476**; being the normal active users with no additional permissions.

You can also try logging in with these users to see the permission differences; all these users (except Andrew984) are using the same password: `django123456`
