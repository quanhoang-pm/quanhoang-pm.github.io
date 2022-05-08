---
title: "Nhảy cầu kính"
date: 2022-05-09 01:00:00 +07:00
last_modified_at: 2022-05-09
categories:
  - puzzle
tags:
  - probability
---

[Squid Game](https://en.wikipedia.org/wiki/Squid_Game) là một series được phát hành trên Netflix vào tháng 09/2021. Nó kể về một cuộc thi nơi 456 người chơi đánh cược mạng sống của bản thân trong khi tham gia các trò chơi _đơn giản_ để giành lấy một phần thưởng vô cùng lớn. Câu đố dưới đây được lấy cảm hứng từ một trong những trò chơi diễn ra trong cuộc thi này.

### Mô tả

Có một nhóm người (đủ đông) tham gia trò chơi **Nhảy cầu kính**. Cây cầu gồm $n$ hàng kính ($n$ là một số nguyên dương), mỗi hàng kính có hai tấm kính: một kính cường lực và một kính thường. Kính cường lực có thể chịu được sức nặng của một người bất kỳ, kính thường thì không.

Tất cả người chơi xếp thành một dãy tại vị trí xuất phát và lần lượt nhảy trên cầu kính, mỗi thời điểm có tối đa một người trên cầu. Mỗi giây, người đứng trên cầu (hoặc đứng đầu ở vị trí xuất phát) phải chọn một trong hai tấm kính trong hàng kính tiếp theo và nhảy tới đó. Nếu đó là kính cường lực, người chơi tiếp tục trò chơi, nếu đó là kính thường, kính vỡ và người chơi bị loại khỏi trò chơi.

Khi có người đầu tiên tới được đầu bên kia của cây cầu, trò chơi kết thúc và anh ấy/cô ấy là người chiến thắng. Những người còn lại bị loại khỏi trò chơi. Mục tiêu của người tham gia là trở thành người chiến thắng trò chơi này.

Dưới đây là một số nhận xét liên quan tới trò chơi:
- Những người đi sau có thể dựa vào lựa chọn của người đi trước để suy luận ra đâu là kính thường, đâu là kính cường lực ở mỗi hàng kính.
- Sau khi người thứ nhất thực hiện bước nhảy lên hàng kính đầu tiên, bất kể kết quả ra sao, những người ở sau sẽ biết chắc chắn đâu là kính cường lực ở hàng kính đầu tiên này.
- Nếu trò chơi vẫn tiếp tục sau khi có người qua được đầu bên kia, những người chơi từ vị trí $n+1$ trở đi chắc chắn sẽ an toàn nhảy qua hết $n$ hàng kính trên cầu.
- Với luật chơi được mô tả bên trên, những người chơi từ vị trí $n+2$ trở đi chắc chắn không thể dành chiến thắng.
- Trò chơi chắc chắn sẽ kết thúc sau một khoảng thời gian hữu hạn.
- Khi $n = 2$, xác suất chiến thắng của ba người đầu tiên lần lượt là $25\%$, $50\%$, $25\%$, những người còn lại không thể chiến thắng.

| ![](/assets/images/SquidGameGlassBridge.png) |
|:---:|
| Cây cầu kính trong series Squid Game |


### Các biến thể
Danh sách dưới đây liệt kê các biến thể của luật chơi được mô tả bên trên.
- Biến thể 0. Luật chơi giữ nguyên như mô tả bên trên.
- Biến thể 1 (thay đổi điều kiện chiến thắng). Hai người đầu tiên đến đích là những người chiến thắng. Trò chơi kết thúc ngay sau đó.
- Biến thể 2 (thay đổi số kính ở mỗi hàng). Mỗi hàng kính có 2 kính thường và 1 kính cường lực.
- Biến thể 3 (đặt giới hạn thời gian). Thời gian được tính từ bước nhảy đầu tiên, nếu quá giới hạn thời gian cho trước (đặt là $m$ giây) mà chưa xác định được người chiến thắng thì tất cả người chơi bị loại.
- Biến thể 4 (hạn chế thông tin truyền lại từ người chơi trước). Người sau không trực tiếp nhìn thấy lựa chọn của người đi trước. Cú nhảy của một người sẽ làm vỡ kính thường, do đó người đến sau có thể nhận ra và tránh. Còn nếu người đó nhảy lên kính cường lực thì tấm kính không thay đổi và người đến sau không có thông tin gì về hai tấm kính. Ví dụ với $n = 2$, xác suất chiến thắng của ba người đầu tiên lần lượt là $25\%$, $37.5\%$, $37.5\%$, những người còn lại không thể chiến thắng.
- Biến thể 5 (yêu cầu chiến thuật phù hợp mỗi khi nhảy). Khi tới một cửa bất kỳ, người chơi chỉ có thể biết số lượng người đi trước đã nhảy lên mỗi tấm kính, chứ không biết trạng thái của các tấm kính (vỡ hay lành, thường hay cường lực). Đâu là chiến thuật tối ưu: nhảy lên tấm kính ít người chọn hay nhảy lên tấm kính nhiều người chọn? Chiến thuật có thay đổi giữa các người chơi hay không?


### Câu hỏi
Trong vai trò là một người tham gia trò chơi, câu hỏi quan trọng nhất cần trả lời là:

**Câu hỏi 1. Chiến thuật tối đa hóa khả năng giành chiến thắng là gì?**

Trong các biến thể 0, 1, 2, 3 và 4, chiến thuật chỉ là việc chọn số thứ tự xuất phát, vì trong quá trình chơi mọi người chỉ cần tránh những tấm kính đã vỡ và chỉ có thể chọn ngẫu nhiên trong (những) tấm kính lành lặn. Riêng đối với biến thể 5, chiến thuật còn bao gồm việc lựa chọn khi đứng trước một hàng kính.

Một câu hỏi khác có liên quan là

**Câu hỏi 2. Trung bình một lần chơi diễn ra trong bao lâu?**


### Hướng dẫn giải

<details>
<summary>Gợi ý</summary>

Xét bài toán gốc với cây cầu gồm $n$ hàng kính, sử dụng phương pháp đệ quy để chỉ ra chỉ có $n+1$ người đầu tiên có cơ hội giành chiến thắng với xác suất là giá trị chuẩn hóa của dòng thứ $n+1$ trong tam giác Pascal.
</details>
