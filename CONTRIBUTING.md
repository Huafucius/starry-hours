# 贡献指南 / Contributing Guide

感谢你对本项目的兴趣！以下是贡献的基本规范。

*Thanks for your interest! Here are the basic guidelines for contributing.*

## 📁 Skill 文件规范 / Skill File Spec

每个 skill 应放在 `skills/` 目录下，以人物名命名（小写拼音或英文），格式为 `.md`：

```
skills/
├── maozedong.md
├── munger.md
├── sunzi.md
└── ...
```

### Skill 文件结构 / Structure

```markdown
---
name: skill 名称
description: 一句话描述
author: 你的 GitHub 用户名
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

## ✅ 提交检查清单 / PR Checklist

- [ ] Skill 文件放在 `skills/` 目录下
- [ ] README 表格中已添加对应条目
- [ ] 经过至少 3 个真实场景测试
- [ ] 包含适用场景和局限性说明
- [ ] 不含角色扮演或语气模仿内容

## 🎯 质量原则 / Quality Principles

1. **蒸馏 > 模仿**：提取思维框架，而非模仿说话方式
2. **实用 > 炫技**：面对真实问题要能产出可操作的拆解
3. **诚实 > 万能**：明确说明局限性，不夸大适用范围
4. **验证 > 想象**：必须经过真实场景测试
