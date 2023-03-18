# Anastasija Bondare 221RDB395
# python3

def build_heap(data):
    n = len(data)
    swaps = []
    elements_swaps = 0
    for i in range(n // 2, -1, -1):
        k = i
        while 2 * k + 1 < n:
            j = 2 * k + 1
            if j + 1 < n and data[j + 1] < data[j]:
                j += 1
            if data[k] <= data[j]:
                break
            swaps.append((k, j))
            data[k], data[j] = data[j], data[k]
            k = j
            elements_swaps += 1
    return swaps, elements_swaps 


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    ievade = input()

    if "I" in ievade: # Ja ievadītajā tekstā ir "I", tad 
        number = int(input()) # ievada elementu skaitu, cik  būs kokā
        

    if "F" in ievade: # Ja ievadītajā tekstā ir "F", tad 
        ievade = "tests/" + input() # nolasa visu ievadīto ceļu līdz failam,
        with open(ievade, 'r') as file: # nolasa faila saturu un aizver to,
            number = int(file.readline().strip())  # pēc tam nolasa pirmo rindu un pārveido to par Integer jeb skaitli, kas norāda, cik elemntu būs kokā
            

    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps, elements_swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(elements_swaps)

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
