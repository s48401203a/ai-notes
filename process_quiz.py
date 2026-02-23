#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# 读取原文件
with open('ai-training-quiz.html.backup', 'r', encoding='utf-8') as f:
    content = f.read()

print(f"Original file size: {len(content)} bytes")

# ===== 修改界面文案 =====
# 1. 修改难度选择页面标题
content = content.replace('选择你的挑战难度', '先选择难度，再开始挑战')

# ===== 修改JS逻辑 =====
# 2. 修改selectDifficulty函数，选择后直接显示规则和开始挑战按钮
old_selectDifficulty = '''function selectDifficulty(difficulty) {
      currentDifficulty = difficulty;
      
      document.querySelectorAll('.difficulty-card').forEach(card => {
        card.classList.remove('selected');
      });
      document.querySelector(`.difficulty-card.${difficulty}`).classList.add('selected');
      
      const descriptions = {
        easy: '初级：基于知识库基础内容，适合AI新手入门测试（35道题库）',
        medium: '中级：基于知识库进阶内容，需要理解工具原理和使用技巧（40道题库）',
        hard: '高级：扩展到整个AI知识圈，包含Transformer、RAG、微调等技术深度题（42道题库）',
        expert: '专业级：全行业AI前沿知识，涵盖MoE、RLHF、DPO、并行训练等地狱难度（38道题库）'
      };
      
      document.getElementById('difficultyDescription').textContent = descriptions[difficulty];
      document.getElementById('selectedDifficultyInfo').style.display = 'block';
      document.getElementById('startBtn').disabled = false;
    }'''

new_selectDifficulty = '''function selectDifficulty(difficulty) {
      currentDifficulty = difficulty;
      
      document.querySelectorAll('.difficulty-card').forEach(card => {
        card.classList.remove('selected');
      });
      document.querySelector(`.difficulty-card.${difficulty}`).classList.add('selected');
      
      // 隐藏提示，显示规则和按钮
      document.getElementById('selectHint').style.display = 'none';
      document.getElementById('difficultyDetails').style.display = 'block';
      
      // 生成称号预览
      const levelTitles = titles[difficulty];
      let previewHtml = '';
      previewHtml += `<span style="background:rgba(100,100,100,0.2);padding:5px 12px;border-radius:15px;">60-69分：${levelTitles[60].title}</span>`;
      previewHtml += `<span style="background:rgba(34,197,94,0.2);color:var(--easy);padding:5px 12px;border-radius:15px;">70-79分：${levelTitles[70].title}</span>`;
      previewHtml += `<span style="background:rgba(245,158,11,0.2);color:var(--medium);padding:5px 12px;border-radius:15px;">80-89分：${levelTitles[80].title}</span>`;
      previewHtml += `<span style="background:rgba(249,115,22,0.2);color:var(--hard);padding:5px 12px;border-radius:15px;">90-99分：${levelTitles[90].title}</span>`;
      previewHtml += `<span style="background:linear-gradient(135deg,rgba(168,85,247,0.3),rgba(236,72,153,0.3));color:#e879f9;padding:5px 12px;border-radius:15px;font-weight:600;">100分：${levelTitles[100].title}</span>`;
      document.getElementById('titlePreview').innerHTML = previewHtml;
    }'''

content = content.replace(old_selectDifficulty, new_selectDifficulty)

