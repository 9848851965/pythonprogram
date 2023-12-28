name=input('PLEASE ENTER YOUR NAME:-')
email=input('PLEASE ENTER YOUR VALID EMAIL ID:-')
password=(input('PLEASE ENTER YOU VALID PASSWORD:-'))
print(' SUCESSFULLY VERIFIED YOUR MAIL ID AND PASS WORD')
print('WELL COME TO BOOK TICKET APPLICATION')
print('1.KGF-200 RS')
print('2.SALAAR-100 RS')
print('3.PUSHPA2-300 RS')
movieName=int(input('PLEASE SELT MOVIE NAME:-'))
print('1.diamond for 200 rs')
print('2.gold for 100 rs')
print('3.silver 50 rs')
option=int(input('PLEASE SELECT YOUR CHOICE:-'))
seats=int(input('PLEASE ENTER HOW MANY SEATS DO YOU WANT:-'))
diamond=30
gold=40
silver=30
match option:
    case 1:
        print('now available seats are')
        out=diamond-seats
        cal=seats*200
    case 2:
        print(' now available seats are')
        out=gold-seats
        cal=seats*100
    case 3:
        print('now available seats are')
        out=silver-seats
        cal=seats*300
print(out)
print(cal)
print('SUCESSFULLY BOOKED YOUR TICKETS THANKS FOR CHOOSING THIS APPLICATION')
        

        
