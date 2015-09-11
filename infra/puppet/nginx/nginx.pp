class  {'nginx': }

$header_size = '4 16k'
nginx::resource::vhost { 'www.myhost2.com':
    listen_port          => 80,
    client_max_body_size => '15k',
    vhost_cfg_prepend => {'large_client_header_buffers' => $header_size},
    index_files          => [],
    format_log           => 'forwarded_logs',
    location_custom_cfg  => {
      'include'           => 'uwsgi_params',
    }
}

