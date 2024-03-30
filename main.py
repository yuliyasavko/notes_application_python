import json
import datetime

notes = {}

def create_note(identificator, title, text):
    notes[identificator] =  {"id":identificator, "title": title, "text": text, "time": datetime.datetime.now().isoformat()}

def delete_note(identificator):
    del notes[identificator]

def get_note(identificator):
    return notes[identificator]

def update_note(identificator, title, text):
    note = get_note(identificator)
    note["title"] = title
    note["text"] = text
    note["time"] = datetime.datetime.now().isoformat()

def read_notes(file_name):
    with open(file_name, "r") as f:
        return json.load(f) 

def save_notes(file_name):
    with open(file_name, "w") as f:
        json.dump(notes, f)

create_note(1,2,7)
print (get_note(1))