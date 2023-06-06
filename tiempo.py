import time

tiempos = []

def timeit():
    input("Press ENTER to start: ")
    start_time = time.time()
    input("Press ENTER to stop: ")
    end_time = time.time()
    the_time = round(end_time - start_time, 2)
    print(f'Your time was: {the_time}')
    tiempos.append(the_time)
    main()

def main():
    print("Do you want to...")
    print("1. Time your solving")
    print("2. See your solvings")
    print("3. Close this program")
    dothis = input(":: ")
    if dothis == "1":
        timeit()
    elif dothis == "2":
        for curr_time in sorted(tiempos):
            print("%d - %f" % ((sorted(tiempos).index(curr_time)+1), curr_time))
        main()
    elif dothis == '3':
        return
    else:
        print ("WTF? Please enter a valid number...\n")
        main()

main()