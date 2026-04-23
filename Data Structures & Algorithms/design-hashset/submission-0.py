class MyHashSet:

    def __init__(self):
        self.set = [0] * 31251

    def add(self, key: int) -> None:
        self.set[key // 32] |= self.getMask(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set[key // 32] ^= self.getMask(key)

    def contains(self, key: int) -> bool:
        return self.set[key // 32] & self.getMask(key) != 0

    def getMask(self, key: int) -> int:
        return 1 << (key % 32)

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)