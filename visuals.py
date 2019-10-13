import numpy as np
import matplotlib.pyplot as plt

subredList = np.array([[.066,.22], #Wholesome Memes
                       [.095,.084], #meirl
                       [.103,.09], #politics
                       [.046,.13], #math
                       [.044,.06], #learn python
                       [.08,.118], #funny
                       [.074,.157], #gaming
                       [.102,.172], #music
                       [.036,.159], #travel
                       [.04,.331]]) #casual conversation


labels = 'Negative', 'Neutral', 'Positive'
for i in subredList:
    neg = i[0]
    pos = i[1]
    neut = 1 - neg - pos
    sizes = [neg, neut, pos]
    colors = ['gold', 'yellowgreen', 'lightcoral']

    # Plot
    plt.pie(sizes, labels=labels, colors=colors, shadow=False, startangle=0)

    plt.axis('equal')
    plt.show()