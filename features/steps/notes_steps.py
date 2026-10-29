from behave import given, when, then 
import requests 

@given('the note playload with the title "{title}" and content "{content}"')
def step_rlz(context, title, content):
    context.note_data = {
        "title": title,
        "content": content
    }

@when('I send a request to create the note')
def step_rlz(context):
    context.response = requests.post("http://127.0.0.1:8000/notes", json=context.note_data)

@then('the response status code should be {status_code:d}')
def step_rlz(context, status_code):
    assert context.response.status_code == status_code, f"Expected {status_code}, got {context.response.status_code}"

@then('the response should contain the correct title')
def step_rlz(context):
    response_json = context.response.json()
    assert response_json["title"] == context.note_data["title"]

@given('the note playload with empty title')
def step_rlz(context):
    context.note_data = {
        "title": None,
        "content": "text"
    }

@given('notes are in the system')
def step_list_note(context):
    for i in range(2):
        requests.post("http://127.0.0.1:8000/notes", json={"title": f"Note {i}", "content": "Text"})

@given('notes are not in the system')
def step_list_note(context):
    response = requests.get("http://127.0.0.1:8000/notes")
    notes = response.json()
    for note in notes:
        requests.delete(f"http://127.0.0.1:8000/notes/{note['id']}")

@when('I send a request to get notes')
def step_list_note(context):
     context.response = requests.get("http://127.0.0.1:8000/notes")

@then('the response should contain a list of notes')
def step_list_note(context):
    response_json = context.response.json()
    assert len(response_json) > 0

@then('the response is an empty list')
def step_list_note(context):
    response_json = context.response.json()
    assert len(response_json) == 0

@given('note with valid id is in the system')
def id_note(context):
    context.note_data = {"title": "Test", "content": "Text"}
    response = requests.post("http://127.0.0.1:8000/notes", json=context.note_data)
    context.note_id = response.json()["id"]

@given('note has not valid id')
def id_note(context):
    context.note_id = 111111

@when('I send a request to get a note')
def id_note(context):
    context.response = requests.get(f"http://127.0.0.1:8000/notes/{context.note_id}")

@when('I send a request to update a note')
def update_note(context):
    update_data = {"title": "new title", "content": "new content"}
    context.response = requests.put(f"http://127.0.0.1:8000/notes/{context.note_id}", json=update_data)

@then('the response should contain to update title')
def update_note(context):
    response_json = context.response.json()
    assert response_json["title"] == "new title"

@when('I send a request to delete a note')
def delete_note(context):
    context.response = requests.delete(f"http://127.0.0.1:8000/notes/{context.note_id}")