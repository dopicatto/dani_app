# Define a variable for the PostgreSQL admin username

variable "db_admin_user" {
  description = "The administrator username for the PostgreSQL server" # Description of the variable
  type        = string  # The type of the variable, which is a string
}

# Define a variable for the PostgreSQL admin password

variable "db_admin_password" {
  description = "The administrator password for the PostgreSQL server" # Description of the variable
  type        = string  # The type of the variable, which is a string
  sensitive   = true    # Mark the variable as sensitive to prevent it from being displayed in logs
}
