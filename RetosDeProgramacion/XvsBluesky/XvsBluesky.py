"""
EJERCICIO:
La alternativa descentralizada a X, Bluesky, comienza a atraer
a nuevos usuarios. ¿Cómo funciona una red de este estilo?

Implementa un sistema que simule el comportamiento de estas
redes sociales.

Debes crear las siguientes operaciones:
- Registrar un usuario por nombre e identificador único.
- Un usuario puede seguir/dejar de seguir a otro.
- Creación de post asociado a un usuario. Debe poseer
  texto (200 caracteres máximo), fecha de creación
  e identificador único.
- Eliminación de un post.
- Posibilidad de hacer like (y eliminarlo) en un post.
- Visualización del feed de un usuario con sus 10 publicaciones
  más actuales ordenadas desde la más reciente.
- Visualización del feed de un usuario con las 10 publicaciones
  más actuales de los usuarios que sigue ordenadas
  desde la más reciente.

Cuando se visualiza un post, debe mostrarse:
ID de usuario, nombre de usuario, texto del post,
fecha de creación y número total de likes.

Controla errores en duplicados o acciones no permitidas.
"""

class red_social:
    def __init__(self):
        self.usuarios = {}
    def registrar_usuario(self, nombre, id):
        if id in self.usuarios:
            print("El id ya existe")
        else:
            self.usuarios[id] = {"nombre": nombre, "siguiendo": set(), "seguido": set(), "posts": {}}

    def seguir_usuario(self, id, id_seguir):
        if id not in self.usuarios or id_seguir not in self.usuarios:
            print("El id no existe")
        else:
            self.usuarios[id]["siguiendo"].add(id_seguir)
            self.usuarios[id_seguir]["seguido"].add(id)

    def dejar_seguir_usuario(self, id, id_seguir):
        if id not in self.usuarios or id_seguir not in self.usuarios:
            print("El id no existe")
        else:
            self.usuarios[id]["siguiendo"].remove(id_seguir)
            self.usuarios[id_seguir]["seguido"].remove(id)

    def crear_post(self, id, texto, id_post):


