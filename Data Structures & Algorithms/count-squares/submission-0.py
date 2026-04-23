class CountSquares:

    def __init__(self):
        self.pts_by_x = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.pts_by_x[x][y] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        res = 0

        if qx not in self.pts_by_x:
            return 0
            
        y_counts = self.pts_by_x[qx]
        
        for y, count in y_counts.items():
            if y == qy: continue 
            
            side_len = abs(qy - y)
            
            left_x = qx - side_len
            if left_x in self.pts_by_x:
                res += count * self.pts_by_x[left_x][qy] * self.pts_by_x[left_x][y]
            
            right_x = qx + side_len
            if right_x in self.pts_by_x:
                res += count * self.pts_by_x[right_x][qy] * self.pts_by_x[right_x][y]
                
        return res
