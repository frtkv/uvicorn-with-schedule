import time
from threading import Thread

import schedule
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def root():
    return {'hello': 'world'}


def func1():
    schedule.every(5).seconds.do(func3)


def func2(app):
    uvicorn.run(app, host='0.0.0.0', port=8000)


def func3():
    print('I\'m working...')


if __name__ == '__main__':
    Thread(target=func1).start()
    Thread(target=func2, args=[app]).start()
    while True:
        schedule.run_pending()
        time.sleep(1)
