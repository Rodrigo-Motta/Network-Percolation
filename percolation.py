import numpy as np

# constants
#BLOCKED = 0
#OPEN    = 1
#FULL    = 2

class Percolation:
    '''
    Represents a network with all the sites blocked.
    '''
    def __init__(self,shape):
        if type(shape) == int: self.shape = (shape,shape)
        else: self.shape = shape
        self.array = np.full(self.shape,0)
        self.cont = 0
        self.lin = self.shape[0]
        self.col = self.shape[1]

            
    
    def __str__(self):
        shape = self.shape
        array = self.array
        s = ""
        for i in range((shape[0])):
            for j in range((shape[1])):
                if j == 0: s+= "+---+"
                else: s+= "---+"
                if j == (shape[1] - 1): s += "\n"

            for j in range((shape[1])):
                if array[i,j] == 0:
                    if j == 0: s+= "|   |"
                    else: s+= "   |"
                if array[i,j] == 1:
                    if j == 0: s+= "| o |"
                    else: s+= " o |"
                if array[i,j] == 2:
                    if j == 0: s+= "| x |"
                    else: s+= " x |"
                if j == (shape[1] - 1): s += "\n"
                
        for j in range((shape[1])):
            if j == 0: s+= "+---+"
            else: s+= "---+"
            if j == (shape[1] - 1): s += "\n"
        
        s += 'grade de dimensão: {}x{} \n'.format(shape[0],shape[1])
        s += 'no. sítios abertos: {}\n'.format(self.no_open())
        s += 'percolou: {}'.format(self.percolates())
        return s
    
    def shape(self):
        return self.shape
        
    def is_open(self,lin,col):
        if self.array[lin,col] == 1 or self.array[lin,col] == 2: return True
        else: return False
        
    def is_full(self, lin, col):
        if self.array[lin,col] == 2: return True
        else: return False
        
    def percolates(self):
        return 2 in self.array[-1, :]
                    
                     
    def no_open(self):
        return self.cont
    
    
    def open(self,lin,col):
        if self.array[lin,col] == 1 or self.array[lin,col] == 2:
            return
        if lin >= self.shape[0] or lin < 0:
            return "open(): posição [{},{}] está fora da grade".format(lin,col)
        if col >= self.shape[1] or col < 0:
            return "open(): posição [{},{}] está fora da grade".format(lin,col)
        self.cont += 1
        fila = []
        fila.append((lin, col))
        confere = []  #as que ja conferi
        confere.append((lin, col))
        test = False
        if lin - 1 >= 0:
            if self.array[lin - 1, col] == 2:
                test = True
        if lin + 1 <= self.lin - 1:
            if self.array[lin + 1, col] == 2:
                test = True
        if col - 1 >= 0:
            if self.array[lin, col - 1] == 2:
                test = True
        if col + 1 <= self.col - 1:
            if self.array[lin - 1, col] == 2:
                test = True
        if lin == 0:
            test = True

        if test == True:
            self.array[lin, col] = 2
            while fila != []:
                i, j = fila.pop(0)
                if i >= 1 and (i - 1, j) not in confere:
                    if self.array[i - 1, j] == 1:
                        fila.append((i - 1, j))
                        confere.append((i - 1, j))
                        self.array[i - 1, j] = 2
                if i <= self.lin - 2 and (i + 1, j) not in confere:
                    if self.array[i + 1, j] == 1:
                        fila.append((i + 1, j))
                        confere.append((i + 1, j))
                        self.array[i + 1, j] = 2
                if j <= self.col - 2 and (i, j + 1) not in confere:
                    if self.array[i, j + 1] == 1:
                        fila.append((i, j + 1))
                        confere.append((i, j + 1))
                        self.array[i, j + 1] = 2
                if j >= 1 and (i, j - 1) not in confere:
                    if self.array[i, j - 1] == 1:
                        fila.append((i, j - 1))
                        confere.append((i, j + 1))
                        self.array[i, j - 1] = 2
        else:
            self.array[lin, col] = 1

    def get_grid(self):
        array = self.array.copy()
        return array

    
    
    
    
    
    