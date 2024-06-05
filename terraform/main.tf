# Define the provider to use Azure Resource Manager (azurerm)

provider "azurerm" {
  features {}
}

# Define a resource group to hold all other resources

resource "azurerm_resource_group" "dani_app" {
  name     = "dani_app_resources" # Name of the resource group
  location = "West Europe"        # Location where resources will be created
}

# Define a PostgreSQL server

resource "azurerm_postgresql_server" "dani_app_db" {
  name                = "daniapppsqlserver"                 # Name of the PostgreSQL server
  location            = azurerm_resource_group.dani_app.location # Location same as the resource group
  resource_group_name = azurerm_resource_group.dani_app.name     # Resource group where the server is located

  administrator_login          = var.db_admin_user       # Admin username for the server
  administrator_login_password = var.db_admin_password   # Admin password for the server

  sku_name   = "B_Gen5_1"   # SKU tier for the PostgreSQL server
  version    = "11"         # PostgreSQL version
  storage_mb = 5120         # Storage size in MB

  backup_retention_days        = 7      # Number of days to retain backups
  geo_redundant_backup_enabled = false  # Disable geo-redundant backups
  auto_grow_enabled            = true   # Enable auto-grow for storage

  public_network_access_enabled    = true                        # Enable public network access
  ssl_enforcement_enabled          = false                       # Disable SSL enforcement
  ssl_minimal_tls_version_enforced = "TLSEnforcementDisabled"    # Disable minimal TLS version enforcement
}

# Define a PostgreSQL database within the server

resource "azurerm_postgresql_database" "dani_app_db" {
  name                = "exampledb"                                    # Name of the database
  resource_group_name = azurerm_resource_group.dani_app.name           # Resource group where the database is located
  server_name         = azurerm_postgresql_server.dani_app_db.name     # Name of the PostgreSQL server
  charset             = "UTF8"                                         # Charset for the database
  collation           = "English_United States.1252"                   # Collation for the database
}

# Define a container group to run the application

resource "azurerm_container_group" "dani_app" {
  name                = "dani_app_containergroup"                      # Name of the container group
  location            = azurerm_resource_group.dani_app.location       # Location same as the resource group
  resource_group_name = azurerm_resource_group.dani_app.name           # Resource group where the container group is located
  os_type             = "Linux"                                        # OS type for the container
  dns_name_label      = "daniappcontainergroup"                        # DNS name for the container group
  ip_address_type     = "Public"                                       # IP address type for the container group

  container {
    name   = "daniappcontainer"     # Name of the container
    image  = "dpicatto/dani_app:latest"   # Docker image to use for the container
    cpu    = "0.5"                  # CPU allocation for the container
    memory = "1.5"                  # Memory allocation for the container

    ports {
      port     = 5000                # Port to expose
      protocol = "TCP"               # Protocol to use for the port
    }

    environment_variables = {        # Environment variables for the container
      DB_NAME     = "exampledb"                           # Database name
      DB_USER     = "${var.db_admin_user}@daniapppsqlserver"  # Database user
      DB_PASSWORD = var.db_admin_password                 # Database password
      DB_HOST     = "daniapppsqlserver.postgres.database.azure.com" # Database host
      DB_PORT     = "5432"                                # Database port
    }
  }

  tags = {
    environment = "testing"          # Tag to specify the environment
  }
}
