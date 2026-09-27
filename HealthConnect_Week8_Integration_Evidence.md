# HealthConnect Clinic — Week 8 Final Integration Evidence
### AnalystLab Africa Experience Lab · Data Analytics Track

## Statement on HC-POD collaboration

I could not find fellow interns from the other tracks to form an HC-POD, so I completed the Week 8 assignment on my own, using only the approved HealthConnect resources and my own Week 5–7 work.

This means no real exchange of outputs between tracks took place. The brief (§9) is clear that collaboration means an actual exchange and use of outputs, not communication alone, so I have **not** described any exchange as having happened and I have **not** created stand-in outputs for other tracks. What I did instead:

1. Prepared a complete, ready-to-use handoff for each track (Sections A–D below), so my component can be integrated the moment a teammate or reviewer picks it up.
2. Recorded, for each dependency, exactly what I needed, what I did without it, and how its absence limits the final solution.
3. Covered the Project Management needs of my own workstream (issue log, risks, timeline) myself.

I would welcome being placed in an HC-POD if one is available, and my handoffs are written so a teammate could use them without needing me to explain them.

---

## Mandatory integration record (brief §9, nine points)

| # | Required item | Data Analytics → Data Science | Data Analytics → Project Management |
|---|---|---|---|
| 1 | Track collaborated with | Data Science (intended) — **no intern available** | Project Management (intended) — **no intern available** |
| 2 | Dependency | DS needs a validated driver ranking and feature cautions; I need DS feature importances to cross-check my ranking | PM needs insights, risks and a presentation section; I need PM to track the cancellation-timestamp request |
| 3 | Output received | **None** | **None** |
| 4 | Output provided | Handoff A (below) | Handoff B (below) |
| 5 | Final integration activity | Wrote the handoff in model-ready form (feature list, thresholds, cautions) | Wrote risk, issue and decision entries in a register format PM can paste in directly |
| 6 | What changed | The Week 6–7 "pending DS exchange" is closed as **not possible** rather than carried forward a third week | My component now includes its own status, risks and decisions instead of relying on a PM track |
| 7 | How the change improved the solution | Removes an open-ended dependency; makes clear the model stage is not built rather than implying it is in progress | The package is self-contained and can be assessed without the missing tracks |
| 8 | Evidence | Section A; `HealthConnect_Week8_Validated_Findings_Register.csv` | Section B; `data/week8_dashboard_figure_validation.csv` |
| 9 | Contribution to final presentation | Slide on "what a model should use" | Slides on status, limitations and recommendations |

---

## A. Handoff to Data Science (ready, not exchanged)

**Features supported by validated evidence, in order of strength:**
1. `booking_lead_days` — strongest driver; useful thresholds at 20, 30 and 45 days (+8.5, +12.8, +20.2 pp).
2. `previous_no_shows` — clear dose-response (46.3% → 69.7% for 0–3). **Caution:** only 13.8% of multi-visit patients' values match their history at each visit, so the field may contain information not known at booking time. Test for leakage before using it as a live input.
3. Reminder channel (SMS / WhatsApp / Email / none) and an interaction term with lead time (reminder gap 1.7 pp at 0–7 days vs 10.7 pp at 46–60 days).

**Things a model should not be credited with:** the absolute ~51% rate (synthetic); the overall "any reminder" effect as settled (provisional); an SMS vs Email difference (not proven).

**What I would have asked for back:** feature importances from a baseline model, so I could check whether the model ranks lead time > prior no-shows > reminder the same way my analysis does.

## B. Handoff to Project Management (ready, not exchanged)

**Status:** Data Analytics component complete and ready; figures validated 27/27.

| Register | Entry |
|---|---|
| Issue | Cancellation timestamp missing; KPI 2 remains an upper-bound proxy (open 4 weeks) |
| Issue | Processed Week 5/6 data file never recovered; `previous_*` sub-split gap of 26 patients unresolved |
| Risk | Stakeholders over-trust the overall reminder effect → mitigated by "provisional" label and pilot (R2) |
| Risk | Small segments shown as misleading rates → mitigated by live n < 30 rule in dashboard |
| Risk | No cross-track review of analytics outputs (no HC-POD) → mitigated by scripted validation |
| Decision | Downgrade overall reminder claim to provisional (Week 7), kept in Week 8 |
| Decision | Show every KPI with its denominator; suppress n < 30 (Week 7 spec, Week 8 build) |
| Decision | Close DS dependency as not possible rather than keep it pending (Week 8) |

**Presentation section supplied:** the analytics slides in `presentation/`.

## C. Handoff to ML Engineering (ready, not exchanged)

Inputs a risk-scoring pipeline would need, from the data dictionary fields used in my analysis: `booking_date`, `appointment_date` (to compute `booking_lead_days`, expected range 0–60), `previous_no_shows` (observed 0–5; see leakage caution), `reminder_sent` / `reminder_channel` (treat missing channel or `reminder_sent = No` as "No reminder", as in my cleaning rule). Only `Attended` and `No-Show` outcomes should be used as training labels; `Cancelled` is excluded. Any reporting output grouped by segment should apply the n < 30 suppression rule.

## D. Handoff to Generative AI (ready, not exchanged)

The assistant must stay within the approved Knowledge Base. From the analytics side, the only thing it needs is **when a patient should be offered extra help**, not statistics to quote to patients:
- A patient rebooking a visit more than 45 days away → offer a reminder and explain how to reschedule.
- A patient with repeated missed visits → offer easy rebooking and escalate to staff for a personal follow-up.
The assistant should not tell patients their "no-show risk" or quote clinic performance figures.
