
### **📜 README.md**

# 🌍 Ling CLI - Quick Translations from Ling.pl

A **command-line tool** that fetches translations from **[Ling.pl](https://ling.pl/)**.

🚀 **Features:**
- 🔄 **Polish → English** and **English → Polish** translations
- 📜 **Categorized, structured output**
- 🔗 **Clickable links to Ling.pl**
- 🎨 **Rich CLI formatting for readability**
- 🏃 **Works directly from the command line**

---

## **🛠 Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/ling-cli.git
cd ling-cli
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Make the Script Executable**
```bash
chmod +x lang.py
```

### **4️⃣ (Optional) Add to PATH**
To run the script from **anywhere**:
```bash
mv lang.py /usr/local/bin/lang
```
Now, you can simply type:
```bash
lang książka
```
instead of:
```bash
python lang.py książka
```

---

## **🚀 Usage**
### **Polish → English (Default)**
```bash
lang książka
```
**Example Output:**
```
┌──────────────────────────────────────────────┐
│ 🔗 https://ling.pl/slownik/polsko-angielski/książka │
└──────────────────────────────────────────────┘

┌───────────────────────────┐
│  Translations for 'książka'  │
└───────────────────────────┘

🔹 **book**
   - (a written work or composition that has been published)
   - "I am reading a good book on economics."

🔹 **book~ kucharska**
   - cookbook

🔹 **book~ telefoniczna**
   - phone book
```

### **English → Polish (`-a` flag)**
```bash
lang book -a
```
**Example Output:**
```
┌──────────────────────────────────────────┐
│ 🔗 https://ling.pl/slownik/angielsko-polski/book │
└──────────────────────────────────────────┘

┌───────────────────────────┐
│  Translations for 'book'  │
└───────────────────────────┘

🔹 **książka**
   - (a collection of written pages)

🔹 **book~ telefoniczna**
   - phone book

🔹 **book~ kucharska**
   - cookbook
```

---

## **📌 Features**
✅ **Polish to English (Default)**  
✅ **English to Polish (`-a` flag)**  
✅ **Formatted output with structured categories**  
✅ **Clickable links to the source on Ling.pl**  
✅ **Works as a standalone CLI tool**  

---

## **🎯 How It Works**
- Uses **BeautifulSoup** to scrape translations from **Ling.pl**.
- Extracts **translations and categories**.
- Formats the **CLI output with Rich** for better readability.

---

---

## **📜 License**
This project is licensed under the **MIT License**.

---


