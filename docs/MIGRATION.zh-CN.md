# 迁移指南

## 一、复制技能目录

复制完整目录：

- skills/natsci-writing/
- skills/natsci-writing-zh/

保留每个技能内的 references/ 与 assets/。不要只复制 SKILL.md。

## 二、技能目录位置

| agent 包 | 常见 skills 目录 |
|---|---|
| DeepSeek Harness / DSH | ~/.agents/skills/ 或项目 .agents/skills/ |
| Codex | ~/.codex/skills/ |
| Claude Code | ~/.claude/skills/ |
| WorkBuddy / CodeBuddy 等 | 该包配置的 skills 目录 |
| 通用 agent | 任何扫描 */SKILL.md 的目录 |

PowerShell：

~~~powershell
$src = "C:\path\to\NatSci-Writing-skills\skills"
Copy-Item "$src\natsci-writing" "$HOME\.agents\skills\" -Recurse -Force
Copy-Item "$src\natsci-writing-zh" "$HOME\.agents\skills\" -Recurse -Force
~~~

Bash：

~~~bash
cp -R NatSci-Writing-skills/skills/natsci-writing ~/.agents/skills/
cp -R NatSci-Writing-skills/skills/natsci-writing-zh ~/.agents/skills/
~~~

或使用安装器：

~~~bash
python tools/install.py --target ~/.agents/skills --skills both --dry-run
python tools/install.py --target ~/.agents/skills --skills both
~~~

## 三、复制之后

1. 重启或刷新 agent 技能目录；
2. 确认两个技能出现，描述以 "NatSci-Writing-skills" 开头；
3. 校验：
   ~~~bash
   python tools/validate_package.py --installed ~/.agents/skills
   ~~~
4. 分别做一次英文和中文冒烟测试。

## 四、兼容性

- frontmatter：name、description、metadata.version、metadata.system、metadata.language、metadata.companion；未知字段无害。
- 参考文件用相对链接，无绝对路径。
- 图件脚本可选依赖 matplotlib/pandas/numpy（Python）或 ggplot2/patchwork（R）。
- 语料统计写在技能内，语料本身不分发。
- 迁移期间可与旧技能 nature-biology-manuscript-writing 并存；验证新技能后停用旧技能，避免重复触发。

## 五、回滚

从备份恢复原 skills 目录，删除两个 natsci-writing 目录。安装器只写入目标 skills 目录。

## 六、迁移检查

- [ ] 两个技能目录均含 references/ 与 assets/
- [ ] 已安装副本通过校验
- [ ] 技能目录显示两个技能
- [ ] 英文与中文冒烟测试通过
- [ ] 图件 demo 能导出文件
- [ ] 旧重复技能已停用
