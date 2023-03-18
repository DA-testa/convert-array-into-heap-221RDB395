# Anastasija Bondare 221RDB395
# python3

def build_heap(data):
    n = len(data)
    swaps = []

    for i in range(n // 2, -1, -1):
        k = i
        while 2 * k + 1 < n:
            j = 2 * k + 1
            if j + 1 < n:
                if data[j + 1] < data[j]:
                    j += 1
            if data[k] > data[j]:
                swaps.append((k, j))
                data[k], data[j] = data[j], data[k]
            else:
                break
            k = j
    return swaps


def main():

    ievade = input()

    if "I" in ievade: # Ja ievadītajā tekstā ir "I", tad 
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