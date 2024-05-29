from string import ascii_lowercase, ascii_uppercase, punctuation, digits
from hashlib import sha256
from random import shuffle
from time import time
from datetime import timedelta
from multiprocessing import Manager, Process

def timit(f):
    def wrapper(*args, **kwargs):
        debut = time()
        result = f(*args, **kwargs)
        fin = time()
        print(timedelta(seconds = fin - debut))
        return result
    return wrapper

def compare(password: str, hash: str) -> bool:
    hashed_password = sha256(password.encode()).hexdigest()
    return hashed_password == hash

def search_worker(hash: str, charset: str, start: int, end: int, long: int, stop_event, return_dict, done_queue) -> str | None:
    for x in range(start, end + 1):
        temp_pwd = ''.join(charset[x // (len(charset) ** y) % len(charset)] for y in range(long))

        if compare(temp_pwd, hash):
            return_dict['result'] = temp_pwd
            stop_event.set()

    done_queue.put(True)

@timit
def search(hash: str, min_len: int, max_len: int, charset = 0b11111, num_processes = 8, verbose = 2) -> str | None:
    used_charset = []
    for i, x in enumerate(bin(charset).split('b')[1]):
        if int(x):
            used_charset.extend([ascii_lowercase, ascii_uppercase, punctuation, digits, " "][i])

    if verbose >= 3: print(f"Charset : {used_charset}")

    shuffle(used_charset)
    shuffled_charset = ''.join(used_charset)

    if verbose >= 4: print(f"Shuffled Charset : {shuffled_charset}")

    for cur_len in range(min_len, max_len + 1):
        cur_max_iters = len(shuffled_charset) ** cur_len
        if verbose >= 3: print(f"Nombre de mots de passe possible de longueur {cur_len} : {cur_max_iters:,}")

        amount_per_process = cur_max_iters // num_processes
        rest = cur_max_iters - (amount_per_process * num_processes)
        starts_ends: list[list[int]] = [[amount_per_process * i, amount_per_process * (i + 1) - 1] for i in range(num_processes)]
        starts_ends[-1][-1] += rest

        manager = Manager()
        return_dict = manager.dict()
        stop_event = manager.Event()
        done_queue = manager.Queue()

        args = [(hash, shuffled_charset, start, end, cur_len) for (start, end) in starts_ends]
        processes = []
        for i, arg in enumerate(args):
            p = Process(target=search_worker, args=(*arg, i, stop_event, return_dict, done_queue))
            processes.append(p)
            p.start()

        finished_processes = 0
        while finished_processes < num_processes:
            if stop_event.is_set():
                for p in processes:
                    p.terminate()
                break
            
            try:
                done_queue.get(block=False)
                finished_processes += 1
            except:
                pass

        for p in processes:
            p.join()

        if 'result' in return_dict:
            return return_dict['result']
        elif verbose >= 2: print(f"Not found at length {cur_len}")

    
if __name__ == "__main__":
    with open("./files/hash/hash.txt") as file:
        hash = file.read()
    print(f"Found : {search(hash, 2, 4, num_processes=24, verbose=4)}")