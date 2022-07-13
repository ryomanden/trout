<div align="center">
  <img src="https://freesvg.org/img/Stylized-Fish-Silhouette.png" width="150px">
  <h1>Trout</h1>
  <p>
情報数学で作ったプログラムを、学習目的でライブラリ化しました。</p>
</div>

## なにこのライブラリ
情報数学で作ったプログラムを、学習目的でライブラリ化しました。

## インストール
```shell
pip install git+https://github.com/ryomanden/trout
```

## 使い方

### インポート
```python
import trout as tr
```
### 逆行列
2*2の配列で指定してください
```python
>>> tr.inverse([[2,3],[7,8]],26)
array([[14, 11],
       [17, 10]], dtype=object)
```
### ユークリッド
ユークリッドで求めた最小公倍数を返します。
余裕があれば、計算の履歴を配列で返すようにする予定です。
```python
>>> tr.euclid(120,77)
1
```
### 連立方程式
計算できます。
```python
>>> tr.renritsu([[2,3],[7,8]],[1,2],26)
array([10,11]d, type=object)
```
## RSA形式で暗号化・復号化
n進数の数値を暗号化・復号化します。
```python
>>> tr.rsa(493,43,6,545)
array(2102, dtype=object)
```