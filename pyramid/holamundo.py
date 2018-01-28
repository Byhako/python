from paste.httpserver import serve
from pyramid.config import Configurator
from pyramid.response import Response

def helo_world(request):
	return Response('Hola mundo.')

if __name__ == "__main__":
	config = Configurator()
	config.add_view(helo_world)
	app = config.make_wsgi_app()
	serve(app, host='0.0.0.0')
