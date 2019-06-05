class Enemy:
    # Class Variables
    imgs = []

    def __init__(self, x_pos, y_pos, width, height):
        self.x = x_pos
        self.y = y_pos
        self.width = width
        self.height = height
        self.animation_count = 0
        self.health = 1
        self.path = []
        self.img = None

    def draw(self, win):
        self.animation_count += 1
        self.img = self.imgs[self.animation_count]

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))

        self.move()
        """
        Draw enemy based on images
        :param win: surface
        :return: none
        """

    def collide(self, x, y):
        """
        Return if object collides the enemy
        :param x: int
        :param y: int
        :return: bool
        """
        if x >= self.x and x <= (self.x + self.width):
            if y >= self.y and y <= (self.y + self.height):
                return True
        return False

    def move(self):
        """
        Move enemy
        :return: none
        """
        pass

    def hit(self):
        """
        Remove enemy health by 1 and return true if enemy is dead
        :return: bool
        """
        self.health -= 1
        if self.health <= 0:
            return True