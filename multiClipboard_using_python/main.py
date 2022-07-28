import sys
#pip install clipboard
import clipboard
import json

SAVED_DATA = "clipboard.json"
#saveing data 
def save_data(filepath, data):
    #opeing the file in write mode so that it can create and overwrite the data into it 
    with open(filepath,"w") as f:
        #dumpting the data into file 
        json.dump(data,f)
#loading data
def load_data(filepath):
    try:
        with open(filepath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    #accessing the data after python main.py
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        #if the command is save that get the key and data form clipboard save into json file
        key = input("Enter a key:")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
        print("Data Save")
    elif command == "load":
        #if the command is load ask for key , if the key is valid then load it to clip board 
        key = input("Enter a key:")
        if key in data:
            clipboard.copy(data[key])
            print("Data is copied in clipboard")
        else:
            print("Key doesn't exit")
    elif command == "list":
        #if the command is list then return all the saved data from the json file
        print(data)
    elif command == "delete":
        #if the command is delete ask for a key and then if the key is valid , delete that info 
        key = input("Enter your delete key")
        if key in data:
            del data[key]
        else:
            print("Invalid key")

    else:
        print("Unknown command")
else:
    print("Print pass exactly one command")
