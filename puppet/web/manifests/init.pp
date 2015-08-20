class web ($page_name, $message){
    $doc_root = '/var/www/html/questguide/'
    $english = 'Hello World'
    $french = 'Bonjour le monde!'

    file { "${doc_root}hello.html":
         ensure      => 'present',
         content => "<em>${english}</em>",
         }
    file { "${doc_root}bonjour.html":
         ensure      => 'present',
         content => "<em>${french}</em>",
         }

    file { "${doc_root}${page_name}.html":
        ensure  => 'present',
        content => "<em>${message}</em>",
}
}
