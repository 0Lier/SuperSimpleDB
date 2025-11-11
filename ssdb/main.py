# SSDB - Super Simple Database
# Copyright (C) 2025 0Lier
# Licensed under the GNU GPL v3.0

import os, json

class Init:
    _instance = None
    globals: "globals" 
    scoped: "scoped"
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.project_path = os.path.dirname(os.path.abspath(os.sys.argv[0]))
            cls._instance.globals = globals(cls._instance.project_path)
            cls._instance.scoped = scoped(cls._instance.project_path)
        return cls._instance
    
class globals:
    def __init__(self, project_path):
        self.db_folder = os.path.join(project_path, "Database", "globals") 
        os.makedirs(self.db_folder, exist_ok=True)
        self.db_file = None
        
    def set(self, name: str, value: str):
        try:
            self.db_file = os.path.join(self.db_folder, f"{name}.json")
            data = {
                "value": str(value)
            }
            with open(self.db_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
                    
        except Exception as e:
            print(f"An error has occurred while saving the variable: {type(e).__name__}: {e}")
            return False
            
    def get(self, name: str):
        try:
            self.db_file = os.path.join(self.db_folder, f"{name}.json")
            with open(self.db_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            return str(data.get('value', ''))
        except (FileNotFoundError) as e:
            return None
        except json.JSONDecodeError:
            return None 
        
    def remove(self, name: str):
        try:
            self.db_file = os.path.join(self.db_folder, f"{name}.json")
            os.remove(self.db_file)
            return True
        except Exception as e:
            print(f"Error removing '{name}.json': {type(e).__name__}: {e}")
            return False
    
class scoped:
    def __init__(self, project_path):
        self.db_folder = os.path.join(project_path, "Database", "scoped") 
        os.makedirs(self.db_folder, exist_ok=True)
        self.db_file = None
    def set(self, name: str, id: str, value: str):
        try:
            self.db_file = os.path.join(self.db_folder, f"{name}.json")
            if os.path.exists(self.db_file):
                with open(self.db_file, "r", encoding="utf-8") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = {}
            else:
                data = {}
            data[id] = value
            with open(self.db_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"An error has occurred while saving the variable: {type(e).__name__}: {e}")
            return False
    def get(self, name: str, id: str):
        try: 
            self.db_file = os.path.join(self.db_folder, f"{name}.json")
            with open(self.db_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            return str(data.get(id, ''))
            
        except (FileNotFoundError) as e:
            return None
        except json.JSONDecodeError:
                    return None
        except Exception as e:
            print(f"An error has occurred while obtaining the variable: {type(e).__name__}: {e}")
            return None
    def remove(self, name: str, id: str):
        try:
            self.db_file = os.path.join(self.db_folder, f"{name}.json")
            with open(self.db_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
            del data[id]
            with open(self.db_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error removing ID '{id}' from '{name}.json': {type(e).__name__}: {e}")
            return False
        

                
                    
                    
            
