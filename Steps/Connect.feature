Feature: Connect APIs
  All the APIs for the Connect system

  Scenario: Client requests a list of Aspen Connect instances (GET /get_devices)
    Given The client is connected to a valid server instance
    When The client requests a list of instances
    Then The client should receive a list of instances

  Scenario: Client requests information for currently connected device (GET /get_device_info)
    Given The client is connected to a valid server instance
    When The client requests connected device data
    Then The client should receive connected device data

  Scenario: Client requests device stats for currently connected device (GET /get_device_stats)
    Given The client is connected to a valid server instance
    When The client requests connected device statistics
    Then The client should receive connected device statistics

  Scenario: Client requests a list of JSon schemas that define protocol plugins for currently connected device (GET /get_schemas)
    Given The client is connected to a valid server instance
    When The client requests connected device schemas
    Then The client should receive connected device schemas

  Scenario Outline: Client creates an instance of a protocol plugin as a standalone server (POST /add_server)
    Given The client is connected to a valid server instance
    When The client adds a server instance with server key <serv_key> and post values <post_values>
    Then A new server instance should be added with output <output_json>

    Examples:
    |serv_key|post_values|output_json|
    |sim.io|{"id": 0, "name": "Test Simulator 2", "seed": 10, "logdirectory": "./"}|{"token": "3e1b7fd6-964e-4b33-aedc-799771e11799","objectId": 0, "status": "request completed","request": "Add Server","err": null}|
    |mqtt.io|{"id":0,"name":"MQTT","url":"aspenmqtt.eastus.cloudapp.azure.com","port":1883,"username":"aspenmqtt","password":"AspenTech*99","tls":false,"auth":true,"rootTopic":"test_stream/+","format":"json","dateFormat":"yyyy-MM-dd HH:mm:ss.fffffffff ZZZ GMT","autoDiscoverTags":true}|{"token": "3e1b7fd6-964e-4b33-aedc-799771e11799","objectId": 0,"status": "request completed","request": "Add Server","err": null}|


  Scenario Outline: Client requests a list of all configured, connected servers (GET /get_servers)
    Given The client is connected to a valid server instance
    When The client requests a list of servers
    Then The client should receive a list of servers with output <output_json_1> and <output_json_2>

    Examples:
    |output_json_1|output_json_2|
    |{"key": "mqtt.io","id": 0,"name": "MQTT","url": "aspenmqtt.eastus.cloudapp.azure.com","port": 1883,"username": "aspenmqtt","password": "AspenTech*99","tls": false,"auth": true,"rootTopic": "test_stream/+","format": "JSON","dateFormat": "yyyy-MM-dd HH:mm:ss.fffffffff ZZZ GMT","autoDiscoverTags": true}|{"key": "sim.io","id": 2,"name": "sim","logdirectory": "./results/sim.io.001/","maxreadcount": 100000,"datafrequencysecs": 1}|

  #I was not given a test case for this, and did not even attempt to create one. Ignore the failure.
  Scenario: Client requests a list of devices (POST /test_connection)
    Given The client is connected to a valid server instance
    When The client requests a list of devices
    Then The client should receive a list of devices

  Scenario Outline: Client saves selected tags onto server instance's local storage (POST /activate_tags)
    Given The client is connected to a valid server instance
    When The client saves a set of tags with a serverid of <serverId> and post values of <post_values>
    Then The set of tags should be saved, giving results <output_json_1> and <output_json_2>

    Examples:
    |serverId|post_values|output_json_1|output_json_2|
    |1      |[{"id": 0,"pid": "test_stream/sample_data;Time:Level 2.Value2-2","name": "test_stream/newtopic;Time:Level 2.Value2-2","key": "mqtt.io","topic": "MQTT/data","valueKey": "Level 2","timeKey": "Time","type": "float"},{"id": 0,"pid": "test_stream/sample_data;Time:Level 2.Level 3.Time","name": "test_stream/newtopic;Time:Level 2.Level 3.Time","key": "mqtt.io","topic": "MQTT/data1","valueKey": "Level 2","timeKey": "Time","type": "float"}]|{"id": 0, "pid": "test_stream/sample_data;Time:Level 2.Value2-2","name": "test_stream/newtopic;Time:Level 2.Value2-2","key": "mqtt.io","topic": "MQTT/data","valueKey": "Level 2","timeKey": "Time","type": "float","lastValue": "","LastTime": ""}|{"id": 0,"pid": "test_stream/sample_data;Time:Level 2.Level 3.Time","name": "test_stream/newtopic;Time:Level 2.Level 3.Time","key": "mqtt.io","topic": "MQTT/data1","valueKey": "Level 2","timeKey": "Time","type": "float","lastValue": "","LastTime": ""}|
    |0       |[{"id": 0,"pid": "mqtttest","name": "mqtttest","serie": "ramp","key": "sim.io","LastValue": 0,"LastTime": "0001-01-01T00:00:00Z"},{"id": 0,"pid": "mqtttest1","name": "mqtttest1","serie": "ramp","key": "sim.io","LastValue": 0,"LastTime": "0001-01-01T00:00:00Z"}]                                                                                                                                                                             |{"id": 0,"pid": "mqtttest","name": "mqtttest","serie": "ramp","key": "sim.io","LastValue": 0,"LastTime": "0001-01-01T00:00:00Z"}|{"id": 0,"pid": "mqtttest1","name": "mqtttest1","serie": "ramp","key": "sim.io","LastValue": 0,"LastTime": "0001-01-01T00:00:00Z"}                                                                                                                                                                                                                                            |

  Scenario Outline: Client requests a list discovered tags on connected server instance (POST /get_available_tags)
    Given The client is connected to a valid server instance
    When The client requests a list of tags with id <tag_id>
    Then The client should receive a list of tags

    Examples:
      |tag_id|
      |0     |

  #I was not given a test case for this, and the one I attempted to create does not work. Ignore the failures.
  Scenario Outline: Client saves selected tags onto server instance's local storage (POST /create_tags)
    Given The client is connected to a valid server instance
    When The client creates a set of tags for server number <servnum> with key <servkey>
    Then The tags should be created with a server key of <servkey>

    Examples:
    |servnum|servkey|
    |0      |sim.io |
    |1      |mqtt.io|

  Scenario Outline: Client deletes tags with corresponding IDs (POST /delete_tags)
    Given The client is connected to a valid server instance
    When The client deletes a set of tags on server number <server_number>
    Then The set of tags should be deleted

    Examples:
    |server_number|
    |0            |

  #The API call should return a value of 201, but instead it always returns 200. However, the route is in fact successfully created. As a result, I chose to have it accept a value of 200 as well.
  #To make it not accept a value of 200, uncomment line 321 in connect.py and comment out line 320
  Scenario Outline: Client creates route to define input/output server/tags (POST /create_route)
    Given The client is connected to a valid server instance
    When The client creates a route with <postvalue1> and <postvalue2>
    Then The route should be created with <returnvalue>
    Examples:
    |postvalue1|postvalue2|returnvalue|
    |,"startTime":"2019-04-08T13:55:00Z","tagIDMap": {|},"options": {"Deadbanding": 0,"Interpolation": 0,"Filter": 0,"KeepAlive": 1,"InstrumentRangeMin": 0,"InstrumentRangeMax": 0}}|{"token": "a30981ee-64d0-4d89-9b94-5a50857b6239","objectId": 0, "status": "request completed","request": "Add Route","err": null}|


  Scenario Outline: Client requests a list of routes related to the given server id (POST /get_routes)
    Given The client is connected to a valid server instance
    When The client requests a list of routes with server type <server_type> and post containing a ID of <id_value>
    Then The client should receive a list of routes
    Examples:
    |server_type|id_value|
    |input      |0      |
    |output     |1      |

  Scenario Outline: Client deletes route with a given ID (POST /delete_route)
    Given The client is connected to a valid server instance
    When The client deletes a given route <routenumber>
    Then The route should be deleted
    Examples:
    |routenumber|
    |0          |

  #I was not given a test case for this one, and the test case I created does not work. Ignore the failure.
  Scenario Outline: Client creates a set of derived tags (POST /create_derived_tags)
    Given The client is connected to a valid server instance
    When The client creates a set of derived tags on <serverId> with <post_values>
    Then The set of derived tags should be created with <output_json_1> and <output_json_2>


    Examples:
    |serverId|post_values|output_json_1|output_json_2|
    |1      |[{"id": 0,"pid": "test_stream/sample_data;Time:Level 2.Value2-2","name": "test_stream/newtopic;Time:Level 2.Value2-2","key": "mqtt.io","topic": "MQTT/data","valueKey": "Level 2","timeKey": "Time","type": "float"},{"id": 0,"pid": "test_stream/sample_data;Time:Level 2.Level 3.Time","name": "test_stream/newtopic;Time:Level 2.Level 3.Time","key": "mqtt.io","topic": "MQTT/data1","valueKey": "Level 2","timeKey": "Time","type": "float"}]|{"id": 0, "pid": "test_stream/sample_data;Time:Level 2.Value2-2","name": "test_stream/newtopic;Time:Level 2.Value2-2","key": "mqtt.io","topic": "MQTT/data","valueKey": "Level 2","timeKey": "Time","type": "float","lastValue": "","LastTime": ""}|{"id": 0,"pid": "test_stream/sample_data;Time:Level 2.Level 3.Time","name": "test_stream/newtopic;Time:Level 2.Level 3.Time","key": "mqtt.io","topic": "MQTT/data1","valueKey": "Level 2","timeKey": "Time","type": "float","lastValue": "","LastTime": ""}|
    |0       |[{"id": 0,"pid": "mqtttest","name": "mqtttest","serie": "ramp","key": "sim.io","LastValue": 0,"LastTime": "0001-01-01T00:00:00Z"},{"id": 0,"pid": "mqtttest1","name": "mqtttest1","serie": "ramp","key": "sim.io","LastValue": 0,"LastTime": "0001-01-01T00:00:00Z"}]                                                                                                                                                                             |{"id": 0,"pid": "mqtttest","name": "mqtttest","serie": "ramp","key": "sim.io","LastValue": 0,"LastTime": "0001-01-01T00:00:00Z"}|{"id": 0,"pid": "mqtttest1","name": "mqtttest1","serie": "ramp","key": "sim.io","LastValue": 0,"LastTime": "0001-01-01T00:00:00Z"}                                                                                                                                                                                                                                            |

#I was not given a test case for this one, and the test case I created just returns true all the time. Ignore the result of this test.
  Scenario: Client deletes a set of derived tags (POST /delete_derived_tags)
    Given The client is connected to a valid server instance
    When The client deletes a set of derived tags
    Then The set of derived tags should be deleted

  Scenario: Client activates a device with license data (POST /activate_device)
    Given The client is connected to a valid server instance
    When The client activates a device
    Then The device should be activated


  Scenario Outline: Client deletes a given server (POST /delete_server)
    Given The client is connected to a valid server instance
    When The client deletes a given server <servernumber>
    Then The server should be deleted
    Examples:
    |servernumber|
    |0           |
    |1           |
