import os , random

for i in range(15):
    d = str(i) + 'days ago'
    rand = random.randrange(1, 9)
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system('git commit --date=" 2021-'+str(rand)+'-'+d+'" -m 1')
os.system('git push -u origin main')