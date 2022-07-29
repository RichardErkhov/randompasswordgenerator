import string as s
import random as r
c=list(s.ascii_letters+s.digits+"!@#$%^&*()")
r.shuffle(c)
p = [r.choice(c) for i in range(int(input("length: ")))]
r.shuffle(p)
print("".join(p))
