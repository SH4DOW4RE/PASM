import time

RAX = 0
RBX = 0
RCX = 0
RDX = 0
RSI = 0
RDI = 0
RBP = 0
RSP = 0
R8  = 0
R9  = 0
R10 = 0
R11 = 0
R12 = 0
R13 = 0
R14 = 0
R15 = 0


def epoch() -> None:
    """
        Gets epoch (time in seconds since January 1st 1970) into rbp.
    """
    global RBP
    RBP = int(time.time())

