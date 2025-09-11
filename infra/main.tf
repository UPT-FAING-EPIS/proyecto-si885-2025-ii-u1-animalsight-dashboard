provider "azurerm" {
  features {}
}

# Resource Group para la base de datos
resource "azurerm_resource_group" "rg_db" {
  name     = "rg-infracost-db"
  location = var.location
}

# Servidor MySQL Flexible
resource "azurerm_mysql_flexible_server" "mysql" {
  name                   = "mysql-infracost-db"
  resource_group_name    = azurerm_resource_group.rg_db.name
  location               = azurerm_resource_group.rg_db.location
  administrator_login    = var.db_username
  administrator_password = var.db_password
  sku_name               = "B_Standard_B1ms"
  version                = "8.0.21"

  storage {
    size_gb = var.storage_gb
  }
}
