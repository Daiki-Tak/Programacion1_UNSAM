# rebotes.py

def rebotar(altura, rebotes):
    for i in range(1,rebotes+1):
        altura*=0.6
        print(i, round(altura, 4))

if __name__ == "__main__":
    import sys
    rebotar(int(sys.argv[1]), int(sys.argv[2]))