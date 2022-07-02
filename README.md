# AirBnB clone - The console
**By [Mauricio Heller](https://github.com/hellerdejanuar) and [Florencia Mestre](https://github.com/FloLys), [Holberton School](https://www.holbertonschool.com/) C17.**

# Project summary
The objective of this project is writing our own AirB&B console using a command interpreter which we will be using to manage our AirB&B objects.

### Contents
- `console.py`: the core of the `cmd` line interpreter
- ***models***
  - `base_model.py`: Defines all common attributes/methods for other classes. It is initialized with ***kwargs* and sets the attributes *id*, *created_at* and *updated_at* with `datetime` and converted in ISO format.\
    *save()*: saves changes and updates the updated time.\
    *to_dict()*: returns a key/value dictionary of __dict__.
  - `Other classes`: (User, State, City, Amenity, Place, Review).
  - ***engine***
    - `file_storage.py`: Serializes instances to a JSON file and deserializes JSON file to instances.\
		*all()*: returns the dictionary `__objects`.\
    *new()*: sets in `__objects` the obj with key "<obj class name>.id".\
		*save()*: serializes `__objects` to the JSON file.\
		*reload()*: deserializes the JSON file to `__objects`.\
- ***tests***


#### Serialization-Deserialization

Writing the dictionary representation to a file:
- It’s not human readable.
- Python doesn’t know how to convert a string to a dictionary (easily).
- Using this file with another program in Python or other language will be hard.

So we will have to:
- Convert an instance to Python built in serializable data structure (list, dict, number and string) to retrieve a dictionary.
- Convert this dictonary representation to a JSON string. For us it will be `my_string = JSON.dumps(my_dict)`.
- Write this string to a file on disk.

And for deserialization, the same but the other way:
- Read a string from a file on disk.
- Convert this JSON string to a data structure. Because it's a JSON representation, it’s easy to convert. For us it will be `my_dict = JSON.loads(my_string)`.
- Convert this data structure to instance. For us it will be `my_instance = MyObject(my_dict)`.

##### Flow:

		<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'>
		-> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>


## Command Interpreter
serialization-deserialization

### How to use it
- Type ./console.py to launch the command interpreter.
- create - Creates a new instance of the class.\
	Usage:
	- create class_name -  Ex: $ create BaseModel
- show - Prints an instance based on the class name and id.\
	Usage:
	- show class_name id - Ex: $ show BaseModel 1234
	- class_name.show(id) - Ex: $ BaseModel.show("1234")
- destroy - Deletes an instance based on the class name and id.\
	Usage:
	- destroy class_name id -  Ex: $ destroy BaseModel 1234
	- class_name.destroy(id) - Ex: $ BaseModel.destroy("1234")
- all - Prints all instances based or not on the class name.\
	Usage:
	- all class_name - Ex: $ all BaseModel
	- all - Ex: $ all
	- class_name.all() - Ex: $ BaseModel.all()
- update: Updates an instance based on the class name and id by adding or updating attribute.\
	Usage:
	- update class_name id attribute_name "attribute_value" - Ex: $ update BaseModel 1234 email "aibnb@mail.com"
	- class_name.update(id, attribute_name, attribute_value) - Ex: $ BaseModel.update("1234", "año de construida", 2010)
- count: Retrieve the number of instances of a class.\
	Usage:
	- class_name.count() - Ex: $ BaseModel.count()
