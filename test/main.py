import ssdb


print("GLOBAL DATA")

# --- SET (Save) a general variable ---
ssdb.Init().globals.set("App_Name", "MyChatApp")
ssdb.Init().globals.set("Version", "1.0")
print("Saved: App_Name and Version.")

# --- GET (Read) a general variable ---
app_name = ssdb.Init().globals.get("App_Name")
app_vers = ssdb.Init().globals.get("Version")
print(f"-> The app is: {app_name} v{app_vers}")

ssdb.Init().scoped.set("Version", "1.0", "4983")
