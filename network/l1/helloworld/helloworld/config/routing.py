"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('/{controller}')
    map.connect('/{controller}/{id}')
    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')


    map.connect('map1', '/users',
        controller='users', action='index',
        username='none' )

    map.connect('map1', '/users/:username',
        controller='users', action='index',
        username='none' )

    map.connect('map1', '/testRest/get',
        controller='testRest', action='test3',
        userid='[nobody]' )

    map.connect('map1', '/testRest/put/:userid',
        controller='testRest', action='test3',
        userid='[nobody]' )

    map.connect('map1', '/testRest/post/:userid',
        controller='testRest', action='test3',
        userid='[nobody]' )

    map.connect('map1', '/testRest/delete/:userid',
        controller='testRest', action='test3',
        userid='[nobody]' )

    return map
