from helper import *


class Tx:
    def __init__(self, version, tx_ins, tx_outs, locktime, testnet=False):
        self.version = version
        self.tx_ins = tx_ins
        self.tx_outs = tx_outs
        self.locktime = locktime
        self.testnet = testnet

    def __repr__(self):
        tx_ins = ""
        for tx_in in self.tx_ins:
            tx_ins += tx_in.__repr__() + "\n"
        tx_outs = ""
        for tx_out in tx_outs:
            tx_outs + tx_out.__repr__() + "\n"
        return "Tx: {}\nversion: {}\nTx_ins:\n{}\nTx_outs:\n{}\nLocktime: {}".format(
            self.id(), self.version, tx_ins, tx_outs, self.locktime
        )

    def id(self):
        """
        人が読める16進数表記のトランザクションハッシュ
        """
        return self.hash().hex()

    def hash(self):
        """
        トランザクションのバイナリハッシュ
        """
        return hash256(self.serialize())[::-1]

    @classmethod
    def parse(cls, serialization, testnet=False):
        version = little_endian_to_int(serialization.read(4))
        return cls(version, None, None, None, testnet)
