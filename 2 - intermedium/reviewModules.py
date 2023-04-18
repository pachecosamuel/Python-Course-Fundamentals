from random import (
    randint as ri,
    random as r,
    uniform as u
)

import arrow

print(arrow.utcnow())

print(ri(1, 1000))
print(r())
print(u(1, 15))