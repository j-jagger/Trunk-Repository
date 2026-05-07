from quart import Quart
from granian import Granian
import subprocess


app = Quart(__name__,static_folder=None)

HOST = "127.0.0.1"
PORT = 3303



@app.route("/")
async def RootRoute():
    print("Hello, World.")
    return "hi"


if __name__ == "__main__":
    print("Starting WebText...")

    server = Granian("main:app", interface="asgi",log_enabled=True,workers=1)
    server.serve()
