import pygame
import abc


class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        raise NotImplementedError()

    def move(self, direction):
        if direction == 'up':
            self.y -= 4
        elif direction == 'down':
            self.y += 4
        elif direction == 'left':
            self.x -= 4
        elif direction == 'right':
            self.x += 4

    @staticmethod
    def factory(type):
        if type == 'Circle':
            return Circle(100, 100)
        if type == 'Square':
            return Square(100, 100)
        assert 0, "Bad Shape Requested: " + type


class Square(Shape):
    def draw(self):
        pygame.draw.rect(
            screen,
            (255, 255, 0),
            pygame.Rect(self.x, self.y, 20, 20)
        )


class Circle(Shape):
    def draw(self):
        pygame.draw.circle(
            screen,
            (0, 255, 255),
            (self.x, self.y),
            10
        )


class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def make_object(self):
        return


class CircleFactory(AbstractFactory):
    def make_object(self):
        # do something
        return Circle()


class SquareFactory(AbstractFactory):
    def make_object(self):
        # do something
        return Square()


def draw_function(factory):
    drawable = factory.make_object()
    drawable.draw()


def prepare_client():
    square_factory = SquareFactory()
    draw_function(square_factory)

    circle_factory = CircleFactory()
    draw_function(circle_factory)


if __name__ == '__main__':
    window_dimensions = 800, 600
    screen = pygame.display.set_mode(window_dimensions)

    obj = Shape.factory("Square")
    player_quits = False

    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_UP]:
                obj.move('up')
            if pressed[pygame.K_DOWN]:
                obj.move('down')
            if pressed[pygame.K_LEFT]:
                obj.move('left')
            if pressed[pygame.K_RIGHT]:
                obj.move('right')

            if pressed[pygame.K_c]:
                obj = Shape.factory("Circle")

            if pressed[pygame.K_s]:
                obj = Shape.factory("Square")

            screen.fill((105, 135, 56))
            obj.draw()

        pygame.display.flip()