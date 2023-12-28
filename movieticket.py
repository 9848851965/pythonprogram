name=input('PLEASE ENTER YOUR NAME:-')
email=input('PLEASE ENTER YOUR VALID EMAIL ID:-')
password=(input('PLEASE ENTER YOU VALID PASSWORD:-'))
print(' SUCESSFULLY VERIFIED YOUR MAIL ID AND PASS WORD')
print('WELL COME TO BOOK TICKET APPLICATION')
print('1.KGF')
print('2.SALAAR')
print('3.PUSHPA2')
movieName=int(input('PLEASE SELT MOVIE NAME:-'))
print('1.diamond for 300 rs')
print('2.gold for 200 rs')
print('3.silver 100 rs')
option=int(input('PLEASE SELECT YOUR CHOICE:-'))
seats=int(input('PLEASE ENTER HOW MANY SEATS DO YOU WANT:-'))
diamond=30
gold=40
silver=30
match option:
    case 1:
        print('now available seats are')
        out=diamond-seats
        cal=seats*300
    case 2:
        print(' now available seats are')
        out=gold-seats
        cal=seats*200
    case 3:
        print('now available seats are')
        out=silver-seats
        cal=seats*100
print(out)
print(cal)
print('SUCESSFULLY BOOKED YOUR TICKETS THANKS FOR CHOOSING THIS APPLICATION')
        

        
