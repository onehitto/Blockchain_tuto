from blocks import *
import json

class C_blockchain:
    def __init__ (self,chaine = []):
        self.chaine = chaine
    
    def createGenesisBlock(self):
        var_block = C_block()
        var_block.hash = var_block.calculated_hash()
        var_block.mining()
        self.chaine.append(var_block)
    
    def addBlock(self,newBlock):
        newBlock.prev_hash = self.chaine[len(self.chaine)-1].hash
        newBlock.hash = newBlock.calculated_hash()
        newBlock.mining() 
        self.chaine.append(newBlock)
    
    def ReadChaine_json(self,file):
        p_data = json.loads(file.read())
        chaine_block = C_blockchain([])
        for x in p_data['chaine']:
            block = C_block(x['data'],
                            x['prev_hash'],
                            x['nonce'],
                            x['hash'])
            self.chaine.append(block)
        return chaine_block

    def toJson_v0(self,file = None ,Save = False):
        print (json.dumps(self, default=lambda o: o.__dict__, indent=4))
        if Save :
            file.write(json.dumps(self, default=lambda o: o.__dict__, indent=4))

    def toJson_v3(self,file = None ,Save = False):
        for x in self.chaine:
            print (json.dumps(x.__dict__))
            if Save :
                file.write(json.dumps(x.__dict__)+'\n')