from pytest_bdd import scenario,given,when,then
from PythonBDDFramework.cucumbers import CucumbersBasket


@scenario('../features/cucumbers.feature','Add cucumbers to a basket')
def test_add():
    pass


@given('the basket has 2 cucumbers')
def basket():
    return CucumbersBasket(initial_count=2)


@when('4 cucumbers are added to the basket')
def add_cucumbers():
    basket.add(4)


@then('the basket contains 6 cucumbers')
def basket_total():
    assert basket.count == 6
