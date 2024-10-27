import math

# COLORS (RGB FORMAT)
WHITE = (255, 255, 255)  # paddles, ball, and center line
BLACK = (0, 0, 0)        # Background 


# WINDOW DIMENSIONS
WIDTH, HEIGHT = 800, 600


# PADDLE PROPERTIES
PADDLE_PADDING = 30  # Distance between the paddle and the edge of the screen


# BALL PHYSICS
GRAVITY = 0.1  
MAX_BOUNCE_ANGLE = math.pi / 4  # 45 degrees
SPIN_FACTOR = 1  # Adjust spin effect
BALL_MASS = .5  # Mass of the ball
MAX_SPEED = 20  # Maximum speed of the ball