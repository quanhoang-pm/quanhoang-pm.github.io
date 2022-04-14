---
title: "A nine-point game"
permalink: /a-nine-point-game/
date: 2020-05-31 20:00:00
last_modified_at: 2020-06-07 14:30:00
categories:
  - mathematics
tags:
  - game
  - two players
  - puzzle
---

Một trò chơi chiến thuật đơn giản dành cho hai người.

### Chuẩn bị
- Hai bộ quân cờ, mỗi bộ gồm ba quân cờ có cùng màu.
- Một sơ đồ như ảnh dưới.
![](/assets/ninePointsGame/ninePointsGame_move_0.png)

### Luật chơi
Sáu quân cờ của hai người chơi được đặt vào sơ đồ theo vị trí được mô tả trong ảnh dưới.

| ![](/assets/ninePointsGame/ninePointsGame_move_1.png) |
|:-----------------------------------------------------:|
|           Vị trí khởi đầu của những quân cờ           |

Hai người chơi luân phiên thực hiện một nước đi hợp lệ. Người chơi thực hiện một nước đi hợp lệ bằng cách chọn một quân cờ của mình và di chuyển nó đến ô trống liền kề với vị trí hiện tại của quân cờ đó. Hai ô trong sơ đồ được gọi là liền kề nếu chúng được nối với nhau bởi một đoạn thẳng trong sơ đồ.

Trò chơi kết thúc khi xác định được người thua cuộc hoặc người thắng cuộc của lần chơi đó. Cụ thể:
- Nếu ba quân cờ của một người chơi được xếp thẳng hàng thì người chơi đó thắng cuộc.
- Nếu một người chơi không thể thực hiện một nước đi hợp lệ thì người chơi đó thua cuộc.

Chú ý, trò chơi có thể không kết thúc khi hai điều kiện trên không thỏa mãn _sau một số lượng lớn các nước đi_. Khi đó hai người chơi cần thỏa thuận để chấp nhận kết quả hòa, hoặc tiếp tục chơi để tìm ra người chiến thắng.

Những ảnh dưới đây thể hiện một lần chơi kết thúc sau 5 nước đi với chiến thắng thuộc về người đi sau (với quân cờ màu xanh).

![](/assets/ninePointsGame/ninePointsGame_move_1.png)
![](/assets/ninePointsGame/ninePointsGame_move_2.png)
![](/assets/ninePointsGame/ninePointsGame_move_3.png)
![](/assets/ninePointsGame/ninePointsGame_move_4.png)
![](/assets/ninePointsGame/ninePointsGame_move_5.png)
![](/assets/ninePointsGame/ninePointsGame_move_6.png)

### Những biến thể của trò chơi
Những biến thể của trò chơi này có thể được xây dựng bằng cách thay đổi những yếu tố sau:
- Sơ đồ sử dụng để đặt các quân cờ.
- Vị trí khởi đầu / số lượng của các quân cờ.
- Quy tắc di chuyển các quân cờ trong một nước đi hợp lệ.
- Điều kiện thắng cuộc / thua cuộc của trò chơi.

### Chú thích
Trò chơi này được mình sưu tầm.

Những ảnh minh họa trong bài đăng này được vẽ bằng ngôn ngữ lập trình Python. Chương trình vẽ ảnh có thể được tìm thấy tại [đây](https://gist.github.com/quanhoang-pm/85cf7dad2b12eb405814fa877f078843).

### Câu hỏi mở
Trong trò chơi này, người đi trước hay người đi sau là người có chiến thuật để luôn giành chiến thắng?
