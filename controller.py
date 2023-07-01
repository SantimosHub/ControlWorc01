from datetime import datetime

import view
import service

notes = []
file_name = "notes.json"


def start():
    view.print_message("Nonebook is open")
    while True:
        action = int(view.input_data(
            "Enter the number of action:\n1 — Show all notes\n2 — Find note by ID\n3 — Find note by DATE\n4 — Add note\n5 — Edit note\n6 - Delete "
            "note\n0 — Exit\n>>> "))
        if action == 0:
            view.print_message('Notebook is closed')
            break
        elif action == 1:
            view.print_notes(service.load_notes(file_name))
        elif action == 2:
            note_id = int(view.input_data('Enter notes ID for search:'))
            find_result = service.find_notes_id(service.load_notes(file_name), note_id)
            if not find_result:
                view.print_message('There is no such note')
            else:
                view.print_notes(find_result)
        elif action == 3:
            date = view.input_data('Enter notes ID for search:')
            find_result = service.find_notes_date(service.load_notes(file_name), date)
            if not find_result:
                view.print_message('There is no such note')
            else:
                view.print_notes(find_result)
        elif action == 4:
            service.add_note(file_name, notes)
            view.print_message('Note is added')
        elif action == 5:
            note_id = int(view.input_data('Enter notes ID of the note to edit '))
            edit_result = service.edit_note(file_name, service.load_notes(file_name), note_id)
            if not edit_result:
                view.print_message('There is no such note')
            else:
                view.print_message('Note is edit')
        elif action == 6:
            note_id = int(view.input_data('Enter the ID of the note to delete: '))
            delete_result = service.delete_note(file_name, service.load_notes(file_name), note_id)
            if not delete_result:
                view.print_message('There is no such note')
            else:
                view.print_message('Note is delete')
        else:
            view.print_message("The number is incorrect.")
