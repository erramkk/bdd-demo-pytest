@login
Feature: user login

    @valid_login
    Scenario: verify login with valid username and password
        Given I launch the given "chrome" browser
        And I open the url "https://odootest17.ksolves.net/web/login" in the tab
        And I enter value "*******" in "username field" having "xpath"="//input[@name='login']"
        And I enter value "*******" in "Password field" having "css"="input[name='password']"
        And I click on the "button" having "css"="button.btn"
        And I wait for "15" seconds
        Then I make sure that "title" is "visible" on "page" having "css"="input[title='Inbox']"
