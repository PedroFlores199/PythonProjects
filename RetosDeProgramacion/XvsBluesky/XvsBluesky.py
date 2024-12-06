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

