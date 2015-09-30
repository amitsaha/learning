# Nginx configuration for rest_app

class nginx {
  package { "nginx":
    ensure => installed
  }

  file { '/etc/nginx/':
    ensure  => 'directory',
    source  => 'puppet:///modules/nginx/nginx/',
    recurse => true,
    purge   => true,
    force   => true,
  }

  file { '/etc/nginx/sites-enabled/freelancer.com.conf':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/freelancer.com.conf',
    require => File['/etc/nginx'],
  }

  include nginx::config::config
}
