from functools import reduce
class MyList:
    def __init__(self, *args):
        self.items = list(args)

    def __len__(self):
        return reduce(lambda acc, x: acc + (sum(x) if hasattr(x, '__iter__') else x), [x*2 for x in self.items])

my_list = MyList(1, 2, 3, [4, 5])
print(len(my_list))