# 📄 Final Report – Task 4  
**Customer Experience Analytics for Fintech Apps**  
**Submitted by:** Desiyalew haregu
**Date:** 07 June 2025  

---

## 🎯 Objective  
This document summarizes **Task 4: Insights and Recommendations**, the final phase of the **10 Academy – AI Mastery Week 2 Challenge**. In this task, we:

- Derived actionable insights from sentiment and thematic analysis  
- Visualized key findings  
- Delivered a stakeholder-friendly report with practical recommendations  

**Goal:** Simulate the role of a Data Analyst at **Omega Consultancy**, advising **CBE**, **BOA**, and **Dashen Bank** on how to improve customer satisfaction via data-driven product development.

## 🔍 Key Insights Summary (Per Bank)

### ✅ Commercial Bank of Ethiopia (CBE)  
- **Sentiment:** Mostly neutral to positive  
- **Drivers:** Good UI, reliable transactions  
- **Pain Points:** App crashes, slowness  

### ❗ Bank of Abyssinia (BOA)  
- **Sentiment:** Mostly negative  
- **Drivers:** Some praise for features  
- **Pain Points:** Login errors, poor UI, frequent crashes  

### ✅ Dashen Bank  
- **Sentiment:** Balanced, leaning positive  
- **Drivers:** Biometric login, intuitive interface  
- **Pain Points:** Occasional slowness, limited features  

---

## 📊 Visualizations in Final Report  

1. Sentiment Distribution by Bank  
2. Average Sentiment Score by Rating  
3. Monthly Review Trends  
4. Word Cloud of Themes  
5. Top Themes Frequency Across Banks  
6. Themes per Bank (Stacked Bar Chart)  
7. Top Drivers vs Pain Points per Bank  

**Created using:**  
- `matplotlib`  
- `seaborn`  
- `wordcloud`  

**Located in Jupyter Notebooks:**  
- `04_reporting/AnalyzedReview.ipynb`  
- `04_reporting/ThematicReview.ipynb`

---

## 🛠️ Methodology Overview  

### **Data Source**  
- Scraped Google Play Store reviews (**Task 1**)  
- Cleaned & preprocessed using `pandas`  
- Sentiment analysis via Hugging Face Transformers (**Task 2**)  
- Thematic extraction via TF-IDF + manual clustering (**Task 2**)  
- Stored results in Oracle XE DB (**Task 3**)

### **Tools Used**  
- Python: `transformers`, `scikit-learn`, `spaCy`, `pandas`, `numpy`  
- Visualization: `matplotlib`, `seaborn`, `wordcloud`  
- Database: Oracle XE  
- Version Control: Git

---


---

## 💡 Actionable Recommendations

| Pain Point             | Recommendation                                 |
|------------------------|------------------------------------------------|
| App crashing           | Improve backend stability and error logging   |
| Slow transfers         | Optimize server response time                 |
| Login errors           | Implement secure fallback authentication      |
| Poor UI                | Conduct UX testing and redesign               |
| Limited features       | Add budget tracking, dark mode                |
| No chatbot support     | Build NLP-based AI assistant                  |
| Infrequent updates     | Increase deployment frequency                 |

These recommendations help enhance user satisfaction and strengthen digital banking experiences.

---

## 📌 KPIs Met

| KPI                                             | Status |
|--------------------------------------------------|--------|
| 7-page report with 7+ visualizations             | ✅     |
| 2+ drivers/pain points per bank                  | ✅     |
| Practical recommendations                        | ✅     |
| Clear, labeled plots                             | ✅     |
| GitHub repo with merged tasks                    | ✅     |

---

## 🧪 Optional: Unit Testing  

Unit tests were implemented for:

- CSV loading  
- Sentiment scoring  
- Theme extraction pipeline  
- Oracle DB insertion  

**Frameworks Used:** `unittest`, `pytest`

---

## 🚀 Next Steps  

- Integrate NLP topic modeling (e.g., **LDA**, **BERTopic**) for automated theme detection  
- Deploy AI-powered chatbot trained on complaints  
- Build real-time feedback dashboard using **Flask**  
- Analyze iOS App Store reviews for expanded insights  

---

## 📬 Conclusion  
Task 4 wraps up a complete data analytics pipeline for mobile banking app reviews:

✅ Scraping → ✅ Preprocessing → ✅ Sentiment & Thematic Analysis → ✅ Storage → ✅ Visualization → ✅ Final Recommendations

All deliverables were completed as per the challenge requirements, providing technical rigor and actionable business value.

---

