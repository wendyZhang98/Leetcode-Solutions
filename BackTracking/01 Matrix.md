### Description:
<img width="588" alt="Screen Shot 2022-02-12 at 23 52 13" src="https://user-images.githubusercontent.com/49216429/153739211-160971e8-e177-46e5-bae5-8fef6170d81e.png">

### Examples:
<img width="583" alt="Screen Shot 2022-02-12 at 23 52 24" src="https://user-images.githubusercontent.com/49216429/153739216-5e0ab030-a59e-499a-8989-1a7c0b11dc5e.png">

### Solutions:
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