# 3. 修改startQuiz函数，直接开始测验（跳过中间的确认页面）
old_startQuiz = '''function startQuiz() {
      if (!currentDifficulty) return;
      
      document.getElementById('difficultyScreen').style.display = 'none';
      document.getElementById('startScreen').style.display = 'block';
      
      const config = difficultyConfig[currentDifficulty];
      document.getElementById('difficultyBadge').textContent = config.emoji + ' ' + config.name;
      document.getElementById('difficultyBadge').className = 'difficulty-badge ' + config.badge;
      
      const sources = {
        easy: '题目来源：知识库基础内容（工具分类、安全规范、基本概念）',
        medium: '题目来源：知识库进阶内容（使用技巧、定价策略、最佳实践、提示词进阶）',
        hard: '题目来源：扩展AI知识圈（Transformer、RAG、量化、推理优化、部署、AI安全）',
        expert: '题目来源：全行业AI前沿知识（MoE、RLHF、DPO、并行训练、推测解码、可解释性）'
      };
      document.getElementById('questionSource').textContent = sources[currentDifficulty];
      
      // 生成称号预览
      const levelTitles = titles[currentDifficulty];
      let previewHtml = '';
      previewHtml += `<span style="background: rgba(100,100,100,0.2); padding: 5px 12px; border-radius: 15px;">60-69分：${levelTitles[60].title}</span>`;
      previewHtml += `<span style="background: rgba(34,197,94,0.2); color: var(--easy); padding: 5px 12px; border-radius: 15px;">70-79分：${levelTitles[70].title}</span>`;
      previewHtml += `<span style="background: rgba(245,158,11,0.2); color: var(--medium); padding: 5px 12px; border-radius: 15px;">80-89分：${levelTitles[80].title}</span>`;
      previewHtml += `<span style="background: rgba(249,115,22,0.2); color: var(--hard); padding: 5px 12px; border-radius: 15px;">90-99分：${levelTitles[90].title}</span>`;
      previewHtml += `<span style="background: linear-gradient(135deg, rgba(168,85,247,0.3), rgba(236,72,153,0.3)); color: #e879f9; padding: 5px 12px; border-radius: 15px; font-weight: 600;">100分：${levelTitles[100].title}</span>`;
      document.getElementById('titlePreview').innerHTML = previewHtml;
    }'''

new_startQuiz = '''function startQuiz() {
      // 此方法已不再使用，保留以兼容旧代码
      beginQuiz();
    }'''

content = content.replace(old_startQuiz, new_startQuiz)

# 4. 添加showHistory函数
old_showTab = '''function showTab(tab) {
      document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
      event.target.classList.add('active');
      
      if (tab === 'quiz') {
        document.getElementById('quizTab').style.display = 'block';
        document.getElementById('historyTab').classList.remove('active');
      } else {
        document.getElementById('quizTab').style.display = 'none';
        document.getElementById('historyTab').classList.add('active');
        renderHistoryList();
        updateHistoryStats();
      }
    }'''

new_showTab = '''function showTab(tab) {
      document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
      if (event && event.target) {
        event.target.classList.add('active');
      }
      
      if (tab === 'quiz') {
        document.getElementById('quizTab').style.display = 'block';
        document.getElementById('historyTab').classList.remove('active');
      } else {
        document.getElementById('quizTab').style.display = 'none';
        document.getElementById('historyTab').classList.add('active');
        renderHistoryList();
        updateHistoryStats();
      }
    }
    
    function showHistory() {
      document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.nav-tab')[1].classList.add('active');
      document.getElementById('quizTab').style.display = 'none';
      document.getElementById('historyTab').classList.add('active');
      renderHistoryList();
      updateHistoryStats();
    }'''

content = content.replace(old_showTab, new_showTab)

print("JS logic updated")

# ===== 修改HTML结构 =====
# 修改难度选择界面，添加提示和详细信息区域
old_difficulty_screen = '''      <!-- 难度选择界面 -->
      <div class="start-screen" id="difficultyScreen">
        <h2 style="margin-bottom: 10px;">先选择难度，再开始挑战</h2>
        <p style="color: var(--text-secondary); margin-bottom: 30px;">不同难度对应不同的知识范围和题目来源</p>
        
        <div class="difficulty-select">'''

new_difficulty_screen = '''      <!-- 难度选择界面 -->
      <div class="start-screen" id="difficultyScreen">
        <h2 style="margin-bottom: 10px;">先选择难度，再开始挑战</h2>
        <p style="color: var(--text-secondary); margin-bottom: 30px;">不同难度对应不同的知识范围和题目来源</p>
        
        <div class="difficulty-select">'''

