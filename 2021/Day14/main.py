from collections import defaultdict, Counter

def parse_input():
    with open("./input") as f:
        counter = True 
        keys = defaultdict()
        for line in f.readlines():
            if counter:
                templet = list(line.strip())
                counter = False
                continue
            key , value = line.strip().split(' -> ')    
            keys[key] = value
    return keys, templet

if __name__=="__main__":
    mapping, template = parse_input()
    new_template = template.copy()
    #steps = 40 
    #for step in range(steps):
    #    j = 0
    #    for i in range(len(new_template)-1):
    #        temp = keys[str(template[i]+template[i+1])]
    #        new_template = new_template[0:j+1] + list(temp) + new_template[j+1:]
    #        j += 2
    #    template = new_template.copy()
    #    print(step)
    #maximum = max(new_template, key=new_template.count)
    #minimum = min(new_template, key=new_template.count)
    #print(new_template.count(maximum) - new_template.count(minimum))
    #

    # better method
    shingles = [template[i]+template[i+1] for i in range(len(template)-1)]
    values = defaultdict(int)
    elements = Counter(template)
    for shingle in shingles:
        values[shingle] = 1
    steps = 40 
    for step in range(steps):
        keys = list(values.keys())
        new_values = defaultdict(int)
        for key in keys:
            length = values[key]
            letter = mapping[key]
            new_values[key[0]+letter] += length 
            new_values[letter+key[1]] += length 
        values = new_values.copy()
        print(step)
    m = elements.most_common()
    ck = Counter()
    for k in values.keys():
        ck[k[0]] += values[k]
    ck[template[-1]] += 1
        
    print(max(ck.values())- min(ck.values()))
    print(m[0][1]-m[-1][1])
    print(m[0][1], m[-1][1])
    #added commet for git code        


        

