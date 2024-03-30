import json
import datetime
import os

notes = {}

def create_note(identificator, title, text):
    notes[identificator] =  {"id": identificator, "title": title, "text": text, "time": datetime.datetime.now()}

def delete_note(identificator):
    del notes[identificator]

def get_note(identificator):
    return notes[identificator]

def update_note(identificator, title, text):
    note = get_note(identificator)
    note["title"] = title
    note["text"] = text
    note["time"] = datetime.datetime.now()

def read_notes(file_name):
    if os.path.exists(file_name):
        global notes
        with open(file_name, "r") as f:
            notes = json.load(f)
            for note in notes.values():
                note["time"] = datetime.datetime.fromisoformat(note["time"])


def save_notes(file_name):
    with open(file_name, "w") as f:
        for note in notes.values():
            note["time"] = note["time"].isoformat()
        json.dump(notes, f)

if __name__ == "__main__":
    read_notes("notes.json")

    while True:
        print("Введите команду")
        command = input().lower()

        if command == "exit":
            break
        elif command == "create":
            pass
        elif command == "update":
            pass
        elif command == "delete":
            pass
        elif command == "list":
            pass
        elif command == "filter":
            pass
        else:
            print("Неизвестная команда")

    # create_note(1,2,7)
    # print(get_note(1))
    print("Хотите сохранить изменения?")
    while True:
        result = input().lower()
        if result == "yes":
            save_notes("notes.json")
            print ("Изменения сохранены")
            break
        elif result == "no":
            print("Изменения не сохранены")
            break
        else:
            print('Допускается ответ "Yes" или "No"')
