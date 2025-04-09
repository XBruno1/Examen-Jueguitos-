import pygame  # Importar la biblioteca Pygame para gráficos y eventos
import sys

class Lanzador:
    # Diccionario que define los movimientos válidos de cada tecla
    MOVIMIENTOS = {
        1: [6, 8], 2: [7, 9], 3: [4, 8],
        4: [3, 9, 0], 5: [],
        6: [1, 7, 0], 7: [2, 6],
        8: [1, 3], 9: [2, 4],
        0: [4, 6]
    }

    @staticmethod
    def contar_movimientos(posicion, movimientos_restantes):
        """Cuenta los caminos posibles desde una posición con X movimientos restantes."""
        if movimientos_restantes == 0:
            return 1
        return sum(
            Lanzador.contar_movimientos(siguiente, movimientos_restantes - 1)
            for siguiente in Lanzador.MOVIMIENTOS[posicion]
        )

    @staticmethod
    def calcular_movimientos_iniciales(num_movimientos):
        """Calcula el total de caminos posibles desde todas las teclas."""
        return sum(
            Lanzador.contar_movimientos(inicio, num_movimientos - 1)
            for inicio in range(10)
        )

    @staticmethod
    def inicializar_pygame():
        """Inicializa la ventana de Pygame."""
        pygame.init()
        return pygame.display.set_mode((800, 600))

    @staticmethod
    def obtener_datos():
        """Devuelve los colores y las posiciones de las teclas."""
        colores = {
            "WHITE": (255, 255, 255),
            "BLUE": (0, 0, 255),
            "GREEN": (0, 255, 0),
            "BLACK": (0, 0, 0)
        }
        posiciones = {
            1: (200, 100), 2: (300, 100), 3: (400, 100),
            4: (200, 200), 5: (300, 200), 6: (400, 200),
            7: (200, 300), 8: (300, 300), 9: (400, 300),
            0: (300, 400)
        }
        return colores, posiciones

    @staticmethod
    def dibujar_teclas_y_conexiones(pantalla, posiciones, colores):
        """Dibuja las teclas y las conexiones entre ellas."""
        fuente = pygame.font.SysFont(None, 24)
        for tecla, (x, y) in posiciones.items():
            # Círculo de la tecla
            pygame.draw.circle(pantalla, colores["BLUE"], (x, y), 30)

            # Texto centrado
            texto = fuente.render(str(tecla), True, colores["WHITE"])
            pantalla.blit(texto, (x - texto.get_width() // 2, y - texto.get_height() // 2))

            # Líneas hacia las teclas conectadas
            for destino in Lanzador.MOVIMIENTOS[tecla]:
                x2, y2 = posiciones[destino]
                pygame.draw.line(pantalla, colores["GREEN"], (x, y), (x2, y2), 2)

    @staticmethod
    def mostrar_resultados(pantalla, num_movimientos, total, colores):
        """Muestra el resultado en la pantalla."""
        fuente = pygame.font.SysFont(None, 36)
        texto = fuente.render(
            f"Movimientos válidos con {num_movimientos} movimiento(s): {total}",
            True,
            colores["BLACK"]
        )
        pantalla.blit(texto, (50, 500))

    @staticmethod
    def ejecutar_simulacion():
        """Función principal de ejecución del programa."""
        pantalla = Lanzador.inicializar_pygame()
        colores, posiciones = Lanzador.obtener_datos()
        reloj = pygame.time.Clock()
        en_ejecucion = True

        # Cambia este número para probar diferentes cantidades de movimientos
        num_movimientos = 2
        total_movimientos = Lanzador.calcular_movimientos_iniciales(num_movimientos)

        while en_ejecucion:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    en_ejecucion = False

            pantalla.fill(colores["WHITE"])
            Lanzador.dibujar_teclas_y_conexiones(pantalla, posiciones, colores)
            Lanzador.mostrar_resultados(pantalla, num_movimientos, total_movimientos, colores)

            pygame.display.flip()
            reloj.tick(60)

        pygame.quit()
        sys.exit()

# Ejecutar la simulación si se corre el script directamente
if __name__ == "__main__":
    Lanzador.ejecutar_simulacion()
