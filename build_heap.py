# Anastasija Bondare 221RDB395
# python3

def build_heap(data):
    n = len(data) # Jauns mainīgais n, kas satur saraksta "data" garumu
    swaps = []

    for i in range(n // 2, -1, -1): # Cikls sākas no viduspunkta līdz 0 ar soli -1
        smallest = i
        left_child = 2 * i + 1 # Nosaka kreisā bērna pozīciju binārā koka struktūrā
        right_child = 2 * i + 2 

        if left_child < n and data[left_child] < data[smallest]: # Pārbauda, vai kreisā bērna pozīcija neatrodas ārpus koka un 
        # pārbauda, vai bērna vērtība ir mazāka par pašreizējā mezgla vērtību.
            smallest = left_child # Tiek piešķirts mainīgajam "smallest" kreisā bērna pozīcijas indekss.

        if right_child < n and data[right_child] < data[smallest]:
            smallest = right_child

        if smallest != i: # Ja mezgls ar mazāko vērtību atšķiras no pašreizējā mezgla, tad
            swaps.append((i, smallest)) # pievieno sarakstam elementa pārus, kuru mezglu indeksi tika nomainīti
            data[i], data[smallest] = data[smallest], data[i] # Maina pašreizējo mezglu ar mezglu, kuram ir mazākā vērtība.
            first_smallest = smallest # Jaunajam mainīgajam piešķir mazākā mezgla vērtību
            s = first_smallest # Un citam mainīgajam piešķir arī mazākā mezgla vērtību

            while 2 * first_smallest + 2 < n: # Pārbauda, vai labā bērna elements ir mazāks par kopējo elementu skaitu
                if data[2 * first_smallest + 2] < data[s]: # Ja labā bērna indekss ir mazāks par mazākā mezgla indeksu, tad
                    s = 2 * first_smallest + 2 # s tiek atjaunots kā labā bērna indekss
                if data[2 * first_smallest + 1] < data[s]:
                    s = 2 * first_smallest + 1
                if s != first_smallest: # Ja indeksi nesakrīt, tad tiek atrast jauns mazākais elements
                    swaps.append((first_smallest, s)) # Jauns pāris tiek pievienots sarakstam
                    data[first_smallest], data[s] = data[s], data[first_smallest] # Un tad notiek mezglu vērtību maiņa starp s un first_smallest, 
                    first_smallest = s # Mainīgajam first_smallest tiek piešķirts mainīgā s indekss.
                else:
                    break

            if 2 * first_smallest + 1 < n and data[2 * first_smallest + 1] < data[s]: # Pārbauda, vai kreisā bērna elements ir mazāks par kopējo elementu skaitu 
            # un ir mazāks par pašreizējo mazāko elementu
                s = 2 * first_smallest + 1 # Ja iepriekšējie nosacījumi tika izpildīti, tad mainīgais s tiek atjaunots ar kreisā bērna indeksu
                swaps.append((first_smallest, s)) # Jauns pāris tiek pievienots sarakstam
                data[first_smallest], data[s] = data[s], data[first_smallest] # Un tad notiek mezglu vērtību maiņa starp s un first_smallest

    return swaps # Atgriež sarakstu, kas satur informācīju par nomainītajiem elementiem

def main():

    ievade = input()
    
    if "I" in ievade: 
        n = int(input()) 
        data = list(map(int, input().split())) # Ievadītajā skaitļu virknē atdala katru elementu ar vienu atstarpi.
        assert len(data) == n # Pārbauda, vai ievadītais skaitlis sakrīt ar elementu skaitu virknē.

    if "F" in ievade: 
        ievade = "tests/" + input() # Nolasa visu ievadīto ceļu līdz failam,
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