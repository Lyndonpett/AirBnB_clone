#  AirBnB_clone

This project uses concepts from Python to start the file storage of a AirBnb clone website.



##  Console

One of the largest parts of this project was creating a console that is able to pull information to and from our file storage system.

###  How to use the Console in Interactive Mode:

Simply run `./console.py` in your command line and voila, you're in the console and you're ready to go.



```

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):

========================================

EOF all create destroy help quit show update

(hbnb)
```

###  How to use the Console in Non-Interactive Mode:

Rather than running just `./console.py` in your command line, you can pipe a command with the console script and it will return whatever the command was intended to be ran.



```

$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):

========================================

EOF all create destroy help quit show update

```



##  Current Commands:

| Command | Use | Description |
| :--- | :----------- | :--- |
| `help` | `help <command>` | shows what a command is used for |
| `quit` | `quit` | command Exits the console |
| `EOF` | `EOF` | command Exits the console |
| `all` | `all` or `all <class>` | displays all the class instances |
| `create` | `create <class>` | creates a new class instance |
| `destroy` | `destroy <class> <id>` | deletes the class instance |
| `show` | `<class> <id>` | command prints instance of class |
| `update` | `<class> <id> <attr_name> <attr_val>` | command updates class attr with value |


##  Example:

```

$ ./console.py
(hbnb) all
[]
(hbnb) create User
f3a6929c-a046-4ae9-90e2-c5d8bde86e86
(hbnb) create City
1f3075d1-9c76-4877-9219-3d1602096df9
(hbnb) all
["[City] (1f3075d1-9c76-4877-9219-3d1602096df9) {'updated_at': datetime.datetime(2021, 10, 28, 19, 54, 56, 964160), 'created_at': datetime.datetime(2021, 10, 28, 19, 54, 56, 964160), 'id':
'1f3075d1-9c76-4877-9219-3d1602096df9'}", "[User] (f3a6929c-a046-4ae9-90e2-c5d8bde86e86) {'updated_at': datetime.datetime(2021, 10, 28, 19, 54, 48, 629362), 'created_at': datetime.datetime(2021,
10, 28, 19, 54, 48, 629362), 'id': 'f3a6929c-a046-4ae9-90e2-c5d8bde86e86'}"]
(hbnb) all City
["[City] (1f3075d1-9c76-4877-9219-3d1602096df9) {'updated_at': datetime.datetime(2021, 10, 28, 19, 54, 56, 964160), 'created_at': datetime.datetime(2021, 10, 28, 19, 54, 56, 964160), 'id':
'1f3075d1-9c76-4877-9219-3d1602096df9'}"]
(hbnb) show User f3a6929c-a046-4ae9-90e2-c5d8bde86e86
[User] (f3a6929c-a046-4ae9-90e2-c5d8bde86e86) {'updated_at': datetime.datetime(2021, 10, 28, 19, 54, 48, 629362), 'created_at': datetime.datetime(2021, 10, 28, 19, 54, 48, 629362), 'id':
'f3a6929c-a046-4ae9-90e2-c5d8bde86e86'}
(hbnb) destroy User f3a6929c-a046-4ae9-90e2-c5d8bde86e86
(hbnb) all
["[City] (1f3075d1-9c76-4877-9219-3d1602096df9) {'updated_at': datetime.datetime(2021, 10, 28, 19, 54, 56, 964160), 'created_at': datetime.datetime(2021, 10, 28, 19, 54, 56, 964160), 'id':
'1f3075d1-9c76-4877-9219-3d1602096df9'}"]
(hbnb) update City 1f3075d1-9c76-4877-9219-3d1602096df9 name "Los Angeles"
(hbnb) show City 1f3075d1-9c76-4877-9219-3d1602096df9
[City] (1f3075d1-9c76-4877-9219-3d1602096df9) {'id': '1f3075d1-9c76-4877-9219-3d1602096df9', 'updated_at': datetime.datetime(2021, 10, 28, 19, 57, 26, 348781), 'name': 'Los Angeles',
'created_at': datetime.datetime(2021, 10, 28, 19, 54, 56, 964160)}
(hbnb) quit
$
```

##  Authors:

> Lyndon Pettersson: [Github](https://github.com/Lyndonpett)

> Tres Serio: [GitHub](https://github.com/treserio)