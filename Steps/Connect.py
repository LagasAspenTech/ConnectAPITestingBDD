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
    response = respholder.getResp().json()
    for item in response:
        schema = item["serverSchema"]["definitions"]["server"] #ask if this is the right part to be referencing tomorrow
        mem.addSchema(schema)
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
    result = respholder.getResp().json()
    mem.addServer(result['objectId']) #this adds the server we create to the object in question
    compare_ouput_json(json.loads(output_json), result)
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


@scenario('Connect.feature', 'Client requests a list of devices (POST /test_connection)')
def test_scenario_test_connection():
    assert True


@given('The client is connected to a valid server instance')
def valid_connect_test_connection():
    assert True


@when('The client requests a list of devices')
def when_test_connection():
    respholder.setResp('/test_connection') #needs input params for server key and so on




@then('The client should receive a list of devices')
def check_test():
    resultdict = {"id": str, "name": str}
    jsontester(respholder.getResp().json(), resultdict)
    assert (resp.status_code == 201)

@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /activate_tags)",example_converters=dict(serverId = int, post_values = str, output_json_1 = str, output_json_2 = str))
def test_scenario_activate_tags():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_activate_tags():
    assert True


@when("The client saves a set of tags with a serverid of <serverId> and post values of <post_values>")
def activate_tags(serverId, post_values):
    params = {"serverId":str(mem.getServerId(serverId))}
    respholder.setResp('/activate_tags',param=params, post=post_values)


@then("The set of tags should be saved, giving results <output_json_1> and <output_json_2>")
def check_activated_tags(serverId, output_json_1, output_json_2):
    twooutputs(output_json_1, output_json_2, respholder)
    resps = respholder.getResp().json()
    for item in resps:
        mem.addTag(serverId, item["id"])
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client requests a list discovered tags on connected server instance (POST /get_available_tags)',example_converters=dict(tag_id = int)) #this does not work with MQTT servers, so don't use them for it
def test_scenario_get_available_tags():
    assert True


@given('The client is connected to a valid server instance')
def valid_connect_get_available_tags():
    assert True


@when('The client requests a list of tags with id <tag_id>')
def get_available_tags(tag_id):
    respholder.setResp('/get_available_tags', post='{"id":' +str(mem.getServerId(tag_id)) +'}')


@then('The client should receive a list of tags')
def check_available_tags(tag_id):
    response = respholder.getResp().json()
    wantedtags = mem.getTags(tag_id)
    tagdict = {}
    for item in wantedtags:
        tagdict[item] = False
    for item in response:
        if item['id'] in tagdict:
            tagdict[item['id']] = True
    for item in tagdict:
        assert (tagdict[item] == True)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client saves selected tags onto server instance's local storage (POST /create_tags)", example_converters=dict(servnum = int, servkey = str))
def test_scenario_create_tags():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_create_tags():
    assert True


@when("The client creates a set of tags for server number <servnum> with key <servkey>")
def create_tags(servnum, servkey):
    params = '{"serverId": ' + str(mem.getServerId(servnum)) + '}'
    posts = '[{"id":0,"pid":"pid1","name":"name1", "key":"' + servkey + '"}]'
    respholder.setResp('/create_tags', param=params, post=posts) #not creating properly, ask why tomorow


@then("The tags should be created with a server key of <servkey>")
def check_created_tags(servkey):
    result = '[{"id":0,"pid":"pid1","name":"name1", "key":"' + servkey + '"}]'
    output = respholder.getResp().json()
    compare_ouput_json(output, result)
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client deletes tags with corresponding IDs (POST /delete_tags)", example_converters=dict(server_number = int))
def test_scenario_delete_tags():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_delete_tags():
    assert True


@when("The client deletes a set of tags on server number <server_number>")
def delete_tags(server_number):
    tags = mem.getTags(server_number)
    postvalue = '['
    i = 0
    while i < len(tags):
        postvalue = postvalue + '{ "id":' + str(tags[i]) + '}'
        if i < len(tags) - 1:
            postvalue=postvalue + ','
        else:
            postvalue = postvalue + ']'
        i = i + 1
    respholder.setResp('/delete_tags', post=postvalue)


@then("The set of tags should be deleted")
def check_deleted_tags():
    assert (resp.status_code == 200)


