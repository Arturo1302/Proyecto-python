from json import dumps, load
import os

def readFile(fileName):
    try:
        with open(fileName) as f:
            return load(f)
    except:
        return []
    

def saveFile(fileName, data):
    os.makedirs(os.path.dirname(fileName), exist_ok=True)

    with open(fileName, "w") as jsonFile:
        jsonFile.write(dumps(data, indent=4))
    
    print("Nuevo gasto guardado con exito")