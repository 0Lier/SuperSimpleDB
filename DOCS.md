# Documentation
- [Usage Examples](#usage)
- [Methods](#methods)
- - [Init](#Init)
- - [globals](#globals)
- - [scoped](#scoped)
- File Structure
***
### Usage Examples
<a id="usage"></a>
```py
import ssdb

# 1. Initialize the database (you only do this once)
db = ssdb.Init()
print("Database ready in: " + db.project_path + "\\Database")
print("\\n")



# ==================================
#            GLOBAL VARIABLES
#    (Variables for the entire application)
# ==================================

print("GLOBAL DATA")

# --- SET (Save) a general variable ---
db.globals.set("App_Name", "MyChatApp")
db.globals.set("Version", "1.0")
print("Saved: App_Name and Version.")

# --- GET (Read) a general variable ---
app_name = db.globals.get("App_Name")
app_vers = db.globals.get("Version")
print(f"-> The app is: {app_name} v{app_vers}")

# --- SET (Replace) a general variable ---
db.globals.set("Version", "2.0")
print("Updated: Version.")

app_vers = db.globals.get("Version")
print(f"-> The app is: {app_name} v{app_vers}")

# --- REMOVE (Delete) a general variable ---
db.globals.remove("Version")
print("REMOVED: Version variable.")

# Check if it's gone
print(f"-> Version after removal: {str(db.globals.get('Version'))} (It's None, so it's gone!)")
print("\\n")

# ==================================
#            SCOPED VARIABLES
#    (Variables saved for a specific ID, like a User)
# ==================================

print("SCOPED DATA")

# --- SET (Save) variables for specific people ---
# Save a color variable for User 'Alex'
db.scoped.set("Fav_Color", "Alex", "Blue")

# Save a color variable for User 'Ben'
db.scoped.set("Fav_Color", "Ben", "Red")
print("Saved Fav_Color variable for Alex and Ben.")

# --- GET (Read) a specific person's variable ---
alex_color = db.scoped.get("Fav_Color", "Alex")
ben_color = db.scoped.get("Fav_Color", "Ben")

print(f"-> Alex's color is: {alex_color}")
print(f"-> Ben's color is: {ben_color}")

# --- SET (Replace) variables for specific people ---
db.scoped.set("Fav_Color", "Ben", "Yellow")
print("Updated Fav_Color variable for Ben.")

ben_color = db.scoped.get("Fav_Color", "Ben")
print(f"-> Ben's color is: {ben_color}")

# --- REMOVE (Delete) a specific person's variable ---
# Delete the Fav_Color variable only for 'Ben'
db.scoped.remove("Fav_Color", "Ben")
print("REMOVED: Fav_Color variable for Ben.")

# Check if it's gone for Ben, but still exists for Alex
print(f"-> Ben's color after removal: {str(db.scoped.get('Fav_Color', 'Ben'))} (Gone!)")
print(f"-> Alex's color is still: {db.scoped.get('Fav_Color', 'Alex')} (Still there!)")
```

Methods
-
**ssdb.Init()** (None) -> object: Database Handler
<a id="Init"></a>
*Initializes the database manager. It should be the first call when using the package, usually in the main file.*
```
ssdb.Init()
```
***

### ssdb.Init().globals
<a id="globals"></a>
Methods
> .get()
.set()
.remove()
***

**.[globals](#globals).get(key: string)** -> string | NoneType: None
<a id="globals_get"></a>
*Retrieves the value of a global variable.*
> **string** *Current value of the variable*
**key** *Name of the variable to retrieve*
```
ssdb.Init().globals.get("VarName")
```
***

**.[globals](#globals).set(key: string, value: string)** -> bool: True | False
<a id="globals_set"></a>
*Stores or replaces the value of a global variable.*
> **key** *Name of the variable to replace or add*
**value** *New value*
```
ssdb.Init().globals.set("VarName", "NewValue")
```
***

**.[globals](#globals).remove(key: string)** -> bool: True | False
<a id="globals_remove"></a>
*Deletes the variable completely.*
> **key** *Name of the variable to remove*
```
ssdb.Init().globals.remove("VarName")
```

### ssdb.Init().scoped
<a id="scoped"></a>
Methods
> .get()
.set()
.remove()
***

**.[scoped](#scoped).get(key: string, id: string)** -> string | NoneType: None
<a id="scoped_get"></a>
*Retrieves the value of a scoped variable.*
> **string** *Current value of the ID related to the variable*
**key** *Name of the variable to retrieve*
**id** Identifier of the value to retrieve in the variable
```
ssdb.Init().scoped.get("VarName", "id")
```
***

**.[scoped](#scoped).set(key: string, id: string, value: string)** -> bool: True | False
<a id="scoped_set"></a>
*Stores or replaces the value of the identifier within a variable.*
> **key** *Name of the variable to replace or add*
**id** Identifier of the value to replace or add in the variable
**value** *New value*
```
ssdb.Init().scoped.set("VarName", "id", "NewValue")
```
***

**.[scoped](#scoped).remove(key: string, id: string)** -> bool: True | False
<a id="scoped_remove"></a>
*Deletes the ID and the value of the variable completely.*
> **key** *Name of the variable where the identifier to be removed is located*
**id** Identifier of the value to be removed in the variable
```
ssdb.Init().scoped.remove("VarName", "id")
```
****
### File Structure
```
📁 Database
    ├─ 📁 globals
    │       └─ 📁 key.json -> {"value": ""}
    │
    └─ 📁 scoped
            └─ 📁 key.json { "id": "", "id": ""}
```
***
### **License**
[**SSDB - Super Simple Database**  
**Copyright (C) 2025 0Lier**  
**Licensed under the GNU GPL v3.0**](./LICENSE.txt)