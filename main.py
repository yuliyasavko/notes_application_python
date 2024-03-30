import json
import datetime
import os

notes = {}

def list_notes():
    print("Список всех заметок:")
    for note in notes.values():
        print(note)

def filter_notes():
    print("Введите дату для фильтрации:")

    try:
        filter_date = input()
        filter_date = datetime.date.fromisoformat(filter_date)

        print(f"Список заметок за дату {filter_date}:")
        for note in notes.values():
            if note["time"].date() == filter_date:
                print(note)
    except:
        print("Введена неверная дата, ожидается yyyy-MM-dd")

def create_note():
    print("Введите заголовок заметки:")
    title = input()

    print("Введите текст заметки:")
    text = input()

    if len(notes) == 0:
        identificator = 0
    else:
        identificator = max(note["id"] for note in notes.values()) + 1

    time = datetime.datetime.now()
    notes[identificator] =  {"id": identificator, "title": title, "text": text, "time": time}

def delete_note():
    pass

def update_note():
    pass

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
            create_note()
        elif command == "update":
            pass
        elif command == "delete":
            pass
        elif command == "list":
            list_notes()
        elif command == "filter":
            filter_notes()
        else:
            print("Неизвестная команда")

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
