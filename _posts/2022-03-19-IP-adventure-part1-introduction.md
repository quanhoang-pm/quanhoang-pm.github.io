---
title: "IP Adventure. Part 1: Introduction"
permalink: /ip-adventure-part1-introduction/
date: 2022-03-19 02:00:00
last_modified_at: 2022-03-19
categories:
  - mathematics
tags:
  - Python
---

Mô hình hóa (modeling) là một trong ba kỹ năng quan trọng để giải quyết những vấn đề thực tế, bên cạnh mô phỏng (simulation) và tối ưu hóa (optimization). Kỹ năng mô hình hóa giúp chuyển một mô hình thực tế thành một mô hình toán học, từ đó cho phép áp dụng những công cụ toán học (ví dụ như tối ưu nguyên) để giải quyết vấn đề. Bài tập dưới đây giúp người đọc làm quen với những suy luận đặc trưng của mô hình hóa.

Bàn cờ vua tiêu chuẩn có 8 hàng và 8 cột. Ta định nghĩa một đường chéo là một tập hợp gồm ít nhất hai tọa độ, các tọa độ cùng nằm trên một đường thẳng tọa với trục ngang (cũng như trục dọc) một góc $45^\circ$. Có tất cả 26 đường chéo trên bàn cờ vua. Một quân hậu có thể tấn công một ô cùng hàng ngang, cột dọc, hoặc đường chéo nếu những ô ở giữa là trống.

[Bài toán tám quân hậu](https://en.wikipedia.org/wiki/Eight_queens_puzzle) yêu cầu đặt 8 quân hậu trên bàn cờ vua tiêu chuẩn $8\times 8$ sao cho không có hai quân hậu nào tấn công nhau. Để phù hợp với tinh thần của Tối ưu hóa, ta sẽ xây dựng một mô hình tối ưu tuyến tính nguyên giải quyết bài toán sau

<center>Đặt các quân hậu trên bàn cờ vua tiêu chuẩn $8\times 8$ với số lượng nhiều nhất có thể sao cho không có hai quân hậu nào tấn công nhau.</center>
<br>

Đầu tiên, cần tìm cách biểu diễn vị trí đặt những quân hậu. Với mỗi tọa độ $(i,j)$ trên bàn cờ, ta định nghĩa một biến $x_{i,j}$ nhận giá trị lần lượt là 1 hoặc 0 ứng với trường hợp tọa độ đó có quân hậu hoặc không có quân hậu.

a) Dựa theo mô tả trên, có tất cả bao nhiêu biến có dạng này? Dựa theo giá trị có thể nhận được, những biến này có tên gọi là gì?

b) Nêu biểu thức thể hiện số quân hậu trên bàn cờ. Chỉ ra hàm mục tiêu của mô hình.

c) Tiếp theo ta quan tâm tới ràng buộc quan trọng nhất của bài toán: không có hai quân hậu nào tấn công nhau. Chứng minh điều đó tương đương với điều kiện **mỗi hàng, mỗi cột, mỗi đường chéo của bàn cờ chỉ có tối đa một quân hậu.**

d) Liệt kê tất cả ràng buộc (tuyến tính) thể hiện điều kiện (AAA).

e) Trình bày mô hình tối ưu nguyên giải quyết bài toán đặt ra ở đầu bài.

f) (Câu hỏi nâng cao) Liệt kê tất cả các cách đặt 8 quân hậu trên bàn cờ vua tiêu chuẩn $8\times 8$ sao cho không có hai quân hậu nào tấn công nhau.

### Bình luận
Bài toán gốc (đặt 8 quân hậu lên bần cờ) có thể giải quyết bởi một mô hình tương tự. Khi đó mô hình sử dụng ràng buộc tuyến tính tổng số quân hậu bằng 8 và không có hàm mục tiêu, thay vì tối đa hóa số quân hậu có trên bàn cờ như trong mô hình xây dựng ở trên.

Để mô tả chuyện "không có hàm mục tiêu" trong mô hình tối ưu, ta cực đại hóa hàm mục tiêu là một hàm hằng (thường quy ước là hàm nhận giá trị 0).

### Lời giải

Nhóm sinh viên [Quý Anh](https://github.com/QuyAnh2005), [Văn Quân](https://github.com/quanpersie2001), [Thanh Tùng](https://github.com/thanhtung1005) đã trả lời tương đối tốt những câu hỏi đặt ra ở trên. Phần trình bày của nhóm có thể xem tại [đây](https://github.com/thanhtung1005/Optimization-Homework).
