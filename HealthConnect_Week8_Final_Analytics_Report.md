# HealthConnect Clinic — Week 8 Final Analytics & Decision Support Package
### AnalystLab Africa Experience Lab · Data Analytics Track · Final Integration & Presentation

**Project:** Improving Patient Appointment Attendance and Healthcare Support Using Data and AI
**Project question:** *How can HealthConnect Clinic use data and AI to reduce missed appointments and improve the patient support experience?*

| Package component (brief §8B) | Where it is |
|---|---|
| Final dashboard | `dashboard/HealthConnect_Week8_Final_Dashboard.html` |
| Final KPIs | Section 3 · `data/validated_aggregates/kpi_final.csv` |
| Validated findings | Section 4 · `HealthConnect_Week8_Validated_Findings_Register.csv` |
| Key visualizations | Section 6 · `figures/F1`–`F6` |
| Business insights | Section 7 |
| Recommendations | Section 8 |
| Analytical limitations | Section 12 |
| Cross-track contribution | Section 10 · `HealthConnect_Week8_Integration_Evidence.md` |
| Executive summary | `HealthConnect_Week8_Executive_Summary.md` |
| Presentation materials | `presentation/` (slides + 5–10 min video script) |

---

## 0. Note to assessors: this was completed as individual work

I was not able to find or connect with fellow interns from the other tracks (Project Management, Data Science, ML Engineering, Generative AI) to form a working HC-POD, in Week 8 or in the earlier weeks. Everything in this package was produced by me alone, using only the approved HealthConnect resources and my own Week 5–7 work.

I have not presented any other track's work as if it existed. Where the brief asks for an output received from another track, this package says "not received" and explains the effect. To make the lack of a team as small a problem as possible, I prepared ready-to-use handoff packages for each track (Section 10), so that my component can be integrated immediately by any HC-POD or reviewer who picks it up.

---

## 1. Week 7 → Week 8 Transition

1. **Main Week 7 output.** A testing and refinement notebook that re-derived every Week 6 KPI and statistic from the raw data, stress-tested the headline findings with split-half and 300-iteration bootstrap resampling, checked dashboard filter logic, and re-ran the `previous_*` field audit.
2. **Most important testing result.** Every one of 20+ Week 6 figures reproduced exactly from the raw file, and the three headline findings (long lead time, repeat non-attendance, the pilot segment) held in both random halves of the data.
3. **Major issue discovered.** The overall claim "any reminder beats no reminder" (z = 2.92) is fragile: it is significant in only 59% of half-size and 84% of full-size resamples. Two dashboard-safety gaps were also found: KPI 3 used a different denominator from the other KPIs, and nothing stopped tiny segments (n = 2, n = 0) being shown as headline rates.
4. **What was refined.** Each KPI now states its population; a minimum-sample rule (n < 30 → suppress) was specified; the reminder claim was downgraded to "provisional"; the audit sub-split is disclosed with a caveat.
5. **Component now ready.** The final KPI set, the validated driver ranking and the named pilot segment.
6. **Still to be integrated.** The two Week 7 dashboard refinements existed only in the notebook. In Week 8 they are now built into a working dashboard (Section 5). A Data Science model output to compare against has never been received.
7. **Tracks involved in final integration.** By design: Data Science, Project Management, GenAI and ML Engineering. In practice: none were available (Section 0), so I prepared handoffs for each.
8. **What I will demonstrate.** The final dashboard, the five KPIs with their denominators, the three priority segments, the evidence behind each finding, and the recommendations.

---

## 2. Part 1 — Final Integration Readiness

| Requirement | My response |
|---|---|
| What is my final component? | The HealthConnect Final Analytics & Decision Support Package: a validated KPI set, an interactive dashboard, a ranked list of no-show drivers, and evidence-graded recommendations. |
| What problem does it address? | The clinic does not know which appointments are most likely to be missed or where to spend reminder and follow-up effort. This component identifies the high-risk groups and sizes them. |
| What is its current status? | **Ready for integration.** All figures validated (27/27 consistency checks pass); dashboard built with both Week 7 safety refinements applied. |
| What did I improve during Week 7? | KPI denominators labelled; n < 30 suppression rule; reminder-effect claim downgraded to provisional; audit sub-split caveated. |
| Which other track(s) does it depend on? | Data Science (a model/feature-importance output to cross-check my driver ranking). Project Management (tracking the cancellation-timestamp data request). |
| Which track(s) depend on my output? | Data Science (driver ranking, feature cautions), ML Engineering (expected input fields and value ranges), GenAI (approved figures and escalation triggers), Project Management (insights, risks, recommendations). |
| What output will I provide? | Section 10 handoff packages, the KPI and findings CSVs, and the dashboard. |
| What output do I need from another track? | A baseline or candidate model with feature importances (Data Science); confirmation of the risk-flag format (ML Engineering). **Neither received** — no teammates available. |
| What evidence demonstrates readiness? | `data/week8_dashboard_figure_validation.csv` (27 checks), Week 7 testing record (carried forward in `week7_carried_forward/`), the figure-build script that regenerates every chart. |
| What limitations remain? | Synthetic data; KPI 2 is an upper-bound proxy; associations, not proven causes; `previous_*` field only partly verified; processed Week 5/6 file still missing (Section 12). |

