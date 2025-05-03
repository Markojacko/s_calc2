variable "resource_group_name" {
  type    = string
  default = "sCalc2-rg"
}

variable "location" {
  type    = string
  default = "westeurope"
}

variable "app_service_plan_name" {
  type    = string
  default = "sCalc2-plan"
}

variable "webapp_name" {
  type = string
  description = "Must be globally unique, e.g. s-calc2-demo"
}
