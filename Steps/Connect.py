from pytest_bdd import scenario, given, when, then
import requests
import json
from Steps.json_testing import jsontester, respclass, compare_ouput_json, twooutputs, memoryclass

URL = "10.16.51.178:6584"
resp = requests.get('http://' + URL + '/get_devices')
respholder = respclass(URL, resp)
mem = memoryclass()
tagresultdict = {"id": int, "pid": str, "name": str, "serie": str, "key": str, "LastValue": int}

@scenario('Connect.feature', 'Client requests a list of Aspen Connect instances (GET /get_devices)')
def test_scenario_get_devices():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_get_devices():
    assert True


@when("The client requests a list of instances")
def request_instances():
    respholder.setResp('/get_devices')


@then("The client should receive a list of instances")
def check_instances():
    resultdict = {"deviceName": str, "versionNumber": str, "macAddress": str, "ipAddress": str, "lastBroadcast": "num"} #this contains the things that should be included in the json file and what their type should be
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests information for currently connected device (GET /get_device_info)')
def test_scenario_get_device_info():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_get_device_info():
    assert True


@when("The client requests connected device data")
def request_device_info():
    respholder.setResp('/get_device_info')


@then("The client should receive connected device data")
def check_device_info():
    resultdict = {"deviceName": str, "versionNumber": str, "macAddress": str, "ipAddress": str, "lastBroadcast": "num"}
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests device stats for currently connected device (GET /get_device_stats)')
def test_scenario_get_device_stats():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_get_device_stats():
    assert True


@when("The client requests connected device statistics")
def request_device_stats():
    respholder.setResp('/get_device_stats')
    print(respholder.getResp().json())


@then("The client should receive connected device statistics")
def check_device_stats():
    resultdict = {"cpuPercent": "num", "memPercent": "num", "diskPercent": "num"}
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list of JSon schemas that define protocol plugins for currently connected device (GET /get_schemas)')
def test_scenario_get_schemas():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_get_schemas():
    assert True


@when("The client requests connected device schemas")
def request_device_schemas():
    respholder.setResp('/get_schemas')


@then("The client should receive connected device schemas")
def check_device_schemas():
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
def valid_connect_get_servers():
    assert True


@when("The client requests a list of servers")
def get_servers():
    respholder.setResp('/get_servers')


@then("The client should receive a list of servers with output <output_json_1> and <output_json_2>")
def check_servers(output_json_1, output_json_2):
    twooutputs(output_json_1, output_json_2, respholder)
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client deletes a given server (POST /delete_server)')
def test_scenario_delete_server():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_delete_server():
    assert True


@when('The client deletes a given server')
def delete_server():
    respholder.setResp('/delete_server')


@then('The server should be deleted')
def check_delete_server():
    #json checking for this on hold due to complexity
    assert (resp.status_code == 200 or resp.status_code == 500)


@scenario('Connect.feature', 'Client requests a list of devices (POST /test_connection)')
def test_scenario_test_connection():
    assert True


@given('The client is connected to a valid server instance')
def valid_connect_test_connection():
    assert True


@when('The client requests a list of devices')
def test_connection():
    respholder.setResp('/test_connection') #needs input params for server key and so on




@then('The client should receive a list of devices')
def check_test():
    resultdict = {"id": str, "name": str}
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 201)


@scenario('Connect.feature', 'Client requests a list discovered tags on connected server instance (POST /get_available_tags)',example_converters=dict(tag_id = str))
def test_scenario_get_available_tags():
    assert True


@given('The client is connected to a valid server instance')
def valid_connect_get_available_tags():
    assert True


@when('The client requests a list of tags with id <tag_id>')
def get_available_tags(tag_id):
    respholder.setResp('/get_available_tags', post='{"id":' +tag_id +'}')


@then('The client should receive a list of tags')
def check_available_tags():
    assert(len(respholder.getResp().json())>1)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /activate_tags)",example_converters=dict(serverId = str, post_values = str, output_json_1 = str, output_json_2 = str))
