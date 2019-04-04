import numpy as np
import matplotlib.pyplot as plt

def reduce_point(X , reduction = 0.3):
    nb_points = len(X)
    new_points = int(nb_points*reduction)
    Y = []
    for i in range(new_points):
        Y.append( X[ ((1+int(1/reduction))*i)%(len(X)) ] )
    return Y
    
def granulate(X, amplitude):
    Y = [X[i] + np.random.rand()*amplitude - np.random.rand()*amplitude*0.9 for i in range(len(X))]
    return Y

def dessin_graph(X,Y,dim = [0,0,0,0],x_lab = "X Axis",y_lab = "Y Axis"):
    """Simple graph"""
    plt.plot(X,Y)
    print(len(X),len(Y))
    if (dim != [0,0,0,0]):
        plt.axis(dim)
    plt.xlabel(x_lab)
    plt.ylabel(y_lab)
    plt.grid(color = "k", linestyle = "-")
    
def show_graph():
    #plt.legend()
    plt.show()
    
    
def first_order_transfer_function(gain, tau, tA, tB, precision):
    """Return a complete graph between tA and tB"""
    X = [precision*i for i in range(int((tB-tA)/precision))]
    Y = [gain*(1-np.exp(-X[j]/tau)) for j in range(len(X))]
    return X,Y