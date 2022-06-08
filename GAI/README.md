## Generate Attachment Images

portalbotに使うための画像生成用のライブラリ


---

構造は以下のようになっている


<pre>
.
├── GAI
│   ├── README.md
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── daily_calendar.cpython-39.pyc
│   │   ├── information_card.cpython-39.pyc
│   │   ├── placeholder.cpython-39.pyc
│   │   └── weekly_calendar.cpython-39.pyc
│   ├── daily_calendar.py
│   ├── information_card.py
│   ├── placeholder.py
│   └── weekly_calendar.py
├── cache
│   └── out.png
├── font
│   └── Roboto-Regular.ttf
├── img
└── test.py
</pre>

関数の引数はdict形式、生成された画像はcacheに保存されるものとする。**dictの構造を決定しろ**