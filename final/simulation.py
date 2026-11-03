import io
import base64
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# סימולציית A/B לשקף 11 – רצה בדפדפן בעזרת Pyodide.
# המצגת קובעת את NAME_EFFECT לפי המחוון לפני ההרצה.
# עותק זהה של הקובץ שמור בתוך final/deck.html (id="simulation-source"),
# כי כשפותחים את המצגת ישירות מהמחשב הדפדפן לא מאפשר לקרוא קבצים אחרים.

# 1. הגדרות הניסוי
CUSTOMERS = 1000            # לקוחות וירטואליים לכל מדף
BASE_RATE = 0.10            # הנחת עבודה: 10% קונים ממדף א' (שמות מספריים, Shade #01)
DEFAULT_NAME_EFFECT = 0.20  # הנחת עבודה: שם של מאכל מגדיל את הסיכוי לקנות ב-20% (יחסי)
SEED = 2026                 # זרע קבוע – אותה תוצאה בכל הרצה עם אותו אפקט

# 2. אפקט השם מהמחוון (אם לא הוגדר – ברירת המחדל)
try:
    name_effect = float(NAME_EFFECT)
except NameError:
    name_effect = DEFAULT_NAME_EFFECT

rate_a = BASE_RATE                      # מדף א': שמות מספריים
rate_b = BASE_RATE * (1 + name_effect)  # מדף ב': AURA עם שמות מאכלים (Golden Honey Glaze)

# 3. ביצוע הסימולציה: כל לקוח קונה או לא לפי הסיכוי של המדף
rng = random.Random(SEED)


def count_buyers(rate):
    return sum(1 for _ in range(CUSTOMERS) if rng.random() < rate)


sales_a = count_buyers(rate_a)
sales_b = count_buyers(rate_b)


# 4. עברית בגרף: Matplotlib כותב משמאל לימין, אז הופכים את סדר המילים
#    ואת האותיות בכל מילה עברית (מילים באנגלית ומספרים נשארים כמו שהם)
def rtl(text):
    lines = []
    for line in text.split('\n'):
        words = []
        for word in reversed(line.split(' ')):
            is_hebrew = any('֐' <= ch <= '׿' for ch in word)
            words.append(word[::-1] if is_hebrew else word)
        lines.append(' '.join(words))
    return '\n'.join(lines)


# 5. הגרף בצבעי המותג של AURA
edge_color = '#4A1E3A'  # שזיף עמוק
labels = [rtl("מדף א׳\nשמות מספריים"), rtl("מדף ב׳ – AURA\nשמות מאכלים")]
sales = [sales_a, sales_b]

fig, ax = plt.subplots(figsize=(7, 5), facecolor='none')
bars = ax.bar(labels, sales, color=['#FFF6EC', '#D9A441'], edgecolor=edge_color, linewidth=2, width=0.55)
for bar, value in zip(bars, sales):
    ax.text(bar.get_x() + bar.get_width() / 2, value + 2, rtl(f"{value} רוכשים"),
            ha='center', va='bottom', fontsize=12, fontweight='bold', color=edge_color)
ax.set_title(rtl(f"אפקט השם: {round(name_effect * 100)}% · {CUSTOMERS:,} לקוחות לכל מדף"),
             fontsize=14, color=edge_color)
ax.set_ylabel(rtl("מספר רוכשים"), fontsize=12, color=edge_color)
ax.set_ylim(0, max(sales) * 1.25 + 5)
ax.tick_params(colors=edge_color)
for side in ('top', 'right'):
    ax.spines[side].set_visible(False)
fig.text(0.5, 0.01, rtl("הנחת עבודה לצורך הדגמה – לא נתון שוק אמיתי"),
         ha='center', fontsize=9, color=edge_color, alpha=0.75)
fig.tight_layout(rect=(0, 0.04, 1, 1))

# 6. המרת הגרף לתמונה (Base64) והצגתה בשקף 11.
#    כשמריצים במחשב (python final/simulation.py) – שומרים את הגרף כקובץ PNG.
try:
    from js import document  # קיים רק בדפדפן (Pyodide)
except ImportError:
    document = None

if document is None:
    fig.savefig('simulation-chart.png', dpi=110)
    print(f"Shelf A: {sales_a} buyers, Shelf B: {sales_b} buyers (name effect {round(name_effect * 100)}%)")
    print("Chart saved: simulation-chart.png")
else:
    buf = io.BytesIO()
    fig.savefig(buf, format='png', transparent=True, dpi=110)
    buf.seek(0)
    encoded_string = base64.b64encode(buf.read()).decode('utf-8')
    img_element = document.getElementById('simulation-chart')
    if img_element:
        img_element.src = f"data:image/png;base64,{encoded_string}"
plt.close(fig)
