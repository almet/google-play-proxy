"""Main entry point
"""
from pyramid.config import Configurator
from pyramid.events import NewRequest
from redis import Redis
from rq import Queue

from gplaycli.gplaycli import GPlaycli


class Client(GPlaycli):
    def __init__(self, config):
        self.config = {
            key.replace('downloader.', '').lower(): value
            for key, value in config.get_settings().items()
            if key.startswith('downloader')
        }
        self.yes = True
        self.verbose = False
        self.progress_bar = False
        self.set_download_folder(self.config['download_folder'])
        success, error = self.connect_to_googleplay_api()
        if not success:
            print "Cannot login to GooglePlay (", error, ")"

    def download_package(self, package_id):
        self.download_packages([package_id])


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.registry.queue = Queue(connection=Redis())
    config.registry.client = Client(config)

    def attach_objects_to_request(event):
        event.request.queue = config.registry.queue
        event.request.client = config.registry.client
    config.add_subscriber(attach_objects_to_request, NewRequest)

    config.include("cornice")
    config.scan("gplayproxy.views")
    return config.make_wsgi_app()
