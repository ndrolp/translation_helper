import os
import json


class TManager:
    _instance = None
    path = ""
    mainLang = ""
    current_module = ""
    data = {}

    def __init__(self):
        print("Init called")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def loadData(self):
        self.data = {}
        try:
            for entry in os.listdir(self.path):
                entry_path = os.path.join(self.path, entry)
                if not os.path.isdir(entry_path):
                    continue
                self.data[entry] = {}
                for file in os.listdir(entry_path):
                    file_path = os.path.join(entry_path, file)
                    if not os.path.isfile(file_path):
                        continue

                    self.data[entry][file] = {}
                    with open(file_path, "r", encoding="utf-8") as entry_data:
                        data_dict = json.load(entry_data)
                        self.data[entry][file] = data_dict

        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except json.JSONDecodeError as e:
            print(f"Invalid JSON in file: {e}")

        print(self.data)
        return self.data

    def getKeys(self):
        keys = []
        items_to_get_keys = self.data[self.mainLang][self.current_module]
        for key, value in items_to_get_keys.items():
            keys.append(key)

        return keys

    def saveData(self):
        # FIX: Remake all the files with the modules
        for lang, value in self.data.items():
            file = os.path.join(self.path, lang, f"{lang}.json")
            print(file)
            with open(file, "w") as f:
                json.dump(value, f, indent=4)


    def addKey(self, key: str, val: str):
        # FIX: Remake all the files with the modules
        self.data[self.mainLang][key] = val

    def removeKey(self, key: str):
        # FIX: Remake all the files with the modules
        for lang, value in self.data.items():
            value.pop(key, None)
