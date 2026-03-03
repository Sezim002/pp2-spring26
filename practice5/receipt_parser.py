import re
import json

# ---------- вспомогательные функции ----------

def to_float(text):
    text = text.replace(' ', '')
    text = text.replace(',', '.')
    return float(text)

# ---------- основной парсер ----------

def parse_receipt(text):
    lines = text.splitlines()

    items = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # 1. если строка — номер товара (например "1.")
        if line.endswith('.'):
            name = lines[i + 1].strip()

            qty_price_line = lines[i + 2].strip()
            total_line = lines[i + 3].strip()

            qty_price_match = re.search(r'([\d,]+)\s*x\s*([\d\s]+,\d{2})', qty_price_line)

            if qty_price_match:
                quantity = to_float(qty_price_match.group(1))
                unit_price = to_float(qty_price_match.group(2))
                total_price = to_float(total_line)

                items.append({
                    "name": name,
                    "quantity": quantity,
                    "unit_price": unit_price,
                    "total_price": total_price
                })

                i += 4
                continue

        i += 1

    # ---------- дата и время ----------

    date = None
    time = None
    date_match = re.search(r'(\d{2}\.\d{2}\.\d{4})\s+(\d{2}:\d{2}:\d{2})', text)
    if date_match:
        date = date_match.group(1)
        time = date_match.group(2)

    # ---------- итог ----------

    total = None
    total_match = re.search(r'ИТОГО:\s*([\d\s]+,\d{2})', text)
    if total_match:
        total = to_float(total_match.group(1))

    # ---------- способ оплаты ----------

    payment_method = None
    if 'Банковская карта' in text:
        payment_method = 'bank_card'

    return {
        "items": items,
        "items_count": len(items),
        "total": total,
        "payment_method": payment_method,
        "date_time": {
            "date": date,
            "time": time
        }
    }

# ---------- запуск ----------

if __name__ == "__main__":
    with open("raw.txt", encoding="utf-8") as f:
        text = f.read()

    result = parse_receipt(text)
    print(json.dumps(result, ensure_ascii=False, indent=2))