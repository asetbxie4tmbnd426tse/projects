import json

def add(file_path: str, cont: dict):
    # The function adds cont to the JSON file
    with open(file_path, 'r') as f_read:
        temp = json.load(f_read)
        temp.append(cont)
        with open(file_path, 'w') as f_write:
            json.dump(temp, f_write, indent=4)
            f_write.close()
        
        f_read.close()

    pass

def new_file(file_path: str, cont: dict):
    # The function creates a new JSON file and stores the content inside.
    pass