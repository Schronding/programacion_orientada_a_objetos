import numpy as np
import matplotlib.pyplot as plt


class Scene:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        # Definición de la imágen de salida (3 colores)
        self.imagen = np.zeros((self.alto, self.ancho, 3))
        # Inicializar cámara en una posición
        self.camara = np.array([0, 0, 1])
        # Proporción de la imágen
        prop = float(self.ancho / self.alto)
        # Posición de la pantalla (fustrum)
        self.pantalla = (-1, 1 / prop, 1, -1 / prop)  # izquirda, arriba, derecha, abajo

    # Normalizar un vector
    def normalizar(self, vector):
        return vector / np.linalg.norm(vector)

    # Intersección entre un rayo y una esfera
    def intersecionEsfera(self, centro, radio, origen, direccion):
        b = 2 * np.dot(direccion, origen - centro)
        c = np.linalg.norm(origen - centro) * 2 - radio * 2
        delta = b ** 2 - 4 * c
        if delta > 0:
            t1 = (-b + np.sqrt(delta)) / 2
            t2 = (-b - np.sqrt(delta)) / 2
            if t1 > 0 and t2 > 0:
                return min(t1, t2)
        return None

    def intersecionMasCercana(self, objetos, origen, direccion):
        distancias = [self.intersecionEsfera(obj['centro'], obj['radio'], origen, direccion) for obj in objetos]
        objetoCercano = None
        distanciaMin = np.inf
        for indice, distancia in enumerate(distancias):
            if distancia and distancia < distanciaMin:
                distanciaMin = distancia
                objetoCercano = objetos[indice]
        return objetoCercano, distanciaMin

    def reflected(self, vector, axis):
        return vector - 2 * np.dot(vector, axis) * axis

    def renderizarImagen(self, objetos, luz):
        print("Renderizando...")
        self.imagen.fill(0)  # Limpiar la imagen con negro (o cualquier color de fondo)
        
        cont = 0
        for i, y in enumerate(np.linspace(self.pantalla[1], self.pantalla[3], self.alto)):
            for j, x in enumerate(np.linspace(self.pantalla[0], self.pantalla[2], self.ancho)):
                # definir pixel y origen
                pixel = np.array([x, y, 0])
                origen = self.camara
                direccion = self.normalizar(pixel - origen)
                reflexion = 1
                color = np.zeros((3))
                cont += 1
                if (((cont / (self.alto * self.ancho)) * 100) % 5 == 0):
                    print((cont / (self.alto * self.ancho)) * 100, "% completado")
                dir = self.normalizar(pixel - origen)
                objetoMasCercano, distanciaMin = self.intersecionMasCercana(objetos, origen, dir)
                if objetoMasCercano is None:
                    continue
                interseccion = origen + distanciaMin * dir
                normalASuperficie = self.normalizar(interseccion - objetoMasCercano['centro'])
                puntoDesplazado = interseccion + 1e-5 * normalASuperficie
                interseccionConLuz = self.normalizar(luz['posicion'] - puntoDesplazado)
                _, distanciaMin = self.intersecionMasCercana(objetos, puntoDesplazado, interseccionConLuz)
                interseccionConLuzDistancia = np.linalg.norm(luz['posicion'] - interseccion)
                esSombreado = distanciaMin < interseccionConLuzDistancia
                if esSombreado:
                    continue
                iluminacion = np.zeros((3))
                iluminacion += objetoMasCercano['ambient'] * luz['ambient']
                iluminacion += objetoMasCercano['diffuse'] * luz['diffuse'] * np.dot(interseccionConLuz, normalASuperficie)
                interseccionConCam = self.normalizar(self.camara - interseccion)
                H = self.normalizar(interseccionConLuz + interseccionConCam)
                iluminacion += objetoMasCercano['specular'] * luz['specular'] * np.dot(normalASuperficie, H) ** (
                        objetoMasCercano['shininess'] / 4)
                color += reflexion * iluminacion
                reflexion *= objetoMasCercano['reflection']
                origen = puntoDesplazado
                direccion = self.reflected(direccion, normalASuperficie)
                self.imagen[i, j] = np.clip(color, 0, 1)

    def mostrarImg(self):
        plt.imshow(self.imagen)

    def guardarImg(self, nombre):
        plt.imsave(nombre, self.imagen)
        print(f"Imágen {nombre} generada correctamente!")


