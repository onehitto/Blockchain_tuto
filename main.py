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
    """creation chaine of 20 bloc"""
    f = open('log.txt', 'w+')
    chaine = newchaine()
    chaine.toJson_v0(f,True)
    f.close()
    """ read the chaine bloc and add a new bloc"""
    # f = open('log.txt', 'a+')
    # chaine = C_blockchain([])
    # chaine.ReadChaine_json(f)
    # chaine.addBlock(C_block("test22"))
    # f.close()
    """read the chaine bloc"""
    # f = open('log.txt', 'r+')
    # chaine.toJson_v0(f,True)
    # f.close()

if __name__ == "__main__":
    main()