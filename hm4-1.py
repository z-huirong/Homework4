import sys
f = open('complete.csv',encoding="utf-8")
lines = f.readlines()
for line in lines[1:]:
    columns = line.split(',')
    clean_columns = [] 
    in_quote = False  
    for x in columns: 
        clean_x = x.replace('""','') 
        n_quotes = clean_x.count('"')
        if not in_quote:
            clean_columns += [ clean_x ] 
            if n_quotes % 2 != 0:  
                in_quote = True
        else:
            clean_columns[-1] += clean_x  
            if n_quotes % 2 != 0:  
                in_quote = False
    try:
        price = int(clean_columns[9])
    except:
        print("Parsing ERROR: ",line)
        sys.exit(1)
    if price >= 100 and price <= 150:
        print(line)
