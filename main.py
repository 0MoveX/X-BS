from fastapi import FastAPI

# 这就是你的平台后端入口。title 和 version 会自动显示在接口文档里。
app = FastAPI(title="资产信息收集与测绘平台", version="0.1.0")


@app.get("/")
def root():
    """首页：证明服务活着。"""
    return {"message": "Hello，这是你的第一个 FastAPI 接口！"}


@app.get("/api/health")
def health():
    """健康检查接口：前后端联调、部署探活都会用到。"""
    return {"status": "ok", "service": "asset-platform", "version": "0.1.0"}
