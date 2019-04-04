import nuLof_graph_fct as nL
import matplotlib.pyplot as plt


A,B = nL.first_order_transfer_function(10,0.4,0,5,0.01)
nL.dessin_graph(A,B)
B = nL.reduce_point( nL.granulate(B,1) ,0.1)
A = nL.reduce_point(A,0.1)
#plt.plot(A,B)
#print()
nL.dessin_graph(A,B)
nL.show_graph()

