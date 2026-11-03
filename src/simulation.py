import io
import base64
import random
import matplotlib.pyplot as plt
from js import document

# 1. הגדרת נתוני הניסוי - 1,000 לקוחות
customers = 1000

# 2. סיכוי הרכישה (הנחת העבודה של שיווק חושי)
prob_shelf_a = 0.15  # מדף א': שמות גוונים מספריים (Shade #01)
prob_shelf_b = 0.45  # מדף ב': מותג AURA עם שמות מאכלים (Golden Honey Glaze)

# ביצוע הסימולציה
sales_a = sum([1 for _ in range(customers) if random.random() < prob_shelf_a])
sales_b = sum([1 for _ in range(customers) if random.random() < prob_shelf_b])

# 3. יצירת הגרף עם צבעי המותג של AURA
labels = ['מדף א\n(שמות רגילים)', 'מדף ב - AURA\n(שמות מאכלים)']
sales = [sales_a, sales_b]
colors = ['#FFF6EC', '#D9A441'] # קרם וזהב-דבש
edge_color = '#4A1E3A' # שזיף עמוק

plt.figure(figsize=(7, 5), facecolor='none')
plt.bar(labels, sales, color=colors, edgecolor=edge_color, linewidth=2)
plt.title('השפעת שם המאכל על רכישת ליפ-טינט (1,000 לקוחות)', fontsize=14, color=edge_color)
plt.ylabel('מספר רכישות', fontsize=12, color=edge_color)

# 4. המרת הגרף לתמונה בזיכרון (Base64) עבור הדפדפן
buf = io.BytesIO()
plt.savefig(buf, format='png', transparent=True)
buf.seek(0)
encoded_string = base64.b64encode(buf.read()).decode('utf-8')

# 5. הזרקת התמונה לתוך המצגת (שקף 11)
try:
    img_element = document.getElementById('simulation-chart')
    if img_element:
        img_element.src = f"data:image/png;base64,{encoded_string}"
except Exception as e:
    print("Error updating DOM:", e)
