
from percolation import Percolation
import numpy as np
import random
import math
                 
class PercolationStats:
    '''Class to analyze the limiar of percolation.
    '''
    def __init__(self,shape,T):
        if type(shape) == int:
            self.shape = (shape,shape)
        if type(shape) == tuple:
            self.shape = shape
        self.N = T
        self.no_abertos_ = np.zeros(T)
        self.mean_ = 0.0
        self.stddev_ = 0.0
        self.x = np.zeros(T)
        
    def no_abertos(self):
        self.no_abertos_ = np.zeros(self.N)
        n = self.shape[0]
        m = self.shape[1]
        div = m*n
        for i in range(self.N):
            perc = Percolation(self.shape)        
            while perc.percolates() == False:
                perc.open(random.randint(0,n-1),random.randint(0,m-1))
            self.no_abertos_[i] = perc.no_open()
            self.x[i] = self.no_abertos_[i]/div
        return self.no_abertos_
        
    def mean(self):
        if self.mean_ != 0.0:
            return self.mean_
        else:
            no = self.no_abertos()
            
            for i in range(self.N):
                self.mean_ += self.x[i]
            self.mean_ = self.mean_/(self.N)
            return self.mean_
    
    def stddev(self):
        if self.stddev_ != 0.0:
            return self.stddev_ 
        else:
            if self.mean_ == 0.0:
                cal_mean = self.mean()
                
            for i in range(self.N):
                self.stddev_ += (self.x[i] - self.mean_)**2
            
            self.stddev_ = np.sqrt(self.stddev_/(self.N - 1))
            return self.stddev_
    
    def confidenceLow(self):
        if self.mean_ == 0.0:
            cal_mean = self.mean()
        if self.stddev_ ==0.0:
            cal_stddev = self.stddev()
            
        conf = self.mean_ - (1.96*self.stddev_)/np.sqrt(self.N)
        return conf
        
    def confidenceHigh(self):
        if self.mean_ == 0.0:
            cal_mean = self.mean()
        if self.stddev_ == 0.0:
            cal_stddev = self.stddev()
            
        conf = self.mean_ + (1.96*self.stddev_)/np.sqrt(self.N)
        return conf
            
            
        
        
        
        
        
        
        
        
        
        
        
        
