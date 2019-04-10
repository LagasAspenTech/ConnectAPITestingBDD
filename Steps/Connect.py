import pytest
from pytest_bdd import scenario, given, when, then
import requests
import json

URL = "10.16.51.178:6584"
resp = requests.get('http://' + URL + '/get_devices')


@scenario('Connect.feature', 'Client requests a list of Aspen Connect instances (GET /get_devices)')
def test_scenario_get_devices():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_devices():
    assert True


@when("The client requests a list of instances")
def test_request_instances():
    resp = requests.get('http://' + URL + '/get_devices')


@then("The client should receive a list of instances")
def test_check_instances():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests information for currently connected device (GET /get_device_info)')
def test_scenario_get_device_info():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_device_info():
    assert True


@when("The client requests connected device data")
def test_request_device_info():
    resp = requests.get('http://' + URL + '/get_device_info')


@then("The client should receive connected device data")
def test_check_device_info():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests device stats for currently connected device (GET /get_device_stats)')
def test_scenario_get_device_stats():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_device_stats():
    assert True


@when("The client requests connected device statistics")
def test_request_device_stats():
    resp = requests.get('http://' + URL + '/get_device_stats')


@then("The client should receive connected device statistics")
def test_check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list of JSon schemas that define protocol plugins for currently connected device (GET /get_schemas)')
def test_scenario_get_schemas():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_schemas():
    assert True


@when("The client requests connected device schemas")
def test_request_device_schemas():
    resp = requests.get('http://' + URL + '/get_schemas')


@then("The client should receive connected device schemas")
def test_check_device_schemas():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client creates an instance of a protocol plugin as a standalone server (POST /add_server)')
def test_scenario_add_server():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_add_server():
    assert True


@when("The client adds a server instance")
def test_add_server():
    resp = requests.post('http://' + URL + '/add_server')


@then("A new server instance should be added")
def test_check_server():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list of all configured, connected servers (GET /get_servers)')
def test_scenario_get_servers():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_servers():
    assert True


@when("The client requests a list of servers")
def test_get_servers():
    resp = requests.get('http://' + URL + '/get_servers')


@then("The client should receive a list of servers")
def test_check_servers():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client deletes a given server (POST /delete_server)')
def test_scenario_delete_server():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_delete_server():
    assert True


@when('The client deletes a given server')
def test_delete_server():
    resp = requests.post('http://' + URL + '/delete_server')


@then('The server should be deleted')
def test_check_delete_server():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list of devices (POST /test_connection)')
def test_scenario_test_connection():
    assert True


@given('The client is connected to a valid server instance')
def test_valid_connect_test_connection():
    assert True


@when('The client requests a list of devices')
def test_test_connection():
    resp = requests.post('http://' + URL + '/test_connection')


@then('The client should receive a list of devices')
def test_check_test():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list discovered tags on connected server instance (POST /get_available_tags)')
def test_scenario_get_available_tags():
    assert True


@given('The client is connected to a valid server instance')
def test_valid_connect_get_available_tags():
    assert True


@when('The client requests a list of tags')
def test_get_available_tags():
    resp = requests.post('http://' + URL + '/get_available_tags')


@then('The client should receive a list of tags')
def test_check_available_tags():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /activate_tags)")
def test_scenario_activate_tags():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_activate_tags():
    assert True


@when("The client saves a set of tags")
def test_activate_tags():
    resp = requests.post('http://' + URL + '/activate_tags')


@then("The set of tags should be saved")
def test_check_activated_tags():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /create_tags)")
def test_scenario_create_tags():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_create_tags():
    assert True


@when("The client creates a set of tags")
def test_create_tags():
    resp = requests.post('http://' + URL + '/create_tags')


@then("The tags should be created")
def test_check_created_tags():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes tags with corresponding IDs (POST /delete_tags)")
def test_scenario_delete_tags():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_delete_tags():
    assert True


@when("The client deletes a set of tags")
def test_delete_tags():
    resp = requests.post('http://' + URL + '/delete_tags')


@then("The set of tags should be deleted")
def test_check_deleted_tags():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client creates route to define input/output server/tags (POST /create_route)")
def test_scenario_create_route():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_create_route():
    assert True


@when("The client creates a route")
def test_create_route():
    resp = requests.post('http://' + URL + '/create_route')


@then("The route should be created")
def test_check_route():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client requests a list of routes related to the given server id (POST /get_routes)")
def test_scenario_get_routes():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_routes():
    assert True


@when('The client requests a list of routes')
def test_get_routes():
    resp = requests.post('http://' + URL + '/get_routes')


@then('The client should receive a list of routes')
def test_check_routes():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client deletes route with a given ID (POST /delete_route)')
def test_scenario_delete_route():
    assert True


@given('The client is connected to a valid server instance')
def test_valid_connect_delete_route():
    assert True


@when('The client deletes a given route')
def test_delete_route():
    resp = requests.post('http://' + URL + '/delete_route')


@then('The route should be deleted')
def test_check_deleted_route():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client creates a set of derived tags (POST /create_derived_tags)')
def test_scenario_create_derived_tags():
    assert True


@given('The client is connected to a valid server instance')
def test_valid_connect_create_derived_tags():
    assert True


@when('The client creates a set of derived tags')
def test_create_derived_tags():
    resp = requests.post('http://' + URL + '/create_derived_tags')


@then('The set of derived tags should be created')
def test_check_derived_tags():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes a set of derived tags (POST /delete_derived_tags)")
def test_scenario_delete_derived_tags():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_delete_derived_tags():
    assert True


@when("The client deletes a set of derived tags")
def test_delete_derived_tags():
    resp = requests.post('http://' + URL + '/delete_derived_tags')


@then("The set of derived tags should be deleted")
def test_check_deleted_derived_tags():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client activates a device with license data (POST /activate_device)")
def test_scenario_activate_device():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_activate_device():
    assert True


@when("The client activates a device")
def test_activated_device():
    resp = requests.post('http://' + URL + '/activate_device')


@then("The device should be activated")
def test_check_activation():
    assert (resp.status_code == 200)