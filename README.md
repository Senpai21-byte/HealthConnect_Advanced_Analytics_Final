# 🏥 HealthConnect Clinic — Week 8 Final Analytics & Decision Support

**AnalystLab Africa Experience Lab · Data Analytics Track · Final Integration, Presentation & Showcase**

> **Project question:** How can HealthConnect Clinic use data and AI to reduce missed appointments and improve the patient support experience?

## ⚡ Headline

Half of booked visits in the dataset are missed (51.2%), but the problem is concentrated: bookings made **more than 45 days ahead** miss **71.4%** of the time and produce **224 excess no-shows**, more than the next two risk groups combined. Reminders matter most exactly there — the SMS vs no-reminder gap grows from **1.7 pp** (within a week) to **10.7 pp** (46–60 days ahead).

## 📁 Contents

```text
Week8_Assignment/
├── HealthConnect_Week8_Final_Analytics_Report.md     ← main deliverable (all brief sections)
├── HealthConnect_Week8_Executive_Summary.md          ← one-page summary for non-technical readers
├── HealthConnect_Week8_Integration_Evidence.md       ← cross-track record + handoffs (individual work)
├── HealthConnect_Week8_Validated_Findings_Register.csv
├── dashboard/
│   └── HealthConnect_Week8_Final_Dashboard.html      ← open in any browser
├── presentation/
│   ├── HealthConnect_Week8_Analytics_Presentation.pptx  (12 slides, speaker notes)
│   └── Video_Presentation_Script.md                  ← 5–10 min individual video script
├── figures/  F1–F6 final charts + Week 7 stability chart
├── data/
│   ├── validated_aggregates/*.csv                    ← Week 7 validated figures (source for everything)
│   └── week8_dashboard_figure_validation.csv         ← 27/27 consistency checks
├── scripts/
│   └── week8_validate_and_build_figures.py           ← validates figures, rebuilds all charts
└── week7_carried_forward/                            ← Week 7 testing record + summary
```

## 🔁 Reproduce

```bash
pip install pandas matplotlib
python scripts/week8_validate_and_build_figures.py
```

## 🧭 Project journey

| Week | Stage | Data Analytics output |
|---|---|---|
| 4 | Problem understanding | Track responsibilities, KPI plan |
| 5 | Analysis | EDA, five KPIs defined |
| 6 | Integration & validation | CIs, z-tests, interaction analysis, `previous_*` audit |
| 7 | Testing & refinement | Exact reproduction, resampling, denominator + small-sample fixes |
| **8** | **Final integration & presentation** | **Final dashboard, validated KPIs, recommendations, presentation** |

## 🤝 A note on collaboration

I was unable to find fellow interns from the other tracks to form an HC-POD, so this project was completed individually. No other track's output is presented as real; instead, ready-to-use handoffs for Data Science, ML Engineering, GenAI and Project Management are in `HealthConnect_Week8_Integration_Evidence.md`.

## ⚠️ Limitations

Synthetic data (use comparisons, not the absolute rate) · findings are associations, not proven causes · lost slot rate is an upper bound (no cancellation timestamp) · `previous_no_shows` only partly verified · the overall reminder effect is provisional · model, pipeline and assistant stages not built.

## 🛠️ Tools

Python · pandas · matplotlib · Wilson confidence intervals · two-proportion z-tests · split-half and bootstrap resampling · HTML/CSS/JavaScript dashboard

#AnalystLabAfrica
