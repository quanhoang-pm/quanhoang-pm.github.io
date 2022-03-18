---
title: "IP Adventure. Part 1: Introduction"
permalink: /foobar/
layout: customPostLayout
date: 2022-03-19 02:00:00
last_modified_at: 2022-03-19
---

Mô hình hóa (modeling) là một trong ba kỹ năng quan trọng để giải quyết những vấn đề thực tế, bên cạnh mô phỏng (simulation) và tối ưu hóa (optimization). Kỹ năng mô hình hóa giúp chuyển một mô hình thực tế thành một mô hình toán học, từ đó cho~phép áp dụng những công cụ toán học (ví dụ như tối ưu nguyên) để giải quyết vấn đề. Bài~tập dưới đây giúp người đọc làm quen với những suy luận đặc trưng của mô hình hóa.

Xét một bài toán nổi tiếng:

>	Đặt 8 quân hậu trên bàn cờ vua tiêu chuẩn $8\times 8$ sao cho không có hai quân hậu nào tấn công nhau.

Bàn cờ vua tiêu chuẩn có 8 hàng và 8 cột. Ta định nghĩa một đường chéo là một tập hợp gồm ít nhất hai tọa độ, các tọa độ cùng nằm trên một đường thẳng tọa với trục ngang (cũng như trục dọc) một góc $45^\circ$. Có tất cả 26 đường chéo trên bàn cờ vua. Một quân hậu có thể tấn công một ô cùng hàng ngang, cột dọc, hoặc đường chéo nếu những ô ở giữa là trống.

Ta sẽ xây dựng một mô hình tối ưu tuyến tính để giải quyết bài toán này.

Đầu tiên, cần tìm cách biểu diễn vị trí đặt những quân hậu. Với mỗi tọa độ $(i,j)$ trên bàn cờ, ta định nghĩa một biến $x_{i,j}$ nhận giá trị lần lượt là 1 hoặc 0 ứng với trường hợp tọa độ đó có quân hậu hoặc không có quân hậu.

a) Dựa theo mô tả trên, có tất cả bao nhiêu biến có dạng này? Dựa theo giá trị có thể nhận được, những biến này có tên gọi là gì?

b) Nêu biểu thức thể hiện số quân hậu trên bàn cờ. Nêu ràng buộc (tuyến tính) thể hiện việc trên bàn cờ có đúng 8 quân hậu.

Tiếp theo ta quan tâm tới ràng buộc quan trọng nhất của bài toán - không có hai quân hậu nào tấn công nhau. Bằng suy luận toán học, ta có thể chứng minh rằng điều này tương đương với điều~kiện

> (*) Mỗi hàng, mỗi cột, mỗi đường chéo của bàn cờ chỉ có tối đa một quân hậu.

c) Chứng minh sự tương đương trên.

d) Liệt kê tất cả ràng buộc (tuyến tính) thể hiện điều kiện (*).

e) Trình bày mô hình tối ưu nguyên giải quyết bài toán đặt ra ở đầu bài.

f) (Câu hỏi nâng cao) Liệt kê tất cả các cách đặt 8 quân hậu trên bàn cờ vua tiêu chuẩn $8\times 8$ sao cho không có hai quân hậu nào tấn công nhau.
