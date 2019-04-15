Feature: Connect APIs
  All the APIs for the Connect system

  Scenario: Client requests a list of Aspen Connect instances (GET /get_devices)
    Given: The client is connected to a valid server instance
    When: The client requests a list of instances
    Then: The client should receive a list of instances

  Scenario: Client requests information for currently connected device (GET /get_device_info)
    Given: The client is connected to a valid server instance
    When: The client requests connected device data
    Then: The client should receive connected device data

  Scenario: Client requests device stats for currently connected device (GET /get_device_stats)
    Given: The client is connected to a valid server instance
    When: The client requests connected device statistics
    Then: The client should receive connected device statistics

  Scenario: Client requests a list of JSon schemas that define protocol plugins for currently connected device (GET /get_schemas)
    Given: The client is connected to a valid server instance
    When: The client requests connected device schemas
    Then: The client should receive connected device schemas

  Scenario Outline: Client creates an instance of a protocol plugin as a standalone server (POST /add_server)
    Given The client is connected to a valid server instance
    When The client adds a server instance with server key <serv_key> and post values <post_values>
    Then A new server instance should be added with output <output_json>

    Examples:
    |serv_key|post_values|output_json|
    |sim.io|{"id": 0, "name": "Test Simulator 2", "seed": 10, "logdirectory": "./"}|{"token": "3e1b7fd6-964e-4b33-aedc-799771e11799","objectId": 0, "status": "request completed","request": "Add Server","err": null}|
    |mqtt.io|{"id":0,"name":"MQTT","url":"aspenmqtt.eastus.cloudapp.azure.com","port":1883,"username":"aspenmqtt","password":"AspenTech*99","tls":false,"auth":true,"rootTopic":"test_stream/+","format":"json","dateFormat":"yyyy-MM-dd HH:mm:ss.fffffffff ZZZ GMT","autoDiscoverTags":true}|{"token": "3e1b7fd6-964e-4b33-aedc-799771e11799","objectId": 3,"status": "request completed","request": "Add Server","err": null}|


  Scenario: Client requests a list of all configured, connected servers (GET /get_servers)
    Given: The client is connected to a valid server instance
    When: The client requests a list of servers
    Then: The client should receive a list of servers

  Scenario: Client deletes a given server (POST /delete_server)
    Given: The client is connected to a valid server instance
    When: The client deletes a given server
    Then: The server should be deleted

  Scenario: Client requests a list of devices (POST /test_connection)
    Given: The client is connected to a valid server instance
    When: The client request a list of devices
    Then: The client should receive a list of devices

  Scenario: Client requests a list discovered tags on connected server instance (POST /get_available_tags)
    Given: The client is connected to a valid server instance
    When: The client requests a list of tags
    Then: The client should receive a list of tags

  Scenario: Client saves selected tags onto server instance's local storage (POST /activate_tags)
    Given: The client is connected to a valid server instance
    When: The client saves a set of tags
    Then: The set of tags should be saved

  Scenario: Client saves selected tags onto server instance's local storage (POST /create_tags)
    Given: The client is connected to a valid server instance
    When: The client creates a set of tags
    Then: The tags should be created

  Scenario: Client deletes tags with corresponding IDs (POST /delete_tags)
    Given: The client is connected to a valid server instance
    When: The client deletes a set of tags
    Then: The set of tags should be deleted

  Scenario: Client creates route to define input/output server/tags (POST /create_route)
    Given: The client is connected to a valid server instance
    When: The client creates a route
    Then: The route should be created

  Scenario: Client requests a list of routes related to the given server id (POST /get_routes)
    Given: The client is connected to a valid server instance
    When: The client requests a list of routes
    Then: The client should receive a list of routes

  Scenario: Client deletes route with a given ID (POST /delete_route)
    Given: The client is connected to a valid server instance
    When: The client deletes a given route
    Then: The route should be deleted

  Scenario: Client creates a set of derived tags (POST /create_derived_tags)
    Given: The client is connected to a valid server instance
    When: The client creates a set of derived tags
    Then: The set of derived tags should be created

  Scenario: Client deletes a set of derived tags (POST /delete_derived_tags)
    Given: The client is connected to a valid server instance
    When: The client deletes a set of derived tags
    Then: The set of derived tags should be deleted

  Scenario: Client activates a device with license data (POST /activate_device)
    Given: The client is connected to a valid server instance
    When: The client activates a device
    Then: The device should be activated