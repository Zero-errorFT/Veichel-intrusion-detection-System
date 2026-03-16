import hashlib
import time

class Block:

    def __init__(self,index,data,prev_hash):
        self.index=index
        self.timestamp=time.time()
        self.data=data
        self.prev_hash=prev_hash
        self.hash=self.generate_hash()

    def generate_hash(self):
        value=str(self.index)+str(self.timestamp)+str(self.data)+str(self.prev_hash)
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:

    def __init__(self):
        self.chain=[]
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis=Block(0,"Genesis Block","0")
        self.chain.append(genesis)

    def add_block(self,data):
        prev=self.chain[-1]
        new_block=Block(len(self.chain),data,prev.hash)
        self.chain.append(new_block)

blockchain = Blockchain()