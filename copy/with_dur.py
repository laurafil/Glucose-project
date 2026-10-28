import pandas as pd

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
        "Salmon with buckwheat",
        None,
        None,
        None,
        None,
    ],
}

df = pd.DataFrame(data)

results_list = []

for i in range(len(df)):
  if pd.notna(df.loc[i, "food"]):
    base = df.loc[i, "gliukose_mg_dl"]
    food = df.loc[i, "food"]

    # 1. Randame, kur yra kitas valgymas (jei yra)
    future_slice = df.loc[i + 1 :]
    subsequent_meals = future_slice[future_slice["food"].notna()]

    if not subsequent_meals.empty:
      next_meal_idx = subsequent_meals.index[0]
      # Imame tik iki kito valgymo pradžios
      future = df.loc[i + 1 : next_meal_idx - 1]
    else:
      # Jei kito valgymo nėra, imame iki pat lentelės galo
      future = df.loc[i + 1 :]

    if not future.empty:
      m_val = future["gliukose_mg_dl"].max()
      spike = m_val - base

      # Ieškome normalizavimo su +5 mg/dl tolerancija
      recovery_rows = future[future["gliukose_mg_dl"] <= (base + 5)]

      if not recovery_rows.empty:
        recovery_row = recovery_rows.iloc[0]
        recovery_time = recovery_row["hour"]
        recovery_index = recovery_rows.index[0]
        duration = recovery_index - i
      else:
        recovery_time = "Did not return"
        duration = None

      results_list.append({
          "Food": food,
          "Base": base,
          "Peak": m_val,
          "Spike": spike,
          "Recovery Time": recovery_time,
          "Duration": duration,
      })

core = pd.DataFrame(results_list)
print(core.to_string(index=False))