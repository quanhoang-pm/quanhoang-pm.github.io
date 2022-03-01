---
title: "Chess-related problems"
permalink: /pythonAdventure-part1-chess/
layout: customPostLayout
date: 2022-03-01 21:45:00
last_modified_at: 2020-03-01
---

Trình bày tất cả trong một file jupyter notebook (mẫu dưới đây)

Được 10 điểm nếu làm những ý sau:
Bài 1. a, b, c,
Bài 2. ....

Với tất cả những ý yêu cầu viết hàm/chương trình, cần bổ sung một số ví dụ ngay trong cell của notebook

Tên hàm cần đặt một cách phù hợp. Tên hàm trong ví dụ chỉ mang tính chất minh hoạ

Khi viết hàm xong thì cần viết các lệnh để test phía sau.

Hàm có thể gọi các hàm con khác

Trả về đối tượng,
không in.


# --------------------------------------------------------------------------- #

[Cờ vua](https://en.wikipedia.org/wiki/Chess) là một trò chơi hai người trên một bàn cờ hình vuông kích thước $8\times 8$ với các quân cờ có đặc điểm khác nhau. Luật chơi cờ vua có thể xem tại [đây](https://en.wikipedia.org/wiki/Rules_of_chess).

Mục tiêu của chuỗi bài tập dưới đây, ngoài việc là bài tập lần thứ hai của lớp Tối ưu hóa HKII 2021-2022, còn là một dịp để giới thiệu về một câu đố liên quan tới cờ vua:

> Khi đặt đủ 8 quân cờ: 1 vua, 1 hậu, 2 xe, 2 tượng, 2 mã lên trên bàn cờ thì số ô không bị KIỂM SOÁT cực đại/cực tiểu lần lượt là bao nhiêu?

## Bài 1. Tọa độ trên bàn cờ
Tọa độ trên bàn cờ vua được quy ước dựa trên tọa độ hàng (gọi là rank) và tọa độ cột (gọi là file). Một tọa độ gồm hai ký tự, trong đó
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

2. (Bonus) Viết một hàm kiểm tra tính hợp lệ của tọa độ, trong đó _không khai báo_ các string chữ cái. Gợi ý: sử dụng ASCII code.

## Bài 2. Tọa độ trên bàn cờ
1. Viết một hàm trả về tọa độ của những quân xe trong [vị trí khởi đầu tiêu chuẩn](https://lichess.org/editor) trong một ván cờ vua.
2. Viết một hàm trả về tọa độ của 64 ô của bàn cờ
3. Viết một hàm trả về tọa độ của 32 ô trắng của bàn cờ
4. (Bonus) Viết một hàm in ra 64 tọa độ của bàn cờ đặt trong các ô của bàn cờ theo góc nhìn của bên cầm quân trắng. Tức là
```txt
a8 b8 ... g8 h8
.. .. ... .. ..
.. .. ... .. ..
a1 b1 ... g1 h1
```

Gợi ý công cụ sử dụng
- Hai vòng lặp `for`
- [List comprehension](https://realpython.com/list-comprehension-python/)
- Thư viện [itertools](https://docs.python.org/3/library/itertools.html)


## Bài 3. Kiểm tra thẳng hàng
1. Viết một hàm kiểm tra xem hai ô đưa vào có cùng hàng ngang hoặc cột dọc hay không
- Input: hai string tọa độ trên bàn cờ vua
- Output: `True` / `False`
- Ví dụ:
```py
bar('a1', 'c2') # False
bar('a1', 'a8') # True
```

2. (Bonus) Bổ sung vào hàm vừa viết tính năng báo lỗi khi input không hợp lệ.


## Bài 4. Nước đi của quân xe (Rook's moves)
Ta bắt đầu quan tâm tới các quân cờ, bắt đầu với quân xe. Đặt một quân xe lên một bài cờ trống, ta cần liệt kê tất cả những tọa độ mà quân xe có thể di chuyển tới trong một nước đi hợp lệ. Hãy viết một hàm thực hiện việc này với mô tả như sau:
- Input: một string gồm ba ký tự, ký tự đầu là `R` và hai ký tự sau là tọa độ hiện tại của quân xe.
- Output: một list các ô mà quân xe có thể di chuyển tới
- Ví dụ:
```py
ham('Ra2') # ['a1', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
```

Điểm thưởng. Sắp xếp các tọa độ trả về của hàm này theo khoảng cách Euclid tăng dần từ ô xuất phát tới ô đang xét. Trong hai ô có cùng khoảng cách tới ô xuất phát, ô nào có chỉ số hàng thấp hơn thì xếp trước.


## Bài 5. Nước đi của quân tượng (bishop)

- Input: một string gồm ba ký tự, ký tự đầu là `B` và hai ký tự sau là tọa độ hiện tại của quân tượng.
- Output: một list các ô mà quân tượng có thể di chuyển tới
- Ví dụ:
```py
ham('Ba2') # ['b1', 'b3', 'c4', 'd5', 'e6', 'f7', 'g8']
```
Gợi ý. dựa theo ý tưởng của bài 3 đối với quân xe, viết hàm tương tự cho quân tượng.


## Bài 6. Những quân cờ còn lại (king, queen, knight)
Ngoài xe và tượng, cờ vua còn có ba loại quân khác, lần lượt là vua, hậu, và mã. Hãy viết các hàm thực hiện công việc tương tự mô tả trong bài 4 và bài 5 cho những quân cờ này. Ví dụ
```py
bar('Kf4')
sor('Qa1')
zer('Nb2')
```

## Bài 7.
Hai ô trên bàn cờ vua được gọi là liên kết với nhau nếu chúng phân biệt và có chung hàng, cột, hoặc đường chéo. Cho hai ô `A` và `B`  liên kết với nhau, một ô `C` được gọi là nằm giữa `A` và `B` nếu ô đó thỏa mãn
- Khác hai ô `Á` và `B`
- Nằm trên đoạn thẳng nối hai ô `A` và `B`.

1. Viết một hàm kiểm tra tính liên kết của hai tọa độ nhập vào
2. Viết một hàm liệt kê tất cả những ô nằm giữa hai ô liên kết nhập vào.
```py
ham1('a1', 'a4') # True
egg2('a1', 'a3') # ['a2']
egg2('a1', 'a2') # []
```

## Bài 8.
Di chuyển hợp lệ theo luật cờ vua.
Một ô trống nếu nó không bị chiếm
Một ô bị tấn công nếu nó trống và một quân cờ có thể thực hiện một nước đi hợp lệ để tấn công ô đó.

Cho list quân cờ, liệt kê tất cả ô bị tấn công
Ví dụ:
Cho loạt các con xe, hậu, tượng, mã, vua vào, chỉ để trống vài quân.    Cố tình để nó chắn nhau

## Bài 9. Câu hỏi cuối cùng
Định nghĩa free. nếu nó trống và không bị tấn công.
Chỉ ra một config đủ 8 quân, sao cho số ô free
- ít nhất có thể
- nhiều nhất có thể

là ít nhất có thể
a) ít hơn 32 ô
b) ít hơn 16 ô
c) ít hơn 8 ô
NOTE. Cái mình có là sót 3 ô.

Điều chỉnh bàn cờ tại [đây](https://lichess.org/editor)

Sao chép [FEN notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation)

Trước tiên cần cài đặt thư viện `chess` trong Python bằng câu lệnh
```sh
pip install chess
```

Rồi chạy đoạn code dưới đây

```py
import chess
import chess.svg

board = chess.Board('8/8/8/8/8/8/8/RNBQKBNR w - - 0 1')
boardsvg = chess.svg.board(board = board)
with open('foobar.svg', 'w') as f:
    f.write(boardsvg)
```


# --------------------------------------------------------------------------- #
## Bình luận

yêu cầu: Trong tập A tất cả phần tử thỏa mãn tính chất X, kiểm tra phần tử m có thỏa mãn tính chất Y hay không
Cách 1.
- Liệt kê mọi phần tử trong A thỏa mãn tính chất X
- Kiểm tra xem phần tử m có thuộc tập đó không.

Cách 2. kết hợp tính chất X và Y thành Z
Kiểm tra m có tính chất Z hay không.


# --------------------------------------------------------------------------- #

## Tài liệu tham khảo
Chuỗi bài tập này được truyền cảm hứng từ mục **7.4 War Story: Covering Chessboards** trong cuốn sách _The algorithm design manual_ (2nd edition, 2008, Springer-Verlag London) của tác giả Steven S. Skiena.

Chúc mọi người tìm được nguồn cảm hứng với toán học, Python, và cờ vua.

# --------------------------------------------------------------------------- #

Một ô được gọi là bị kiểm soát nếu nó bị chiếm hoặc bị tấn công.

Bài cuối sẽ là đặt 8 quân mạnh
vào bàn cờ
sao cho kiểm soát nhiều ô nhất có thể.

https://lichess.org/editor/R7/2K2N2/5B2/8/2B1Q3/1N6/8/7R_w_-_-_0_1
Sót. b4, f2, g3
Vậy nên yêu cầu phủ được 30 ô là không khó khăn.


Another kind of mathematical chess problems is a domination problem (or covering). This is a special case of the vertex cover problem. In these problems it is requested to find a minimum number of pieces of the given kind and place them on a chess board in such a way, that all free squares of the board are attacked by at least one piece.



https://en.wikipedia.org/wiki/Mathematical_chess_problem

Domination problems
Another kind of mathematical chess problems is a domination problem (or covering). This is a special case of the vertex cover problem. In these problems it is requested to find a minimum number of pieces of the given kind and place them on a chess board in such a way, that all free squares of the board are attacked by at least one piece. The minimal number of dominating kings is 9, queens - 5, rooks - 8, bishops - 8, knights - 12. To get 8 dominating rooks it is sufficient to place them on any rank, one for each file. Solutions for other pieces are provided on diagrams below.
--> the case for queen is interesting, able to solve by IP
với mối ô, thì nó và tất cả ô kề nó phải có ít nhất 1 hậu.

xe: dễ nhất. 8 con. Nếu có 7 thì sẽ thiếu 1 hàng 1 cột, giao chúng sẽ không phủ được.
vua: 9 con, bằng cách chỉ ra 9 ô mà 1 vua không thể phủ cùng lúc 2 ô
mã, tượng, hậu có vẻ khó.
