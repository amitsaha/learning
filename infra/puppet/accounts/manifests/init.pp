class accounts ($user_name) {

  if  $::operatingsystem == 'centos' {
    $groups = 'wheel'
  }
  elsif $::operatingsystem == 'debian' {
    $groups = 'admin'
  }
  else {
    fail("This module doesn't support ${::operatingsystem}.")
  }
  notice("Groups for user ${user_name} set to ${groups}")

  user { $user_name:
    ensure => 'present',
    home   => "/home/${user_name}",
    groups => $groups,
  }
}
