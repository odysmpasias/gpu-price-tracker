import pandas as pd
import glob

def clean_data(df):
    df = df.copy()
    df["name"] = df["name"].str.replace("VGA ", "")
    df["brand"] = df["name"].str.split().str[0]
    
    amd = df["name"].str.contains("Radeon|AMD", case = False)
    nvidia = df["name"].str.contains("GeForce|Nvidia|Quadro", case = False)
    intel = df["name"].str.contains("Intel|Arc", case = False)
    
    df.loc[amd, "gpu_maker"] = "AMD"
    df.loc[nvidia, "gpu_maker"] = "NVIDIA"
    df.loc[intel, "gpu_maker"] = "INTEL"
    
    amd_pro_cards = df["name"].str.contains("Radeon pro|Radeon AI PRO", case = False)
    nvidia_pro_cards = df["name"].str.contains("Quadro|RTX PRO", case = False)
    intel_pro_cards = df["name"].str.contains("Arc Pro", case = False)
    df["is_pro"] = (amd_pro_cards|nvidia_pro_cards|intel_pro_cards)

    is_id_4699505 = df["id"] == 4699505
    df.loc[is_id_4699505, "is_pro"] = True

    df["vram"] = df["name"].str.extract(r"(\d+)\s?GB?\b").astype(float)

    is_id_4761812 = df["id"] == 4761812
    df.loc[is_id_4761812, "vram"] = 16

    df["model"] = df["name"].str.extract(r"(?i)((?:RTX|GTX|GT)\s+\d+(?:\sTi)?)", expand=False).str.upper()
    
    model_amd = df["name"].str.extract(r"(?i)(RX\s+\d+(?:\s?(?:XT|GRE))?)", expand=False).str.upper()
    df["model"] = df["model"].fillna(model_amd)
    model_intel = df["name"].str.extract(r"(?i)(ARC\s+[A-Z]\d+)", expand=False).str.upper()
    df["model"] = df["model"].fillna(model_intel)
    df["model"] = df["model"].str.replace(" ", "")
    return df

raw_files = sorted(glob.glob("data/raw/*.csv"))


cleaned_days = []
for file in raw_files:
    raw = pd.read_csv(file)
    cleaned = clean_data(raw)
    cleaned_days.append(cleaned)

all_days = pd.concat(cleaned_days, ignore_index=True)

no_model = all_days[(all_days["model"].isna()) & (~all_days["is_pro"])]
if not no_model.empty:
    raise ValueError(f"{len(no_model)} non-pro cards have no model")

no_maker = all_days[(all_days["gpu_maker"].isna())]
if not no_maker.empty:
    raise ValueError(f"{len(no_maker)} cards have no gpu_maker")

if all_days["is_pro"].all():
    raise ValueError("All cards are marked as pro, check the pro masks")

all_days.to_csv("data/processed/price_clean.csv", index=False)