import pandas as pd

# Sukuriame vienos dienos duomenis kas valandą (nuo 7:00 iki 21:00)
data = {
    "hour": [
        "07:00",
        "08:00",
        "09:00",
        "10:00",
        "11:00",
        "12:00",
        "13:00",
        "14:00",
        "15:00",
        "16:00",
        "17:00",
        "18:00",
        "19:00",
        "20:00",
        "21:00",
    ],
    "gliukose_mg_dl": [
        90,
        95,
        135,
        120,
        100,
        98,
        145,
        130,
        105,
        95,
        92,
        140,
        125,
        100,
        95,
    ],
    "food": [
        None,
        "Scrambled eggs, bread",
        None,
        None,
        None,
        "Chicken salad, risotto",
        None,
        None,
        None,
        None,
        None,
        "Salmon with buckwheat",
        None,
        None,
        None,
    ],
}

# Paverčiame žodyną į Pandas lentelę
df = pd.DataFrame(data)

# Atspausdiname pradinę lentelę
print("INITIAL TABLE:")
print(df.to_string(index=False))
print("-" * 50)
print("RESULTS (Glucose spikes after meals):")

results_list=[]
# Einam per kiekvieną eilutę pagal indeksą
for i in range(len(df)):
  # Patikriname, ar šioje eilutėje yra įrašytas maistas
  if pd.notna(df.loc[i, "food"]):
    base = df.loc[i, "gliukose_mg_dl"]
    food = df.loc[i, "food"]
    ini_time = df.loc[i, 'hour']

    # Paimame kitas 2 valandas (i+1 ir i+2 eilutes)
    future = df.loc[i + 1 : i + 3, "gliukose_mg_dl"]
   # back_level =df.loc[i : i + 6, "gliukose_mg_dl"]

    if not future.empty:
      m_val = future.max()
      spike = m_val - base





      results_list.append({'Food': food, 'Base': base, 'Peak': m_val, 'Spike': spike})

core = pd.DataFrame(results_list)
print(core)

    