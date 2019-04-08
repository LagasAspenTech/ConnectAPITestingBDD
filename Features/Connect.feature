Feature: Connect APIs

  Scenario Outline: Client requests a list of Aspen Connect instances (GET /get_devices)
    Given: The client is connected to a valid server instance
    When: The client requests a list of instances
    Then: The client should receive a list of instances
    Examples:
      |  |
  Scenario Outline: Client requests information for currently connected device (GET /get_device_info)
    Given: The client is connected to a valid server instance
    When: The client requests connected device data
    Then: The client should receive connected device data
    Examples:
      |  |
  Scenario Outline: Client requests device stats for currently connected device (GET /get_device_stats)
    Given: The client is connected to a valid server instance
    When: The client requests connected device statistics
    Then: The client should receive connected device statistics
    Examples:
      |  |
  Scenario Outline: Client requests a list of JSon schemas that define protocol plugins for currently connected device (GET /get_schemas)
    Given: The client is connected to a valid server instance
    When: The client requests connected device schemas
    Then: The client should receive connected device schemas
    Examples:
      |  |
  Scenario Outline: Client creates an instance of a protocol plugin as a standalone server (POST /add_server)
    Given: The client is connected to a valid server instance
    When: The client adds a server instance
    Then: A new server instance should be added
    Examples:
      |  |
  Scenario Outline: Client requests a list of all configured, connected servers (GET /get_servers)
    Given: The client is connected to a valid server instance
    When: The client requests a list of servers
    Then: The client should receive a list of servers
    Examples:
      |  |
  Scenario Outline: Client deletes a given server (POST /delete_server)
    Given: The client is connected to a valid server instance
    When: The client deletes a given server
    Then: The server should be deleted
    Examples:
      |  |
  Scenario Outline: Client requests a list of devices (POST /test_connection)
    Given: The client is connected to a valid server instance
    When: The client request a list of devices
    Then: The client should receive a list of devices
    Examples:
      |  |
  Scenario Outline: Client requests a list discovered tags on connected server instance (POST /get_available_tags)
    Given: The client is connected to a valid server instance
    When: The client requests a list of tags
    Then: The client should receive a list of tags
    Examples:
      |  |
  Scenario Outline: Client saves selected tags onto server instance's local storage (POST /activate_tags)
    Given: The client is connected to a valid server instance
    When: The client saves a set of tags
    Then: The set of tags should be saved
    Examples:
      |  |
  Scenario Outline: Client saves selected tags onto server instance's local storage (POST /create_tags)
    Given: The client is connected to a valid server instance
    When: The client creates a set of tags
    Then: The tags should be created
    Examples:
      |  |
  Scenario Outline: Client deletes tags with corresponding IDs (POST /delete_tags)
    Given: The client is connected to a valid server instance
    When: The client deletes a set of tags
    Then: The set of tags should be deleted
    Examples:
      |  |
  Scenario Outline: Client creates route to define input/output server/tags (POST /create_route)
    Given: The client is connected to a valid server instance
    When: The client creates a route
    Then: The route should be created
    Examples:
      |  |
  Scenario Outline: Client requests a list of routes related to the given server id (POST /get_routes)
    Given: The client is connected to a valid server instance
    When: The client requests a list of routes
    Then: The client should receive a list of routes
    Examples:
      |  |
  Scenario Outline: Client deletes route with a given ID (POST /delete_route)
    Given: The client is connected to a valid server instance
    When: The client deletes a given route
    Then: The route should be deleted
    Examples:
      |  |
  Scenario Outline: Client creates a set of derived tags (POST /create_derived_tags)
    Given: The client is connected to a valid server instance
    When: The client creates a set of derived tags
    Then: The set of derived tags should be created
    Examples:
      |  |
  Scenario Outline: Client deletes a set of derived tags (POST /delete_derived_tags)
    Given: The client is connected to a valid server instance
    When: The client deletes a set of derived tags
    Then: The set of derived tags should be deleted
    Examples:
      |  |
  Scenario Outline: Client activates a device with license data (POST /activate_device)
    Given: The client is connected to a valid server instance
    When: The client activates a device
    Then: The device should be activated
    Examples:
      |  |