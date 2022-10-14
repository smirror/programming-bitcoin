import unittest
from io import BytesIO

from script import Script


class ScriptTest(unittest.TestCase):
    def test_parse(self):
        script_pubkey = BytesIO(
            bytes.fromhex(
                "6a47304402207899531a52d59a6de200179928ca900254a36b8dff8bb75f5f5d71b1cdc26125022008b422690b8461cb52c3cc30330b23d574351872b7c361e9aae3649071c1a7160121035d5c93d9ac96881f19ba1f686f15f009ded7c62efe85a872e6a19b43c15a2937"
            )
        )
        script = Script.parse(script_pubkey)
        want = bytes.fromhex(
            "304402207899531a52d59a6de200179928ca900254a36b8dff8bb75f5f5d71b1cdc26125022008b422690b8461cb52c3cc30330b23d574351872b7c361e9aae3649071c1a71601"
        )
        self.assertEqual(script.cmds[0].hex(), want.hex())
        want = bytes.fromhex(
            "035d5c93d9ac96881f19ba1f686f15f009ded7c62efe85a872e6a19b43c15a2937"
        )
        self.assertEqual(script.cmds[1], want)

    def test_serialize(self):
        want = "6a47304402207899531a52d59a6de200179928ca900254a36b8dff8bb75f5f5d71b1cdc26125022008b422690b8461cb52c3cc30330b23d574351872b7c361e9aae3649071c1a7160121035d5c93d9ac96881f19ba1f686f15f009ded7c62efe85a872e6a19b43c15a2937"
        script_pubkey = BytesIO(bytes.fromhex(want))
        script = Script.parse(script_pubkey)
        self.assertEqual(script.serialize().hex(), want)

    def test_ex6_3(self):
        """
        Create a ScriptSig that can unlock this ScriptPubKey:
        ----
        767695935687
        ----
        Note that `OP_MUL` multiplies the top two elements of the stack.
        * `56 = OP_6`
        * `76 = OP_DUP`
        * `87 = OP_EQUAL`
        * `93 = OP_ADD`
        * `95 = OP_MUL`
        """
        script_pubkey = Script([0x76, 0x76, 0x95, 0x93, 0x56, 0x87])
        script_sig = Script([0x52])
        combined_script = script_sig + script_pubkey
        self.assertEqual(combined_script.evaluate(0), True)


if __name__ == "__main__":
    ScriptTest.main()
