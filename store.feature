Feature: Login

Scenario: Testing user access

Given user is on homepage
When login_link is clicked
When email is entered
When password is entered
When login_button is clicked
Then user is logged_in