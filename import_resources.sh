#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Import the resource group
terraform import azurerm_resource_group.dani_app /subscriptions/${ARM_SUBSCRIPTION_ID}/resourceGroups/dani_app_resources || true

# Import the PostgreSQL server
terraform import azurerm_postgresql_server.dani_app_db /subscriptions/${ARM_SUBSCRIPTION_ID}/resourceGroups/dani_app_resources/providers/Microsoft.DBforPostgreSQL/servers/daniapppsqlserver || true

# Import the PostgreSQL database
terraform import azurerm_postgresql_database.dani_app_db /subscriptions/${ARM_SUBSCRIPTION_ID}/resourceGroups/dani_app_resources/providers/Microsoft.DBforPostgreSQL/servers/daniapppsqlserver/databases/exampledb || true

# Import the container group
terraform import azurerm_container_group.dani_app /subscriptions/${ARM_SUBSCRIPTION_ID}/resourceGroups/dani_app_resources/providers/Microsoft.ContainerInstance/containerGroups/dani_app_containergroup || true
