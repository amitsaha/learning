class nginx::config::config{
  
  file { '/etc/nginx/nginx.conf':
    ensure  => present,
  }
  include nginx::config::config1
}


