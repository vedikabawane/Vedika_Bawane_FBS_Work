# Convert the time entered in hh,min and sec into seconds.

hr=int(input('Enter the hr:'))
min=int(input('Enter the min:'))
sec=int(input('Enter the sec:'))

min1=hr*60
sec1=min1*60
sec2=min*60

total_sec=sec1+sec2+sec
# print(total_sec)

print(f'conver time into sec {total_sec}')