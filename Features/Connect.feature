Feature: Connect APIs

  Scenario Outline: Client requests a list of Aspen Connect instances (GET /get_devices)
    Given: The client is connected to a valid server instance
    When: The client requests a list of instances
    Then: The client should receive a list of instances
    Examples:
      |  |
  Scenario Outline: Client requests information for currently connected device (GET /get_device_info)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client requests device stats for currently connected device (GET /get_device_stats)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client requests a list of JSon schemas that define protocol plugins for currently connected device (GET /get_schemas)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client creates an instance of a protocol plugin as a standalone server (POST /add_server)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client requests a list of all configured, connected servers (GET /get_servers)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client deletes a given server (POST /delete_server)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client requests a list of devices (POST /test_connection)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client requests a list discovered tags on connected server instance (POST /get_available_tags)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client saves selected tags onto server instance's local storage (POST /activate_tags)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client saves selected tags onto server instance's local storage (POST /create_tags)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client deletes tags with corresponding IDs (POST /delete_tags)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client creates route to define input/output server/tags (POST /create_route)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client requests a list of routes related to the given server id (POST /get_routes)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client deletes route with a given ID (POST /delete_route)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client creates a set of derived tags (POST /create_derived_tags)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client creates a set of derived tags (POST /delete_derived_tags)
    Given:
    When:
    Then:
    Examples:
      |  |
  Scenario Outline: Client activates a device with license data (POST /activate_device)
    Given:
    When:
    Then:
    Examples:
      |  |