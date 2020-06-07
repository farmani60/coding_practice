"""
Polynomial running is represented as O(nc), when c > 1. As you already saw, two
inner loops almost translate to O(n2) since it has to go through the array twice
in most cases. Are three nested loops cubic? If each one visit all elements,
then yes!

Usually, we want to stay away from polynomial running times (quadratic, cubic,
nc, etc.) since they take longer to compute as the input grows fast. However,
they are not the worst.
"""
# O(n^3)
def findXYZ(n):
    solutions = []
    for x in range(n+1):
        for y in range(n+1):
            for z in range(n+1):
                if (3*x+9*y+8*z==79):
                    solutions.append({x, y, z})
    return solutions

print(findXYZ(10))