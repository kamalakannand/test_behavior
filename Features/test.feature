Feature: Testing the Incrementor
  Scenario: test to increment a number
    Given To increment a size of 4
    When we increment to 10
    Then it should be 13
