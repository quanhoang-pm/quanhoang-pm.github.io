---
title: "Chess-related problems"
permalink: /pythonAdventure-part1-chess/
layout: customPostLayout
date: 2022-03-01 21:45:00
last_modified_at: 2022-03-02
---

[Cờ vua](https://en.wikipedia.org/wiki/Chess) là một trò chơi hai người trên một bàn cờ hình vuông kích thước $8\times 8$ với các quân cờ có đặc điểm khác nhau. Luật chơi cờ vua có thể xem tại [đây](https://en.wikipedia.org/wiki/Rules_of_chess).

Mục tiêu của chuỗi bài tập dưới đây, ngoài việc là bài tập lần thứ hai của [lớp Tối ưu hóa HKII 2021-2022](http://seminar.optima.vn/opt), còn là một dịp để giới thiệu về một câu đố liên quan tới cờ vua:

> Khi đặt đủ 8 quân cờ bao gồm 1 vua, 1 hậu, 2 xe, 2 tượng, 2 mã lên trên bàn cờ thì số ô không bị tấn công cực đại/cực tiểu là bao nhiêu?


## Yêu cầu chung
- Trình bày tất cả câu trả lời của những bài tập dưới đây trong **một file jupyter notebook duy nhất** với phần mở đầu ghi đầy đủ thông tin sinh viên (họ và tên, mã sinh viên, lớp đại học, lớp học phần). Tên file đặt theo đúng hướng dẫn, chỉ thay đổi phần đuôi từ `pdf` sang `ipynb`.
- Nhóm sinh viên đạt **điểm tối đa** cho bài tập lần này nếu **làm trọn vẹn 5 bài đầu tiên của chuỗi bài, bỏ qua những ý bonus**. Có những cách khác để đạt điểm tối đa.
- Cần đặt tên hàm trong lời giải một cách phù hợp. Tên hàm trong ví dụ chỉ mang tính chất minh hoạ.
- Chỉ thực hiện hàm `print()` nếu có yêu cầu. Hầu hết các hàm trong chuỗi bài đều yêu cầu trả về đối tượng (kiểu `list`, `string`, `int`, ...)
- Trong quá trình làm bài, nên sử dụng lại những hàm đã viết trước đó để tránh trùng lặp code.
- Phải **bổ sung ví dụ** sau khi viết một hàm theo yêu cầu của đề bài để **kiểm tra tính đúng đắn của hàm**. Ví dụ như:

```py
def getArea(length, width):
    return length * width

print(getArea(10, 4)) # 40
print(getArea(7, 5)) # 35
print(getArea(6, 6)) # 36
```


## Bài 1. Tọa độ trên bàn cờ
Tọa độ trên bàn cờ vua được quy ước dựa trên chỉ số hàng (gọi là rank) và chỉ số cột (gọi là file). Một tọa độ gồm hai ký tự, trong đó
- ký tự đầu tiên chỉ thứ tự cột, nhận một trong các giá trị `a`, `b`, `c`,  `d`, `e`, `f`, `g`, `h`.
- ký tự thứ hai chỉ thứ tự hàng, nhận một trong các giá trị `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`.

1. Viết một hàm kiểm tra tính hợp lệ của tọa độ trên bàn cờ vua với mô tả sau:
- Input: một `string`
- Output: `True` / `False`
- Ví dụ:
```py
foo('Aone') # False
foo('A1') # False
foo('1a') # False
foo('a1.') # False
foo('a1') # True
```

2. (Bonus) Viết một hàm với yêu cầu như trên, trong đó _không khai báo_ các string chữ cái. Gợi ý: sử dụng ASCII code.


## Bài 2. Tọa độ trên bàn cờ
1. Viết một hàm trả về tọa độ của những quân xe trong [vị trí khởi đầu tiêu chuẩn](https://lichess.org/editor) của một ván cờ vua.
2. Viết một hàm trả về tọa độ của 64 ô trên bàn cờ.
3. Viết một hàm trả về tọa độ của 32 ô trắng trên bàn cờ.
4. (Bonus) Viết một hàm **in ra màn hình** tọa độ của tất cả các ô trên bàn cờ, sắp xếp theo góc nhìn của bên cầm quân trắng. Thông tin in ra màn hình có dạng
```txt
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
bar('a1', 'c2') # False
bar('a1', 'a8') # True
bar('c3', 'e3') # True
```

Bonus. Bổ sung vào hàm vừa viết tính năng báo lỗi khi input không hợp lệ.


## Bài 4. Nước đi của quân xe (rook's moves)
Ta quan tâm tới các quân cờ, bắt đầu với quân xe. Đặt một quân xe lên một bài cờ trống, ta cần liệt kê tất cả những tọa độ mà quân xe này có thể di chuyển tới trong một nước đi hợp lệ. Hãy viết một hàm thực hiện việc này với mô tả như sau:
- Input: một `string` gồm ba ký tự, ký tự đầu là `R` và hai ký tự sau là tọa độ hiện tại của quân xe.
- Output: một `list` các ô mà quân xe có thể di chuyển tới trong một nước đi hợp lệ.
- Ví dụ:
```py
ham('Ra2') # ['a1', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
```

Bonus. Sắp xếp các tọa độ trả về của hàm này theo khoảng cách Euclid tăng dần từ ô xuất phát tới ô đang xét. Trong hai ô có cùng khoảng cách tới ô xuất phát, ô nào có chỉ số hàng thấp hơn thì xếp trước.


## Bài 5. Nước đi của quân tượng (bishop's moves)

Đặt một quân tượng lên một bàn cờ trống. Hãy viết một hàm liệt kê các vị trí mà quân tượng này có thể di chuyển tới, hàm cần viết có mô tả như sau:
- Input: một string gồm ba ký tự, ký tự đầu là `B` và hai ký tự sau là tọa độ hiện tại của quân tượng.
- Output: một `list` các ô mà quân tượng có thể di chuyển tới trong một nước đi hợp lệ.
- Ví dụ:
```py
ham('Ba2') # ['b1', 'b3', 'c4', 'd5', 'e6', 'f7', 'g8']
```

Gợi ý. Dựa theo ý tưởng của bài 3 và bài 4.


## Bài 6. Những quân cờ còn lại (king, queen, knight)
Ngoài xe và tượng, cờ vua còn có ba loại quân khác, lần lượt là vua, hậu, và mã. Hãy viết hàm với yêu cầu tương tự bài 5 cho từng quân trong số ba quân cờ này.
```py
bar('Kf4')
sor('Qa1')
zer('Nb2')
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


## Bài 8. Free squares enumeration
Một ô bị tấn công nếu nó trống và một quân cờ có thể thực hiện một nước đi hợp lệ để di chuyển đến ô đó. Cần chú ý tình huống khi các hướng tấn công/di chuyển của một quân cờ bị chặn bởi một quân cờ khác. Ta quy ước một quân cờ luôn có thể tấn công chính ô nó đang đứng.

Viết hàm tính số lượng các ô không bị tấn công trên bàn cờ dựa theo tọa độ các quân cờ cho trước.
- Input: một `list` các quân cờ kèm theo tọa độ của chúng
- Output: số ô không bị tấn công trên bàn cờ
- Ví dụ:
```py
qux(['Ra1', 'Rb2', 'Rc3', 'Rd4', 'Re5', 'Rf6', 'Rg7', 'Rh8']) # 0
qux(['Ra1', 'Rb2', 'Rc3', 'Rd4', 'Re5', 'Rf6']) # 4
qux(['Qa1', 'Ra2', 'Rb1', 'Rb2']) # 36
qux(['Qa1', 'Ra2', 'Rb1']) # 42
```


## Bài 9. The last question
> Khi đặt đủ 8 quân cờ bao gồm 1 vua, 1 hậu, 2 xe, 2 tượng, 2 mã lên trên bàn cờ thì số ô không bị tấn công cực đại/cực tiểu là bao nhiêu?

Sử dụng 8 quân cờ như trong câu hỏi trên, đặt chúng lên một bàn cờ trống sao cho số ô không bị tấn công là:
1. Ít nhất có thể.
2. Nhiều nhất có thể.

Với câu hỏi này, bạn có thể thử nghiệm với bàn cờ tại [đây](https://lichess.org/editor). Khi đã hài lòng với cách sắp xếp các quân cờ, hãy sao chép [FEN notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) ở ngay dưới bàn cờ, rồi dán `string` này vào đoạn code Python dưới đây

```py
import chess
import chess.svg

FENNotationStr = '8/8/8/8/8/8/8/RNBQKBNR w - - 0 1'
board = chess.Board(FENNotationStr)
boardsvg = chess.svg.board(board = board)
with open('foobar.svg', 'w') as f:
    f.write(boardsvg)
```


## Tài liệu tham khảo
Chuỗi bài tập này được truyền cảm hứng từ mục **7.4 War Story: Covering Chessboards** trong cuốn sách _The algorithm design manual_ (2nd edition, 2008, Springer-Verlag London) của tác giả Steven S. Skiena.

Chúc mọi người tìm được cảm hứng với toán học, Python, và cờ vua.
