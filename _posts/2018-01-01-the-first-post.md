---
title: "The first post"
date: 2018-01-01 00:00:00
last_modified_at: 2020-07-30 00:00:00
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

<iframe width="560" height="315" src="https://www.youtube.com/embed/N4o0qnSeVQQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


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

### Quotes

> To code or not to code, that is the question.
>
> --- Anonymous ---

## Code snippets
```txt
# white background by three quotes and "txt" header
# Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

```
# black background by three quotes
# Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
```

### LaTeX snippets (mostly math equations)

Example of inline equation with `$` symbol, $\frac{1}{2} + \frac{1}{3} = \frac{5}{6}$.

Absolute value.
- Correct. method 1.  `\lvert`: $\lvert x \rvert$
- Others. method 2. norm `\lVert`: $\lVert x \rVert$
- Wrong (in some articles) `| . |`: $|x|$

Example of an equation in a new line with `$$` symbol

$$a^2 + b^2 = c^2$$

space at the beginning

$$ a^2 + b^2 = c^2$$

and this one with `\begin{equation}` environment

\begin{equation}
  \sum_{1}^{n} i = \dfrac{n(n+1)}{2}
\end{equation}


{% raw %}
 $$a^2 + b^2 = c^2$$ --> hello

 \begin{matrix}
 1 & 2 & 3\\
 a & b & c
 \end{matrix}
{% endraw %}

Raw matrix environment

\begin{matrix}
1 & 2 & 3\\
a & b & c
\end{matrix}

Matrix environment inside equation environment

\begin{equation}
  \begin{matrix}
  1 & 2 & 3\\
  a & b & c
  \end{matrix}
\end{equation}


We examine some environment in LaTeX below
`align` environment (not working)
\begin{align}
  1 &+ 2 + 3 = 6 \\
  1 + 2 &+ 3 = 6 \\
  1 + 2 + 3 &= 6 \\
\end{align}

`itemize` environment (not working)
\begin{itemize}
  \item Foo
  \item Bar
  \item Ham
  \item Egg
\end{itemize}

`enumerate` environment (not working)
\begin{enumerate}
  \item Python
  \item Java
  \item R
  \item SageMath
\end{enumerate}


### Final section

To quickly turn a URL into a link, enclose it in angle brackets <https://github.com>.

Click-to-expand section
<details>
<summary>Click to expand</summary>
This is hidden
Cannot render an image using markdown syntax here.

What about an equation $a^2$? OK

![image](/assets/images/avatar.jpg)
</details>

**Manual line breaks**

End a line with  
two or more spaces

Edited at 16h44

### Static link to a post
[The article](/the-shortest-infinite-program-in-Python/)

### Link to email

[Ref1](https://github.com/github/markup/issues/1030)
[Ref2](https://www.wikihow.com/Create-an-Email-Link-in-HTML)

- Email: <a href="mailto:quanhoang.pm@gmail.com">Send to my email</a>
- Email: [quanhoang.pm@gmail.com](mailto:quanhoang.pm@gmail.com)
- Email: [quanhoang.pm@gmail.com](mailto:quanhoang.pm@gmail.com?subject=[Subject]%20Big%20Title)


---

[^footnote]: The detailed description in one paragraph.

[^1]: The other footnote of emoji :joy:.
