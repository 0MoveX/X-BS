# X-BS · 网络安全资产信息收集与测绘平台

> 本科毕业设计 · 重庆移通学院 信息安全学院 · 申崇曦（2023212485） · 指导教师：高明

输入一个域名或 IP，平台调度插件化扫描引擎，把子域名、端口、指纹、ICP 备案、目录、JS 接口等零星信息统一归集成可检索的资产台账，并支持资产聚合、可视化看板与报告导出。

**本平台只做信息收集与资产测绘，不含任何攻击性能力**——没有漏洞利用、没有弱口令爆破、没有反弹 shell、没有内网横向、没有 WebShell 管理。设计定位是帮助资产负责人搞清楚"我到底有哪些资产暴露在公网上"，而非突破它们。

---

## 项目现状

当前处于**骨架搭建阶段**（2026 学年秋季学期）。已经能跑起来的东西：

- [x] FastAPI 应用骨架与健康检查接口
- [x] 依赖清单（`requirements.txt`）与一键环境自检（`scripts/check_env.py`）
- [x] VSCode 调试 / 任务配置（断点调试、一键起服务、接口文档跳转）
- [x] Git 仓库与分支规范

规划中（随进度更新）：

- [ ] 用户认证与项目管理（JWT）
- [ ] 统一资产数据模型（User / Project / Asset / Task / ScanResult）
- [ ] 插件化扫描引擎（统一 `run(target) -> 标准化结果` 接口，注册即用）
- [ ] 异步任务调度器（并发限流、状态机、SSE 进度推送、取消、断点续扫）
- [ ] 内置插件：子域名枚举 / 端口探测 / C 段扫描 / 目录探测 / 指纹识别 / ICP 备案 / JS 接口提取
- [ ] 前端管理界面与资产可视化
- [ ] 报告导出（Excel / PDF）
- [ ] AI 助手（自然语言查询资产、解释扫描结果）
- [ ] Docker 一键部署

## 技术栈

| 层次 | 选型 |
| --- | --- |
| 后端框架 | FastAPI + Uvicorn |
| 数据层 | SQLAlchemy 2.0 + PostgreSQL（开发期用 SQLite）+ Alembic 迁移 |
| 认证 | JWT（python-jose + passlib + bcrypt） |
| 前端 | Vue 3 + Vite + Element Plus + Pinia + Vue Router + Axios + ECharts |
| 扫描能力 | asyncio + dnspython + httpx + socket |
| 部署 | Docker + docker-compose |

## 快速开始

环境要求：Python 3.12+、Node 20+、Git。

```bash
# 1. 克隆
git clone https://github.com/0MoveX/X-BS.git
cd X-BS

# 2. 创建虚拟环境并安装依赖
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt

# 3. 自检：确认所有依赖都能正常导入、密码哈希库工作正常
python scripts/check_env.py

# 4. 启动服务
uvicorn main:app --reload --port 8000
```

启动后：

- 服务首页 → <http://127.0.0.1:8000/>
- 交互式接口文档 → <http://127.0.0.1:8000/docs>
- 健康检查 → <http://127.0.0.1:8000/api/health>

## 目录结构

```
X-BS/
├── main.py                 # 后端入口（后续会拆分为 app/ 分层结构）
├── requirements.txt        # Python 依赖，每行带用途注释
├── scripts/
│   └── check_env.py        # 环境自检：导入检查 + 密码哈希实测
├── .vscode/                # 调试、任务、格式化配置
└── .gitignore
```

## 免责声明

本项目仅用于**已获得明确授权**的资产梳理、安全建设与教学演示场景。使用者须自行确保对目标资产拥有合法测试授权，并遵守《中华人民共和国网络安全法》及相关法律法规。作者不对任何未经授权的使用行为承担责任。
