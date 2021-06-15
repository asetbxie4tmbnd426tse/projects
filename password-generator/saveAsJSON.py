import json

def add(file_path: str, cont: dict):
    # The function adds cont to the JSON file
    with open(file_path, 'r+') as file:
        temp = json.load(file)
        temp.append(cont)
        json.dump(temp, file, indent=4)        
        file.close()

def new_file(directory_path: str, name: str, cont: dict):
    # The function creates a new JSON file and stores the content inside.
    file_path = f"{directory_path}/{name}.json"
    temp = [cont]
    with open(file_path, 'w') as file:
        json.dump(temp, file, indent=4)
        file.close()
    