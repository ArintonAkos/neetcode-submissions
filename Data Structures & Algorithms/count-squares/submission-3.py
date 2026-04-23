
class CountSquares:

    def __init__(self):
        self.pts = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0
        
        # Itt nem kell list(), ha a cikluson belül NEM módosítjuk a dict-et
        for (x, y), freq in self.pts.items():
            
            if (abs(qx - x) != abs(qy - y)) or (qx == x):
                continue
            
            # JAVÍTÁS: .get() használata [] helyett!
            # Ez NEM ír a dictionary-be, csak olvas.
            count1 = self.pts.get((x, qy), 0)
            count2 = self.pts.get((qx, y), 0)
            
            res += freq * count1 * count2
            
        return res