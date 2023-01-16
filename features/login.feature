Feature: Login Feature

Scenario: Success Login with correct credential
    Given I am on the homepage
    When I fill my credential
    Then I should be logged in

Scenario: Failed login with wrong username
    Given I am on the homepage
    When I fill wrong email
    Then I should not be logged in
    And I should see the error message