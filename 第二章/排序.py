def doubbleSort(numbers):
    for j in range(len(numbers)-1,-1,-1):
        for i in range(j):
            if(numbers[i]>numbers[i+1]):
                numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
        print(numbers)

def main():
    numbers=[2,4,365,7,3,1]
    doubbleSort(numbers)
if __name__=='__main__':
    main()
