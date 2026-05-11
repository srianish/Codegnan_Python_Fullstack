'''
#Generators:
-----------
--> Generators in python is enable lazy evalution for producing
sequence of values efficiently.
--> They differ from regular functions by execution and
resuming on demand.
--> Generators create iterations that yeild values one at a
time using the yeild keyword.

#Functons vs Generators:
----------------------
--> Regular functions execute fully upon call and return a
single value, terminating afterward.
--> Generators use yield to produce multiple value lazily,
acting like iterators without building the entire sequence in
memory.


def count_(num):
    i = 1
    while i <= num:
        yield i
        i +=1
Gen_ = count_(3)
print(next(Gen_))
print(next(Gen_))

#Yield:
------
--> Yield pauses the generator function, saves its
state(local variable, position), and yielded value to the caller.

#Next:
------
--> This advances the generator by executing until the next
yield, returning that value, subseqent calls resume from there.

'''
def msg_gen():
    yield "First Msg"
    yield "Snd Msg"
    yield "Done"
gen = msg_gen()
print(next(gen))
print(next(gen))






















