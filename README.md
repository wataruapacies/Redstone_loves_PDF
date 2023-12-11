i love pdf https://www.ilovepdf.com/ja でもPDFの分割・結合はできるが，
ファイルサイズが大きい場合やネット速度が大きい場合は使えない．

このPythonプログラムを使えばネット速度・ファイルサイズに関係なく
PDFの分割．結合ができる．

<br>
＜使い方＞<br>
Pythonのインストール https://www.python.org/downloads/
<br>
最新バージョンのインストールで良い<br>

```
py -V
```
で何かバージョンが返ってきたらインストール完了<br>


その後，以下コマンド<br>

```
pip install pycryptodome==3.15.0
```
```
pip install PyPDF2==3.0.1
```

このプログラムを分割したいPDFのあるディレクトリに置いて<br>
```
py split_PDF.py
```

結合は<br>
```
py merge_PDF.py
```