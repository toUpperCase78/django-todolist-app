from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewForm

# Create your views here.
# This views.py file is important to store the different views and return responses for our application.

def home(response):
    return render(response, "main/home.html", {"id": "999", "name": "Django To-Do List"})
    # return HttpResponse("<h1>Hello, this is Django Tutorial, To-Do List Project'.</h1>")

def view_add_list_items(response, id):
    # print(response)    # <WSGIRequest: GET '/view-list-items/2'>
    ls = ToDoList.objects.get(id=id)
    click_cnt = 0
    if ls in response.user.todolist.all():
        if response.method == "POST":
            print("POST Content:", response.POST)
            if response.POST.get("saveItem"):
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
            elif response.POST.get("newItem"):
                text = response.POST.get("newItemName")
                if len(text) > 1:
                    ls.item_set.create(text=text, complete=False)
                else:
                    print("Invalid input")
            elif response.POST.get("deleteItem"):
                itemId = int(response.POST.get("deleteItem"))
                item = ls.item_set.get(id=itemId)
                # print(item)
                item.delete()
            for item in ls.item_set.all():
                if item.complete:
                    click_cnt += 1
        elif response.method == "GET":
            for item in ls.item_set.all():
                if item.complete:
                    click_cnt += 1
        # print(ls, '->', ls.item_set.all())
        return render(response, "main/listitem.html", {"ls": ls, "item_cnt": ls.item_set.count(), "click_cnt": click_cnt})
    else:
        return render(response, "main/viewlist.html", {})

    # return render(response, "main/base.html", {"id": id, "name": ls.name})
    # item = ls.item_set.get(id=1)
    # return HttpResponse("<h2>This is Django Tutorial, taught by 'Tech With Tim'.</h2>" +
    #                     "<h3>List: %s | First Item: %s</h3>" % (ls.name, item.text))

# def index(response, name):
#     ls = ToDoList.objects.get(name=name)
#     item = ls.item_set.get(id=1)
#     return HttpResponse("<h3>List: %s | %s</h3>" % (ls.name, item.text))

def create_list(response):
    if response.method == "POST":
        print(response.POST)
        form = CreateNewForm(response.POST)
        # print(form)
        print("Form Valid?:", form.is_valid())
        if form.is_valid():
            # user_id = response.user.id
            list_name = form.cleaned_data["name"]
            new_list = ToDoList(name=list_name)
            new_list.save()
            response.user.todolist.add(new_list)
            # HttpResponseRedirect("/view-list-items/%i" % new_list.id)
            return render(response, "main/viewlist.html", {"list_cnt": response.user.todolist.count()})
    else:
        form = CreateNewForm()
    return render(response, "main/createlist.html", {"form": form})

def about(response):
    return render(response, "main/about.html", {})

def view_list(response):
    return render(response, "main/viewlist.html", {"list_cnt": response.user.todolist.count()})

def simple_view(response):
    return HttpResponse("<h1>This is a simple view with this header.</h1>")

def user_profile(response):
    # print(dir(response.user))
    # print(response.user.EMAIL_FIELD)    # email
    # print(response.user.REQUIRED_FIELDS)    # ['email']
    # print(response.user.USERNAME_FIELD)    # username
    # print(response.user.date_joined)
    # print(response.user.last_login)
    # print(response.user.username)
    # print(response.user.password)    # pbkdf2_sha256$<salt>$<hash>
    # print(response.user.first_name)
    # print(response.user.last_name)
    # print(response.user.email)
    # print(response.user.id)
    # print(response.user.pk)
    # print(response.user.todolist)    # main.ToDoList.None
    # print(response.user.natural_key())
    # print(response.user.groups)    # auth.Group.None
    # print(response.user.logentry_set)    # admin.LogEntry.None
    # print(response.user.validate_constraints())    # None
    # print(response.user.validate_unique())    # None
    # print(response.user.is_active)    # True
    # print(response.user.is_anonymous)    # False
    # print(response.user.is_authenticated)    # True
    # print(response.user.is_staff)    # True
    # print(response.user.is_superuser)    # True
    # print(response.user.has_perm("main.add_todolist"))
    # print(response.user.has_usable_password())    # True
    # print(response.user.get_all_permissions(), len(response.user.get_all_permissions()))
    # print(response.user.get_constraints())
    # print(response.user.get_deferred_fields())
    # print(response.user.get_email_field_name())    # email
    # print(response.user.get_full_name())
    # print(response.user.get_group_permissions(), len(response.user.get_group_permissions()))
    # print(response.user.get_next_by_date_joined())
    # print(response.user.get_previous_by_date_joined())
    # print(response.user.get_session_auth_hash())
    # print(response.user.get_short_name())
    # print(response.user.get_user_permissions(), len(response.user.get_user_permissions()))
    # print(response.user.get_username())
    # print(response.user.normalize_username())
    # print(response.user.objects())    # AttributeError: Manager isn't accessible via User instances
    return render(response, "main/profile.html", {})

