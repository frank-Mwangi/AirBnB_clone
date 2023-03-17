#!/usr/bin/python3
import json
from base_model import BaseModel


class FileStorage:
    """A class that serializes and deserializes objects to/from a JSON file."""

    file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return a dictionary of all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the storage."""
        key = obj.__class.name + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to a JSON file."""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_dict, f)

    def reload(self):
        """Deserialize the JSON file to __objects (if the file exists)."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                json_dict = json.load(f)
                for key, value in json_dict.items():
                    cls_name, obj_id = key.split('.')
                    obj = eval(cls_name)(**value)
                    self.new(obj)
        except FileNotFoundError:
            pass
