
class nginx {
  package { "nginx":
    ensure => installed
  }

  include nginx::config::config
}
