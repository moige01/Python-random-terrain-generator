import random


class RandomNoise():
    """
    Random noise class to create random values in 2d array
    """
    def __init__(self, width=32, height=32, bit_depth=255, extra=32):
        self.w = width + extra
        self.h = height + extra
        self.bit_depth = bit_depth
        self.extra = extra

    def randomize(self):
        """
        Creates a random grid of w x h of values between 0-1 with precision
        determined by the bit_depth; e.g. bit_depth = 255 values can be from
        0 to 1 with 255 distinct values; 0/255, 1/255, 2/255, etc...
        """
        self.n = [[random.randint(0, self.bit_depth)/self.bit_depth for y in range(self.h)] for x in range(self.w)]

    def noise2d(self, x, y):
        """
        Returns a certain value from the randomized grid.
        """
        return self.n[x][y]

    def smoothNoise2d(self, bit_depth=255, smoothing_passes=15, upper_value_limit=1):
        """
        Smooths the random grid and returns the smoothed noise values
        """
        # Convert the grid to values between 0 and the upper_value_limit
        # values = [[upper_value_limit*self.noise2d(x,y) for y in range(self.h-self.extra+smoothing_passes)] for x in range(self.w-self.extra+smoothing_passes)]
        values = self.n

        # Smoothing the random grid
        for _ in range(smoothing_passes):
            values = [[((values[x][y]+values[x+1][y]+values[x][y+1]+values[x-1][y]+values[x][y-1])/5) for y in range(len(values[x])-1)] for x in range(len(values)-1)]

        return values
