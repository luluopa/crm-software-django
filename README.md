# CRMtool-Django

Description
===========

Users can act as agents or organizers

Each agent has only one organizer and their leads (tasks) are created and signed by their organizer

Password reset functionality using email for validation

Login and Logout where each user has specific permissions within the system (implementation of custom
mixins)

Demonstration
=============

### `Initial Screen`
![ezgif com-gif-maker](https://user-images.githubusercontent.com/56770452/151399118-803d5c9d-ab10-4728-9acf-e70ed681a108.gif)


### `User Screen`
![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/56770452/151399203-e82aaffa-8425-4b71-816f-05ab4897e8d6.gif)


Installation 
============

```md
python -m virtualenv djangoenv
source ./djangoenv/bin/activate
python -m pip install -r ./CRMtool/requirements.txt
```
### `In CRMtool folder`
```md
python manage.py runserver
```

