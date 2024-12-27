# x and y values need to be XORed (A) and ANDed (D)
# A needs to be XORed (B) and ANDed (C) with input carry bit
# output carry bit (E) derived from C | D
# bit from the AND needs to be ORed with the

# x, y, cin
# z = x ^ y ^ cin
# cout = ((x ^ y) & cin) | (x & y)

# therefore: a z must come from an XOR (3 out of 8 issues)
# the result of an OR must be used in an XOR and an AND
# the inputs to the OR must both come from ANDs


with open("input.txt") as f:
    input = f.read()

out = 0

values, gates = input.split("\n\n")


def print_graphviz():
    print("digraph {")
    print("  node [shape=record fontname=Arial];")

    for gate in gates.splitlines():
        a, op, b, _, val = gate.split()

        print(f'  {a} -> {{ "{gate}" }}')
        print(f'  {b} -> {{ "{gate}" }}')
        print(f'  "{gate}" -> {{ "{val}" }}')

    print("}")


# mostly manual solution for this problem. visualized the deps in graphviz and
# compared against what you'd expect from a full adder
#
# the automated solution would check for the conditions written in the notes at
# the top of this file
print_graphviz()
