class nginx::config::config{
  package { "firefox":
    ensure => installed
  }

  include nginx::config::config1
}


