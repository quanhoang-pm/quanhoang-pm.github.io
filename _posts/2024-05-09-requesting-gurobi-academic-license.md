---
title: "Hướng dẫn lấy Gurobi academic license"
date: 2024-05-09
last_modified_at: 2024-05-13 16:03:00
categories:
  - programming
tags:
  - Gurobi
---

TLDR: Người dùng với mục đích học thuật được phép sử dụng [Gurobi Optimizer](https://www.gurobi.com/) miễn phí với [academic license](https://www.gurobi.com/academia/academic-program-and-licenses/). Tuy nhiên [cách nhận giấy phép phổ biến nhất](https://support.gurobi.com/hc/en-us/articles/360040541251-How-do-I-obtain-a-free-academic-license) có vẻ như không khả thi tại Việt Nam. Bài viết này hướng dẫn mọi người một cách khác.

### Các bước để lấy license key

Bước 1. Sử dụng email `.edu` **chính chủ** (mà đại học cung cấp) để đăng ký tài khoản tại [Gurobi](https://www.gurobi.com/) (mục Register ở góc trên bên phải).

<div>
    <img src="/assets/images/Gurobi_academic_license/step_A.png"
    style="width:70%;
    max-width:700px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding-top:20px;
    padding-bottom:20px;">
</div>

<center> Source: Gurobi Optimization </center>

Bước 2. Đăng nhập vào tài khoản vừa tạo. Trên thanh hỗ trợ, chọn **Support/Help center**.

<div>
    <img src="/assets/images/Gurobi_academic_license/step_B.png"
    style="width:70%;
    max-width:700px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding-top:20px;
    padding-bottom:20px;">
</div>

<center> Source: Gurobi Optimization </center>

Bước 3. Tại Gurobi Help Center, chọn **Submit a Request**.

<div>
    <img src="/assets/images/Gurobi_academic_license/step_C.png"
    style="width:70%;
    max-width:700px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding-top:20px;
    padding-bottom:20px;">
</div>

<center> Source: Gurobi Optimization </center>

Bước 4. Điền thông tin cần thiết, gồm có
- Request type: Academic and/or Research
- Subject: ...
- Type of issue: License request
- Description of issue/request: giới thiệu bản thân, mục đích sử dụng Gurobi (bản đầy đủ) trong học tập/nghiên cứu.

Bước 5. Chọn **Submit** ở cuối trang.

<div>
    <img src="/assets/images/Gurobi_academic_license/step_D.png"
    style="width:70%;
    max-width:700px;
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding-top:20px;
    padding-bottom:20px;">
</div>

<center> Source: Gurobi Optimization </center>

Bước 6. Bạn sẽ nhận được email thông báo khi có phản hồi từ đội ngũ hỗ trợ. Thực hiện theo hướng dẫn để cung cấp thông tin cá nhân
- Nếu là sinh viên: ảnh chụp thẻ sinh viên (còn hạn)
- Nếu là giảng viên: đường dẫn tới trang web cá nhân tại trường đại học

Tài liệu bổ sung sẽ cần được gửi qua phần **Add file or drop files here**.

Sau khi thực hiện các bước trên, bạn sẽ được cấp một license key với format `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`. Một số điểm cần lưu ý:
- Cần sử dụng license key để kích hoạt Gurobi phiên bản đầy đủ (xem mục dưới).
- Sau khi kích hoạt, license key trở nên vô giá trị.
- Thời hạn sử dụng phiên bản đầy đủ (thường) là một năm.
- Mỗi license key chỉ có thể kích hoạt trên **một user** của **một máy tính**. Cài lại hệ điều hành được tính là hai user khác nhau.

### Hoàn thiện cài đặt nào!
Khi có được license key, bạn đã hoàn thành 99% công việc rồi. Chỉ cần thực hiện theo hướng dẫn [này](https://support.gurobi.com/hc/en-us/articles/360047265972-grbgetkey-command-not-found) để hoàn thành 1% còn lại, nhìn chung gồm có:
- Cài đặt `gurobipy` (nếu bạn sử dụng Gurobi qua Python).
- Cài đặt `grbgetkey` (tùy thuộc vào hệ điều hành bạn sử dụng).
- Tạo file `gurobi.lic` với license key ở trên.

### Happy modeling!
