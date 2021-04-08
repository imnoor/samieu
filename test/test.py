data = {"One" :1, "Two" : 2, "Three" :  3 }
data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}
print ("{:<8} {:<15} {:<10}".format('Sl','Label','Count'))
slno=0
for k, v in data.items():
    slno = slno + 1
    print ("{:<8} {:<15} {:<10}".format(slno, k, v))