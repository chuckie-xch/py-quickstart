---
comments: true
difficulty: 简单
edit_url: https://github.com/doocs/leetcode/edit/main/solution/0200-0299/0206.Reverse%20Linked%20List/README.md
tags:
    - 递归
    - 链表
---

<!-- problem:start -->

# [206. 反转链表](https://leetcode.cn/problems/reverse-linked-list)

[English Version](/solution/0200-0299/0206.Reverse%20Linked%20List/README_EN.md)

## 题目描述

<!-- description:start -->

给你单链表的头节点 <code>head</code> ，请你反转链表，并返回反转后的链表。

<div class="original__bRMd">
<div>
<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0206.Reverse%20Linked%20List/images/rev1ex1.jpg" style="width: 542px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2,3,4,5]
<strong>输出：</strong>[5,4,3,2,1]
</pre>

<p><strong>示例 2：</strong></p>
<img alt="" src="https://fastly.jsdelivr.net/gh/doocs/leetcode@main/solution/0200-0299/0206.Reverse%20Linked%20List/images/rev1ex2.jpg" style="width: 182px; height: 222px;" />
<pre>
<strong>输入：</strong>head = [1,2]
<strong>输出：</strong>[2,1]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>head = []
<strong>输出：</strong>[]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>链表中节点的数目范围是 <code>[0, 5000]</code></li>
	<li><code>-5000 <= Node.val <= 5000</code></li>
</ul>

<p> </p>

<p><strong>进阶：</strong>链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？</p>
</div>
</div>

<!-- description:end -->