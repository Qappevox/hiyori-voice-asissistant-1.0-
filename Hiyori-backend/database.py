import os
import json
from json import JSONDecodeError
tail  = ""
class Database():
    def __init__(self):
        super(Database, self).__init__()
        
    def checkDB(self):
        global dbFlag
        print("[+]Connecting to database")
        try:
            with open("hiyoriDatabase.json") as d:
                try:
                    data = json.load(d)
                    tmp = str(data)
                except (JSONDecodeError):
                    print("Database is empty or broken...")
                    print("[-]Fixing problems...")
                    with open("hiyoriDatabase.json", "w") as d:
                        d.write('{"key": "value"}')
                        d.close()
                        tmp = '{"key": "value"}'
                d.close()
        except FileNotFoundError:
            open("hiyoriDatabase.json", "x")
            with open("hiyoriDatabase.json") as d:
                try:
                    data = json.load(d)
                    tmp = str(data)
                except (JSONDecodeError):
                    print("Database is empty or broken...")
                    print("[-]Fixing problems...")
                    with open("hiyoriDatabase.json", "w") as d:
                        d.write('{"key": "value"}')
                        d.close()
                        tmp = '{"key": "value"}'
                d.close()
        if tmp == '{"key": "value"}':
            print("    [+]Database has been fixed.")
        print("[+]Connected to database")

    def addToDB(self, newKey, newValue):
        #tail = {'key', 'value}
        global dbFlag, tail

        tail = [newKey, newValue]
        self.convertToJsonData()
        with open("hiyoriDatabase.json") as d:
            data = json.load(d)
            tmp = str(data)
            tmp = tmp.replace("}", ",")
            tmp = tmp.replace("'", '"')
            d.close()

        with open("hiyoriDatabase.json", "w") as d:
            d.write(tmp)
            d.close()
            
        with open("hiyoriDatabase.json", "+a") as d:
            d.write(tail)
            d.close()


    def deleteToDB(self, key):
        targetData = [key, self.getValue(key)]
        targetData = ', "{}": "{}"'.format(targetData[0], targetData[1])
        print("target data is --> {0}".format(targetData))
        with open("hiyoriDatabase.json") as d:
            data = json.load(d)
            tmp = str(data)
        with open("hiyoriDatabase.json") as d:
            data = json.load(d)
            tmp = str(data)
            tmp = tmp.replace("'", '"')
            tmp = tmp.replace(targetData, "")
            d.close()

        with open("hiyoriDatabase.json", "w") as d:
            d.write(tmp)
            d.close()
        if self.getValue(key) == None:
            print("Target value is none.")
        else:
            print("Process successful.")

    def convertToJsonData(self):
        global tail
        tail = str(tail)
        dirtyData = ["[", "]", ",", "'"]
        for dirt in dirtyData:
            if dirt == ",":
                tail = tail.replace(dirt, ":")
            elif dirt == "'":
                tail = tail.replace(dirt, '"')
            else:
                tail = tail.replace(dirt, "")
        tail = tail + "}"

    def getValue(self, key):
        with open("hiyoriDatabase.json") as d:
            data = json.load(d)
            try:
                value = data[key]
                d.close()
                return value
            except:
                print("none")

    def resetDB(self):
        for i in os.listdir():
            if "hiyoriDatabase.json" == i:
                os.remove(i)
        with open("hiyoriDatabase.json", "w") as d:
            d.write('')
            d.close()
    def main(self):  
        self.checkDB()
        
database = Database()

