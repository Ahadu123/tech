from cmd import Cmd
import threading
import time

globalTimer = 0
thread = None


def printTime():
    global globalTimer
    global thread
    thread = threading.Timer(1.0, printTime)
    thread.start()
    globalTimer = globalTimer + 1
    print(time.strftime("%H:%M:%S", time.localtime(globalTimer)))


class MyCmd(Cmd):
    status = 0
    prompt = "> "

    def do_start(self, args):
        global thread
        if thread == None or not thread.is_alive():
            printTime()

    def do_c(self, args):
        global thread
        if thread != None and thread.is_alive():
            thread.cancel()
            print("Zatrzymano zegar")

    def do_set(self, time):
        global globalTimer
        if time == '':
            print("Musisz podać wartośc w sekundach")
            return
        globalTimer = int(time)

    def do_exit(self, args):
        raise SystemExit()


MyCmd().cmdloop("""
start - startuje zegar, 
c - zatrzymuje zegar, 
set - pozwala ustawić zegar (podaj sekundy po spacji np 'set 3600'), 
exit - wyjście z programu""")