from behave import Given, When, Then
from main import incrementor


@Given("To increment a size of {stride}")
def givenincrementor(context, stride: str):
    context.incrementor = incrementor(int(stride))


@When("we increment to {num}")
def when_increment(context, num: str):
    context.results = context.incrementor(int(num))


@Then("it should be {results}")
def then_results(context, results: str):
    assert (context.results == int(results))
