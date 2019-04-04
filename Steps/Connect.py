from pytest_bdd import scenario, given, when, then
import requests

global resp

@scenario('Connect.feature','Client requests a list of Aspen Connect instances (GET /get_devices)')
def test_connect():
    pass

@given("The client is connected to a valid server instance")
def valid_connect():

@when("The client requests a list of instances")
def request_instances():
    resp = requests.get('http://10.16.51.178:6584/get_devices')

@then("The client should receive a list of instances")
def check_instances():
    assert (resp.status_code == 200)