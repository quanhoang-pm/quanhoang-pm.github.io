---
title: "Triangular differences"
date: 2022-03-19 21:30:00 +07:00
last_modified_at: 2022-05-09 00:00:00 +07:00
categories:
  - puzzle
tags:
  - Python
---

Câu đố thứ 533 trong cuốn [The Big Book of Brain Games: 1,000 PlayThinks of Art, Mathematics & Science](https://www.amazon.com/Big-Book-Brain-Games-Mathematics/dp/0761134662) (tựa tiếng Việt: 1000 câu đó tự duy về Toán, Khoa học & Nghệ thuật) của tác giả Ivan Moscovich được tóm tắt như sau:

> Điền các số tự nhiên từ 1 đến 15 vào các ô trong lưới tam giác cạnh 5 (như hình vẽ) sao cho mỗi số là hiệu của hai số nằm ngay phía trên nó.

![Câu đố Các tam giác hiệu](/assets/images/triangularDifference.jpg)

Một cách tổng quát, ta có thể đặt câu hỏi tương tự cho mọi lưới tam giác có độ dài cạnh bằng một số nguyên dương $N$.

## Một số cách tiếp cận bài toán

Trong phần này, tác giả liệt kê hai cách tiếp cận bài toán.Với cách tiếp cận này, tất cả nghiệm của bài toán trong trường hợp $N \le 5$ đã được xác định đầy đủ và liệt kê trong phần cuối của bài viết.

### Phương pháp vét cạn (exhaustive search)

Ta nhận thấy rằng bảng số hoàn toàn được xác định khi biết giá trị của những ô số trong hàng đầu tiên của bảng. Với nhận xét như vậy, cách tiếp cận ngây thơ nhất là duyệt qua mọi bộ giá trị mà hàng thứ nhất có thể nhận được, rồi xác định giá trị của toàn bảng số, cuối cùng là kiểm tra xem các giá trị này có hợp lệ hay không.

Về phần thực thi chương trình, thư viện [itertools](https://docs.python.org/3/library/itertools.html) giúp ta liệt kê tất cả bộ giá trị như trong ví dụ dưới đây.
```py
import itertools

for bar in itertools.permutations([4, 5, 6], r = 2):
    print(bar)
# (4, 5)
# (4, 6)
# (5, 4)
# (5, 6)
# (6, 4)
# (6, 5)
```

Ngoài ra, thư viện [tqdm](https://github.com/tqdm/tqdm) theo dõi tốc độ thực thi trong vòng lặp rất hiệu quả. Từ đó ta đánh giá được về thời gian chạy của thuật toán.

### Mô hình tối ưu nguyên (IP model)

Hướng tiếp cận mô hình tối ưu nguyên là tự nhiên vì phương pháp này giải quyết tốt những bài toán điền số đi kèm yếu tố phân biệt (ví dụ như sudoku, ma phương). Ở bài toán này, trở ngại lớn nhất khi áp dụng mô hình tối ưu nguyên là ràng buộc có dạng $\lvert x-y \rvert = z$ xuất phát từ yêu cầu của đề bài. Người đọc có thể tham khảo cách mô hình hóa điều kiện giá trị tuyệt đối trong [tài liệu này](https://github.com/thanhtung1005/Optimization-Homework/blob/main/Modeling_Constraint.pdf).

Sau khi đã có mô hình tối ưu nguyên hoàn chỉnh, việc giải quyết bài toán chỉ còn là vấn đề liên quan tới kỹ thuật lập trình.

## Danh sách nghiệm với $1\le N\le 5$

Có tất cả 12 nghiệm với những giá trị $N$ thỏa mãn $1\le N \le 5$. Những nghiệm đối xứng với nhau qua trục thẳng đứng được coi là giống nhau.

Với $N = 1$, có duy nhất một nghiệm hiển nhiên.
```
1
```

Với $N = 2$, có chính xác hai nghiệm thỏa mãn yêu cầu của đề bài.
```
1 3
 2

2 3
 1
```

Với $N = 3$, có tất cả bốn nghiệm thỏa mãn yêu cầu của đề bài.
```
1 6 4
 5 2
  3

2 6 5
 4 1
  3

4 1 6
 3 5
  2

5 2 6
 3 4
  1
```

Với $N = 4$, có đúng bốn nghiệm thỏa mãn yêu cầu của đề bài.
```
6   1  10   8
  5   9   2
    4   7
      3

6  10   1   8
  4   9   7
    5   2
      3

8   3  10   9
  5   7   1
    2   6
      4

8  10   3   9
  2   7   6
    5   1
      4
```

Với $N = 5$, có duy nhất một nghiệm thỏa mãn yêu cầu của đề bài.
```
6  14   15   3   13
  8   1   12   10
    7   11   2
      4    9
         5
```

## Những trường hợp tổng quát
Sau khi bài viết được đăng tải, bạn P. C. Tài đã tìm được [một bài báo](/assets/documents/EXACT DIFFERENCE TRIANGLES.pdf) chứng minh sự vô nghiệm của bài toán trong trường hợp $N \ge 6$. Với giả định bài báo là chính xác, như vậy bài toán được nêu ra ở đầu bài viết đã được giải quyết trọn vẹn.

## Mở rộng: Điền số trên ống trụ
Thay vì điền số vào lưới tam giác như trên, ta có thể nghiên cứu bài toán điền số vào một ống trụ sao cho vẫn thỏa mãn yêu cầu của đề bài: số ở dưới bằng chênh lệch của hai số ở ngay trên. Một cách hình thức, bài toán yêu cầu điền số vào một bảng chữ nhật với các hàng so le nhau rồi dán chúng lên một ống trụ. Dưới đây là một lời giải cho trường hợp điền 6 số 1,2,3,4,5,6 vào ống trụ gồm hai hàng, mỗi hàng có ba số.
```
4 6 1\4
 2 5 3
```

---

Edit
- 20/03/2022. Bổ sung mục **Điền số trên ống trụ**.
- 09/05/2022. Trích dẫn bài báo chỉ ra sự vô nghiệm của bài toán với $N \ge 6$.
