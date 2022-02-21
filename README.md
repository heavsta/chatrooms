# Chatrooms

This project is the capstone of the CS50: Web Programming with Python and JavaScript course.
CS50: Chatrooms allows students all over the world to discuss in discord-like chatrooms about the diverse CS50 courses.

## Requirements

In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:

- Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the old CS50W Pizza project), and more complex than those.
    - A project that appears to be a social network is a priori deemed by the staff to be indistinct from Project 4, and should not be submitted; it will be rejected.
    - A project that appears to be an e-commerce site is strongly suspected to be indistinct from Project 2, and your README.md file should be very clear as to why it’s not. Failing that, it should not be submitted; it will be rejected.
- Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
- Your web application must be mobile-responsive.

## Distinctiveness and Complexity

This project has been fulfilled on the back-end side with the help of the python framework [Django](https://www.djangoproject.com/) and the [Django Channels](https://channels.readthedocs.io/en/stable/) project.
On the other hand the front-end side has been handled with the [JavaScript WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket) and some vanilla JavaScript.
The mobile version has been dealt with [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries).


![WebSocket](https://upload.wikimedia.org/wikipedia/commons/1/10/Websocket_connection.png)
###### _Why the use of a [WebSocket](https://en.wikipedia.org/wiki/WebSocket) and not just a classic HTTP protocol?_
WebSocket is a communications protocol, providing full-duplex communication channels over a single TCP connection.
Advantages:
* It is a bi-directional protocol
* It provides a full-duplex communication
* It is supported by all modern browsers

The full-duplex communication is clearly the killer point. On a chat app, instant interactivity and high dynamism is mandatory. WebSocket allows the users to receive & send messages from & to each other without having to reload any page, or keeping sending HTTP requests, as everyone will get notified as soon as any update will happen. Hence the use of Channels, that allow us to keep track of all the users in groups.

#### Structure
```
.
├── capstone
    ├── asgi.py
    ├── __init__.py
    ├── routing.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
├── chat
    ├── admin.py
    ├── apps.py
    ├── consumers.py
    ├── __init__.py
    ├── migrations
        ├── 0001_initial.py
        ├── 0002_room.py
        ├── 0003_room_fullname.py
        └── __init__.py
    ├── models.py
    ├── routing.py
    ├── static
        └── chat
        ├── img
            ── cs50.png
        ├── script.js
        └── styles.css
    ├── templates
        └── chat
            ├── chatroom.html
            ├── index.html
            ├── layout.html
            ├── login.html
            └── register.html
    ├── tests.py
    ├── urls.py
    └── views.py
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

#### Files Description

[`./capstone/routing.py`](https://github.com/heavsta/chatrooms/blob/main/capstone/routing.py)
Use of the [ProtocolTypeRouter](https://channels.readthedocs.io/en/stable/topics/routing.html#protocoltyperouter) to define the chat routing.

[`./capstone/settings.py`](https://github.com/heavsta/chatrooms/blob/main/capstone/settings.py)
Setup of the Installed apps, WSGI app, static & login URLs, ASGI app and channel layers.

[`./capstone/urls.py`](https://github.com/heavsta/chatrooms/blob/main/capstone/urls.py)
Setup the root '/' path as the default path for the chat app.

[`./chat/admin.py`](https://github.com/heavsta/chatrooms/blob/main/chat/admin.py)
Registered to Room model to allow superusers to edit the rooms.

[`./chat/consumers.py`](https://github.com/heavsta/chatrooms/blob/main/chat/consumers.py)
[Consumers](https://channels.readthedocs.io/en/stable/topics/consumers.html), as the documentation describes it, are a rich abstraction that allows us to make ASGI applications easily.
We there write the functions that are called uppon diverse events.
We are using here the [AsyncWebsocketConsumer](https://channels.readthedocs.io/en/stable/topics/consumers.html#asyncwebsocketconsumer) in order to use the WebsocketConsumer methods in an async manner.
`connect` and `disconnect` to handle groups on our channel layer.
`receive` receives the json data and sends to any user in channel layer group
`chatroom_message` sends the message and username in a json format

[`./chat/models.py`](https://github.com/heavsta/chatrooms/blob/main/chat/models.py)
Created the Room model to allow users to discuss in different pre-defined rooms.

[`./chat/routing.py`](https://github.com/heavsta/chatrooms/blob/main/chat/routing.py)
Use of a relative path and define the websocket urlpatterns of the rooms to link them to our ChatRoomConsumer.

[`./chat/static/script.js`](https://github.com/heavsta/chatrooms/blob/main/chat/static/script.js)
JS file that mostly handles animations & mobile version.

[`./chat/templates/chat/chatroom.html`](https://github.com/heavsta/chatrooms/blob/main/chat/templates/chat/chatroom.html)
This file matters, as the JavaScript block inside of it handles the WebSocket communications from the client side.
We there make use of the WebSocket API, setup event listeners to send the data in a json format if we send a message, and edit our chat everytime the websocket notifies that a new message has arrived.

[`./chat/urls.py`](https://github.com/heavsta/chatrooms/blob/main/chat/urls.py)
Here we define the diverse url paths & views functions for our app.

[`./chat/views.py`](https://github.com/heavsta/chatrooms/blob/main/chat/views.py)
List of the functions that we call on the paths we defined earlier.
Handling the Registration, Login, Logout, Index and Chatroom.

#### Run

Inside of your local environment, first install the requirements:
```
$ pip install -r requirements.txt
```

Execute the necessary migrations:
```
$ python manage.py makemigrations chat
$ python manage.py migrate
```

Run the app:
```
$ python manage.py runserver
```
