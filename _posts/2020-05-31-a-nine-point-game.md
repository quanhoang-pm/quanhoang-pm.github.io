---
title: "A nine-point game"
date: 2020-05-31 20:00:00
last_modified_at: 2020-05-31 20:15:00
categories:
  - mathematics
tags:
  - game
  - two players
  - puzzle
---

Một trò chơi chiến thuật đơn giản dành cho hai người.

### Chuẩn bị.
- Hai bộ quân cờ, mỗi bộ gồm ba quân cờ có cùng màu.
- Một sơ đồ như ảnh dưới.
![](/assets/ninePointsGame/ninePointsGame_move_0.png)

### Luật chơi
Hai người chơi đặt những quân cờ vào 6 ô trên sơ đồ như trong ảnh dưới.

| ![](/assets/ninePointsGame/ninePointsGame_move_1.png) |
|:-----------------------------------------------------:|
|             Vị trí khởi đầu của trò chơi              |

Hai người chơi luân phiên thực hiện một nước đi hợp lệ. Người chơi thực hiện một nước đi hợp lệ bằng cách chọn một quân cờ của mình và di chuyển nó đến ô trống liền kề với vị trí hiện tại của quân cờ đó. Hai ô trong sơ đồ được gọi là liền kề nếu chúng được nối với nhau bởi một đoạn thẳng trong sơ đồ.

Trò chơi kết thúc khi xác định được người thua cuộc hoặc người thắng cuộc của lần chơi đó. Cụ thể,
- Nếu có một người chơi không thể thực hiện một nước đi hợp lệ thì người chơi đó thua cuộc.
- Nếu ba quân cờ của một người chơi được xếp thẳng hàng thì người chơi đó thắng cuộc.

Chú ý, trò chơi có thể không kết thúc khi hai điều kiện trên không thỏa mãn _sau một sốlượng lớn các nước đi_. Khi đó hai người chơi cần thỏa thuận để chấp nhận kết quả hòa, hoặc tiếp tục chơi để tìm ra người chiến thắng.

Những ảnh dưới đây thể hiện một lần chơi kết thúc sau 5 nước đi với chiến thắng thuộc về người đi sau (với quân cờ màu xanh).

![](/assets/ninePointsGame/ninePointsGame_move_2.png)
![](/assets/ninePointsGame/ninePointsGame_move_3.png)
![](/assets/ninePointsGame/ninePointsGame_move_4.png)
![](/assets/ninePointsGame/ninePointsGame_move_5.png)
![](/assets/ninePointsGame/ninePointsGame_move_6.png)

### Biến thể.

Trò chơi có thể được mở rộng bằng cách thay đổi thiết kế của

Những biến thể của trò chơi này có thể được xây dựng bằng cách thay đổi những yếu tố sau:
- Sơ đồ sử dụng để đặt các quân cờ.
- Vị trí khởi đầu / số lượng của các quân cờ.
- Quy tắc di chuyển các quân cờ trong một nước đi hợp lệ.
- Điều kiện thắng cuộc / thua cuộc.

### Phụ lục

Tác giả sử dụng ngôn ngữ lập trình Python để vẽ những ảnh minh họa trong bài đăng này. Chương trình vẽ ảnh này có thể được tìm thấy tại [đây](/assets/ninePointsGame/aNinePointGame.py)

**Câu hỏi thêm.** Trong trò chơi này, người đi trước hay người đi sau là người có chiến thuật để luôn giành chiến thắng?
