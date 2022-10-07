Consider a CSP, where there are eight variables A, B, C, D, E, F, G, H, each with domain {1, 2, 3, 4}. Suppose the constraints are:
•  A > G
• |G – C| = 1
• D != C
• G != F
• |E – F| is odd
• A ≤ H
• |H – C| is even
• E != C
• H != F
• |F – B| = 1
• H != D
• E < D – 1
• C != F
• G < H
• D ≥ G
• E != H – 2
• D != F – 1

The solutions are:
{'A': 2, 'B': 3, 'C': 2, 'D': 4, 'E': 1, 'F': 4, 'G': 1, 'H': 2}
{'A': 3, 'B': 2, 'C': 3, 'D': 4, 'E': 2, 'F': 1, 'G': 2, 'H': 3}
{'A': 4, 'B': 1, 'C': 4, 'D': 3, 'E': 1, 'F': 2, 'G': 3, 'H': 4}
{'A': 4, 'B': 3, 'C': 4, 'D': 3, 'E': 1, 'F': 2, 'G': 3, 'H': 4}
Number of failed branches: 1266
