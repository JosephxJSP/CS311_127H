# Import type 1
import myFunction
result = myFunction.plus(1, 5)
print(result)

# Import type 2
import myFunction as fn
result = fn.minus(10, 5)
print(result)

# Import type 3
from myFunction import multiply, divide
result = multiply(5, 5)
result = divide(5, 5)
print(result)