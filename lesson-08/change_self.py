import re

__called_time = 24


for i in range(__called_time):
    print(i)


lines = []
with open(__file__) as f:
    for line in f.read().split('\n'):
        num = re.findall('called_time .* (\d+)', line)    
        if num:
            num = num[0]
            line = re.sub('\d+', str(int(num)+1), line)
            
        lines.append(line)

with open(__file__, 'w') as f:
    for line in lines:
        f.write(line + '\n')
    
