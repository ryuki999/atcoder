"""行列処理用のライブラリ
"""


def rotate90(A):
    """正方行列を右に90度回転させた行列を得る
    m = [[0, 1, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]]
    for i in rotate90(m):
        print(i)
    """
    H, W = len(A), len(A[0])
    ans = [[""] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            ans[j][W - 1 - i] = A[i][j]
    return ans
