import csv

# combine wsmerwin.txt & newyorker_text.txt
filenames = ['wsmerwin_clean.txt', 'newyorker_text_clean.txt']
with open('wsmerwin_total.txt', 'w') as outfile:
    for file in filenames:
        with open(file) as infile:
            for line in infile:
                outfile.write(line)

                
# convert into csv for easier gpt-2 processing (i think)
lines = []

with open('wsmerwin_total.txt') as text:
    text_lines = text.readlines()
    for line in text_lines:
        lines.append(line)

# break into four-line "stanzas" for optimal tweet length
lines_new=[]
for i in range(0, len(lines), 4):
    lines_new.append(''.join(lines[i: i+4]))
        
with open('wsmerwin_total.csv','w', newline='') as f:    
    write = csv.writer(f)
    write.writerows([lines_new[index]] for index in range(0, len(lines_new))) 