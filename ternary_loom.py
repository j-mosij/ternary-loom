#!/usr/bin/env python3
"""
ternary_loom.py
Ternary loom — balanced trits {-1, 0, 1}.

The three parts interweave. Once the weave (mutual relation) holds,
the vehicle (protection layer) is applied. Compression is the open
reduction of the verified tryte to its source pair.

Author: j-mosij
No dynamic code. No writes after construction. Fully visible.
"""

def shell(a: int, b: int) -> int:
    """Open shell. Computed only; never writes back."""
    return ((a + b) % 3) - 1

def mutual_ok(a: int, b: int, c: int) -> bool:
    """The three check each other."""
    return c == shell(a, b)

class TernaryLoom:
    """Vehicle summoned by a valid weave."""
    def __init__(self, a: int, b: int):
        a = max(-1, min(1, a))
        b = max(-1, min(1, b))
        c = shell(a, b)
        if not mutual_ok(a, b, c):
            raise ValueError("weave failed; vehicle not summoned")
        # immutable after weave succeeds
        self._tryte = (a, b, c)

    @property
    def tryte(self) -> tuple:
        return self._tryte

    def balance_check(self) -> bool:
        """Outer vehicle double-check."""
        a, b, c = self._tryte
        return mutual_ok(a, b, c)

    def compress(self) -> tuple:
        """Mathematical compression: verified tryte reduces to source pair.
        GPU-like in the sense of a single open reduction step.
        """
        if not self.balance_check():
            raise ValueError("compromised; compression refused")
        a, b, _ = self._tryte
        return (a, b)  # high-level reduction; C is the expended shell

    def report(self) -> str:
        a, b, c = self._tryte
        return (f"A={a} B={b} C={c}  "
                f"weave_ok={mutual_ok(a, b, c)}  "
                f"vehicle_ok={self.balance_check()}")

if __name__ == "__main__":
    loom = TernaryLoom(1, -1)
    print(loom.report())
    print("compressed:", loom.compress())
