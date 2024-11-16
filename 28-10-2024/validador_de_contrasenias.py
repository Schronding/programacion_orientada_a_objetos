from multiprocessing import Pipe
import threading

def send_password(conn):
    password = 'holajaja82'
    conn.send(password)
    #total_strength = conn.recv()
    #print(f'Your password is {total_strength}')

def judge_password(conn):
    enough_characters, numbers, uppercase, lowercase = False, False, False, False
    metrics = [enough_characters, numbers, uppercase, lowercase]
    password = conn.recv()
    print(password)
    total_strength = 0
    map_of_strength = {0: 'Very Weak', 
                       1: 'Weak', 
                       2: 'Decent', 
                       3: 'Strong', 
                       4: 'Very Strong'}
    if len(password) >= 8:
        enough_characters = True
    for character in password:
        if character.isinstance(int):
            numbers = True
        elif character.islower():
            lowercase = True
        elif character.isupper():
            uppercase = True 
    for metric in metrics:
        if metric:
            total_strength += 1
    conn.send(map_of_strength[total_strength])

writing_pipe, judging_pipe = Pipe()

writing_thread = threading.Thread(target = send_password, args = (writing_pipe))
judging_thread = threading.Thread(target = judge_password, args = (judging_pipe))

writing_thread.start()
judging_thread.start()

writing_thread.join()
judging_thread.join()