# 实际上标题已经改了，现在需要修改选择后的显示
old_after_cards = '''        </div>
        
        <div id="selectedDifficultyInfo" style="margin: 20px 0; padding: 15px; background: var(--panel); border-radius: 10px; display: none;">
          <p id="difficultyDescription" style="color: var(--text-secondary);"></p>
        </div>
        
        <button class="btn btn-primary" id="startBtn" onclick="startQuiz()" style="font-size: 1.1em; padding: 15px 50px; margin-top: 20px;" disabled>
          开始挑战
        </button>
      </div>'''

new_after_cards = '''        </div>
        
        <div class="select-hint" id="selectHint" style="color:var(--text-secondary);font-size:14px;margin-top:15px;padding:10px;background:rgba(106,166,255,0.05);border-radius:8px;border:1px dashed var(--border);">
          💡 请先选择上方的难度等级，查看规则后开始挑战
        </div>
        
        <div class="difficulty-details" id="difficultyDetails" style="display:none;margin:30px 0;padding:25px;background:var(--panel);border-radius:12px;border:1px solid var(--border);">
          <h3 style="margin-bottom:15px;color:var(--accent);">📋 测验规则</h3>
          <ul style="color:var(--text-secondary);line-height:2;padding-left:20px;margin-bottom:20px;">
            <li>限时 <strong>5分钟</strong>，超时自动提交</li>
            <li>共 <strong>10道单选题</strong>，每题10分</li>
            <li>可用键盘 <strong>1-4</strong> 快速选择，<strong>← →</strong> 切换题目</li>
            <li>60-100分可获得不同称号，100分有神秘称号！</li>
          </ul>
          <div style="margin:20px 0;padding-top:20px;border-top:1px solid var(--border);">
            <h4 style="color:var(--text-secondary);margin-bottom:15px;font-size:14px;">🏆 称号预览</h4>
            <div id="titlePreview" style="display:flex;flex-wrap:wrap;justify-content:center;gap:10px;font-size:13px;"></div>
          </div>
          <div style="display:flex;gap:15px;justify-content:center;flex-wrap:wrap;margin-top:25px;">
            <button class="btn btn-secondary" onclick="showHistory()">📊 历史记录</button>
            <button class="btn btn-primary" onclick="beginQuiz()" style="font-size:1.1em;padding:15px 40px;">🚀 开始挑战</button>
          </div>
        </div>
      </div>'''

content = content.replace(old_after_cards, new_after_cards)

print("HTML structure updated")

# ===== 修改题库 =====
# 删除UI相关的题目（初级）
# 1. 删除字体大小调节题目
content = re.sub(
    r'\{\s*category:\s*"general",\s*question:\s*"[^"]*字体大小调节[^"]*",[^}]*\},?\s*',
    '',
    content
)

# 2. 删除搜索框快捷键题目
content = re.sub(
    r'\{\s*category:\s*"general",\s*question:\s*"[^"]*搜索框[^"]*",[^}]*\},?\s*',
    '',
    content
)

# 3. 删除Cmd/Ctrl + K题目
content = re.sub(
    r'\{\s*category:\s*"general",\s*question:\s*"[^"]*Cmd/Ctrl \+ K[^"]*",[^}]*\},?\s*',
    '',
    content
)

# 4. 删除doc-center主入口题目
content = re.sub(
    r'\{\s*category:\s*"general",\s*question:\s*"[^"]*doc-center[^"]*",[^}]*\},?\s*',
    '',
    content
)

print("UI questions removed")

# 添加新的AI工具题目到初级题库
# 找到初级题库的末尾位置
easy_end_pattern = r'(// 初级题库.*?const easyQuestions = \[.*?)(\];\s*// 中级题库)'
easy_match = re.search(easy_end_pattern, content, re.DOTALL)
if easy_match:
    print("Found easyQuestions array")
else:
    print("Could not find easyQuestions array")

# 保存修改后的文件
with open('ai-training-quiz.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Updated file size: {len(content)} bytes")
print("Done!")
