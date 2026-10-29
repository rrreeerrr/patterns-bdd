Feature: Create a note 

Scenario: Succcessfully create a note
Given the note playload with the title "Test" and content "This is a note"
When I send a request to create the note
Then the response status code should be 200
And the response should contain the correct title 

Scenario: Unsuccessfully create a note
Given the note playload with empty title 
When I send a request to create the note
Then the response status code should be 422

Scenario: get list of notes when they are in system
Given notes are in the system 
When I send a request to get notes
Then the response status code should be 200
And the response should contain a list of notes

Scenario: get list of notes when they are not in system
Given notes are not in the system
When I send a request to get notes
Then the response status code should be 200
And the response is an empty list 

Scenario: There is a note with a valid id
Given note with valid id is in the system
When I send a request to get a note
Then the response status code should be 200
And the response should contain the correct title

Scenario: There is not a note with not valid id
Given note has not valid id
When I send a request to get a note
Then the response status code should be 404

Scenario: Edit a note with valid id
Given note with valid id is in the system
When I send a request to update a note
Then the response status code should be 200
And the response should contain to update title

Scenario: Edit a note with not valid id
Given note has not valid id
When I send a request to update a note
Then the response status code should be 404

Scenario: Delete a note with valid id
Given note with valid id is in the system
When I send a request to delete a note
Then the response status code should be 200

Scenario: Delete a note with not valid id
Given note has not valid id
When I send a request to delete a note
Then the response status code should be 404