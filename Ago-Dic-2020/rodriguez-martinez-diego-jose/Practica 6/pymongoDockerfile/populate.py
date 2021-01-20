import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mi-db"]

# Name
print("Nombre de la DB: ", db.name)

#Agrego la coleccion
collist = db.list_collection_names()
if "pet" not in collist:
    mycol = db["customers"]

# Crea colección e inserta un registro
print(db.pet.insert_many([
    {
        "name": "firulais",
        "owner": "jahir",
        "specie": "perro"
    },
    {
        "name": "taco",
        "owner": "jonathan",
        "specie": "perro"
    },
    {
        "name": "garfield",
        "owner": "erick",
        "specie": "gato"
    },
    {
        "name": "charlotte",
        "owner": "juan daniel",
        "specie": "araña"
    },
    {
        "name": "solovino",
        "owner": "jorge",
        "specie": "perro"
    },
]))