from pytest_bdd import scenario, given, when, then
import requests

global resp


@scenario('Connect.feature', 'Client requests a list of Aspen Connect instances (GET /get_devices)')
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client requests a list of instances")
def request_instances():
    resp = requests.get('http://10.16.51.178:6584/get_devices')


@then("The client should receive a list of instances")
def check_instances():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests information for currently connected device (GET /get_device_info)')
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client requests connected device data")
def request_device_info():
    resp = requests.get('http://10.16.51.178:6584/get_device_info')


@then("The client should receive connected device data")
def check_device_info():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests information for currently connected device (GET /get_device_stats)')
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client requests connected device statistics")
def request_device_stats():
    resp = requests.get('http://10.16.51.178:6584/get_device_stats')


@then("The client should receive connected device statistics")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list of JSon schemas that define protocol plugins for currently connected device (GET /get_schemas)')
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client requests connected device schemas")
def request_device_stats():
    resp = requests.get('http://10.16.51.178:6584/get_schemas')


@then("The client should receive connected device schemas")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client creates an instance of a protocol plugin as a standalone server (POST /add_server)')
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client adds a server instance")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/add_server')


@then("A new server instance should be added")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list of all configured, connected servers (GET /get_servers)')
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client requests a list of servers")
def request_device_stats():
    resp = requests.get('http://10.16.51.178:6584/get_servers')


@then("The client should receive a list of servers")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client deletes a given server (POST /delete_server)')
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client deletes a given server")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/delete_server')


@then("The server should be deleted")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list of devices (POST /test_connection)')
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client request a list of devices")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/test_connection')


@then("The client should receive a list of devices")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list discovered tags on connected server instance (POST /get_available_tags)')
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client requests a list of tags")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/get_available_tags')


@then("The client should receive a list of tags")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /activate_tags)")
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client saves a set of tags")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/activate_tags')


@then("The set of tags should be saved")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /create_tags)")
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client creates a set of tags")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/create_tags')


@then("The tags should be created")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes tags with corresponding IDs (POST /delete_tags)")
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client deletes a set of tags")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/delete_tags')


@then("The set of tags should be deleted")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client creates route to define input/output server/tags (POST /create_route)")
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client creates a route")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/create_route')


@then("The route should be created")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client requests a list of routes related to the given server id (POST /get_routes)")
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client requests a list of routes")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/get_routes')


@then("The client should receive a list of routes")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes route with a given ID (POST /delete_route)")
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client deletes a given route")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/delete_route')


@then("The route should be deleted")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client creates a set of derived tags (POST /create_derived_tags)")
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client creates a set of derived tags")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/create_derived_tags')


@then("The set of derived tags should be created")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes a set of derived tags (POST /delete_derived_tags)")
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client deletes a set of derived tags")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/delete_derived_tags')


@then("The set of derived tags should be deleted")
def check_device_stats():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client activates a device with license data (POST /activate_device)")
def test_connect():
    pass


@given("The client is connected to a valid server instance")
def valid_connect():
    assert True


@when("The client activates a device")
def request_device_stats():
    resp = requests.post('http://10.16.51.178:6584/activate_device')


@then("The device should be activated")
def check_device_stats():
    assert (resp.status_code == 200)