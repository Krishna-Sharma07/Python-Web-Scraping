<div align="center">
  <h1>📈 Stock Info Scraper – Web Scraping with BeautifulSoup</h1>
  <p>
    A Python-based tool that scrapes live stock data, financial ratios, quarterly results,<br />
    and shareholding patterns from multiple financial websites.
  </p>
  <br />
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/BeautifulSoup-WebScraping-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/CMD-App-informational?style=for-the-badge" />
</div>

---

## 📋 Table of Contents

* [📌 Overview](#overview)
* [✨ Features](#features)
* [🛠 Tech Stack](#tech-stack)
* [🚀 Getting Started](#getting-started)
* [📁 Project Structure](#project-structure)
* [🧠 How It Works](#how-it-works)
* [🔐 Disclaimer](#disclaimer)
* [🤝 Contributing](#contributing)

---

## 📌 Overview

This project allows you to:

* Search for a stock by its **name** (e.g., `Infosys`, `Tata Motors`)
* Scrape its **live price**, **financial ratios**, **quarterly results**, **shareholding patterns**, and **cash flow**
* Fetch data from:

  * [Kotak Securities](https://www.kotaksecurities.com/)
  * [Screener.in](https://www.screener.in/)

> All of this runs directly in the **command line**, powered by `BeautifulSoup` and `requests`.

---

## ✨ Features

* 🔎 Search stocks by name (auto-parsed URL structure)
* 💸 Get live stock price
* 📊 View key financial ratios (ROE, ROCE, etc.)
* 📅 Quarterly results: Sales, Interest, Expenses, Operating Profit
* 🧾 Shareholding patterns (Promoters, FII, DII, Public)
* 🔄 Cash conversion cycle (Debtor Days, Payables, Cash Cycle)
* 💰 Cash flow from operational activity
* 💡 Lightweight & fast — No browser automation or Selenium

---

## 🛠 Tech Stack

| Layer    | Technology        |
| -------- | ----------------- |
| Language | Python 3.10+      |
| Scraping | BeautifulSoup     |
| Requests | `requests` module |
| Parsing  | lxml parser       |

---

## 🚀 Getting Started

### 🔧 Prerequisites

* Python 3.10+
* Install required libraries:

```bash
pip install beautifulsoup4 requests lxml
```

### ▶️ Run the App

```bash
python main.py
```

Then enter a stock name when prompted:

```bash
Enter Stock Name: Infosys
```

> Output includes stock price, key ratios, financials, and more.

---

## 📁 Project Structure

```
stock-scraper/
├── main.py       # Core logic for scraping and data display
└── README.md     # Documentation
```

---

## 🧠 How It Works

### 🔗 Step-by-Step:

1. **Stock Link Search**
   Scrapes stock list from [kotaksecurities.com/stocks](https://www.kotaksecurities.com/stocks/) and identifies the correct URL from partial match.

2. **Live Price Fetch**
   Scrapes live price from Kotak’s stock detail page.

3. **Fundamentals + Financials**
   Goes to [screener.in](https://www.screener.in/company/) using the stock name and scrapes:

   * Financial ratios
   * Quarterly results
   * Shareholding patterns
   * Operating metrics (Debtor/Payable days)
   * Cash flow

---

## 🔐 Disclaimer

> This project is for **educational and informational** purposes only.
> Web scraping is subject to [robots.txt](https://www.robotstxt.org/) and each site's **terms of service**.
> Do not overuse or deploy this at scale without permission.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes
4. Open a Pull Request 🚀

---

<div align="center">
  🛠️ Built with Python & ❤️ by <a href="https://github.com/Krishna-Sharma07" target="_blank">Krishna Sharma</a>
</div>

---
