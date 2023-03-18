# Anastasija Bondare 221RDB395
# python3

def build_heap(data):
    n = len(data) # Jauns mainīgais n, kas satur saraksta "data" garumu
    swaps = []

    for i in range(n // 2, -1, -1):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and data[left] < data[smallest]:
            smallest = left

        if right < n and data[right] < data[smallest]:
            smallest = right

        if smallest != i:
            swaps.append((i, smallest))
            data[i], data[smallest] = data[smallest], data[i]
            s = smallest
            k = s

            while 2 * s + 2 < n:
                if data[2 * s + 2] < data[k]:
                    k = 2 * s + 2
                if data[2 * s + 1] < data[k]:
                    k = 2 * s + 1
                if k != s:
                    swaps.append((s, k))
                    data[s], data[k] = data[k], data[s]
                    s = k
                else:
                    break

            if 2 * s + 1 < n and data[2 * s + 1] < data[k]:
                k = 2 * s + 1
                swaps.append((s, k))
                data[s], data[k] = data[k], data[s]

    return swaps

def main():

    ievade = input()
    
    if "I" in ievade: # Ja ievadītajā tekstā ir "i", tad 
        n = int(input()) # ievada elementu skaitu, cik  būs kokā.
        data = list(map(int, input().split())) # Ievadītajā skaitļu virknē atdala katru elementu ar vienu atstarpi.
        assert len(data) == n # Pārbauda, vai ievadītais skaitlis sakrīt ar elementu skaitu virknē.

    if "F" in ievade: # Ja ievadītajā tekstā ir "F", tad 
        ievade = "tests/" + input() # nolasa visu ievadīto ceļu līdz failam,
        with open(ievade, 'r') as file: # nolasa faila saturu un aizver to,
            n = int(file.readline().strip())  # pēc tam nolasa pirmo rindu un pārveido to par Integer jeb skaitli, kas norāda, cik elemntu būs kokā
            data = list(map(int, file.readline().strip().split())) # Lasa nākamo rindu, atdala elementus sava starpā ar vienu atstarpi un pārveido katru elementu par Integer skaitli.
            # Mainīgajā "data" tiek piešķirta vērtība, kas saturēs n elementus no faila.
            assert len(data) == n # Pārbauda, vai ievadītais skaitlis sakrīt ar elementu skaitu virknē.

    swaps = build_heap(data) # Tiek izveidots maksimālais koks no mainīgā "data" elementiem,
    # tas nozīmē, ka vislielākais elements kļūst par koka sakni un nākāmais lielākais elements tiks novietots koka otrajā līmenī.
    # Un ar komandu swaps notiks elementu maiņa koka struktūrā.

    print(len(swaps)) # Izdrukā skaitu, cik reižu tika apmaninīti elementi ar vietām.
    for i, j in swaps:
        print(i, j) # Tiek izvadīti divi skaitļi, kurus samainīja vietām.

if __name__ == "__main__":
    main()