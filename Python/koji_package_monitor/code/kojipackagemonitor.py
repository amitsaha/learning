import fedmsg.consumers

class KojiPackageMonitor(fedmsg.consumers.FedmsgConsumer):
    topic = 'org.fedoraproject.prod.buildsys.build.state.change'
    # http://fedmsg2.readthedocs.org/en/latest/topics.html#buildsys
    config_key = 'kojipackagemonitor'

    def __init__(self, *args, **kw):
        super(KojiPackageMonitor, self).__init__(*args, **kw)

    def consume(self, msg):
        new_state = msg['body']['msg']['new']
        # care only about completed packages
        if new_state == 3:
            name = msg['body']['msg']['name']
            version = msg['body']['msg']['version']
            release = msg['body']['msg']['release']
            instance = msg['body']['msg']['instance']

            print name, version, release,  instance

            

        
        
