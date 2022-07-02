from blockchain import *
from types import SimpleNamespace
from collections import namedtuple
import sys


def newchaine():
    chaine = C_blockchain([])
    chaine.createGenesisBlock()
    for x in range(20):
        c = C_block("test"+str(x),str(x))
        chaine.addBlock(c)
    return chaine

def main():
    # creation 
    #f = open('log.txt', 'r+')
    #chaine = newchaine()
    #chaine.toJson_v0(f,True)
    #f.close()

    f = open('log.txt', 'r+')
    chaine = C_blockchain([])
    chaine.ReadChaine_json(f)
    chaine.addBlock(C_block("test22"))
    #f.close()

    #f = open('log.txt', 'w+')
    chaine.toJson_v0(f,True)
    f.close()

if __name__ == "__main__":
    main()