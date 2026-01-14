# 💎 AI-Driven Inventory Intelligence SaaS
### Transforming Traditional Excel Workflows into Intelligent Systems

## 🚀 The Business Problem
Despite the rise of expensive ERP systems, over **67% of inventory managers** worldwide still rely on **Microsoft Excel** for their daily operations. Global leaders like **PepsiCo** and **Amazon** still utilize spreadsheet data for critical supply chain analysis because of its flexibility.

However, static spreadsheets are "blind." This project bridges that gap by layering **Google Gemini AI** over Excel/SQLite data to provide real-time business intelligence.

## ✨ Key Features
* **Excel/DB Integration:** Seamlessly reads from existing inventory databases to minimize friction for small business owners.
* **AI Recommendations:** Integrated with **Google Gemini API** to analyze stock levels and predict restock needs for maximum profit.
* **Location-Aware Strategy:** Uses geolocation context (Karachi-focused) to provide advice on logistics and warehouse optimization.
* **Custom GUI:** A professional, user-friendly interface designed for non-technical business managers.
* **Google Search Integration:** The AI can search the live web to compare local market trends against your current inventory.

## 🛠️ Tech Stack
* **Language:** Python
* **AI Engine:** Google Gemini (Generative AI)
* **Data Science:** Pandas
* **Database:** SQLite / Microsoft Excel
* **GUI:** Tkinter / CustomTkinter

## 🛡️ Security First
This repository follows professional security standards:
* **Environment Variables:** Sensitive API keys are managed via `.env` files (not tracked by Git).
* **Gitignore:** Standard Python `.gitignore` implemented to prevent credential leaks.

## ⚙️ How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Add your `GEMINI_API_KEY` to a local `.env` file.
4. Run `gui.py` to launch the application.

**IMPORTANT**
This product has not been finalised and it requies some work before using. Its GUI needs updating which when done will make it more better
