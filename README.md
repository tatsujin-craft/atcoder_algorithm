# atcoder_algorithm

## 1. 使い方

### 1.1. ワークスペース作成
各ABCコンテストごとに、新規ワークスペースを作成。\
(テンプレートをコピーする。)

`$ cp template_abc/ <directory name> -r`\
例: `$ cp template_abc/ abc368 -r`

### 1.2. プログラム作成
Pythonプログラムを作成する場合\
`scripts`ディレクトリ内にある、`{a..g}.py`にPythonプログラムを作成。

C++プログラムを実行する場合\
`src`ディレクトリ内にある、`{a..g}.cpp`にC++プログラムを作成。

### 1.3. サンプルのコピー
`<directory>input_data`ディレクトリ内にある、`data{a..g}.txt`にテストケースの入力を貼りつける。

複数のサンプルを一括でテスト可能。\
下記の例のように、サンプル末尾に空行を追加することで、異なる3つのサンプルとして実行される。

例: `template_abc/input_data/data_a.txt`

```
5 3
1 2 3 4 5

6 2
1 2 1 2 1 2

10 3
1 2 3 4 5 6 7 8 9 10
```

### 1.4. サンプルをローカルで実行
`$ ./local_tester.py <directory name> <file name>`\
例: `$ ./local_tester.py abc368 a`

※ ファイル名の拡張子は不要 (a.py => a)

実行結果の例\
異なる3つのサンプルが、それぞれ実行される。\
`$ ./local_tester.py template_abc/ a` \

```
--- Execution 1 ---
3 4 5 1 2


--- Execution 2 ---
1 2 1 2 1 2


--- Execution 3 ---
8 9 10 1 2 3 4 5 6 7
```

C++プログラムを実行する場合\
`--cpp`オプションを指定する\
`$ ./local_tester.py template_abc/ a --cpp`

### 1.5. その他

* 鉄則問題集(`tessoku`)の実行例\
`$ ./local_tester.py tessoku a03`

* 典型アルゴリズム問題集(`typical`)の実行例\
`$ ./local_tester.py typical/ 001`

* アルゴリズムと数学の演習問題(`algorithm_math`)の実行例\
`$ ./local_tester.py algorithm_math/ 028`

* ABC過去門(`past_abc`)の実行例\
`$ ./local_tester.py past_abc/ 365_a`

* 練習用プログラムを実行\
`--prac`オプションを指定する\
`$ ./local_tester.py template_abc/ a --prac`

## 2. 参考リンク

* [AtCoder コンテスト一覧](https://atcoder.jp/contests/)

* [競技プログラミングの鉄則 演習問題集](https://atcoder.jp/contests/tessoku-book)

* [競プロ典型 90問](https://atcoder.jp/contests/typical90)

* [アルゴリズムと数学 演習問題集](https://atcoder.jp/contests/math-and-algorithm)
