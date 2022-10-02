Nó cung cấp công cụ giúp người đọc tìm hiểu một câu hỏi Toán học liên quan tới cờ vua:

> Có thể đặt tối đa bao nhiêu quân hậu lên bàn cờ vua sao cho chúng đôi một không tấn công nhau?



> Khi đặt đủ 8 quân cờ bao gồm 1 vua, 1 hậu, 2 xe, 2 tượng (khác màu), 2 mã lên trên bàn cờ thì số ô không bị tấn công cực đại/cực tiểu là bao nhiêu?


## Bài 1. Tọa độ trên bàn cờ

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
