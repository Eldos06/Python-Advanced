
def power(nums):
    for i in nums:
        yield i ** i
    
# for i in power(range(1,6)):
#     print(i)

def waiter():
    print("what would you like?")
    order = yield
    print(f"your order: {order}")

# w = waiter()
# next(w)
# w.send("Pasta") 

# for i in waiter():
#     print(i)


# for i in w:
#     print("gonna order salad")
#     w.send("salad")
#     print("Nice one, thank you for every one")



def waiter():
    order_items = []
    print("What would U like?")
    while True:
        order = yield order_items
        if order is None:
            print("done", order_items)
            return order_items
        order_items.append(order)
        print(order, "ok, what else")

# w = waiter()
i_want_to_order = [
    "fruit salad",
    "palay",
    "kola"
]
# next(w)

# for food in i_want_to_order:
#     w.send(food)

# next(w)

class OrderCoplete(Exception):
    pass

def waiter():
    order_items = []
    print("What would U like?")
    while True:
        
        try:
            order = yield order_items
        except:
            print("done", order_items)
            return order_items
        

        if order is not None:
            order_items.append(order)
            print(order, "ok, what else")


# w = waiter()

# for food, already_order in zip(i_want_to_order, w):
#     print("already_order", already_order)
#     w.send(food)
    

# for i in range(5):
#     print(next(w))
# w.throw(OrderCoplete)


def power(num):
    p = 0
    while True:
        p = yield num ** p
        

# p = power(2)
# next(p)
# # print(p.send(3))

# for i in range(5):
#     print(i, p.send(i))
# p.close()
# for i in range(5):
#     print(i, p.send(i))

# def items_by_one(seq):
#     yield from seq

# for i in items_by_one(range(4)):
#     print(i)

def add_count():
    counter = 0
    while True:
        num = yield 
        if num is None:
            return counter
        counter += num
        print(f"counter inc by {num} now = {counter}")

def collect_counters(counters: list):
    while True:
        counter = yield from add_count()
        counters.append(counter)

numbers = []
collector = collect_counters(numbers)
print(numbers)
next(collector)
collector.send(4)
collector.send(5)
# collector.send(None)
print(numbers)
collector.send(11)
print(numbers)

