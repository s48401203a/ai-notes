#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# 读取当前文件
with open('ai-training-quiz.html', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Current file size: {len(content)} bytes")

# 定义要添加的新题目
new_easy_questions = '''      // 新增的AI工具题目
      {
        category: "tool",
        question: "Trae的Builder模式适合什么场景？",
        options: ["简单问答", "从零创建完整项目", "代码审查", "文档阅读"],
        correct: 1,
        explanation: "Trae的Builder模式适合从零创建完整项目，自动生成文件结构和代码。"
      },
      {
        category: "tool",
        question: "Claude Code中用于创建Pull Request的命令是什么？",
        options: ["/commit", "/pr", "/review", "/test"],
        correct: 1,
        explanation: "Claude Code使用/pr命令可以创建Pull Request。"
      },
      {
        category: "tool",
        question: "Kimi Code CLI的Skills命令是什么格式？",
        options: ["/load-skill", "/skill:name", "/use-skill", "/apply-skill"],
        correct: 1,
        explanation: "Kimi Code CLI使用/skill:name格式加载Skills，如/skill:brainstorming。"
      },
      {
        category: "tool",
        question: "Cherry Studio如何实现模型切换？",
        options: ["只能使用默认模型", "点击模型图标快速切换", "需要重新安装", "不支持切换"],
        correct: 1,
        explanation: "Cherry Studio支持点击模型图标快速切换不同的AI模型。"
      },
      {
        category: "tool",
        question: "以下哪个工具的定价是$20/月？",
        options: ["Trae个人版", "Claude Pro", "GitHub Copilot", "Cherry Studio"],
        correct: 1,
        explanation: "Claude Pro定价为$20/月，Trae个人版免费，GitHub Copilot $10/月起。"
      },
      {
        category: "tool",
        question: "API Key管理最佳实践不包括以下哪项？",
        options: ["定期轮换", "硬编码在代码中", "使用环境变量", "设置使用限额"],
        correct: 1,
        explanation: "不应将API Key硬编码在代码中，应使用环境变量或密钥管理服务。"
      },
      {
        category: "tool",
        question: "适合快速原型开发的AI工具组合是？",
        options: ["仅使用ChatGPT", "Trae + Cherry Studio", "仅使用Claude Code", "仅使用Kimi CLI"],
        correct: 1,
        explanation: "Trae适合编程，Cherry Studio适合多模型对话，两者组合适合快速原型开发。"
      },
'''

new_medium_questions = '''      // 新增的AI工具深度题目
      {
        category: "tool",
        question: "Trae的Composer模式与Chat模式的主要区别是？",
        options: ["Composer是免费版", "Chat用于问答，Composer用于代码编辑", "没有区别", "Chat功能更强大"],
        correct: 1,
        explanation: "Chat模式用于问答交流，Composer模式专门用于代码编辑和重构。"
      },
      {
        category: "tool",
        question: "Claude Code + Claude Pro订阅相比Cursor的优势是？",
        options: ["价格更便宜", "可以访问更大的上下文", "功能完全相同", "支持更多语言"],
        correct: 1,
        explanation: "Claude Code组合可以访问更大的上下文窗口，适合处理大型代码库。"
      },
      {
        category: "tool",
        question: "Kimi Code CLI的斜杠命令中，用于切换模型的是？",
        options: ["/help", "/model", "/config", "/switch"],
        correct: 1,
        explanation: "使用/model命令可以切换Kimi Code CLI使用的AI模型。"
      },
      {
        category: "tool",
        question: "Cherry Studio的'深度研究'功能最适合？",
        options: ["写简单邮件", "需要多步骤推理的复杂问题", "只查询天气", "播放音乐"],
        correct: 1,
        explanation: "深度研究基于Kimi 1.5长思考能力，适合需要多步骤推理的复杂问题。"
      },
      {
        category: "tool",
        question: "Google Antigravity的5小时滚动窗口限制意味着？",
        options: ["每天只能用5小时", "任意连续5小时内的使用量受限", "总共只能用5小时", "每月5小时"],
        correct: 1,
        explanation: "滚动窗口指任意连续5小时内有一定限制，不是每日总量限制。"
      },
      {
        category: "tool",
        question: "OpenCode的推荐模型配置在哪里修改？",
        options: ["不能修改", "~/.config/opencode/config.json", "系统注册表", "仅Web界面"],
        correct: 1,
        explanation: "OpenCode的配置文件位于~/.config/opencode/config.json。"
      },
      {
        category: "tool",
        question: "API Key被泄露后应该首先做什么？",
        options: ["等待观察", "立即撤销并重新生成", "修改密码", "联系客服"],
        correct: 1,
        explanation: "API Key泄露后应立即在控制台撤销该Key并重新生成新的Key。"
      },
      {
        category: "tool",
        question: "个人开发者最适合的AI编程助手方案是？",
        options: ["Cursor Pro $20/月", "Trae个人版免费", "Claude Code + API按量", "全部购买"],
        correct: 1,
        explanation: "Trae个人版完全免费且不限量使用Claude 3.7，是个人开发者的最佳选择。"
      },
      {
        category: "tool",
        question: "以下哪种场景应该使用企业版AI工具？",
        options: ["个人学习", "处理客户敏感数据", "写个人博客", "查询公开文档"],
        correct: 1,
        explanation: "处理客户敏感数据时应使用企业版，通常有更强的数据保护和使用协议。"
      },
'''

# 在初级题库中添加新题目
# 找到初级题库中"知识库使用基础"部分之前的位置
pattern_easy = r'(// 初级题库.*?// 知识库使用基础)'
match = re.search(pattern_easy, content, re.DOTALL)
if match:
    insert_pos = match.start(1) + len(match.group(1))
    content = content[:insert_pos] + '\n' + new_easy_questions + content[insert_pos:]
    print("Added easy questions")
else:
    print("Could not find easy questions insertion point")

# 在中级题库中添加新题目  
pattern_medium = r'(// 中级题库.*?// 知识库进阶)'
match = re.search(pattern_medium, content, re.DOTALL)
if match:
    insert_pos = match.start(1) + len(match.group(1))
    content = content[:insert_pos] + '\n' + new_medium_questions + content[insert_pos:]
    print("Added medium questions")
else:
    print("Could not find medium questions insertion point")

# 保存修改后的文件
with open('ai-training-quiz.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated file size: {len(content)} bytes")
print("Done!")
