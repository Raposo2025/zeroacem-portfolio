# Generates synthetic messy sales CSV (fake data)
import random, csv
random.seed(7)
names=["Acme Corp","acme corp ","ACME CORP","Blue Fox LLC","blue fox llc","Nordic Tea","Delta Tools","delta tools  "]
regions=["north","North ","NORTH","south","South","east","West","west "]
dates=["2026-09-0{}","09/{:02d}/2026","{}-Sep-2026"]
rows=[]
for i in range(60):
    d=random.randint(1,9); fmt=random.choice(dates)
    rows.append([f"INV-{1000+i}",random.choice(names),random.choice(regions),fmt.format(d),
      random.choice(["$","","USD "])+f"{random.uniform(50,900):,.2f}",random.choice(["1","2","3"," 4",""])])
rows+=rows[:5]  # duplicates
with open("messy_sales.csv","w",newline="") as f:
    w=csv.writer(f);w.writerow(["Invoice #"," customer","REGION","date","Amount","qty"]);w.writerows(rows)
