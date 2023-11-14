---
title: "Bài tập lập trình: cờ vua"
permalink: /pythonAdventure-part1-chess/
layout: customPostLayout
date: 2022-03-01 21:45:00
last_modified_at: 2023-11-14
---

[Cờ vua](https://en.wikipedia.org/wiki/Chess) là một trò chơi hai người trên một bàn cờ hình vuông kích thước $8\times 8$ sử dụng các quân cờ có đặc điểm khác nhau. Luật chơi cờ vua có thể xem tại [đây](https://en.wikipedia.org/wiki/Rules_of_chess).

Chuỗi bài tập dưới đây là phiếu bài tập thứ hai của [lớp Tối ưu hóa MAT2407](http://seminar.optima.vn/opt).

## Yêu cầu chung
- Trình bày tất cả câu trả lời của những bài tập dưới đây trong **một file `.py` duy nhất**. Nếu sử dụng jupyter notebook thì cần chuyển đổi sang file `.py` trước khi nộp bài.
- Phần mở đầu phải có thông tin sinh viên (họ và tên, mã sinh viên, lớp đại học, lớp học phần) và danh sách những bài tập đã làm được, ví dụ như

    ```py
    """
    Thông tin nhóm
    Lê Phúc A, 21001234, K65TH
    Lê Nhật B, 21005678, K65TT

    Danh sách bài tập
    - Bài 1. getAllCells(), printChessboard()
    - Bài 2. getRandomElement()
    ...
    """
    ```

- Tên file đặt theo mẫu `NhomXX_BaiTap02_TenCacThanhVien.py` với `XX` là số thứ tự của nhóm và `TenCacThanhVien` là tên các thành viên viết liền không dấu, ví dụ
    + `Nhom07_BaiTap02_AnBinhChi.py`
    + `Nhom12_BaiTap02_AnBinhChi.py`
- Cần lựa chọn tên hàm phù hợp. Tên hàm có trong ví dụ (`foo, bar, ham, ...`) chỉ mang tính chất minh hoạ.
- Chỉ nên sử dụng hàm `print(), input()` nếu có yêu cầu. Hầu hết các hàm trong chuỗi bài đều yêu cầu trả về đối tượng cơ bản (kiểu `list`, `string`, `int`, ...).
- Trong quá trình làm bài, nên sử dụng lại những hàm đã viết trước đó để tránh trùng lặp code.
- Cần **bổ sung ví dụ** sau khi viết một hàm theo yêu cầu của đề bài để kiểm tra tính đúng đắn của chương trình. Xem mục **Minh họa lời giải của một bài tập** phía cuối bài viết này.


## Bài 1. Tọa độ trên bàn cờ
Tọa độ trên bàn cờ vua được quy ước dựa trên chỉ số hàng (rank) và chỉ số cột (file). Một tọa độ gồm hai ký tự, trong đó
- ký tự đầu tiên chỉ thứ tự cột, nhận một trong các giá trị `a`, `b`, `c`,  `d`, `e`, `f`, `g`, `h`.
- ký tự thứ hai chỉ thứ tự hàng, nhận một trong các giá trị `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`.

1. Viết một hàm trả về tọa độ của 64 ô trên bàn cờ.
2. (Điểm thưởng) Viết một hàm trả về tọa độ của 32 ô trắng của bàn cờ.
3. Viết một hàm **in ra terminal** tọa độ của tất cả các ô trên bàn cờ, sắp xếp theo góc nhìn của bên cầm quân trắng. Thông tin in ra màn hình có dạng

```
a8 b8 ... g8 h8
.. .. ... .. ..
.. .. ... .. ..
a1 b1 ... g1 h1
```

Gợi ý công cụ
- Vòng lặp `for` lồng nhau (nested for-loops)
- Tham số `end` trong hàm `print`
    ```py
    print('foobar', end='')
    ```
- [List comprehension](https://realpython.com/list-comprehension-python/)
- Thư viện [itertools](https://docs.python.org/3/library/itertools.html)


## Bài 2. Lấy phần tử ngẫu nhiên
Viết một hàm nhận vào một `list` và trả về một phần tử ngẫu nhiên trong danh sách đó. Cần đưa ra phương án xử lý phù hợp khi `list` đưa vào là rỗng.

```py
# first run
foo(['a1', 'a2', 'b3', 'c4']) # 'a1'
# second run
foo(['a1', 'a2', 'b3', 'c4']) # 'b3'
```

Bài tập này _có thể_ thực hiện theo các bước như sau:
- Tính độ dài $n$ của `list` truyền vào
- Lấy chỉ số $i$ là một số nguyên ngẫu nhiên trong đoạn $[0,n-1]$
- Trả về phần tử tại chỉ số $i$ của danh sách truyền vào

Câu hỏi thêm: cách thiết kế "trả về `None` khi `list` truyền vào là rỗng" có vấn đề gì?


## Bài 3. Lọc phần tử
Viết một hàm nhận vào hai `list` $A$, `list` $B$ và trả về `list` $C$ chứa các phần tử thuộc $A$ nhưng không thuộc $B$.


## Bài 4. (điểm thưởng) Nước đi của quân hậu
Quân hậu trong cờ vua di chuyển theo hàng ngang, hàng dọc hoặc đường chéo. Viết một hàm nhận vào một tọa độ trên bàn cờ vua thể hiện cho vị trí của một quân hậu và trả về một `list` những ô mà quân hậu đó có thể di chuyển tới trong một nước đi hợp lệ.

```py
bar('a1') # ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8']
```

## Bài 5. (điểm thưởng) FEN
Viết hàm nhận vào một Forsyth-Edwards Notation (FEN) và biểu diễn nó một cách phù hợp. Có thể sử dụng các thư viện hỗ trợ.

```py
ham('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1') # ...
```

Nguồn tham khảo: [Wikipedia](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) và [Lichess](https://lichess.org/editor).

<center>
    ------ Kết thúc phần bài tập ------
</center>


### Minh họa lời giải của một bài tập
Giả sử đề bài yêu cầu viết một hàm tính diện tích hình chữ nhật cho trước chiều dài và chiều rộng. Xét lời giải sau đây

```py
def foo(a, b):
    print(a * b)
value = foo(5, 4)
```

Đây là một lời giải _tồi_ với hai lý do sau đây
- Tên biến, tên hàm (`foo`, `a`, `b`) không có ý nghĩa.
- Hàm này không có tác dụng trong chương trình thực tế. Khi sử dụng hàm này, ta chỉ _nhìn thấy_ giá trị diện tích mà không có được giá trị này để thực hiện các bước tiếp theo. Trong ví dụ trên, giá trị của biến `value` là `None` chứ không phải là 20.

Ta viết lại hàm tính diện tích như sau

```py
def getArea(length, width):
    return length * width
```

Đoạn code trên đã sử dụng tên biến phù hợp, đồng thời _trả về_ giá trị diện tích. Tuy nhiên nó thiếu những ví dụ để thể hiện tính đúng đắn của chương trình. Cách đơn giản nhất là sử dụng hàm đã cho với một số bộ giá trị đầu vào cho trước, rồi in ra kết quả để so sánh. Chương trình đầy đủ sẽ là

```py
def getArea(length, width):
    return length * width

print(getArea(10, 4)) # 40
print(getArea(7, 5)) # 35
print(getArea(6, 6)) # 36
```
