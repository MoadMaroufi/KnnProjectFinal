from scipy.spatial import distance_matrix
import numpy as np
from scipy.spatial import cKDTree
from scipy import stats 
class KNN:
    '''
    k nearest neighboors algorithm class
    __init__() initialize the model
    train() trains the model
    predict() predict the class for a new point
    '''

    def __init__(self, k):
        '''
        INPUT :
        - k : is a natural number bigger than 0 
        '''

        if k <= 0:
            raise Exception("Sorry, no numbers below or equal to zero. Start again!")
            
        # empty initialization of X and y
        self.X = []
        self.y = []
        # k is the parameter of the algorithm representing the number of neighborhoods
        self.k = k

        ##Initialize Kdtree
        self.kdtree=None
        
    def fit(self,X,y):
        '''
        INPUT :
        - X : is a 2D NxD numpy array containing the coordinates of points
        - y : is a 1D Nx1 numpy array containing the labels for the corrisponding row of X
        '''       

        self.y = np.copy(y) 
        ##because we are going to sum the labels in the majority vote and check if the sum>=0
        self.labels=np.unique(self.y)
        if len(self.labels==2):##i.e binary classification
            if self.labels[0]!=-1:
                self.y[self.y==self.labels[0]] = -1
            if self.labels[1]!=1:
                self.y[self.y==self.labels[1]] = 1
        self.kdtree=cKDTree(np.copy(X))
       
    def predict(self,X_new):
        '''
        INPUT :
        - X_new : is a MxD numpy array containing the coordinates of new points whose label has to be predicted
        A
        OUTPUT :
        - y_hat : is a Mx1 numpy array containing the predicted labels for the X_new points
        ''' 
        _, indices = self.kdtree.query(X_new, k=self.k)
        neighbor_labels = self.y[indices]
        if len(self.labels==2):
            # Summing neighbor labels
            sum_labels = np.sum(neighbor_labels, axis=1)
            # Assigning labels based on the sum=>faster than stats.mode, everything is vectorized
            y_hat = (sum_labels >= 0).astype(int)
        else:
            y_hat, _ = stats.mode(neighbor_labels, axis=1)

        return y_hat
    
    def minkowski_dist(self,X_new,p):
        '''
        INPUT : 
        - X_new : is a MxD numpy array containing the coordinates of points for which the distance to the training set X will be estimated
        - p : parameter of the Minkowski distance
        
        OUTPUT :
        - dst : is an MxN numpy array containing the distance of each point in X_new to X
        '''
        dst=distance_matrix(X_new,self.X,p)
        return dst
    def get_params(self, deep=True):
        return {"k": self.k}