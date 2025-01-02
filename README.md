# atcoder_algorithm

## 使い方

### 1. 新規のABCワークスペースを作成
`$ cp abc_template/ abc{index} -r`\
例: `$ cp abc_template/ abc370 -r`

### 2. ABCの問題を解く
`abc{index}/scripts`ディレクトリ内にある、`{a..g}.py`にPythonプログラムを作成。

### 3. サンプルのコピー
`abc{index}/input_data`ディレクトリ内にある、`data{a..g}.txt`にテストケースの入力を貼りつける。

複数のサンプルを一括でテスト可能。\
下記の例のように、改行することで異なるサンプルとして実行される。

例: `abc_template/input_data/data_a.txt`

```
5 3
1 2 3 4 5

6 2
1 2 1 2 1 2

10 3
1 2 3 4 5 6 7 8 9 10
```

### 4. サンプルをローカルで実行
`$ ./local_tester.py abc{index} {a..g}`\
例: `$ ./local_tester.py abc370 a`

実行結果の例\
3つの異なるサンプルが、それぞれ実行される。\
`$ ./local_tester.py abc_template/ a` \

```
--- Execution 1 ---
3 4 5 1 2


--- Execution 2 ---
1 2 1 2 1 2


--- Execution 3 ---
8 9 10 1 2 3 4 5 6 7
```

## Link

* [AtCoder Contest](https://atcoder.jp/contests/)

* [アルゴリズムと数学　演習問題集](https://atcoder.jp/contests/math-and-algorithm)

* [競技プログラミングの鉄則　演習問題集](https://atcoder.jp/contests/tessoku-book)