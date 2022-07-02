#!/usr/bin/env python3

import hashlib
import codecs

class C_block:

    def __init__(self, data="empty",prev_hash="0"*64,nonce = "0",hash = "0"):
        self.data = data
        self.prev_hash= prev_hash
        self.nonce = nonce
        self.hash = hash
       
    def calculated_hash(self):
        return hashlib.sha256((self.data + self.prev_hash + self.nonce).encode()).hexdigest()

    def mining(self,difficulty = 5):
        while (self.hash[0:difficulty] != "0"*difficulty):
            self.nonce = str (int(self.nonce) + 1)
            self.hash = self.calculated_hash()

