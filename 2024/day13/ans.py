import re

with open("test.txt", "r") as f:
    for row in f.read().split("\n\n"):
        Ax, Ay, Bx, By, Px, Py = map(int, re.findall(r"\d+", row))
        """
        Example how it works:

        Input is as follow

        Button A: X+94, Y+34
        Button B: X+22, Y+67
        Prize: X=8400, Y=5400

        So we can say the following:
        Ax * T + Bx * S = Px
        Ay * T + By * S = Py

        To solve for T:
        First remove 1 constant lets remove S
        Ax * T + Bx * S = Px    *By
        Ay * T + By * S = Py    *Bx
  
        By * Ax * T + By * Bx * S = Px * By
        Bx * Ay * T + By * Bx * S = Py * Bx

        Then subtract 1 equation from the other note that the (By * Bx * S) is the same in both so the cancle out
        By * Ax * T + By * Bx * S = Px * By
        Bx * Ay * T + By * Bx * S = Py * Bx  -
        _______________________________________
        By * Ax * T - Bx * Ay * T = Px * By - Py * Bx

        Now isolated the T
        (By * Ax - Bx * Ay) * T = Px * By - Py * Bx
        T = (Px * By - Py * Bx) / (By * Ax - Bx * Ay)
        
        Now isolated S form the starting equation
        Ax * T + Bx * S = Px
        S = (Px - Ax * T) / Bx
        """
        T = (Px * By - Py * Bx) / (By * Ax - Bx * Ay)
        S = (Px - Ax * T) / Bx
        print(T, S)