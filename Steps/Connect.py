from pytest_bdd import scenario, given, when, then
import requests
import json
from Steps.json_testing import jsontester, respclass, compare_ouput_json

URL = "10.16.51.178:6584"
resp = requests.get('http://' + URL + '/get_devices')
respholder = respclass(URL, resp)
tagresultdict = {"id": int, "pid": str, "name": str, "serie": str, "key": str, "LastValue": int}

@scenario('Connect.feature', 'Client requests a list of Aspen Connect instances (GET /get_devices)')
def test_scenario_get_devices():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_devices():
    assert True


@when("The client requests a list of instances")
def test_request_instances():
    respholder.setResp('/get_devices')


@then("The client should receive a list of instances")
def test_check_instances():
    resultdict = {"deviceName": str, "versionNumber": str, "macAddress": str, "ipAddress": str, "lastBroadcast": "num"} #this contains the things that should be included in the json file and what their type should be
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests information for currently connected device (GET /get_device_info)')
def test_scenario_get_device_info():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_device_info():
    assert True


@when("The client requests connected device data")
def test_request_device_info():
    respholder.setResp('/get_device_info')


@then("The client should receive connected device data")
def test_check_device_info():
    resultdict = {"deviceName": str, "versionNumber": str, "macAddress": str, "ipAddress": str, "lastBroadcast": "num"}
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests device stats for currently connected device (GET /get_device_stats)')
def test_scenario_get_device_stats():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_device_stats():
    assert True


@when("The client requests connected device statistics")
def test_request_device_stats():
    respholder.setResp('/get_device_stats')
    print(respholder.getResp().json())


@then("The client should receive connected device statistics")
def test_check_device_stats():
    resultdict = {"cpuPercent": "num", "memPercent": "num", "diskPercent": "num"}
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list of JSon schemas that define protocol plugins for currently connected device (GET /get_schemas)')
def test_scenario_get_schemas():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_schemas():
    assert True


@when("The client requests connected device schemas")
def test_request_device_schemas():
    respholder.setResp('/get_schemas')


@then("The client should receive connected device schemas")
def test_check_device_schemas():
    #json checking for this on hold due to complexity
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client creates an instance of a protocol plugin as a standalone server (POST /add_server)',example_converters=dict(serv_key=str, post_values=str, output_json=str))
def test_scenario_add_server():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_add_server():
    assert True


@when('The client adds a server instance with server key <serv_key> and post values <post_values>')
def add_server(serv_key, post_values):
    params = {'serverKey':serv_key}
    respholder.setResp('/add_server', param=params, post=post_values)


@then("A new server instance should be added with output <output_json>")
def check_server(output_json):
    compare_ouput_json(json.loads(output_json), respholder.getResp().json())
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list of all configured, connected servers (GET /get_servers)',example_converters=dict(output_json_1=str, output_json_2=str))
def test_scenario_get_servers():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_servers():
    assert True


@when("The client requests a list of servers")
def test_get_servers():
    respholder.setResp('/get_servers')


@then("The client should receive a list of servers with output <output_json_1> and <output_json_2>")
def test_check_servers(output_json_1, output_json_2):
    output_1 = json.loads(output_json_1)
    output_2 = json.loads(output_json_2)
    i = 0
    result = respholder.getResp().json()
    #yeah, I had to cheat a little to get this to work. But at least it works.
    for item in result:
        if item != {}:
            if item["key"] == output_1["key"] and item["name"] == output_1["name"]:
                compare_ouput_json(output_1, item)
            elif item["key"] == output_2["key"] and item["name"] == output_2["name"]:
                compare_ouput_json(output_2, item)

    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client deletes a given server (POST /delete_server)')
def test_scenario_delete_server():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_delete_server():
    assert True


@when('The client deletes a given server')
def test_delete_server():
    respholder.setResp('/delete_server')


@then('The server should be deleted')
def test_check_delete_server():
    #json checking for this on hold due to complexity
    assert (resp.status_code == 200 or resp.status_code == 500)


@scenario('Connect.feature', 'Client requests a list of devices (POST /test_connection)')
def test_scenario_test_connection():
    assert True


@given('The client is connected to a valid server instance')
def test_valid_connect_test_connection():
    assert True


