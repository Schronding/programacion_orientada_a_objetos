from multiprocessing import Pipe

conn1, conn2 = Pipe()

conn1.send("hello")
conn2.recv()

