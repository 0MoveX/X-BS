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


if __name__ == "__main__":
    # 有了这一段，直接点 VSCode 右上角的 ▷（Run Python File）就能把服务起起来。
    # 没有它的话，python main.py 只是把上面几行 import 完就退出，什么都不会发生。
    # 注意 uvicorn 收的是「模块名:变量名」的字符串，不是 app 对象本身——这样 reload 才能生效。
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
