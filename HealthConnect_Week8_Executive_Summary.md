# HealthConnect Clinic — Executive Summary of Analytical Findings
### Data Analytics Track · Week 8 · AnalystLab Africa Experience Lab

**The question.** How can HealthConnect Clinic reduce missed appointments and make better use of its slots?

**The answer in one line.** Missed visits are concentrated in bookings made far in advance and among patients who have missed before, and a reminder helps most exactly where the risk is highest, so the clinic should target its reminder and follow-up effort rather than spread it evenly.

**What the data shows** (5,000 synthetic appointments; every figure reproduced exactly and stress-tested in Week 7, 27/27 consistency checks in Week 8):

- **51.2%** of attended-or-missed visits are no-shows (95% CI 49.7–52.6%). This is a synthetic-data level, so the comparisons below matter more than the level itself.
- **Bookings made more than 45 days ahead** miss **71.4%** of the time. They are 23.4% of visits but produce **224 excess no-shows**, more than the next two risk groups combined.
- **Patients with 2 or more previous no-shows** miss **63.5%** of visits; the risk rises with every previous miss.
- **SMS reminders** have the lowest no-show rate (48.0%), clearly better than WhatsApp (52.7%) and no reminder (54.6%). SMS vs Email is not a proven difference.
- **Reminders matter most for long-lead bookings:** the gap between SMS and no reminder is 1.7 points for visits within a week and 10.7 points for visits 46–60 days out.
- **286 long-lead visits received no reminder at all** and missed 77.6% of the time, versus 69.2% for similar visits that were reminded — about **24 recoverable visits** in this dataset.

**Recommendations.**
1. Flag every booking made more than 45 days ahead and re-confirm it about a week before the visit.
2. Run a controlled SMS reminder pilot on the long-lead, unreminded group to prove the effect before making a clinic-wide rule.
3. Give patients with repeated missed visits a personal follow-up and easy rebooking.
4. Use SMS as the default channel, keeping Email available.
5. Start recording when cancellations happen, so freed slots can be measured and reused.

**How confident we are.** The lead-time, patient-history, SMS and pilot-segment findings are robust. The broad claim that "any reminder beats none" is provisional, which is why recommendation 2 is a pilot rather than a policy. All findings are associations, not proven causes.

**Scope note.** This component was completed individually; no HC-POD teammates were available, so the predictive model, ML pipeline and AI assistant stages were not built. The analytics findings are usable on their own as a rule-based targeting approach, and handoffs for each missing track are ready.
