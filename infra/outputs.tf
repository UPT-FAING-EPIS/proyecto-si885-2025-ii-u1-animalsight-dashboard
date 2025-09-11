output "resource_group_db_name" {
  description = "Nombre del grupo de recursos para la base de datos"
  value       = azurerm_resource_group.rg_db.name
}

output "mysql_fqdn" {
  description = "Nombre DNS completo del servidor MySQL Flexible Server"
  value       = azurerm_mysql_flexible_server.mysql.fqdn
}

output "mysql_location" {
  description = "Región donde se desplegó el servidor MySQL"
  value       = azurerm_mysql_flexible_server.mysql.location
}

output "mysql_storage_gb" {
  description = "Almacenamiento asignado en GB"
  value       = var.storage_gb
}