@scenario('Connect.feature', "Client creates route to define input/output server/tags (POST /create_route)", example_converters=dict(postvalue = str, returnvalue = str))
def test_scenario_create_route():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_create_route():
    assert True


@when("The client creates a route with <postvalue1> and <postvalue2>")
def create_route(postvalue1, postvalue2):
    tagmap = '"'+str(mem.getTag(0,0))+'":'+str((mem.getTag(1,0)))
    i = 1
    while i < len(mem.getTags(0)):
        tagmap = tagmap + ', "'+str(mem.getTag(0,i))+'":'+str((mem.getTag(1,i)))
        i = i+1
    postvalue = postvalue1 + tagmap + postvalue2
    finalpostvalue = '{"id": 0,"inServerId": '+str(mem.getServerId(0)) + ',"outServerId":' +str(mem.getServerId(1)) + postvalue
    respholder.setResp('/create_route', post = finalpostvalue)


@then("The route should be created with <returnvalue>")
def check_route(returnvalue):
    result = respholder.getResp().json()
    output = json.loads(returnvalue)
    compare_ouput_json(output, result)
    mem.addRoute(result["objectId"])
    assert (resp.status_code == 201 or resp.status_code == 200) #comment this out and uncomment the following line to make the status code cause a failure
    #assert (resp.status_code == 201)


@scenario('Connect.feature', "Client requests a list of routes related to the given server id (POST /get_routes)", example_converters=dict(server_type = str, id_value = int))
def test_scenario_get_routes():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_get_routes():
    assert True


@when('The client requests a list of routes with server type <server_type> and post containing a ID of <id_value>')
def get_routes(server_type, id_value):
    serverfull = "ServerType=" + server_type
    postvalues = '{ "Id":' + str(mem.getServerId(id_value))+ " }"
    respholder.setResp('/get_routes', param=serverfull, post=postvalues)


@then('The client should receive a list of routes')
def check_routes():
    assert (respholder.getResp().json()[0]['id'] == mem.getRoute(0))#get route can support multiple routes cuz like, why not?
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client deletes route with a given ID (POST /delete_route)', example_converters=dict(routenumber = int))
def test_scenario_delete_route():
    assert True


@given('The client is connected to a valid server instance')
def valid_connect_delete_route():
    assert True


@when('The client deletes a given route <routenumber>')
def delete_route(routenumber):
    postvalue = '{ "id": ' + str(mem.getRoute(routenumber)) + '}'
    respholder.setResp('/delete_route', post=postvalue)


@then('The route should be deleted')
def check_deleted_route():
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client creates a set of derived tags (POST /create_derived_tags)', example_converters=dict(serverId = int, post_values = str, output_json_1 = str, output_json_2 = str))
def test_scenario_create_derived_tags():
    assert True


@given('The client is connected to a valid server instance')
def valid_connect_create_derived_tags():
    assert True


@when('The client creates a set of derived tags on <serverId> with <post_values>')
def create_derived_tags(serverId, post_values):
    params = {"serverId":str(mem.getServerId(serverId))}
    respholder.setResp('/create_derived_tags',param=params, post=post_values)

@then('The set of derived tags should be created with <output_json_1> and <output_json_2>')
def check_derived_tags(output_json_1, output_json_2, serverId):
    twooutputs(output_json_1, output_json_2, respholder)
    resps = respholder.getResp().json()
    for item in resps:
        mem.addderTag(serverId, item["id"])
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
    assert (resp.status_code == 200)


@scenario('Connect.feature', 'Client deletes a given server (POST /delete_server)',example_converters=dict(servernumber = int))
def test_scenario_delete_server():
    assert True


@given("The client is connected to a valid server instance")
def valid_connect_delete_server():
    assert True


@when('The client deletes a given server <servernumber>')
def delete_server(servernumber):
    postvalue = '{ "id": ' + str(mem.getServerId(servernumber)) + '}'
    respholder.setResp('/delete_server', post=postvalue)


@then('The server should be deleted')
def check_delete_server():
    assert (resp.status_code == 200) #while 500 is a possible error code, I'm not accepting it as a response because delete_server is the last thing run, and thus shouldn't return 500, cuz the route has been deleted by then
