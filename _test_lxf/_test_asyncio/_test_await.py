# 可等待对象
# 如果一个对象可以在 await 语句中使用，那么它就是 可等待 对象。
# 许多 asyncio API 都被设计为接受可等待对象。
# 可等待 对象有三种主要类型: 协程, 任务 和 Future.


import asyncio

async def nested():
    return 42


# 协程
async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    # nested()

    # Let's do it differently now and await it:
    print(await nested())  # will print "42".

asyncio.run(main())


# 任务
async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())


# Futures
# Future 是一种特殊的 低层级 可等待对象，表示一个异步操作的 最终结果。
#
# 当一个 Future 对象 被等待，这意味着协程将保持等待直到该 Future 对象在其他地方操作完毕。
#
# 在 asyncio 中需要 Future 对象以便允许通过 async/await 使用基于回调的代码。
#
# 通常情况下 没有必要 在应用层级的代码中创建 Future 对象。
#
# Future 对象有时会由库和某些 asyncio API 暴露给用户，用作可等待对象:

# async def main():
#     await function_that_returns_a_future_object()
#
#     # this is also valid:
#     await asyncio.gather(
#         function_that_returns_a_future_object(),
#         some_python_coroutine()
#     )