# 贡献指南 / Contributing Guide

## 添加索引 / Add to Index

发现了好的 personalized skill 仓库？直接编辑 `README.md`，将其添加到对应分类表格，提交 PR。

*Found a great personalized skill repo? Edit `README.md`, add it to the right category table, and submit a PR.*

**要求 / Requirements:**
- 仓库必须真实存在且可访问
- 必须与人物、著作或思维框架蒸馏相关
- 附上准确的 star 数（取近似值即可）

## 贡献原创 Skill / Contribute Original Skills

在 `skills/` 目录下创建 `.md` 文件：

```
skills/
├── your-skill-name.md
└── ...
```

**Skill 文件结构 / Structure:**

```markdown
---
name: skill 名称
figure: 蒸馏对象
source: 主要参考资料
---

## 核心框架 / Core Framework
（提取的思维模型、方法论）

## 适用场景 / When to Use
（什么问题适合用这个 skill）

## 局限性 / Limitations
（什么场景不适用）

## Skill 正文 / Skill Body
（实际的 skill prompt 内容）
```

## 原则 / Principles

**蒸馏 > 模仿**：提取思维框架，而非模仿说话方式。

**实用 > 炫技**：面对真实问题要能产出可操作的拆解。

**诚实 > 万能**：明确说明局限性，不夸大适用范围。
