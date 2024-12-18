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
from datetime import datetime

class Red_social:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, nombre, id_usuario):
        if id_usuario in self.usuarios:
            print("El id ya existe")
        else:
            self.usuarios[id_usuario] = {"nombre": nombre,
                                         "siguiendo": set(),
                                         "seguido": set(),
                                         "posts": {}}

    def seguir_usuario(self, id_usuario, id_seguido):
        if id_usuario not in self.usuarios or id_seguido not in self.usuarios:
            print("usuario no encontrado")
        else:
            self.usuarios[id_usuario]["siguiendo"].add(id_seguido)
            self.usuarios[id_seguido]["seguido"].add(id_usuario)
            print(f'{self.usuarios[id_usuario]["nombre"]} ahora sigue a {self.usuarios[id_seguido]["nombre"]}')

    def dejar_seguir_usuario(self, id_usuario, id_seguido):
        if id_usuario not in self.usuarios or id_seguido not in self.usuarios:
            print("usuario no encontrado")
        else:
            self.usuarios[id_usuario]["siguiendo"].discard(id_seguido)
            self.usuarios[id_seguido]["seguido"].discard(id_usuario)

    def crear_post(self, id_usuario, texto):
        if id_usuario not in self.usuarios:
            print("usuario no encontrado")
            return

        if len(texto) > 200:
            print("El texto supera los 200 caracteres")
            return

        id_post = len(self.usuarios[id_usuario]["posts"]) + 1
        self.usuarios[id_usuario]["posts"][id_post] = {"texto": texto,
                                                       "likes": [],
                                                       "creado_en": datetime.now()}

    def eliminar_post(self, id_usuario, id_post):
        if id_usuario not in self.usuarios:
            print("usuario no encontrado")
            return

        if id_post not in self.usuarios[id_usuario]["posts"]:
            print("post no encontrado")
            return

        del self.usuarios[id_usuario]["posts"][id_post]

    def dar_like(self, id_usuario, id_post):
        if id_usuario not in self.usuarios:
            print("usuario no encontrado")
            return

        if id_post not in self.usuarios[id_usuario]["posts"]:
            print("post no encontrado")
            return

        self.usuarios[id_usuario]["posts"][id_post]["likes"].append(id_usuario)
        print(f'{self.usuarios[id_usuario]["nombre"]} ha dado like al post {id_post}')

    def quitar_like(self, id_usuario, id_post):
        if id_usuario not in self.usuarios:
            print("usuario no encontrado")
            return

        if id_post not in self.usuarios[id_usuario]["posts"]:
            print("post no encontrado")
            return

        self.usuarios[id_usuario]["posts"][id_post]["likes"].remove(id_usuario)
        print(f'{self.usuarios[id_usuario]["nombre"]} ha quitado el like al post {id_post}')

    def feed_usuario(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("usuario no encontrado")
            return

        print(f'Feed de {self.usuarios[id_usuario]["nombre"]}')
        for id_post, post in self.usuarios[id_usuario]["posts"].items():
            print(f'Post {id_post}: {post["texto"]}')
            print(f'Creado en: {post["creado_en"]}')
            print(f'Likes: {len(post["likes"])}')
            print("")

    def feed_seguidos(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("usuario no encontrado")
            return

        print(f'Feed de {self.usuarios[id_usuario]["nombre"]}')
        posts = []
        for id_seguido in self.usuarios[id_usuario]["siguiendo"]:
            for id_post, post in self.usuarios[id_seguido]["posts"].items():
                posts.append((id_post, post))

        posts.sort(key=lambda x: x[1]["creado_en"], reverse=True)
        for id_post, post in posts[:10]:
            print(f'Post {id_post}: {post["texto"]}')
            print(f'Creado en: {post["creado_en"]}')
            print(f'Likes: {len(post["likes"])}')
            print("")

red_social = Red_social()

red_social.registrar_usuario("Juan", 1)
red_social.registrar_usuario("Maria", 2)
red_social.registrar_usuario("Pedro", 3)

red_social.seguir_usuario(1, 2)
red_social.seguir_usuario(1, 3)
red_social.seguir_usuario(2, 3)

red_social.crear_post(1, "Hola, soy Juan")
red_social.crear_post(2, "Hola, soy Maria")
red_social.crear_post(3, "Hola, soy Pedro")

red_social.dar_like(1, 1)
red_social.dar_like(1, 2)
red_social.dar_like(2, 3)

red_social.feed_usuario(1)
red_social.feed_seguidos(1)
red_social.feed_seguidos(2)

red_social.dejar_seguir_usuario(1, 2)
red_social.feed_seguidos(1)