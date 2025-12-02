def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Tea"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()
for cup in stall:
    print(cup)


def get_chai_list():
    for i in range(1000):
        yield "Cup "+str(i+1)

chai_list = get_chai_list()

# for chai in chai_list:
#     print(chai)

# To just get the immediate value from generator
print(next(chai_list))