class Car:
    def __init__(self, i, j, L, horiz):
        """
        Parameters
        i: int
            Row of the car
        j: int
            Column of the car
        L: int
            Length of the car
        horiz: boolean
            True if the car is horizontal, false
            if the car is vertical
        """
        self.i = i
        self.j = j
        self.L = L
        self.horiz = horiz

class State:
    def __init__(self):
        self.N = 0 # Our cars are on an NxN grid
        self.cars = [] # The first car is the red car
        self.goal = [0, 0] # The state that our red car needs to reach
        self.prev = None # Pointers to previous states (use later)

    def clone(self):
        """
        Make a deep copy of this state

        Return
        ------
        State: copy of this state
        """
        s = State()
        s.N = self.N
        for c in self.cars:
            s.cars.append(Car(c.i, c.j, c.L, c.horiz))
        s.goal = self.goal.copy()
        return s

    def load_puzzle(self, filename):
        """
        Load in a puzzle from a text file
        
        Parameters
        ----------
        filename: string
            Path to puzzle
        """
        fin = open(filename)
        lines = fin.readlines()
        fin.close()
        self.N = int(lines[0])
        self.goal = [int(k) for k in lines[1].split()]
        for line in lines[2::]:
            fields = line.rstrip().split()
            i, j, L = int(fields[0]), int(fields[1]), int(fields[3])
            horiz = True
            if "v" in fields[2]:
                horiz = False
            self.cars.append(Car(i, j, L, horiz))

    def get_state_grid(self):
        """
        Return an NxN 2D list corresponding to this state.  Each
        element has a number corresponding to the car that occupies 
        that cell, or is a -1 if the cell is empty

        Returns
        -------
        list of list: The grid of numbers for the state
        """
        grid = [[-1]*self.N for i in range(self.N)]
        for idx, c in enumerate(self.cars):
            di = 0
            dj = 0
            if c.horiz:
                dj = 1
            else:
                di = 1
            i, j = c.i, c.j
            for k in range(c.L):
                grid[i][j] = idx
                i += di
                j += dj
        return grid
    
    def __str__(self):
        """
        Get a string representing the state
        """
        s = ""
        grid = self.get_state_grid()
        for i in range(self.N):
            for j in range(self.N):
                s += "%5s"%grid[i][j]
            s += "\n"
        return s
    
    def get_state_hashable(self):
        """
        Return a shorter string used to hash the state
        """
        s = ""
        grid = self.get_state_grid()
        for i in range(self.N):
            for j in range(self.N):
                s += "{}".format(grid[i][j])
        return s

    def plot(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib import cm
        from matplotlib.colors import ListedColormap
        c = cm.get_cmap("Paired", len(self.cars))
        colors = [[1, 1, 1, 1], [1, 0, 0, 1]]
        colors = colors + c.colors.tolist()
        cmap = ListedColormap(colors)
        grid = self.get_state_grid()
        grid = np.array(grid)
        plt.figure()
        plt.imshow(grid, interpolation='none', cmap=cmap)

    def solve(self):
        ## TODO: Fill this in
        pass