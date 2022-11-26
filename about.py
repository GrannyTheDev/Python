import json
table = {
    "name: ": "granny",
    "age: ": 15,
    "country: ": "Netherlands",
    "languages: ": "lua, python, C, C#, C++, javascript, html, css"
}
json.dumps(table)
print("Name " + table["name"])
print("Age " + str(table["age"]))
print("Country " + table["country"])
print("Languages " + table["languages"])