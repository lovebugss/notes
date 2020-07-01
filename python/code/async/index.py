import asyncio
import time


def timeit(func):
    start = time.time()

    async def wrapper(*args, **kwargs):
        resp = await func(*args, **kwargs)
        print('fucntion name: [%s] used time: [%f], args: [%s], kwargs: [%s]' % (
            func.__name__, time.time() - start, args, kwargs))
        return resp

    return wrapper


@timeit
async def do():
    print("haha------0")
    await asyncio.sleep(1)
    print("haha------1")
    return time.time()


@timeit
async def test(loop):
    task_list = []
    for i in range(200):
        task = loop.create_task(do())
        task_list.append(task)
    await asyncio.wait(task_list)
    # for task in asyncio.as_completed(task_list):
    #     t = await task
    #     print(t)


def main():
    # 建立 loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    # 执行 loop
    loop.run_until_complete(test(loop))
    # 关闭资源
    loop.close()


if __name__ == '__main__':
    main()
