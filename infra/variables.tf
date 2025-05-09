// infra/variables.tf
variable "subscription_id" {
  description = "Azure subscription ID"
}
variable "tenant_id" {
  description = "Azure tenant ID"
}
variable "resource_group_name" {
  description = "Name of the resource group"
}
variable "location" {
  description = "Region (e.g. westus2)"
}
variable "app_service_plan_name" {
  description = "Name for the App Service Plan"
}
variable "webapp_name" {
  description = "Name for the Web App"
}
