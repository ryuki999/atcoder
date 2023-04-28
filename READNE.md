# 戦い方
### 組み合わせ
以下の公式が成り立つ。
```
2^N = nC0 + nC1 + ... + nCn-1 + nCn
```

### 繰り返し二乗法
* 組み合わせ・場合の数を求める問題
* 素数pに対しn^(p-2)(mod p)を計算→逆元
* 数だけでなく行列などの累乗も計算できる

### 深さ優先探索/幅優先探索
* 深さ優先探索の注意
 * Pypyでは再帰が深くなるとTLEが増えるため、Pythonの方が良い場合がある
 * `sys.setrecursionlimit(10**6)`などを指定しないとREする
 * 

### PythonとPypyの整数値の特徴
* Pythonは多倍長整数が使えるが、数値が2^63-1を超えるとTLEの原因になる
  * C++のlong long型でも数値が2^63-1を超えるとオーバーフローする

### 幾何
https://blog.hamayanhamayan.com/entry/2018/02/27/105814
  

### やりがちなエラー
https://kakedashi-engineer.appspot.com/2020/02/11/procon-miss/
