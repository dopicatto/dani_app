variable "db_admin_user" {
  description = "The administrator username for the PostgreSQL server"
  type        = string
}

variable "db_admin_password" {
  description = "The administrator password for the PostgreSQL server"
  type        = string
  sensitive   = true
}
    