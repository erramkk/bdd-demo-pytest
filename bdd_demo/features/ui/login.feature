@login
Feature: user login

    @valid_login
    Scenario: verify login with valid username and password
        Given I launch the given "chrome" browser
        And I open the url "https://practice.expandtesting.com/login" in the tab
        And I enter value "practice" in "username field" having "xpath"="//input[@name='username']"
        And I enter value "SuperSecretPassword!" in "Password field" having "css"="input[name='password']"
        And I click on the "button" having "css"="button.btn"
        And I wait for "10" seconds
        Then I make sure that "title" is "visible" on "page" having "xpath"="//h4[contains(text(),'Welcome to the Secure Area')]"