class Transformaciones:
    def _init_(self):
        pass

    def matriz_traslacion(self, tx, ty, tz):
        # Retorna una matriz de traslación 4x4"""
        return np.array([
            [1, 0, 0, tx],
            [0, 1, 0, ty],
            [0, 0, 1, tz],
            [0, 0, 0, 1]
        ])

    def matriz_rotacion_y(self, angulo):
        # Retorna una matriz de rotación alrededor del eje Y 4x4"""
        cos_ang = np.cos(np.radians(angulo))
        sin_ang = np.sin(np.radians(angulo))
        return np.array([
            [cos_ang, 0, sin_ang, 0],
            [0, 1, 0, 0],
            [-sin_ang, 0, cos_ang, 0],
            [0, 0, 0, 1]
        ])

    def matriz_escalado(self, sx, sy, sz):
        # Retorna una matriz de escalado 4x4"""
        return np.array([
            [sx, 0, 0, 0],
            [0, sy, 0, 0],
            [0, 0, sz, 0],
            [0, 0, 0, 1]
        ])

    def aplicar_transformacion(self, objeto, transformacion):
        # Aplica una transformación a un objeto"""
        centro_homogeneo1 = np.append(objeto['centro'], 1)  # Convertir a coordenadas homogéneas (x, y, z, 1)
        centro_homogeneo = np.transpose(centro_homogeneo1)
        nuevo_centro = np.dot(transformacion, centro_homogeneo)  # Multiplicación de matrices
        objeto['centro'] = nuevo_centro[:3]  # Volver a convertir a coordenadas 3D (x, y, z)

    def traslacion(self, objeto, tx, ty, tz):
        # Aplica una traslación a un objeto"""
        T = self.matriz_traslacion(tx, ty, tz)
        self.aplicar_transformacion(objeto, T)

    def rotacion(self, objeto, angulo):
        # Aplica una rotación a un objeto alrededor del eje Y"""
        R = self.matriz_rotacion_y(angulo)
        self.aplicar_transformacion(objeto, R)

    def escalado(self, objeto, sx, sy, sz):
        # Aplica un escalado a un objeto"""
        S = self.matriz_escalado(sx, sy, sz)
        self.aplicar_transformacion(objeto, S)


def animar_escena(objScene, transformaciones, frames=60):
    objetos = [
        {'centro': np.array([0, -.10, 0]), 'radio': 9000 - 0.7, 'ambient': np.array([0.1, 0.1, 0.1]), 'diffuse': np.array([0.6, 0.6, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5},
        {'centro': np.array([-0.5, 0, -1]), 'radio': 0.7, 'ambient': np.array([0.1, 0, 0]), 'diffuse': np.array([0.7, 0, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5},
        {'centro': np.array([0.1, -0.3, 0]), 'radio': 0.1, 'ambient': np.array([0.1, 0, 0.1]), 'diffuse': np.array([0.7, 0, 0.7]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5},
        {'centro': np.array([-0.3, 0, 0]), 'radio': 0.15, 'ambient': np.array([0, 0.1, 0.1]), 'diffuse': np.array([0, 0.6, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5}
    ]

    luz = {
        'posicion': np.array([5, 5, 5]),
        'ambient': np.array([1, 1, 1]),
        'diffuse': np.array([1, 1, 1]),
        'specular': np.array([1, 1, 1])
    }

    for frame in range(frames):
        print(f"Generando frame {frame + 1}/{frames}")
        # Aplicar rotación a los objetos en cada frame
        transformaciones.traslacion(objetos[1], 0.01, 0, 0)  # Trasladar el objeto[1]
        transformaciones.traslacion(objetos[2], 0.01, 0, 0)  # Trasladar el objeto[2]
        transformaciones.escalado(objetos[3], 1.01, 1.01, 1.01)  # Escalar el objeto[3]
        transformaciones.rotacion(objetos[1], 5)  # Rotar el objeto 1 ligeramente en cada frame
        transformaciones.rotacion(objetos[2], -3)  # Rotar el objeto 2 en dirección contraria



        objScene.renderizarImagen(objetos, luz)
        objScene.mostrarImg()
        objScene.guardarImg(f"frame_{frame}.png")




# Crear la escena y aplicar las transformaciones
ancho, alto = 400, 400
escena = Scene(ancho, alto)
transformaciones = Transformaciones()

# Generar la animación
animar_escena(escena, transformaciones, frames=20)