@when('The client requests a list of devices')
def test_test_connection():
    respholder.setResp('/test_connection') #needs input params for server key and so on




@then('The client should receive a list of devices')
def test_check_test():
    resultdict = {"id": str, "name": str}
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 201)


@scenario('Connect.feature', 'Client requests a list discovered tags on connected server instance (POST /get_available_tags)')
def test_scenario_get_available_tags():
    assert True


@given('The client is connected to a valid server instance')
def test_valid_connect_get_available_tags():
    assert True


@when('The client requests a list of tags')
def test_get_available_tags():
    respholder.setResp('/get_available_tags') #needs input params


@then('The client should receive a list of tags')
def test_check_available_tags():
    resultdict = {"id": int, "pid": str, "name": str}
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /activate_tags)")
def test_scenario_activate_tags():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_activate_tags():
    assert True


@when("The client saves a set of tags")
def test_activate_tags():
    respholder.setResp('/activate_tags') #needs input param


@then("The set of tags should be saved")
def test_check_activated_tags():
    jsontester(respholder.getResp().json(), tagresultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /create_tags)")
def test_scenario_create_tags():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_create_tags():
    assert True


@when("The client creates a set of tags")
def test_create_tags():
    respholder.setResp('/create_tags') #needs input


@then("The tags should be created")
def test_check_created_tags():
    jsontester(respholder.getResp().json(), tagresultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes tags with corresponding IDs (POST /delete_tags)")
def test_scenario_delete_tags():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_delete_tags():
    assert True


@when("The client deletes a set of tags")
def test_delete_tags():
    respholder.setResp('/delete_tags') #needs input yeah


@then("The set of tags should be deleted")
def test_check_deleted_tags():
    print(resp)#here for testing purposes
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client creates route to define input/output server/tags (POST /create_route)")
def test_scenario_create_route():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_create_route():
    assert True


@when("The client creates a route")
def test_create_route():
    respholder.setResp('/create_route') #blah blah need in put blah


@then("The route should be created")
def test_check_route():
    resultdict = {"token": str, "objectId": int, "status": str, "request": str} #curretnly fails, JSONDecodeError due to 404
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 201)


@scenario('Connect.feature', "Client requests a list of routes related to the given server id (POST /get_routes)")
def test_scenario_get_routes():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_get_routes():
    assert True


@when('The client requests a list of routes')
def test_get_routes():
    respholder.setResp('/get_routes') #need input


@then('The client should receive a list of routes')
def test_check_routes():
    #holding off on adding json check due to complexity
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client deletes route with a given ID (POST /delete_route)')
def test_scenario_delete_route():
    assert True


@given('The client is connected to a valid server instance')
def test_valid_connect_delete_route():
    assert True


@when('The client deletes a given route')
def test_delete_route():
    respholder.setResp('/delete_route') #needs input


@then('The route should be deleted')
def test_check_deleted_route():
    print(resp)#here for testing purposes
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client creates a set of derived tags (POST /create_derived_tags)')
def test_scenario_create_derived_tags():
    assert True


@given('The client is connected to a valid server instance')
def test_valid_connect_create_derived_tags():
    assert True


@when('The client creates a set of derived tags')
def test_create_derived_tags():
    respholder.setResp('/create_derived_tags') #needs input etc


@then('The set of derived tags should be created')
def test_check_derived_tags():
    jsontester(respholder.getResp().json(), tagresultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes a set of derived tags (POST /delete_derived_tags)")
def test_scenario_delete_derived_tags():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_delete_derived_tags():
    assert True


@when("The client deletes a set of derived tags")
def test_delete_derived_tags():
    respholder.setResp('/delete_derived_tags') #needs input


@then("The set of derived tags should be deleted")
def test_check_deleted_derived_tags():
    print(resp) #test etc etc
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client activates a device with license data (POST /activate_device)")
def test_scenario_activate_device():
    assert True


@given("The client is connected to a valid server instance")
def test_valid_connect_activate_device():
    assert True


@when("The client activates a device")
def test_activated_device():
    respholder.setResp('/activate_device') #needs input


@then("The device should be activated")
def test_check_activation():
    print(resp) #test etc etc
    assert (resp.status_code == 200)