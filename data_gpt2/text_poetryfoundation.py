# clean up wsmerwin.txt
# file is from: https://github.com/eli8527/poetryfoundation-scraper

with open("wsmerwin.txt", "r") as f:
    lines = f.readlines()
with open("wsmerwin_clean.txt", "w") as f:
    for line in lines:
        if not line.isspace():
            f.write(line.strip())
            f.write('\n')
    

