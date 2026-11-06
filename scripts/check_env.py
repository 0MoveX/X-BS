# -*- coding: utf-8 -*-
"""一次性体检：确认整条后端依赖链都能 import，且 passlib+bcrypt 真的能哈希密码。"""
import importlib

mods = [
    ("fastapi", "后端框架"),
    ("uvicorn", "ASGI 服务器"),
    ("pydantic", "数据校验"),
    ("pydantic_settings", "配置管理"),
    ("sqlalchemy", "ORM"),
    ("alembic", "数据库迁移"),
    ("aiosqlite", "异步 SQLite 驱动"),
    ("jose", "JWT (python-jose)"),
    ("passlib", "密码哈希"),
    ("bcrypt", "bcrypt 后端"),
    ("multipart", "表单/OAuth2 登录"),
    ("httpx", "异步 HTTP 客户端"),
    ("dns", "DNS 查询 (dnspython)"),
    ("pytest", "测试"),
    ("email_validator", "邮箱校验"),
]

print("%-20s %-12s %s" % ("模块", "版本", "说明"))
print("-" * 62)
fail = []
for name, desc in mods:
    try:
        m = importlib.import_module(name)
        ver = getattr(m, "__version__", "")
        print("%-20s %-12s %s" % (name, ver, desc))
    except Exception as e:
        fail.append(name)
        print("%-20s %-12s %s  <<< 失败: %s" % (name, "导入失败", desc, e))

print()
print("=== 密码哈希实测（passlib + bcrypt 4.0.1）===")
try:
    from passlib.context import CryptContext

    ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")
    h = ctx.hash("MyPassw0rd!")
    print("hash  :", h[:29] + "...")
    print("verify:", ctx.verify("MyPassw0rd!", h), "(正确密码应为 True)")
    print("wrong :", ctx.verify("wrongpass", h), "(错误密码应为 False)")
except Exception as e:
    fail.append("passlib+bcrypt")
    print("失败:", e)

print()
print("=== 结果 ===")
print("全部通过" if not fail else ("有失败: " + ", ".join(fail)))
