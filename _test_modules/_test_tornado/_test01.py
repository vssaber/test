import tornado.ioloop


def pub_message():

    print("hello")
    print("world")


tornado.ioloop.PeriodicCallback(pub_message, 5000).start()
tornado.ioloop.IOLoop.instance().start()
