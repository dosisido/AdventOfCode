from math import sqrt
import os
import threading
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FILE = 'file.txt'


def read_table():
    seeds = []
    data = {}
    new_line = True
    last_index = 0
    with open(FILE, 'r') as f:
        lines = f.readlines()
        line = lines[0].split()
        line.pop(0)
        for i in range(len(line)):
            seeds.append(int(line[i]))

        for i in range(1, len(lines)):
            line = lines[i].strip()
            
            if line == '':
                new_line = True
                continue
        
            if new_line:
                new_line = False
                line = line.replace(' map:', '').replace("-to-", ' ').split()
                last_index = line[0]
                data[last_index] = {
                    'to': line[1],
                    'values': []
                }
                continue
            
            ints = []
            for el in line.split():
                ints.append(int(el))
            data[last_index]['values'].append(ints)
        
                
    # print(seeds)
    # print(data)
    return seeds, data

def num_from_seed(seed, data, print_el = False):
    num = seed
    # if print_el: print(seed)  
    location = 'seed'
    while location != 'location':
        if print_el: print(num, end=' ')
        # converte il numero 
        for el in data[location]['values']:
            if num >= el[1] and num < el[1]+el[2]:
                num = el[0] + num - el[1]
                break
        else:
            correct = el
    
        location = data[location]['to']
    
    if print_el: print(num, end=' ')
    if print_el: print()
    return num

def primo(seeds, data):
    low = 9999999999999999999999999999999999

    for seed in seeds:
        num = num_from_seed(seed, data)
        low = min(num, low)
        
    print(low)

def secondo(seeds, data):
    low = 9999999999999999999999999999999999
    number_of_low = None
    step_of_low = None

    def process_seed_range(start, end, step):
        nonlocal low
        nonlocal number_of_low
        nonlocal step_of_low

        for seed in range(start, end, step):
            num = num_from_seed(seed, data)
            if num < low:
                low = num
                number_of_low = seed
                step_of_low = step
            # low = min(num, low)

    # prendo solo alcuni numeri e poi faccio solo quelli attorno al minimo
    threads = []
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        end = seeds[i] + seeds[i+1]
        step = int(sqrt(end - start))
        thread = threading.Thread(target=process_seed_range, args=(start, end, step))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(low, number_of_low, step)

    low = 999999999999999999999999999999999
    for i in range(number_of_low - step, number_of_low + step):
        num = num_from_seed(i, data)
        low = min(low, num)
    print('low:', low)

def main():
    seeds, data = read_table()
    # num_from_seed(82, data, print_el=True)

    # primo(seeds, data)
    secondo(seeds, data)


if __name__ == "__main__":
    main()