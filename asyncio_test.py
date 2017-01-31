def sendme():
    while 1:
        something = yield
        if something is None:
            raise StopIteration()
        print(something)

gen = sendme()
next(gen)

gen.send('a')
gen.send('b')
gen.send(None)