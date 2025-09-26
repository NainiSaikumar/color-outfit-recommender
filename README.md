# 🎨 Color Psychology Outfit Recommender  

A fun Python console app that suggests outfit colors based on your **mood** using simple rules from **color psychology**.  
For example:  
- Red → Confidence, passion  
- Blue → Calmness, trust  
- Yellow → Happiness, energy  

👕👗 This project helps you decide *what to wear today* in a fun, interactive way.  

---

## ✨ Features
- Asks for your **mood** (happy, calm, confident, energetic, stressed).  
- Recommends an outfit color + style with friendly messages.  
- Randomizes suggestions so results feel fresh each time.  
- Emojis for a more fun experience 🎉.  
- (Optional) Use `outfits.json` to store outfit data separately.  
- (Optional) Save user history in a text file like a mini fashion diary.  

---

## 🛠️ Requirements
- **Python 3.x**  

Built-in libraries:
- `random` → pick random suggestions  
- `json` → load data from `outfits.json`  

Optional libraries (for colors & emojis in console):  
```bash
pip install colorama emoji
