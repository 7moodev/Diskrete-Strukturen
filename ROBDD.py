from pyeda.inter import expr, expr2bdd, bddvar
from graphviz import Source


# Define variables
x1, x2, x3, x4 = map(bddvar, ['x1', 'x2', 'x3', 'x4'])

# Define Boolean functions F and G
F = x1 & x2 & x4 | (~x1 & ~x2 & ~x4) | (~x1 & ~x2 & x3 & x4) |(x1 & ~x2 & ~x3 & ~x4)| (~x1 &x2 &x3 &x4) | (~x1 & x2 &~x3 &~x4 )
G = x1 & x3 & x4 | ~x1 & x2 & x3& x4

# Convert expressions to BDDs
F = expr2bdd(F)
G = expr2bdd(G)

# Compute F XOR G
F_mit_G= F ^ G

# Write BDDs to dot files
with open('bdd_F.dot', 'w') as f:
    f.write(F.to_dot())

with open('bdd_G.dot', 'w') as f:
    f.write(G.to_dot())

with open('bdd_F_xor_G.dot', 'w') as f:
    f.write(F_mit_G.to_dot())

for dot_file in ['bdd_F.dot', 'bdd_G.dot', 'bdd_F_xor_G.dot']:
    src = Source.from_file(dot_file)
    src.render(filename=dot_file, format='png', cleanup=True)