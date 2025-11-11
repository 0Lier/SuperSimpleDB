import scopedb


print("GLOBAL DATA")

# --- SET (Save) a general variable ---
scopedb.Init().globals.set("App_Name", "MyChatApp")
scopedb.Init().globals.set("Version", "1.0")
print("Saved: App_Name and Version.")

# --- GET (Read) a general variable ---
app_name = scopedb.Init().globals.get("App_Name")
app_vers = scopedb.Init().globals.get("Version")
print(f"-> The app is: {app_name} v{app_vers}")

scopedb.Init().scoped.set("Version", "1.0", "4983")