def test_scenario_activate_tags():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_activate_tags():
    assert True


@when("The client saves a set of tags with a serverid of <serverId> and post values of <post_values>")
def activate_tags(serverId, post_values):
    params = {"serverId":serverId}
    respholder.setResp('/activate_tags',param=params, post=post_values)


@then("The set of tags should be saved, giving results <output_json_1> and <output_json_2>")
def check_activated_tags(output_json_1, output_json_2):
    twooutputs(output_json_1, output_json_2, respholder)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /create_tags)")
def test_scenario_create_tags():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_create_tags():
    assert True


@when("The client creates a set of tags")
def create_tags():
    respholder.setResp('/create_tags') #needs input


@then("The tags should be created")
def check_created_tags():
    jsontester(respholder.getResp().json(), tagresultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes tags with corresponding IDs (POST /delete_tags)")
def test_scenario_delete_tags():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_delete_tags():
    assert True


@when("The client deletes a set of tags")
def delete_tags():
    respholder.setResp('/delete_tags') #needs input yeah


@then("The set of tags should be deleted")
def check_deleted_tags():
    print(resp)#here for testing purposes
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client creates route to define input/output server/tags (POST /create_route)", example_converters=dict(postvalue = str, returnvalue = str))
def test_scenario_create_route():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_create_route():
    assert True


@when("The client creates a route with <postvalue>")
def create_route(postvalue):
    respholder.setResp('/create_route', post = postvalue) #blah blah need in put blah


@then("The route should be created with <returnvalue>")
def check_route(returnvalue):
    print(respholder.getResp().text)
    result = respholder.getResp().json()
    output = json.loads(returnvalue)
    compare_ouput_json(output, result)
    assert (resp.status_code == 201)


@scenario('Connect.feature', "Client requests a list of routes related to the given server id (POST /get_routes)", example_converters=dict(server_type = str, id_value = str))
def test_scenario_get_routes():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_get_routes():
    assert True


@when('The client requests a list of routes with server type <server_type> and post containing a ID of <id_value>')
def get_routes(server_type, id_value):
    serverfull = "ServerType=" + server_type
    postvalues = '{ "Id":' + id_value+ " }"
    respholder.setResp('/get_routes', param=serverfull, post=postvalues)


@then('The client should receive a list of routes')
def check_routes():
    assert (isinstance(respholder.getResp().json(), list)) #no test was provided so I did this, probably not the best but I'm not sure what else to do.
    #holding off on adding json check due to complexity
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client deletes route with a given ID (POST /delete_route)')
def test_scenario_delete_route():
    assert True


@given('The client is connected to a valid server instance')
def valid_connect_delete_route():
    assert True


@when('The client deletes a given route')
def delete_route():
    respholder.setResp('/delete_route') #needs input


@then('The route should be deleted')
def check_deleted_route():
    print(resp)#here for testing purposes
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client creates a set of derived tags (POST /create_derived_tags)')
def test_scenario_create_derived_tags():
    assert True


@given('The client is connected to a valid server instance')
def valid_connect_create_derived_tags():
    assert True


@when('The client creates a set of derived tags')
def create_derived_tags():
    respholder.setResp('/create_derived_tags') #needs input etc


@then('The set of derived tags should be created')
def check_derived_tags():
    jsontester(respholder.getResp().json(), tagresultdict)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes a set of derived tags (POST /delete_derived_tags)")
def test_scenario_delete_derived_tags():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_delete_derived_tags():
    assert True


@when("The client deletes a set of derived tags")
def delete_derived_tags():
    respholder.setResp('/delete_derived_tags') #needs input


@then("The set of derived tags should be deleted")
def check_deleted_derived_tags():
    print(resp) #test etc etc
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client activates a device with license data (POST /activate_device)")
def test_scenario_activate_device():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_activate_device():
    assert True


@when("The client activates a device")
def activated_device():
    respholder.setResp('/activate_device') #needs input


@then("The device should be activated")
def check_activation():
    print(resp) #test etc etc
    assert (resp.status_code == 200)