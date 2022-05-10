import json

# join all generated text together

filenames = ['gpt2_gentext_20220429_010003.txt',
             'gpt2_gentext_20220429_005746.txt',
             'gpt2_gentext_20220429_005529.txt',
             'gpt2_gentext_20220429_005314.txt',
             'gpt2_gentext_20220429_005058.txt',
             'gpt2_gentext_20220429_003604.txt',
             'gpt2_gentext_20220429_003946.txt',
             'gpt2_gentext_20220429_004201.txt',
             'gpt2_gentext_20220429_004416.txt',
             'gpt2_gentext_20220429_004629.txt',
             'gpt2_gentext_20220429_004843.txt']

with open('gentext_total.txt', 'w') as f:
    for file in filenames:
        with open(file) as finalfile:
            f.write(finalfile.read())     
            
# clean up text; i'm sure there's a more elegant way to do this!
with open('gentext_total.txt', 'r') as f:
    with open('gentext_total_2.txt', 'w') as w:
        for line in f:
            w.write(line.replace('====================', '').replace('* * *', '').replace('startoftext', '').replace('endoftext', '').replace('|', '').replace('</', '').replace('* *', '').replace('<','').replace('>',''))

# remove blank lines
with open('gentext_total_2.txt', 'r') as f:
    with open('gentext_total_3.txt', 'w') as w:
        for line in f:
            if line.strip():
                w.write(line)
                
# remove any lines that exceed 70 char
with open('gentext_total_3.txt', 'r') as f:
    with open('gentext_total_final.txt', 'w') as w:
        for line in f:
            if len(line) < 70:
                w.write(line)

                
# split into 4-line stanzas, which will each become a tweet
text=[]
with open('gentext_total_final.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        text.append(line)

text_new=[]
for i in range(0, len(text), 4):
    text_new.append(''.join(text[i: i+4]))

with open('gentext_total_four.json', 'w') as w:
        w.write(json.dumps(text_new))

