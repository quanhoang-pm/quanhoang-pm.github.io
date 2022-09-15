---
title: "Chess-related problems"
permalink: /pythonAdventure-part1-chess/
layout: customPostLayout
date: 2022-03-01 21:45:00
last_modified_at: 2022-09-15
---

[Cờ vua](https://en.wikipedia.org/wiki/Chess) là một trò chơi hai người trên một bàn cờ hình vuông kích thước $8\times 8$ với các quân cờ có đặc điểm khác nhau. Luật chơi cờ vua có thể xem tại [đây](https://en.wikipedia.org/wiki/Rules_of_chess).

Chuỗi bài tập dưới đây là phiếu bài tập đầu tiên của [lớp Tối ưu hóa MAT2407](http://seminar.optima.vn/opt). Nó cung cấp công cụ giúp trả lời một câu hỏi không quá hiển nhiên liên quan tới cờ vua:

> Khi đặt đủ 8 quân cờ bao gồm 1 vua, 1 hậu, 2 xe, 2 tượng (khác màu), 2 mã lên trên bàn cờ thì số ô không bị tấn công cực đại/cực tiểu là bao nhiêu?


## Yêu cầu chung
- Trình bày tất cả câu trả lời của những bài tập dưới đây trong **một file jupyter notebook (hoặc một file py) duy nhất** với phần mở đầu ghi đầy đủ thông tin sinh viên (họ và tên, mã sinh viên, lớp đại học, lớp học phần) và mục lục liệt kê những bài tập đã làm được. Tên file đặt theo mẫu `NhomX_BaiTap01.ipynb` hoặc `NhomX_BaiTap01.py`, ví dụ `Nhom07_BaiTap01.py`.
- Nhóm sinh viên đạt **điểm tối đa** cho bài tập lần này nếu **làm trọn vẹn 5 bài đầu tiên của chuỗi bài, bỏ qua những câu hỏi thêm**. Có thể thực hiện những ý còn lại để nhận điểm thưởng.
- Cần lựa chọn tên hàm phù hợp. Tên hàm có trong ví dụ (`foo, bar, ham, ...`) chỉ mang tính chất minh hoạ.
- Chỉ thực hiện hàm `print()` nếu có yêu cầu. Hầu hết các hàm trong chuỗi bài đều yêu cầu trả về đối tượng (kiểu `list`, `string`, `int`, ...)
- Trong quá trình làm bài, nên sử dụng lại những hàm đã viết trước đó để tránh trùng lặp code.
- Cần **bổ sung ví dụ** sau khi viết một hàm theo yêu cầu của đề bài để kiểm tra tính đúng đắn của chương trình. Xem mục **Minh họa lời giải của một bài tập** phía cuối bài viết này.



## Bài 1. Tọa độ trên bàn cờ
Tọa độ trên bàn cờ vua được quy ước dựa trên chỉ số hàng (gọi là rank) và chỉ số cột (gọi là file). Một tọa độ gồm hai ký tự, trong đó
- ký tự đầu tiên chỉ thứ tự cột, nhận một trong các giá trị `a`, `b`, `c`,  `d`, `e`, `f`, `g`, `h`.
- ký tự thứ hai chỉ thứ tự hàng, nhận một trong các giá trị `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`.

Viết một hàm kiểm tra tính hợp lệ của tọa độ trên bàn cờ vua với input/output như sau:
```py
# Input: một string
# Output: True / False
# Ví dụ
foo('Aone') # False
foo('A1') # False
foo('1a') # False
foo('a1.') # False
foo('a1') # True
```

(Câu hỏi thêm) Viết một hàm với yêu cầu như trên, trong đó _không khai báo_ 8 string chữ cái từ `a` đến `h` mà chỉ khai báo hai string `a` và `h`. Gợi ý: sử dụng bảng mã ASCII.


## Bài 2. Tọa độ trên bàn cờ
1. Viết một hàm trả về tọa độ của bốn quân xe trong [vị trí khởi đầu tiêu chuẩn](https://lichess.org/editor) của một ván cờ vua, đặt trong một list (hoặc một tuple).
2. Viết một hàm trả về tọa độ của 64 ô trên bàn cờ.
3. Viết một hàm trả về tọa độ của 32 ô trắng trên bàn cờ.
4. (Câu hỏi thêm) Viết một hàm **in ra màn hình** (sử dụng hàm `print`) tọa độ của tất cả các ô trên bàn cờ, sắp xếp theo góc nhìn của bên cầm quân trắng. Thông tin in ra màn hình có dạng

```
a8 b8 ... g8 h8
.. .. ... .. ..
.. .. ... .. ..
a1 b1 ... g1 h1
```

Gợi ý về công cụ sử dụng
- Vòng lặp `for` (hai vòng lặp)
- [List comprehension](https://realpython.com/list-comprehension-python/)
- Thư viện [itertools](https://docs.python.org/3/library/itertools.html)


## Bài 3. Kiểm tra thẳng hàng
Viết một hàm kiểm tra xem hai ô đưa vào có cùng hàng ngang hoặc cột dọc hay không, trong đó
- Input: hai `string` tọa độ trên bàn cờ vua
- Output: `True` / `False`
- Ví dụ:
```py
bar('a1', 'a1') # True
bar('a1', 'c2') # False
bar('a1', 'a8') # True
bar('c3', 'e3') # True
```

(Câu hỏi thêm) Bổ sung vào hàm vừa viết tính năng báo lỗi khi giá trị truyền vào không hợp lệ.


## Bài 4. Nước đi của quân xe (rooks' moves)
Ta quan tâm tới các quân cờ, bắt đầu với quân xe. Đặt một quân xe lên một bài cờ trống, hãy viết một hàm liệt kê tất cả những tọa độ mà quân xe này có thể di chuyển tới trong một nước đi hợp lệ.
- Input: một `string` gồm ba ký tự, ký tự đầu là `R` và hai ký tự sau là tọa độ hiện tại của quân xe.
- Output: một `list` các ô mà quân xe có thể di chuyển tới trong một nước đi hợp lệ.
- Ví dụ:
```py
ham('Ra2') # ['a1', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
```

(Câu hỏi thêm) Sắp xếp các tọa độ trả về của hàm này theo khoảng cách Euclid tăng dần từ ô xuất phát tới ô đang xét. Trong hai ô có cùng khoảng cách tới ô xuất phát, ô nào có chỉ số hàng thấp hơn thì xếp trước.


## Bài 5. Nước đi của quân tượng (bishops' moves)

Đặt một quân tượng lên một bàn cờ trống. Hãy viết một hàm liệt kê các vị trí mà quân tượng này có thể di chuyển tới trong một nước đi (hợp lệ).
- Input: một string gồm ba ký tự, ký tự đầu là `B` và hai ký tự sau là tọa độ hiện tại của quân tượng.
- Output: một `list` các ô mà quân tượng có thể di chuyển tới trong một nước đi hợp lệ.
- Ví dụ:
```py
ham('Ba2') # ['b1', 'b3', 'c4', 'd5', 'e6', 'f7', 'g8']
```

Gợi ý. Dựa theo ý tưởng của bài 3 và bài 4.


## Bài 6. Những quân cờ còn lại
Ngoài xe và tượng, cờ vua còn có ba loại quân khác, lần lượt là vua (king), hậu (queen), và mã (knight). Hãy viết hàm với yêu cầu tương tự bài 5 cho từng quân cờ trong số ba quân cờ này.
```py
bar('Kf4') # ...
sor('Qa1') # ...
zer('Nb2') # ...
```

## Bài 7. Sự liên kết giữa các tọa độ
Hai ô trên bàn cờ vua được gọi là liên kết với nhau nếu chúng phân biệt và có chung hàng, cột, hoặc đường chéo. Cho hai ô `A` và `B` liên kết với nhau, một ô `C` được gọi là nằm giữa `A` và `B` nếu ô đó khác hai ô `Á, B` và nằm trên đoạn thẳng nối ô `A` và ô `B`.

1. Viết một hàm (trả về `True`/`False`) kiểm tra tính liên kết của hai tọa độ được cung cấp.
2. Viết một hàm liệt kê tất cả những ô nằm giữa hai ô liên kết.

```py
ham1('a1', 'a4') # True
ham1('c2', 'h8') # False
ham1('a1', 'h8') # True

egg2('a1', 'a3') # ['a2']
egg2('a1', 'a2') # []
```


## Bài 8. Đếm số ô cờ không bị tấn công
Một ô cờ được gọi là bị tấn công nếu thỏa mãn một trong hai điều kiện sau:
- Có một quân cờ tại vị trí đó.
- Ô đó trống và một quân cờ có thể thực hiện một nước đi hợp lệ để di chuyển đến ô đó.
Cần chú ý tình huống khi các hướng tấn công/di chuyển của một quân cờ bị chặn bởi một quân cờ khác.

Đặt các quân cờ _cùng màu_ vào các tọa độ trên một bàn cờ trống. Viết hàm tính số lượng các ô không bị tấn công trên bàn cờ này.
- Input: một `list` các quân cờ kèm theo tọa độ của chúng
- Output: số ô không bị tấn công trên bàn cờ
- Ví dụ:
```py
qux(['Ra1', 'Rb2', 'Rc3', 'Rd4', 'Re5', 'Rf6', 'Rg7', 'Rh8']) # 0
qux(['Ra1', 'Rb2', 'Rc3', 'Rd4', 'Re5', 'Rf6']) # 4
qux(['Qa1', 'Ra2', 'Rb1', 'Rb2']) # 36
qux(['Qa1', 'Ra2', 'Rb1']) # 42
```


## Bài 9. Câu hỏi cuối cùng
> Khi đặt đủ 8 quân cờ bao gồm 1 vua, 1 hậu, 2 xe, 2 tượng (khác màu), 2 mã lên trên bàn cờ thì số ô không bị tấn công cực đại/cực tiểu là bao nhiêu?

Đặt 8 quân cờ như mô tả trong câu hỏi trên lên một bàn cờ trống sao cho mỗi ô có tối đa một quân cờ. Tìm giá trị lớn nhất và giá trị nhỏ nhất của số ô không bị tấn công trên bàn cờ.

Với câu hỏi này, bạn có thể thử nghiệm với bàn cờ tại [đây](https://lichess.org/editor). Khi đã hài lòng với cách sắp xếp các quân cờ, hãy sao chép [FEN notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) phía dưới bàn cờ, rồi dán `string` này vào đoạn code Python dưới đây

```py
import chess
import chess.svg

FENNotationStr = '8/8/8/8/8/8/8/RNBQKBNR w - - 0 1'
board = chess.Board(FENNotationStr)
boardsvg = chess.svg.board(board = board)
with open('image.svg', 'w') as f:
    f.write(boardsvg)
```

**Ghi chú.** Bài toán này _có thể được giải quyết_ bởi mô hình tối ưu nguyên (IP model).


## Tài liệu tham khảo
Chuỗi bài tập này được truyền cảm hứng từ mục **7.4 War Story: Covering Chessboards** trong cuốn sách _The algorithm design manual_ (2nd edition, 2008, Springer-Verlag London) của tác giả Steven S. Skiena.


### Minh họa lời giải của một bài tập
Giả sử đề bài yêu cầu viết một hàm tính diện tích hình chữ nhật cho trước chiều dài và chiều rộng. Xét lời giải sau đây

```py
def foo(a, b):
    print(a * b)
value = foo(5, 4)
```

Đây là một lời giải _tồi_ với hai lý do sau đây
- Tên biến, tên hàm (foo, a, b) không có ý nghĩa.
- Hàm này không có tác dụng trong chương trình thực tế. Khi sử dụng hàm này, ta chỉ _nhìn thấy_ giá trị diện tích mà không có được giá trị này để thực hiện các bước tiếp theo. Trong ví dụ trên, giá trị của biến `value` là `None` chứ không phải là 20.

Ta viết lại hàm tính diện tích như sau

```py
def getArea(length, width):
    return length * width
```

Đoạn code trên đã sử dụng tên biến phù hợp, đồng thời _trả về_ giá trị diện tích. Tuy nhiên nó chưa có những ví dụ để thể hiện tính đúng đắn của chương trình. Cách đơn giản nhất là sử dụng hàm đã cho với một số bộ giá trị đầu vào cho trước, rồi in ra kết quả để so sánh. Chương trình đầy đủ sẽ là

```py
def getArea(length, width):
    return length * width

print(getArea(10, 4)) # 40
print(getArea(7, 5)) # 35
print(getArea(6, 6)) # 36
```

Nâng cao hơn một chút, ta có thể sử dụng hàm `assert` hoặc thư viện `pytest` để chuẩn hóa quy trình kiểm thử chương trình.
