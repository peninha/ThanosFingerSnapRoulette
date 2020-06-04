# -*- coding: utf-8 -*-
"""
@author: Pena

Calcula a chance de um grupo de x pessoas (por exemplo, os 4 milhões de
habitantes da Croácia) sobreviver quando o Thanos estala os dedos.
Para x grande o cálculo se aproxima de 1/2^x
"""


def ChanceToSurviveThanosSnaps(x):
    n = 7000000000  # World Population
    nsobre2 = n/2
    T0 = 1/2
    T1 = T0
    for i in range(1, x):
        T1 = (nsobre2 - i)*T0/(n-i)
        T0 = T1
    return T1


def OneOver2RaisedToX(x):
    return 1/(2**x)


if __name__ == "__main__":
    for x in range(1, 121):
        print("x = {}\nreal_prob = {:2.36%}\n1/2^x     = {:2.36%}\n"
              .format(x,
                      ChanceToSurviveThanosSnaps(x),
                      OneOver2RaisedToX(x))
              )
