vegetables_features = [
    "swieze", "mrozone",
    "ostre", "slodkie",
    "zielone", "czerwone",
    "lokalne", "tropikalne",
    "lisciaste", "bulwowe"
    ]


vegetables = {
    "A": ["swieze", "ostre", "czerwone"],
    "B": ["mrozone", "zielone", "slodkie","lisciaste"],
    "C": ["swieze", "zielone", "czerwone", "slodkie"]
}

def softSetAnalize(features, items, selected_features):

    reduct = []

    for item in items:
        row = []
        for feature in features:
            if (feature in items[item]) and (feature in selected_features): # jeśli cecha znajduje się w danym przedmiocie oraz w szukanych cechach
                row.append(1*selected_features[feature]) # do reduktu dodaj 1 * waga szukanej cechy
        reduct.append(row)

    #print("Tabelka cech")
    #for elem in reduct:
    #    print(elem)

    items_values = {}

    for i, elem in enumerate(items): # do elementow dokładamy sumę wartości ich cech
        items_values[elem] = sum(reduct[i])

    #print("Elementy z wagami")
    #print(items_values) 

    max_val = float("-inf")
    max_elem_tab = []

    for elem in items_values: # znajdujemy element o maksymalnej wartosci
        if items_values[elem] >= max_val:
            max_val = items_values[elem]

    for elem in items_values: # znajdujemy resztę elementów o wartości równej max i dodajemy do tablicy wynikowej
        if items_values[elem] == max_val:
            max_elem_tab.append(elem)

    return max_elem_tab


selected_features = {"swieze":0.3,"ostre":0.6,"zielone":0.6}

solution = softSetAnalize(vegetables_features, vegetables, selected_features)

print("Wybraliśmy element najbardziej dopasowany do twoich oczekiwań:")
for elem in solution:
    print(elem)