# There are two main method ways of storing submitted information: POST & GET
# You may want to use POST because the information you are going to send to the server needs to be encrypted.
# This includes modifications to fields in databases.
# Otherwise, use GET whenever you want to retrieve information.
# With such a request, the related variables and values might appear in the URL.

# >>> dir(response)
# ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__',
# '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_current_scheme_host', '_encoding',
# '_get_full_path', '_get_host', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files',
# '_mark_post_parse_error', '_messages', '_read_started', '_set_content_type_params', '_set_post', '_stream',
# '_upload_handlers', 'accepted_types', 'accepts', 'auser', 'body', 'build_absolute_uri', 'close', 'content_params',
# 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_full_path_info', 'get_host',
# 'get_port', 'get_signed_cookie', 'headers', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info',
# 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user']

# >>> dir(response.user)
# ['DoesNotExist', 'EMAIL_FIELD', 'Meta', 'MultipleObjectsReturned', 'REQUIRED_FIELDS', 'USERNAME_FIELD',
# '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__',
# '__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_constraints',
# '_check_db_table_comment', '_check_default_pk', '_check_field_name_clashes', '_check_fields', '_check_id_field',
# '_check_indexes', '_check_local_fields', '_check_long_column_names', '_check_m2m_through_same_relationship',
# '_check_managers', '_check_model', '_check_model_name_db_lookup_clashes', '_check_ordering',
# '_check_property_name_related_field_accessor_clashes', '_check_single_primary_key', '_check_swappable',
# '_check_unique_together', '_do_insert', '_do_update', '_get_FIELD_display', '_get_expr_references',
# '_get_field_expression_map', '_get_next_or_previous_by_FIELD', '_get_next_or_previous_in_order', '_get_pk_val',
# '_get_session_auth_hash', '_get_unique_checks', '_meta', '_parse_params', '_password', '_perform_date_checks',
# '_perform_unique_checks', '_prepare_related_fields_for_save', '_save_parents', '_save_table', '_set_pk_val',
# '_state', '_validate_force_insert', 'acheck_password', 'adelete', 'arefresh_from_db', 'asave', 'check',
# 'check_password', 'clean', 'clean_fields', 'date_error_message', 'date_joined', 'delete', 'email', 'email_user',
# 'first_name', 'from_db', 'full_clean', 'get_all_permissions', 'get_constraints', 'get_deferred_fields',
# 'get_email_field_name', 'get_full_name', 'get_group_permissions', 'get_next_by_date_joined',
# 'get_previous_by_date_joined', 'get_session_auth_fallback_hash', 'get_session_auth_hash', 'get_short_name',
# 'get_user_permissions', 'get_username', 'groups', 'has_module_perms', 'has_perm', 'has_perms',
# 'has_usable_password', 'id', 'is_active', 'is_anonymous', 'is_authenticated', 'is_staff', 'is_superuser',
# 'last_login', 'last_name', 'logentry_set', 'natural_key', 'normalize_username', 'objects', 'password', 'pk',
# 'prepare_database_save', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'set_password',
# 'set_unusable_password', 'todolist', 'unique_error_message', 'user_permissions', 'username', 'username_validator',
# 'validate_constraints', 'validate_unique']