---

## 3. Final KPIs

| # | KPI | Final value | Population (denominator) | 95% CI | Confidence |
|---|---|---|---|---|---|
| 1 | No-Show Rate | **51.2%** | 2,423 of 4,737 Attended + No-Show visits | 49.7–52.6% | High |
| 2 | Lost Slot Rate | **53.7%** | 2,686 No-Show + Cancelled of 5,000 bookings | — | Low: upper-bound proxy |
| 3 | Reminder Coverage | **72.7%** | 3,634 of 5,000 bookings (72.9% = 3,452 of 4,737 on KPI 1's base) | — | High |
| 4 | Repeat No-Show Rate (≥2 prior) | **63.5%** | 510 visits by patients with ≥2 prior no-shows | 59.3–67.6% | High |
| 5 | High-Risk Booking Rate (>45 days lead) | **71.4%** | 1,107 visits booked >45 days ahead (23.4% of visits) | 68.6–73.9% | High |

**Final confirmation:** these five KPIs are unchanged from Week 6 in value. What changed in Weeks 7–8 is that each now states its population and confidence level, which is what makes them safe to show a non-technical audience.

---

## 4. Validated Findings

| ID | Finding | Evidence | Status |
|---|---|---|---|
| V1 | Booking lead time is the strongest driver. >45 days: 71.4% vs 51.2% baseline (+20.2 pp). | Reproduced exactly; halves +18.6 / +21.9 pp | **Robust** |
| V2 | Risk rises with each prior no-show: 46.3% → 55.9% → 62.1% → 69.7% for 0–3 prior. | Reproduced exactly; ≥2 prior halves 62.4 / 64.6% | **Robust** |
| V3 | SMS has the lowest no-show rate (48.0%), below WhatsApp (52.7%, z = −2.47) and no reminder (54.6%, z = −3.68). | Significant in all resampling checks | **Robust** |
| V4 | SMS vs Email (48.0% vs 51.0%) is **not** a proven difference (z = −1.20). | Non-significant in both halves | **Confirmed non-significant** |
| V5 | Reminders matter far more for long-lead bookings: the SMS vs no-reminder gap is 1.7 pp at 0–7 days and 10.7 pp at 46–60 days. | Interaction table reproduced exactly | **Robust** |
| V6 | Pilot segment: >45 days and no reminder, n = 286, 77.6% vs 69.2% for reminded peers (~24 recoverable visits). | Gap 8.1 / 9.0 pp in halves | **Robust** |
| V7 | "Any reminder beats none" overall (49.9% vs 54.6%, z = 2.92). | Significant in only 59% / 84% of resamples | **Provisional** |
| V8 | `previous_no_shows` matches true history at each visit for only 13.8% of multi-visit patients. | As-at-appointment share reproduced exactly; sub-split off by 26 patients | **Headline confirmed; detail caveated** |

A note on the channel rates in V3/V4/V7: Week 7 printed the channel sizes and z-scores but not the rates. Solving for the no-show counts that satisfy all five reported statistics at once (baseline, three SMS z-tests, none-vs-any z-test) gives exactly one answer (SMS 915/1,907; Email 258/506; WhatsApp 548/1,039; None 702/1,285). These counts are used for the dashboard and are re-checked by the validation script.

---

## 5. Dashboard Finalisation & Figure Validation

**What was built.** `dashboard/HealthConnect_Week8_Final_Dashboard.html` is a single-file interactive dashboard (opens in any browser, no install) with five KPI cards and four views: lead time & reminders (with a lead-band selector), patient history, where to act, and confidence & limits.

**Week 7 refinements now implemented in the dashboard (previously only in the notebook):**
- Every KPI card states its numerator, denominator and population, so the KPI 3 base difference is visible rather than hidden.
- The n < 30 rule is live: the 4-prior (n = 12) and 5-prior (n = 3) groups are hidden by default and shown as "hidden · n=12". A review toggle can reveal them, marked with a warning. The 5-prior group would otherwise have shown a misleading "100%" rate.
- Every finding carries its evidence grade (Robust / Provisional / No proven difference).

**Validation of dashboard figures.** `scripts/week8_validate_and_build_figures.py` checks that every number on the dashboard and slides is internally consistent before any chart is drawn. **27 of 27 checks pass**, including: channel sizes add to 4,737 and channel no-shows add to 2,423; the dose-response groups add to 4,737 and the ≥2-prior groups to 510; all three KPI confidence intervals recompute exactly; all four reminder z-scores recompute exactly from the counts; the lost-slot proxy equals (2,423 + 263) / 5,000; the pilot segment plus its complement equals the 1,107 high-risk visits. Output: `data/week8_dashboard_figure_validation.csv`.

---

## 6. Key Visualizations

| Figure | Message |
|---|---|
| `F1_lead_time_noshow.png` | Risk climbs from 51.2% overall to 71.4% for bookings made >45 days ahead. |
| `F2_prior_noshow_dose_response.png` | Each prior no-show adds risk; groups with n < 30 are shown as suppressed. |
| `F3_reminder_channel.png` | SMS has the lowest no-show rate; axis starts at zero so small gaps are not exaggerated. |
| `F4_lead_time_x_reminder.png` | The reminder gap widens from 1.7 pp to 10.7 pp as lead time grows. |
| `F5_impact_ranking.png` | Long-lead bookings account for 224 excess no-shows, more than the other two segments combined. |
| `F6_robustness_split_half.png` | The three headline findings hold in two random halves of the data. |
| `week7_reminder_effect_stability.png` | (Week 7) Why the overall reminder claim is provisional. |

---

## 7. Business Insights

1. **The problem is concentrated, not spread evenly.** Bookings made more than 45 days ahead are about a quarter of visits but produce 224 excess no-shows, more than repeat non-attenders (63) and unreminded patients (45) combined. The clinic can target its effort.
2. **Lead time and reminders work together.** A reminder matters little for a visit next week, but matters a lot for a visit two months away. The value of each reminder depends on when the visit was booked.
3. **Past behaviour is a practical warning sign.** A patient with 3 previous no-shows misses about 70% of visits. Staff can act on this without any model.
4. **Channel choice matters, but less than timing.** SMS clearly beats WhatsApp and no reminder. Whether SMS beats Email is not proven, so Email should not be dropped.
5. **About 27% of visits get no reminder at all.** That is 1,285 visits, 286 of them in the highest-risk long-lead group, which is the most obvious gap to close.

---

## 8. Recommendations

| # | Recommendation | Evidence | Owner (suggested) |
|---|---|---|---|
| R1 | **Flag every booking made >45 days ahead** and add a re-confirmation step about 7 days before the visit. | V1, V5 — Robust | Clinic admin / scheduling |
| R2 | **Run a controlled reminder pilot on the 286 long-lead, unreminded visits** (half reminded by SMS, half not) to prove the effect before a clinic-wide rule. Target: ~24 recovered visits. | V6 Robust; V7 Provisional → pilot is the test | Clinic admin + PM |
| R3 | **Give patients with ≥2 prior no-shows extra support:** a personal call, easy rebooking, and a GenAI assistant rebooking prompt. | V2 — Robust | Patient support + GenAI |
| R4 | **Use SMS as the default reminder channel;** keep Email as an option. Move WhatsApp-only patients to SMS where they agree. | V3 Robust, V4 | Clinic admin |
| R5 | **Close the reminder gap** (27% of visits unreminded), starting with long-lead bookings. | V5, V6 | Clinic admin |
| R6 | **Start recording cancellation date/time** so the lost-slot rate can be measured properly and late cancellations offered to waiting-list patients. | KPI 2 limitation | PM / data owner |
| R7 | **Keep the dashboard rules** (denominators shown, n < 30 hidden) in any future version. | Week 7 Tests 2 & 4 | Data Analytics |

---

## 9. How the Findings Support HealthConnect Decisions

| Clinic decision | What the analytics tells them |
|---|---|
| Which appointments need extra reminder effort? | Long-lead (>45 days) first, then repeat non-attenders (R1, R3). |
| Which reminder channel to standardise on? | SMS, without dropping Email (R4). |
| Is a blanket "remind everyone" policy proven? | Not yet — pilot first (R2). |
| Where can freed slots come from? | Long-lead no-shows; requires cancellation timestamps to manage properly (R6). |
| Which patients should the GenAI assistant proactively support? | Patients with ≥2 prior no-shows and long-lead bookings (Section 10). |

---

## 10. Cross-Track Contribution (Individual — no HC-POD available)

The full record, in the nine-point format required by brief §9, is in `HealthConnect_Week8_Integration_Evidence.md`. Summary:

| Intended link (brief §10 matrix) | What I provided | What I received | Status |
|---|---|---|---|
| Data Analytics → Data Science | Validated driver ranking; feature cautions (`previous_*` only 13.8% verified; lead time is safe); suggested features and thresholds | Nothing — no DS intern | Handoff ready, not exchanged |
| Data Analytics → ML Engineering | Required input fields, valid ranges, the n < 30 reporting rule | Nothing — no MLE intern | Handoff ready, not exchanged |
| Data Analytics → GenAI | Approved figures the assistant may quote, and patient situations that should trigger escalation to staff | Nothing — no GenAI intern | Handoff ready, not exchanged |
| Data Analytics → Project Management | Insights, recommendations, risk and issue entries, presentation section | Nothing — no PM intern | Handoff ready, not exchanged |

I did not simulate any other track's output. The Week 6/7 pending Data Science exchange is now closed as **"not possible — no Data Science intern available"** rather than carried forward as pending.

---

## 11. Final End-to-End Walkthrough (Analytics View)

| Step | Content | Status |
|---|---|---|
| 1. The problem | 51.2% of booked visits in the dataset are missed; the clinic wants fewer missed visits and better use of slots. | Delivered |
| 2. The data | `HealthConnect_Appointment_Data.csv` (5,000 synthetic bookings), data dictionary, knowledge base. Originals untouched. | Delivered |
| 3. The analytics | Lead time, prior no-shows and reminder channel drive no-shows; long-lead unreminded visits are the top priority. | **Delivered (this package)** |
| 4. Predictive component (DS) | My driver ranking and feature cautions are ready to feed a model. | Not built — no DS intern |
| 5. ML Engineering component | Input specification ready (Integration Evidence §C). | Not built — no MLE intern |
| 6. GenAI component | Approved figures and escalation triggers ready (Integration Evidence §D). | Not built — no GenAI intern |
| 7. Project management layer | I kept my own issue log, risk list and timeline across Weeks 5–8. | Partly covered by me |
| 8. The final solution | Intended flow: data → analytics flags high-risk bookings → a model scores each booking → the pipeline sends targeted reminders → the assistant supports rebooking. Only the analytics stage exists today, but it is usable on its own as a rule-based targeting method (R1–R5). | Analytics stage complete |
| 9. Business value | Staff effort focused on about a quarter of bookings where the excess no-shows are; a pilot that can prove or disprove the reminder effect cheaply. | Delivered |
| 10. Limitations | Section 12. | Delivered |

---

## 12. Analytical Limitations

1. **Synthetic data.** The 51% no-show rate is a feature of the dataset, not a real clinic benchmark. Comparisons between groups are the useful output.
2. **Associations, not causes.** None of the findings is proven to be causal. The reminder pilot (R2) is how cause should be tested.
3. **KPI 2 is an upper bound.** No cancellation timestamp exists, so late and early cancellations cannot be separated. Unresolved for four weeks.
4. **`previous_*` fields only partly verified.** Only 13.8% of multi-visit patients' values match their visit-by-visit history. Good for description; not proven safe as a live model input.
5. **Reminder effect overall is provisional** (59–84% of resamples significant).
6. **Band-level channel counts** were not exported in Week 7, so the dashboard's per-band channel view shows rates without group sizes and is labelled indicative.
7. **Missing artefacts.** The processed Week 5/6 file was never recovered, and the raw CSV was not part of my Week 8 file set, so Week 8 consolidates the Week 7 validated outputs rather than recomputing from raw. The script is ready to be re-run if a raw-data version is added.
8. **No cross-track validation.** Without teammates, no one outside my track has reviewed these outputs.

---

## 13. Remaining Issues & Dependencies

| Item | Status |
|---|---|
| Cancellation timestamp (KPI 2) | Open — recommendation R6 |
| `previous_*` 26-patient sub-split gap | Open — needs the original processed file |
| Data Science model / feature importances | Closed as not possible (no DS intern) |
| Dashboard refinements (denominators, n < 30) | **Closed — implemented in Week 8** |
| Reminder claim provisional | Open — resolved only by running the pilot |

---

## 14. Reflection

**Key takeaway.** Testing mattered more than the first analysis: my numbers were all correct, but Week 7 still found a fragile claim, a hidden denominator difference and a missing safety rule.

**What I learned.** How to grade evidence (robust vs provisional) instead of treating every result the same; how to design a dashboard so it cannot mislead with tiny groups; and how to document honestly when a dependency cannot be met.

**Next version.** Add cancellation timestamps; run the reminder pilot; build a simple risk score with a Data Science partner; connect the dashboard directly to the raw file so it refreshes automatically.
