variable "subscription_id" {
  type        = string
  description = "Azure Subscription ID for the provider"
}

variable "tenant_id" {
  type        = string
  description = "Azure Tenant ID for the provider"
}

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
  type        = string
  default = "sCalc2-Demo-MJ7676"
  description = "Must be globally unique, e.g. s-calc2-demo"
}
