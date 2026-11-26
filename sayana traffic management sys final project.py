import pygame
import sys

pygame.init()

# WINDOW

WIDTH = 1200
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Traffic Management System")
clock = pygame.time.Clock()

# COLORS

SKY = (100, 190, 225)
GRASS = (75, 160, 75)
DARK_GRASS = (55, 135, 60)

ROAD = (48, 48, 48)
SIDEWALK = (145, 145, 145)

WHITE = (255, 255, 255)
BLACK = (20, 20, 20)

RED_CAR = (150, 25, 25)
BLUE_CAR = (25, 105, 200)
YELLOW_CAR = (220, 165, 20)

WINDOW = (90, 160, 180)
TIRE = (15, 15, 15)
HUB = (140, 140, 140)

RED = (240, 30, 40)
YELLOW = (255, 205, 0)
GREEN = (0, 220, 80)
GREY = (65, 65, 65)

# TRAFFIC SIGNAL

signal = "RED"
signal_timer = 0

RED_TIME = 5
GREEN_TIME = 5
YELLOW_TIME = 2


def update_signal():

    global signal, signal_timer

    signal_timer += 1 / 60

    if signal == "RED" and signal_timer >= RED_TIME:
        signal = "GREEN"
        signal_timer = 0

    elif signal == "GREEN" and signal_timer >= GREEN_TIME:
        signal = "YELLOW"
        signal_timer = 0

    elif signal == "YELLOW" and signal_timer >= YELLOW_TIME:
        signal = "RED"
        signal_timer = 0

# BACKGROUND

def draw_background():

    screen.fill(GRASS)

    # Sky
    pygame.draw.rect(
        screen, SKY, (0, 0, WIDTH, 195)
    )

    # Clouds
    for x, y in [(100, 70), (850, 85)]:

        pygame.draw.circle(screen, WHITE, (x, y), 20)
        pygame.draw.circle(screen, WHITE, (x + 25, y - 8), 27)
        pygame.draw.circle(screen, WHITE, (x + 52, y), 20)

    # Trees
    for x in [80, 250, 1030, 1130]:

        pygame.draw.rect(
            screen, (100, 65, 35),
            (x, 150, 12, 45)
        )

        pygame.draw.circle(
            screen, (35, 125, 55),
            (x + 5, 140), 30
        )

    # Grass details
    for x in range(20, WIDTH, 50):

        pygame.draw.circle(
            screen,
            DARK_GRASS,
            (x, 570),
            3
        )

# ROAD

def draw_road():

    # Main road
    pygame.draw.rect(
        screen,
        ROAD,
        (0, 230, WIDTH, 280)
    )

    # Sidewalks
    pygame.draw.rect(
        screen,
        SIDEWALK,
        (0, 195, WIDTH, 35)
    )

    pygame.draw.rect(
        screen,
        SIDEWALK,
        (0, 510, WIDTH, 35)
    )

    # Road edge lines
    pygame.draw.line(
        screen,
        WHITE,
        (0, 240),
        (WIDTH, 240),
        4
    )

    pygame.draw.line(
        screen,
        WHITE,
        (0, 500),
        (WIDTH, 500),
        4
    )

    # Lane divider
    for x in range(0, WIDTH, 80):

        pygame.draw.rect(
            screen,
            WHITE,
            (x, 355, 40, 7)
        )

    
    # ZEBRA CROSSING
    
    for y in range(250, 490, 25):

        pygame.draw.rect(
            screen,
            WHITE,
            (600, y, 80, 12)
        )


# ONE TRAFFIC LIGHT

def draw_traffic_light():

    # Pole
    pygame.draw.rect(
        screen,
        BLACK,
        (700, 70, 8, 160)
    )

    # Top support
    pygame.draw.rect(
        screen,
        BLACK,
        (700, 70, 70, 8)
    )

    # Light box
    pygame.draw.rect(
        screen,
        BLACK,
        (675, 35, 60, 125),
        border_radius=10
    )

    # Light colors
    red_light = RED if signal == "RED" else GREY
    yellow_light = YELLOW if signal == "YELLOW" else GREY
    green_light = GREEN if signal == "GREEN" else GREY

    pygame.draw.circle(
        screen,
        red_light,
        (705, 60),
        15
    )

    pygame.draw.circle(
        screen,
        yellow_light,
        (705, 98),
        15
    )

    pygame.draw.circle(
        screen,
        green_light,
        (705, 136),
        15
    )


# CAR

