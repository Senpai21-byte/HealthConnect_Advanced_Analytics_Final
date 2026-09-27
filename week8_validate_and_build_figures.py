"""
HealthConnect Clinic - Week 8 Final Analytics
Validates every dashboard / presentation figure for internal consistency and
rebuilds the final figures from the validated aggregate tables.

Inputs : data/validated_aggregates/*.csv  (figures carried forward from the
         Week 7 validated notebook outputs - no new raw-data calculations)
Outputs: figures/*.png and data/week8_dashboard_figure_validation.csv

Run from the repository root:  python scripts/week8_validate_and_build_figures.py
"""
from math import sqrt
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
AGG = ROOT / "data" / "validated_aggregates"
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)
MIN_N = 30  # Week 7 refinement: suppress any segment with n < 30

INK, TEAL, AMBER, RED, GREY = "#1D2B36", "#0F5257", "#D08C2E", "#A8323E", "#9AA5AD"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": GREY, "axes.labelcolor": INK, "xtick.color": INK,
                     "ytick.color": INK, "axes.titleweight": "bold", "axes.titlesize": 11})


def wilson(s, n, z=1.96):
    p = s / n
    d = 1 + z**2 / n
    c = (p + z**2 / (2 * n)) / d
    m = z * sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / d
    return round((c - m) * 100, 1), round((c + m) * 100, 1)


def ztest(s1, n1, s2, n2):
    pp = (s1 + s2) / (n1 + n2)
    return round((s1 / n1 - s2 / n2) / sqrt(pp * (1 - pp) * (1 / n1 + 1 / n2)), 2)


kpi = pd.read_csv(AGG / "kpi_final.csv")
lead = pd.read_csv(AGG / "lead_time_thresholds.csv")
dose = pd.read_csv(AGG / "prior_noshow_dose_response.csv")
ch = pd.read_csv(AGG / "reminder_channel.csv")
inter = pd.read_csv(AGG / "lead_x_reminder_interaction.csv")
impact = pd.read_csv(AGG / "impact_ranking.csv")
robust = pd.read_csv(AGG / "robustness_split_half.csv")

checks = []
def check(name, expected, actual, tol=0.05):
    ok = abs(float(expected) - float(actual)) <= tol
    checks.append({"check": name, "expected": expected, "recomputed": actual, "result": "PASS" if ok else "FAIL"})

# --- 1. Population / denominator consistency ---
channels = ch[ch.channel != "Any reminder (pooled)"]
check("Channel n sums to KPI1 analysis base (4,737)", 4737, channels.n.sum(), 0)
check("Channel no-shows sum to KPI1 numerator (2,423)", 2423, channels.noshows.sum(), 0)
check("Dose-response n sums to analysis base (4,737)", 4737, dose.n.sum(), 0)
check("Dose-response n for >=2 prior equals KPI4 denominator (510)", 510, dose[dose.previous_no_shows >= 2].n.sum(), 0)
check("Reminder coverage on analysis base (%)", 72.9, round((4737 - 1285) / 4737 * 100, 1))
check("Reminder coverage on all bookings (%) = KPI3", 72.7, round(3634 / 5000 * 100, 1))
check("Lost slot proxy (No-Show 2,423 + Cancelled 263) / 5,000 (%)", 53.7, round((2423 + 263) / 5000 * 100, 1))
check("High-risk share of bookings (%)", 23.4, round(1107 / 4737 * 100, 1))
check("Pilot segment + remainder = >45-day segment (n)", 1107, 286 + 821, 0)
check("46-60 day / no-reminder cell equals pilot-segment rate (%)", 77.6, inter.loc[4, "No reminder"])

# --- 2. KPI values and confidence intervals ---
for _, r in kpi.dropna(subset=["ci95_low"]).iterrows():
    check(f"{r.kpi_id} value (%)", r.value_pct, round(r.numerator / r.denominator * 100, 1))
    lo, hi = wilson(r.numerator, r.denominator)
    check(f"{r.kpi_id} Wilson CI lower", r.ci95_low, lo, 0.11)
    check(f"{r.kpi_id} Wilson CI upper", r.ci95_high, hi, 0.11)

# --- 3. Reminder z-tests reproduce from derived channel counts ---
g = channels.set_index("channel")
sms = (g.loc["SMS", "noshows"], g.loc["SMS", "n"])
for c, zrep in [("WhatsApp", -2.47), ("Email", -1.20), ("No reminder", -3.68)]:
    check(f"z SMS vs {c}", zrep, ztest(*sms, g.loc[c, "noshows"], g.loc[c, "n"]), 0.005)
any_s = channels[channels.channel != "No reminder"].noshows.sum()
check("z No reminder vs Any reminder", 2.92, ztest(702, 1285, any_s, 3452), 0.005)

# --- 4. Impact ranking arithmetic ---
for _, r in impact.iterrows():
    check(f"Expected excess no-shows: {r.segment}", r.expected_excess_noshows, round(r.lift_pp / 100 * r.n), 1)
check("Recoverable appointments in pilot segment", 24, round((0.776 - 0.692) * 286), 0)

val = pd.DataFrame(checks)
val.to_csv(ROOT / "data" / "week8_dashboard_figure_validation.csv", index=False)
print(val.to_string(index=False))
print(f"\n{(val.result == 'PASS').sum()}/{len(val)} checks passed")

# ------------------------------- FIGURES -------------------------------
# F1 lead-time thresholds
fig, ax = plt.subplots(figsize=(7, 3.8))
labels = ["All appointments"] + lead.threshold.tolist()
rates = [51.2] + lead.noshow_rate_pct.tolist()
cols = [GREY, AMBER, AMBER, RED]
bars = ax.bar(labels, rates, color=cols, width=0.6)
for b, r, n in zip(bars, rates, [4737] + lead.n.tolist()):
    ax.text(b.get_x() + b.get_width() / 2, r + 1.2, f"{r:.1f}%\nn={n:,}", ha="center", fontsize=9, color=INK)
