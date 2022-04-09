---
title: "Magic squares"
permalink: /magic-squares/
date: 2022-04-08 09:30:00
last_modified_at: 2022-04-08
categories:
  - mathematics
tags:
  - Python
---

Dàn bài.

Khi đặt điều kiện |a-b|>=1 với mọi cặp, tức là có thêm 36 điều kiện. (bên cạnh 8 điều kiện tổng)
Note. mô tả nó bằng đk abs hoặc điều kiện x**2>=1
Thì việc chặn lb,ub 1,9 khiến cho nghiệm nếu có hiển nhiên là nguyên.

# --------------------------------------------------------------------------- #

= 15,

 = k, có thể tự suy ra = 15 rồi quay lại bài trước, nhưng mà cách khác là giới thiệu thêm biến k.

rồi đặt đk nguyên một cách thực sự, tức là thể hiện việc ô đó chọn số nào.  sigma theo k của bijk = 1 (1 ô có đúng 1 số)
và đến việc thể hiện giá trị, x_ij = sigma kb_ijk.

Rồi đến điều kiện 2 ô bất kỳ phải khác nhau, tương đương với 1 giá trị bất kỳ xuất hiện ở tối đa 1 ô. tổng theo i,j <= 1.
(vì có tổng b_ijk = 9 nên dấu đẳng thức xảy ra.)


Điều kiện phá tính đối xứng.
M là tập nghiệm của bài toán
M* là tập nghiệm của bài toán thỏa mãn tính chất X.
phải đảm bảo M khác rỗng khi và khỉ khi M* khác rỗng.
chiều "suy ra" cần dùng suy luận để chứng minh.
ứng cử viên.
x_11 = 5, không hay khi dùng toán học.
x_00 = 2, không tốt do đã nhìn vào lời giải để phán
x_00 < x_02, không dùng nó. mà dùng cái <= . - 1

Tính đối xứng gồm có xoay và lật.

a . b
. . .
c . d
a = min, and b < c


Ma phương là gì.
ví dụ về 3x3
8 3 4
1 5 9
6 7 2


Xây dựng LP
có thể ra
6.5 4 4.5
3 5 7
5.5 6 3.5
(cái trên chia đôi rồi cộng 2.5 mỗi ô)

Lời giải.
LP + IP
https://gist.github.com/quanhoang-pm/e841d6579ff6b42f1c898d04049be1ed


# --------------------------------------------------------------------------- #
Cut nghiệm: tiêu chỉ trong tập nghiệm: bỏ đi duy nhất nó, ở ngoài tập nghiệm thì cắt đi càng nhiều càng tốt.
b008 = 0, liệu có quá tay không?

# --------------------------------------------------------------------------- #



- Thêm keyword "symmetry breaking in IP" trong bài tập về ma phương gửi sinh viên.


# --------------------------------------------------------------------------- #
Biết chắc chắn, đặt luôn đk.
biết sơ sơ: MIP.Start, có thể đưa vào đk mâu thuẫn.


# --------------------------------------------------------------------------- #

Bài tập về nhà sau bài về ma phương
Prob1. Điền các số nguyên tố tạo ma phương <= 200
There are magic squares consisting entirely of primes. Rudolf Ondrejka (1928–2001) discovered the following 3×3 magic square of primes, in this case nine Chen primes:
17	89	71
113	59	5
47	29	101
Source Wikipedia

Prob2. ma phương lộn ngược. câu chuyện nếu chọn số "X" thì xuôi là 68 và ngược là 89, từ đó tính ra giá trị. Chốt 6-9, 1-1, 8-8, 0-0,
  TH1. 2-7, 5 không quay
  TH2. 2-7, 5-5
  TH3. 2-2, 5-5. 7 không quay.
  Lời giải có trên mạng.
  102.—A Reversible Magic Square.
  Can you construct a square of sixteen different numbers so that it shall be magic (that is, adding up alike in the four rows, four columns, and two diagonals), whether you turn the diagram upside down or not? You must not use a 3, 4, or 5, as these figures will not reverse; but a 6 may become a 9 when reversed, a 9 a 6, a 7 a 2, and a 2 a 7. The 1, 8, and 0 will read the same both ways. Remember that the constant must not be changed by the reversal.

  (tức là chỉ cho phép 1-6-8-9)
  The following "reversible magic square" has a magic constant of 264 both upside down and right way up:[76]
  96	11	89	68
  88	69	91	16
  61	86	18	99
  19	98	66	81

Prob3. Ma phương tích. cần kỹ cái đoạn lấy log, vì nó có thể sai số (chắc ổn). cẩn thận nhất là lấy theo số mũ Vp(x) --> code mất công.

Prob4. Đặt nhiều tổng bằng nhau  3x3x3, 1->27 hoặc chỉ yêu cầu các số khác nhau. (khởi tạọ nghiệm 37 bộ luôn, chính là cái magicCube.)

Bt thêm. Câu đố của Dudeney yêu cầu đặt 8 ở cạnh.

Other related probs
Area magic square
Images in there. TODO. find the exact method to construct the figure.
https://www.primepuzzles.net/puzzles/puzz_865.htm
https://carresmagiques.blogspot.com/2020/04/area-magic-squares-and-tori-of-order-3.html


https://en.wikipedia.org/wiki/Magic_square



# --------------------------------------------------------------------------- #

"""
Bảng 3x3, mỗi phần tử là một hoán vị của tập M phần tử
Sao cho hợp của chúng theo "chiều xác định" là bằng nhau.

Cách 1. Mỗi ô là một bảng nhị phân MxM, mỗi dòng mỗi cột có tổng = 1.
Rồi xét tích bằng tạo một bảng mới M x M x M x M
b_ijkl = 1 nếu arrA_ij = arrB_jk = arrC_kl = 1, rồi bảng tích có cỡ MxM, kiểu B_il = sum b_i**l.

Cách 2. (có lẽ ổn). Hiểu đơn giản mỗi hoán vị là một phần tử, tự tính luôn mối quan hệ giữa chúng.
Vd, M = 6,--> 720 phần tử. Mình tự tính xem tích của indexA * indexB * indexC là index D nào. rồi đặt điều kiện
arrA[indexA] + arrB[indexB] + arrC[indexC] - arrD[indexD] <= 2. (rồi đặt thêm điều kiện là các kết quả phải cùng index)
"""