class Car:

    def __init__(self, x, y, color, direction):

        self.x = x
        self.y = y
        self.color = color
        self.direction = direction

        self.width = 120
        self.speed = 3
        self.slow_speed = 1

    # DRAW CAR
  
    def draw(self):

        x = int(self.x)
        y = int(self.y)

        # Shadow
        pygame.draw.ellipse(
            screen,
            (25, 25, 25),
            (x + 8, y + 37, 105, 10)
        )

        # Main body
        pygame.draw.rect(
            screen,
            self.color,
            (x, y + 10, 120, 32),
            border_radius=9
        )

        # Roof
        pygame.draw.polygon(
            screen,
            self.color,
            [
                (x + 25, y + 10),
                (x + 43, y - 7),
                (x + 82, y - 7),
                (x + 103, y + 10)
            ]
        )

        # Windows
        pygame.draw.polygon(
            screen,
            WINDOW,
            [
                (x + 42, y - 2),
                (x + 60, y - 2),
                (x + 60, y + 7),
                (x + 34, y + 7)
            ]
        )

        pygame.draw.polygon(
            screen,
            WINDOW,
            [
                (x + 65, y - 2),
                (x + 82, y - 2),
                (x + 97, y + 7),
                (x + 65, y + 7)
            ]
        )

        # Wheels
        pygame.draw.circle(
            screen,
            TIRE,
            (x + 23, y + 42),
            11
        )

        pygame.draw.circle(
            screen,
            TIRE,
            (x + 97, y + 42),
            11
        )

        # Wheel hubs
        pygame.draw.circle(
            screen,
            HUB,
            (x + 23, y + 42),
            4
        )

        pygame.draw.circle(
            screen,
            HUB,
            (x + 97, y + 42),
            4
        )

        # Headlights
        if self.direction == "RIGHT":

            pygame.draw.rect(
                screen,
                (255, 245, 180),
                (x + 114, y + 17, 6, 7)
            )

            pygame.draw.rect(
                screen,
                RED,
                (x, y + 17, 6, 7)
            )

        else:

            pygame.draw.rect(
                screen,
                (255, 245, 180),
                (x, y + 17, 6, 7)
            )

            pygame.draw.rect(
                screen,
                RED,
                (x + 114, y + 17, 6, 7)
            )


# CARS

cars = [

    Car(-130, 285, RED_CAR, "RIGHT"),
    Car(150, 285, BLUE_CAR, "RIGHT"),
    Car(WIDTH, 420, YELLOW_CAR, "LEFT")
]

# CAR MOVEMENT

def move_cars():

    # Zebra crossing boundaries
    zebra_start = 600
    zebra_end = 680

   
    # RIGHT MOVING CARS
    

    right_cars = [car for car in cars if car.direction == "RIGHT"]

    # Sort cars from front to back
    right_cars.sort(key=lambda c: c.x, reverse=True)

    for i, car in enumerate(right_cars):

        new_x = car.x

        # Traffic light behavior
        if signal == "RED":

            # Stop before zebra
            if car.x + car.width < zebra_start - 15:
                new_x += car.speed

        elif signal == "YELLOW":

            new_x += car.slow_speed

        else:

            new_x += car.speed

        # Keep distance from car in front
        if i > 0:

            front_car = right_cars[i - 1]

            if new_x + car.width > front_car.x - 25:
                new_x = front_car.x - car.width - 25

        car.x = new_x

   
    # LEFT MOVING CAR
    

    left_car = [car for car in cars if car.direction == "LEFT"][0]

    if signal == "RED":

        if left_car.x > zebra_end + 15:
            left_car.x -= left_car.speed

    elif signal == "YELLOW":

        left_car.x -= left_car.slow_speed

    else:

        left_car.x -= left_car.speed

    # Reset cars
    for car in cars:

        if car.x > WIDTH + 150:
            car.x = -150

        if car.x < -150:
            car.x = WIDTH + 150


# STATUS

def draw_status():

    pygame.draw.rect(
        screen,
        BLACK,
        (20, 20, 210, 45),
        border_radius=8
    )

    font = pygame.font.SysFont(
        "Arial", 20, True
    )

    text = font.render(
        "Signal: " + signal,
        True,
        WHITE
    )

    screen.blit(
        text,
        (35, 32)
    )

# MAIN LOOP

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

    # Update signal
    update_signal()

    # Draw background
    draw_background()

    # Draw road
    draw_road()

    # Draw traffic light
    draw_traffic_light()

    # Move cars
    move_cars()

    # Draw cars
    for car in cars:
        car.draw()

    # Signal status
    draw_status()

    pygame.display.update()

    clock.tick(60)


pygame.quit()
sys.exit()