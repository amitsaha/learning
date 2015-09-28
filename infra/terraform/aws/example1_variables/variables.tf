variable "access_key" {}
variable "secret_key" {}
variable "region" {
	default = "us-west-2"
}
variable "ami" {
	default = "ami-01122131"
}
variable "instance_type" {
	default = "t1.micro"
}
