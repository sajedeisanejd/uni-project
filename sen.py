count=0
c=1
sum=0
print('enter 0 when you done')
while(c>0):
    sen=int(input('sen daneshjo ra vared konid'))
    if(sen==0):
        break
    sum=sum+sen
    count+=1
print(f'miangin sen {count} daneshjo :{sum/count}')