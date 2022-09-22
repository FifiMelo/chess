import random
import time



def main():
    malisz = 0
    muniak = 0
    for x in range(10000):
        if bool(random.getrandbits(1)):
            malisz += 1
        else:
            muniak += 1
        time.sleep(0.004)
        print(f"malisz: {malisz} muniak: {muniak}")
        


if __name__ == "__main__":
    main()