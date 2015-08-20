class emacsd_init_el {
    file { '/home/asaha/.emacs.d/init.el':
        ensure     => 'present',
        source => 'puppet:///modules/emacsd_init_el/emacsd_init_el'
    }
}
