from helper import (
    hash256,
    little_endian_to_int,
    read_varint,
)
from script import Script


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
    def parse(cls, s, testnet=False):
        version = little_endian_to_int(s.read(4))
        num_inputs = read_varint(s)
        inputs = []
        for _ in range(num_inputs):
            inputs.append(TxIn.parse(s))
        num_outputs = read_varint(s)
        outputs = []
        for _ in range(num_outputs):
            outputs.append(TxOut.parse(s))
        locktime = little_endian_to_int(s.read(4))
        return cls(version, inputs, outputs, locktime, testnet=testnet)


class TxIn:
    def __init__(self, prev_tx, prev_index, script_sig, sequence):
        self.prev_tx = prev_tx
        self.prev_index = prev_index
        if script_sig is None:
            self.script_sig = Script()
        else:
            self.script_sig = script_sig
        self.sequence = sequence

    def __repr__(self):
        return "Prev_tx: {}\nPrev_index: {}".format(self.prev_tx.hex(), self.prev_index)

    @classmethod
    def parse(cls, s):
        """
        Takes a byte stream and parses the tx_input at the start
        return a TxIn object
        """
        prev_tx = s.read(32)[::-1]
        prev_index = little_endian_to_int(s.read(4))
        script_sig = Script.parse(s)
        sequence = little_endian_to_int(s.read(4))
        return cls(prev_tx, prev_index, script_sig, sequence)


class TxOut:
    def __init__(self, amount, script_pubkey):
        self.amout = amount
        self.script_pubkey = script_pubkey

    def __repr__(self):
        return "TxOut(amount:{}, script_pubkey:{})".format(
            self.amount, self.script_pubkey
        )

    @classmethod
    def parse(cls, s):
        """
        Takes a byte stream and parses the tx_output at the start.
        Returns a TxOut object.
        """
        amount = little_endian_to_int(s.read(8))
        script_pubkey = Script.parse(s)
        return cls(amount, script_pubkey)
