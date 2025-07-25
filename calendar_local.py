def calendar():
    level=8
    num=1
    for f in range(level):
        for f1 in range(f):
            print(chr(64+num),end=' ')
            if ord('Z')==64+num:
                break
            num = num + 1


        print()
    class play():
        strr="ismail"
        def fff(self):
            dd={}
            for f in self.strr:
                cnt=self.strr.count(f)
                dd[f]=cnt

            print(dd)
    p=play()
    p.fff()

    lim=5
    num=65
    for f2 in range(1,lim+1):
        for f1 in range(num,num+1):
            print(chr(f1)*f2)
            num=num+1


    from datetime import datetime

    # Create two datetime objects
    date1 = datetime(2023, 1, 15, 10, 30, 0)
    date2 = datetime(2023, 1, 20, 14, 0, 0)

    # Calculate the difference
    difference = date2 - date1

    # Access components of the difference
    print(f"Difference in days: {difference.days}")
    print(f"Total difference in seconds: {difference.total_seconds()}")

    # Get the current date and time
    current_datetime = datetime.now()

    # Extract only the time
    current_time = current_datetime.time()

    print("Current Time:", current_time)

if __name__ == "__main__":
    calendar()