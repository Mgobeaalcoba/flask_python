from flask_testing import TestCase
from flask import current_app, url_for

from main import app

class MainTest(TestCase):
    # Sobre escribo metodo de TestCase para crear instancia de la app que vo ya testear:
    def create_app(self):
        app.config['TESTING'] = True
        # Desactivamos el validador de formularios:
        app.config['WTF_CSRF_ENABLED'] = False
        return app
    
    # Primer prueba (Verifica si hay una instancia de nuestro proyecto activo)
    def test_app_exists(self):
        self.assertIsNotNone(current_app)

    # Segunda prueba (Verifica que la app esté en ambiente de testing)
    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    # Tercera prueba (Verifica que nuestro index redirija a Hello)
    def test_index_redirect(self):
        response = self.client.get(url_for('index'))

        # ¿Es cierto que la response a mi request get redirije a Hello? 
        self.assertEqual(response.location, '/hello')

    # Cuarta prueba (Probar que hello nos regresa status code 200 al hacer GET)
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))

        self.assert200(response)

    # Quinta prueba (Probar que hello funcione bien al hacer un post):
    def test_hello_post(self):
        fake_user = {
            "username":"Mariano Gobea Alcoba",
            "password": "lalala1234"
        }
        response = self.client.post(url_for('hello'), data=fake_user)

        # ¿Luego del post me redirige al index mi route "hello"?
        self.assertEqual(response.location, '/')