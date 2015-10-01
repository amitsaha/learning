class nginx::config::config1{
  file { '/etc/nginx/conf.d':
    ensure  => directory,
  }
}


