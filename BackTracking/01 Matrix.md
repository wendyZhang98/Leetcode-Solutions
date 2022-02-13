### Description:
<img width="588" alt="Screen Shot 2022-02-12 at 23 52 13" src="https://user-images.githubusercontent.com/49216429/153739211-160971e8-e177-46e5-bae5-8fef6170d81e.png">

### Examples:
<img width="583" alt="Screen Shot 2022-02-12 at 23 52 24" src="https://user-images.githubusercontent.com/49216429/153739216-5e0ab030-a59e-499a-8989-1a7c0b11dc5e.png">

### Solutions:
- https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space


<img width="1318" alt="Screen Shot 2022-02-12 at 23 58 18" src="https://user-images.githubusercontent.com/49216429/153739361-e796422a-1966-4ec2-997e-b313363214ed.png">

```
class Solution:  # 520 ms, faster than 96.50%
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat
```

<img width="1280" alt="Screen Shot 2022-02-13 at 00 03 44" src="https://user-images.githubusercontent.com/49216429/153739478-59a2d50e-e753-40a3-8167-81a78e4ef9ae.png">

```
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        DIR = [0, 1, 0, -1, 0]

        q = deque([])
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1  # Marked as not processed yet!

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + DIR[i], c + DIR[i + 1]
                if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
                mat[nr][nc] = mat[r][c] + 1
                q.append((nr, nc))
        return mat
```