ax.set_ylim(0, 85); ax.set_ylabel("No-show rate (%)")
ax.set_title("F1. The further ahead a visit is booked, the more likely it is missed")
plt.tight_layout(); plt.savefig(FIG / "F1_lead_time_noshow.png", dpi=150); plt.close()

# F2 dose-response with suppression
fig, ax = plt.subplots(figsize=(7, 3.8))
for _, r in dose.iterrows():
    shown = r.n >= MIN_N
    x = str(int(r.previous_no_shows))
    if shown:
        ax.bar(x, r.noshow_rate_pct, color=TEAL if r.previous_no_shows < 2 else RED, width=0.6)
        ax.errorbar(x, r.noshow_rate_pct, yerr=[[r.noshow_rate_pct - r.ci95_low], [r.ci95_high - r.noshow_rate_pct]],
                    color=INK, capsize=4, lw=1)
        ax.text(x, r.ci95_high + 1.5, f"{r.noshow_rate_pct:.1f}%", ha="center", fontsize=9)
    else:
        ax.bar(x, 20, color="none", edgecolor=GREY, hatch="//", width=0.6)
        ax.text(x, 23, f"n={int(r.n)}\nsuppressed", ha="center", fontsize=8, color=INK)
ax.set_xlabel("Previous no-shows recorded for the patient"); ax.set_ylabel("No-show rate (%)")
ax.set_ylim(0, 90)
ax.set_title("F2. Each previous no-show raises the risk of the next (n<30 suppressed)")
plt.tight_layout(); plt.savefig(FIG / "F2_prior_noshow_dose_response.png", dpi=150); plt.close()

# F3 channel
fig, ax = plt.subplots(figsize=(7, 3.8))
order = ["SMS", "Email", "WhatsApp", "No reminder"]
cc = [TEAL, GREY, AMBER, RED]
for c, col in zip(order, cc):
    r = g.loc[c]
    ax.barh(c, r.noshow_rate_pct, color=col, height=0.55)
    ax.text(r.noshow_rate_pct + 0.4, c, f"{r.noshow_rate_pct:.1f}%  (n={int(r.n):,})", va="center", fontsize=9)
ax.set_xlim(0, 68); ax.invert_yaxis(); ax.set_xlabel("No-show rate (%)")
ax.set_title("F3. SMS reminders have the lowest no-show rate")
plt.tight_layout(); plt.savefig(FIG / "F3_reminder_channel.png", dpi=150); plt.close()

# F4 interaction lines
fig, ax = plt.subplots(figsize=(7, 3.8))
ax.plot(inter.lead_band, inter["No reminder"], marker="o", color=RED, lw=2, label="No reminder")
ax.plot(inter.lead_band, inter["SMS"], marker="o", color=TEAL, lw=2, label="SMS reminder")
ax.fill_between(range(5), inter["SMS"], inter["No reminder"], color=RED, alpha=0.08)
ax.annotate("gap 10.7 pp", (4, 72.3), xytext=(2.9, 76), fontsize=9, color=RED,
            arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
ax.annotate("gap 1.7 pp", (0, 30.4), xytext=(0.2, 40), fontsize=9, color=INK,
            arrowprops=dict(arrowstyle="-", color=GREY, lw=0.8))
ax.set_ylabel("No-show rate (%)"); ax.set_xlabel("Booking lead time")
ax.legend(frameon=False); ax.set_ylim(20, 85)
ax.set_title("F4. Reminders matter most for bookings made far in advance")
plt.tight_layout(); plt.savefig(FIG / "F4_lead_time_x_reminder.png", dpi=150); plt.close()

# F5 impact ranking
fig, ax = plt.subplots(figsize=(8, 3.2))
ax.barh(impact.segment, impact.expected_excess_noshows, color=[RED, AMBER, GREY], height=0.55)
for i, r in impact.iterrows():
    ax.text(r.expected_excess_noshows + 3, i, f"{int(r.expected_excess_noshows)}  (n={r.n:,}, +{r.lift_pp}pp)",
            va="center", fontsize=9)
ax.invert_yaxis(); ax.set_xlim(0, 340); ax.set_xlabel("No-shows above the clinic baseline (reach x lift)")
ax.set_title("F5. Excess no-shows by segment: long lead times dominate")
plt.tight_layout(); plt.savefig(FIG / "F5_impact_ranking.png", dpi=150); plt.close()

# F6 robustness (small multiples - each finding on its own scale)
rb = robust.iloc[:3]
fig, axes = plt.subplots(1, 3, figsize=(8, 2.8))
for ax, (_, r) in zip(axes, rb.iterrows()):
    ax.bar(["Full", "Half A", "Half B"], [r.full_sample, r.half_a, r.half_b], color=[INK, TEAL, TEAL], width=0.6)
    for i, v in enumerate([r.full_sample, r.half_a, r.half_b]):
        ax.text(i, v * 1.02, f"{v}", ha="center", fontsize=9)
    ax.set_title(r.finding, fontsize=9.5); ax.set_ylim(0, max(r.half_a, r.half_b, r.full_sample) * 1.25)
    ax.set_yticks([])
fig.suptitle("F6. Headline findings hold when the data is split into random halves", fontweight="bold", fontsize=11)
plt.tight_layout(); plt.savefig(FIG / "F6_robustness_split_half.png", dpi=150); plt.close()
print("Figures written to", FIG)
