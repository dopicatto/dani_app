provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "dani_app" {
  name     = "dani_app-resources"
  location = "West Europe"
}

resource "azurerm_postgresql_server" "dani_app_db" {
  name                = "dani_app-psqlserver"
  location            = azurerm_resource_group.dani_app.location
  resource_group_name = azurerm_resource_group.dani_app.name

  administrator_login          = "psqladmin"
  administrator_login_password = "admin1"

  sku_name   = "B_Gen5_1"
  version    = "11"
  storage_mb = 5120

  backup_retention_days        = 7
  geo_redundant_backup_enabled = false
  auto_grow_enabled            = true

  public_network_access_enabled = true
  ssl_enforcement_enabled       = true  # Aquí se incluye el argumento obligatorio
}

resource "azurerm_postgresql_database" "dani_app_db" {
  name                = "exampledb"
  resource_group_name = azurerm_resource_group.dani_app.name
  server_name         = azurerm_postgresql_server.dani_app_db.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}

resource "azurerm_container_group" "dani_app" {
  name                = "dani_app-containergroup"
  location            = azurerm_resource_group.dani_app.location
  resource_group_name = azurerm_resource_group.dani_app.name
  os_type             = "Linux"

  container {
    name   = "dani_app-container"
    image  = "dpicatto/dani_app:latest"
    cpu    = "0.5"
    memory = "1.5"

    ports {
      port     = 5000
      protocol = "TCP"
    }

    environment_variables = {
      DATABASE_URL = "postgresql://psqladmin:admin1@${azurerm_postgresql_server.dani_app_db.fqdn}:5432/exampledb"
    }
  }

  ip_address {
    type            = "public"
    ports {
      port     = 5000
      protocol = "TCP"
    }
  }
}
