import sys
import pygame

class NQueens:
    """Clase para resolver y visualizar el problema de las N-Reinas."""
    
    def __init__(self, n):
        if not isinstance(n, int) or n < 1:
            raise ValueError("N debe ser un entero positivo")
        self.n = n
        self.solutions = []

    def is_valid(self, board, row, col):
        """Verifica si es seguro colocar una reina en la posición."""
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(self, row=0, board=None):
        """Encuentra todas las soluciones al problema."""
        if board is None:
            board = [-1] * self.n

        if row == self.n:
            self.solutions.append(board[:])
            return

        for col in range(self.n):
            if self.is_valid(board, row, col):
                board[row] = col
                self.solve(row + 1, board)
                board[row] = -1

    def get_solutions(self):
        """Obtiene todas las soluciones posibles."""
        self.solutions.clear()
        self.solve()
        return self.solutions

    def setup_pygame(self):
        """Configura la ventana de Pygame."""
        pygame.init()
        size = min(800, max(400, self.n * 100))  # Tamaño dinámico
        screen = pygame.display.set_mode((size, size + 50))  # +50 para info
        pygame.display.set_caption(f"N-Reinas (N={self.n})")
        return screen

    def get_colors(self):
        """Define los colores de la visualización."""
        return {
            "WHITE": (255, 255, 255),
            "BLACK": (0, 0, 0),
            "BLUE": (0, 0, 255),
            "RED": (255, 0, 0),
            "GRAY": (150, 150, 150)
        }

    def draw_board(self, screen, colors, solution, current_solution, total_solutions):
        """Dibuja el tablero y la información."""
        cell_size = screen.get_width() // self.n
        # Dibujar tablero
        for row in range(self.n):
            for col in range(self.n):
                color = colors["WHITE"] if (row + col) % 2 == 0 else colors["GRAY"]
                pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
                
                if solution[row] == col:
                    pygame.draw.circle(screen, colors["RED"],
                                     (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2),
                                     cell_size // 3)

        # Dibujar información
        font = pygame.font.Font(None, 36)
        text = font.render(f"Solución {current_solution + 1}/{total_solutions}", True, colors["BLACK"])
        screen.blit(text, (10, screen.get_height() - 40))

    def run_visualization(self):
        """Ejecuta la visualización interactiva."""
        solutions = self.get_solutions()
        if not solutions:
            print(f"No hay soluciones para N={self.n}")
            return

        screen = self.setup_pygame()
        colors = self.get_colors()
        clock = pygame.time.Clock()
        current_solution = 0
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        current_solution = (current_solution + 1) % len(solutions)
                    elif event.key == pygame.K_LEFT:
                        current_solution = (current_solution - 1) % len(solutions)
                    elif event.key == pygame.K_ESCAPE:
                        running = False

            screen.fill(colors["WHITE"])
            self.draw_board(screen, colors, solutions[current_solution], 
                          current_solution, len(solutions))
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

def main():
    try:
        n = int(input("Ingrese el tamaño del tablero (N): "))
        game = NQueens(n)
        game.run_visualization()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    finally:
        pygame.quit()
