class Counter:
    _count = 0  # Class variable to track instances
    
    def __init__(self):
        Counter._count += 1
    
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls._count}")

Counter.display_count()  
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
Counter.display_count()  