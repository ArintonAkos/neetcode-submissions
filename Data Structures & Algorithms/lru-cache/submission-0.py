class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # Move accessed element to front
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # print(f"Putting {key} with {value}")
        self.cache[key] = value
        self.cache.move_to_end(key)

        if len(self.cache) == self.capacity + 1:
            self.cache.popitem(last=False)

        # print(f"Self.cache: {self.cache}")
        return None