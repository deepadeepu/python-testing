Feature: Cucumber Basket
  As a gardner,
  I want to carry cucumbers in a basket
  so that I don't stop them at all

  Scenario Add cucumbers to a basket
    Given the basket has 2 cucumbers
    When 4 cucumbers are added to the basket
    Then the basket contains 6 cucumbers
    śśśś