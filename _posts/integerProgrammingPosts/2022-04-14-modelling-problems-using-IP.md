---
title: "Modelling problems using IP"
permalink: /modelling-problems-using-IP/
date: 2022-04-15 00:15:00
last_modified_at: 2022-04-15
categories:
  - mathematics
tags:
  - IP
---

## Danh sách bài tập mô hình hóa

**Bài toán 1.** Đặt 8 quân hậu lên bàn cờ vua kích thước $8\times 8$ sao cho không có hai quân hậu nào tấn công nhau.

**Bài toán 2.** Cho $n$ là một số nguyên dương. Tô màu mỗi số nguyên $1,2,\ldots,n$ bởi một trong hai màu sao cho không tồn tại ba số nguyên $a<b<c$ thỏa mãn $a+b=c$ được tô cùng màu.

**Bài toán 3.** Điền các số nguyên từ 1 đến 9 vào một bảng vuông có kích thước $3\times 3$ sao cho tổng các số trên mỗi hàng ngang, cột dọc và đường chéo đều bằng nhau và bằng 15.

**Bài toán 4.** Cho $n$ là một số nguyên dương. Đặt $2n$ điểm lên trên lưới vuông kích thước $n\times n$ sao cho không có ba điểm nào thẳng hàng. Mô tả chi tiết về bài toán có tại [Wikipedia](https://en.wikipedia.org/wiki/No-three-in-line_problem).

## Hướng dẫn

**Bài toán 1.** Ta coi bàn cờ là một lưới vuông gồm các tọa độ $(i,j)$ (ứng với hàng $i$, cột $j$) thỏa mãn $1\le i,j \le 8$. Với mỗi tọa độ $(i,j)$ trong bàn cờ, ta sử dụng biến nhị phân $x_{ij}$ thể hiện việc có đặt quân hậu tại tọa độ đó hay không. Điều kiện không có hai quân hậu tấn công nhau tương đương với điều kiện: **có tối đa một quân hậu trong mỗi hàng, mỗi cột, hoặc mỗi đường chéo**. Ví dụ, hệ điều kiện dưới đây mô tả việc mỗi cột có tối đa một quân hậu:

$$\sum_{i=1}^{8} x_{ij} \le 1 \quad \forall j=1,2,\ldots,8$$

Mô hình này không có hàm mục tiêu, nói cách khác, thuật toán sẽ kết thúc khi tìm được một nghiệm thỏa mãn tất cả các ràng buộc kể trên (gọi là nghiệm chấp nhận được - feasible solution).

**Bài toán 2.** Đặt hai màu có thể tô là [đỏ và xanh](https://en.wikipedia.org/wiki/Red_pill_and_blue_pill). Với mỗi $i$ thỏa mãn $1\le i \le n$, ta đặt biến nhị phân $x_i$ thể hiện màu tô cho số $i$

$$x_i=
\begin{cases}
    1 & \text{if } i \text{ is red} \\
    0 & \text{if } i \text{ is blue} \\
\end{cases}
$$

Từ điều kiện đã cho, với mỗi bộ ba số $1\le a<b<c \le n$ thỏa mãn $a+b=c$, ta suy ra bộ $(x_a,x_b,x_c)$ không thể nhận giá trị $(0,0,0)$ hoặc $(1,1,1)$. Khi minh họa ba biến này trong không gian ba chiều, ta chỉ ra được hai điều kiện tuyến tính loại bỏ đi đúng hai trường hợp trên (trong số 8 trường hợp có thể của bộ $(x_a,x_b,x_c)$), đó là

$$
\left.
  \begin{array}{ c c }
    x_a + x_b + x_c & \ge 1 \\
    x_a + x_b + x_c & \le 2 \\
  \end{array}
\right.$$

Mô hình này không có hàm mục tiêu.

**Bài toán 3.** Với mỗi $1 \le i,j \le 3$, ta đặt biến nguyên $x_{ij}$ thể hiện giá trị của số đặt trong ô ở hàng $i$, cột $j$. Với mỗi $1 \le i,j \le 3$ và $1\le k \le 9$, ta đặt biến nhị phân $x_{ijk}$ nhận giá trị bằng 1 khi và chỉ khi số $k$ đặt tại ô $(i,j)$. Các ràng buộc của bài toán này bao gồm:

- Mỗi ô chỉ chứa đúng một số.
- Hai ô bất kì có giá trị khác nhau, hay nói cách khác, mỗi số chỉ xuất hiện tối đa một lần.
- Tổng các số trên mỗi hàng ngang, cột dọc và đường chéo đều bằng 15.

Mô hình này không có hàm mục tiêu.

**Bài toán 4.** Rõ ràng ta sẽ đặt các biến $x_{ij}$ thể hiện việc có đặt điểm nào vào tọa độ $(i,j)$ hay không. Điều thú vị ở bài toán nằm ở cách xây dựng ràng buộc.

Từ điều kiện không có ba điểm nào thẳng hàng, một cách hiển nhiên, ta chứng minh được nó tương đương với điều kiện **với mọi ba tọa độ thẳng hàng, có không quá hai điểm được đặt tại những chỗ đó**. Ví dụ với bốn điểm `A,B,C,D` thẩng hàng trong bảng $4\times 4$ như hình dưới đây
```txt
A . . .
. B . .
. . C .
. . . D
```
ta suy ra hệ điều kiện tương ứng là

$$
\left.
  \begin{array}{ c c }
    x_A + x_B + x_C & \le 2 \\
    x_B + x_C + x_D & \le 2 \\
    x_C + x_D + x_A & \le 2 \\
    x_D + x_A + x_B & \le 2 \\
  \end{array}
\right.$$

Tuy nhiên, ta có thể rút ra được một hệ điều kiện khác. Trước tiên, ta chứng minh điều kiện không có ba điểm nào thẳng hàng tương đương với điều kiện **có không quá hai điểm được chọn trên mỗi đường thẳng đi qua các tọa độ trong bảng**. Với ký hiệu như trên, hệ điều kiện trong ví dụ thu gọn chỉ còn

$$x_A + x_B + x_C + x_D \le 2.$$

Mặc dù hai cách mô hình này cho ta lời giải _tương đương_, cách mô hình sau tốt hơn cách mô hình trước. Bạn có thể tin như vậy, hoặc tự mình kiểm chứng kết luận đó.


## Bài tập nâng cao
**Bài toán 5.** Đặt các quân hậu lên bàn cờ vua kích thước $8\times 8$ sao cho mỗi quân hậu tấn công tối đa một quân hậu khác. Số quân hậu tối đa có thể đặt lên bàn cờ là bao nhiêu?

Gợi ý. Nếu ta đặt quân hậu lên một ô nào đó, thì tổng số quân hậu ở những ô _kề_ ô đó phải thỏa mãn điều kiện gì?

**Bài toán 6.** Điền các số nguyên từ 1 đến 27 vào các khối lập phương đơn vị trong khối lập phương kích thước $3\times 3\times 3$ và tính tổng các số trong mỗi bộ ba khối lập phương đơn vị phân biệt và thẳng hàng. Ba khối lập phương đơn vị được gọi là thẳng hàng nếu tâm của chúng cùng nằm trên một đường thẳng. Đặt $(s,k)$ là một cặp số nguyên thỏa mãn giá trị $s$ xuất hiện $k$ lần trong số những tổng vừa tính được. Tìm giá trị lớn nhất của $k$.

Gợi ý. Sử dụng phương pháp vẽ hình để tìm ra mối quan hệ phù hợp liên quan tới biến nhị phân kiểm soát sự bằng nhau của giá trị một tổng và giá trị của $s$
