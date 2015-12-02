""" Cornice services.
"""
from cornice import Service

package = Service(name='package', path='/package/{package_id}')


@package.post()
def get_info(request):
    """Returns Hello in JSON."""
    package_id = request.matchdict['package_id']
    request.queue.enqueue(request.client.download_package, package_id)
    request.response.status_code = 201
    return {'success': True}
