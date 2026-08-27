# Convert distant given in feet and inches into meter and centimeter. 
#1foot=12inches
#1inch=2.54centimeter
# 100centimeter=1meter


F=int(input('Enter the distant in feet:'))
I=int(input('Enter the distant in inches:'))

I1=F*12
CM=2.54*I1
M=0.01*CM

CM1=2.54*I
M1=0.01*CM1
total_M=M+M1
total_CM=CM+CM1

print(f'Convert distant feet and inches into {total_M}m and {total_CM}cm.')

# I1 = F * 12
# CM = 2.54 * I1
# CM1 = 2.54 * I
# total_CM = CM + CM1
# total_M = total_CM / 100
