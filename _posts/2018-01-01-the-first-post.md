---
title: "The first post"
date: 2018-01-01 00:00:00
last_modified_at: 2020-05-11 17:25:00
categories:
  - common
tags:
  - markdown
---


## Welcome to my site

Edited on May 2, 15h35.

_Xin chào_, my name is Quan.

This is the link to [my site](https://quanhoang-pm.github.io/).

This is my avatar. ![](/assets/images/avatar.jpg)

A way to ~~alter~~ resize an image using `HTML`.
```html
<img src="/assets/images/avatar.jpg" width="150" height="100" />
```
<img src="/assets/images/avatar.jpg" width="150" height="100" />

<!--
multiple lines comment
-->

A list of different *notice* types
- [Normal notice](#).
{: .notice}
- [Primary notice](#).
{: .notice--primary}
- [Info notice](#).
{: .notice--info}
- [Warning notice](#).
{: .notice--warning}
- [Danger notice](#).
{: .notice--danger}
- [Success notice](#).
{: .notice--success}

A sentence with a [notice](#) is displayed by adding `{: .notice--<type>}` at **a new line after** the intended line.
{: .notice}


A list of tasks

- [x] This is a complete item
- [ ] This is an incomplete item

Formatting
- **Bold**
- *Italic*
- ~~Strikethrough~~


Inline-style:
![alt text](/assets/images/avatar.jpg)

Reference-style:
![alt text][logo]

[logo]: /assets/images/avatar.jpg

Link to an amazing song [![Remember When - Alan Jackson](/assets/images/avatar.jpg)](https://www.youtube.com/watch?v=TOmZ66lIzJA)

Table

| Side | Area |
|:----:|-----:|
|  2   |    4 |
|  9   |   81 |

### Some advanced formats in Markdown {#advanced-format}


Here are [^footnote] some footnotes. Of course we can keep writing as normal and add another footnote [^1]. Keep in mind that the footnotes are listed at the end of the post.

### Shall we continue? {#custom-id}

In the section about [Advanced formats](#advanced-format), the footnote technique has been introduced.

The link can be created as follows

In `markdown`,
```markdown
## Heading {#custom-id}

In the [section](#custom-id), ...
In another post, at the [section](https://site.com/category/foo#custom-id)
```

In `HTML`,
```html
<h3 id="custom-id">Heading</h3>
<a href="#custom-id">the section</a>
```

### Math equations

Example of inline equation $\frac{1}{2} + \frac{1}{3} = \frac{5}{6}$.

Example of an equation in a new line

$$ a^2 + b^2 = c^2$$

and this one

\begin{equation}
  \sum_{1}^{n} i = \dfrac{n(n+1)}{2}
\end{equation}

### Final section

To quickly turn a URL into a link, enclose it in angle brackets <https://github.com>.

Click-to-expand section
<details>
<summary>Click to expand</summary>
This is hidden
Cannot render an image using markdown syntax here.
![image](/assets/images/avatar.jpg)
</details>

**Manual line breaks**

End a line with  
two or more spaces

Edited at 16h30
---

[^footnote]: The detailed description in one paragraph.

[^1]: The other footnote of emoji :joy:.
