import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set seed for reproducible data
np.random.seed(42)
num_orders = 500

# 1. GENERATE PRODUCTS TABLE (1688 Sourcing Data)
categories = ['Electronics', 'Fashion & Apparel', 'Home & Kitchen', 'Beauty Tools', 'Phone Accessories']
suppliers = [
    'Yiwu Small Commodities Trading Co.',
    'Guangzhou Fashion Hub Ltd.',
    'Shenzhen Tech Export Co.',
    'Ningbo Household Goods Ltd.',
    'Foshan Hardware & Beauty Co.'
]

products_data = []
for i in range(1, 51):
    cat = random.choice(categories)
    supp = random.choice(suppliers)
    unit_cost_rmb = round(random.uniform(12.0, 280.0), 2)
    weight_kg = round(random.uniform(0.15, 3.5), 2)
    
    products_data.append({
        'product_id': f"PROD-{1000 + i}",
        'product_name': f"{cat} Item {i}",
        'category': cat,
        'supplier_name': supp,
        'unit_cost_rmb': unit_cost_rmb,
        'weight_kg': weight_kg
    })

df_products = pd.DataFrame(products_data)

# 2. GENERATE ORDERS & LOGISTICS TABLE (China -> Nigeria Pipeline)
orders_data = []
start_date = datetime(2025, 1, 1)

for i in range(1, num_orders + 1):
    prod = df_products.sample(1).iloc[0]
    quantity = random.randint(20, 250)
    order_date = start_date + timedelta(days=random.randint(0, 360))
    
    # Logistics specs
    shipping_method = random.choice(['Air Freight', 'Sea Freight'])
    rmb_to_ngn_rate = round(random.uniform(215.0, 240.0), 2) # RMB/NGN exchange rate
    
    # Freight cost per KG in NGN (Air is significantly more expensive than Sea)
    freight_rate_per_kg_ngn = 12500.0 if shipping_method == 'Air Freight' else 3800.0
    total_weight = round(prod['weight_kg'] * quantity, 2)
    shipping_cost_ngn = round(total_weight * freight_rate_per_kg_ngn, 2)
    
    # Financials
    total_cost_rmb = round(prod['unit_cost_rmb'] * quantity, 2)
    product_cost_ngn = round(total_cost_rmb * rmb_to_ngn_rate, 2)
    customs_clearing_ngn = round(product_cost_ngn * 0.05, 2) # Estimated 5% clearing fee
    
    total_landing_cost_ngn = round(product_cost_ngn + shipping_cost_ngn + customs_clearing_ngn, 2)
    unit_landing_cost_ngn = round(total_landing_cost_ngn / quantity, 2)
    
    # Pricing strategy & Sales in Nigeria
    markup = random.uniform(1.35, 1.75) # 35% to 75% profit margin
    unit_selling_price_ngn = round(unit_landing_cost_ngn * markup, 2)
    total_revenue_ngn = round(unit_selling_price_ngn * quantity, 2)
    net_profit_ngn = round(total_revenue_ngn - total_landing_cost_ngn, 2)
    
    # Shipping Lead Time (Days from China supplier to Lagos warehouse)
    lead_time_days = random.randint(7, 14) if shipping_method == 'Air Freight' else random.randint(35, 55)

    orders_data.append({
        'order_id': f"ORD-{10000 + i}",
        'order_date': order_date.strftime('%Y-%m-%d'),
        'product_id': prod['product_id'],
        'quantity': quantity,
        'shipping_method': shipping_method,
        'exchange_rate_rmb_ngn': rmb_to_ngn_rate,
        'total_cost_rmb': total_cost_rmb,
        'product_cost_ngn': product_cost_ngn,
        'shipping_cost_ngn': shipping_cost_ngn,
        'customs_clearing_ngn': customs_clearing_ngn,
        'total_landing_cost_ngn': total_landing_cost_ngn,
        'unit_landing_cost_ngn': unit_landing_cost_ngn,
        'unit_selling_price_ngn': unit_selling_price_ngn,
        'total_revenue_ngn': total_revenue_ngn,
        'net_profit_ngn': net_profit_ngn,
        'lead_time_days': lead_time_days
    })

df_orders = pd.DataFrame(orders_data)

# Save to CSV files
df_products.to_csv('products_1688.csv', index=False)
df_orders.to_csv('import_orders_nigeria.csv', index=False)

print("CSVs generated successfully:")
print("1. products_1688.csv (50 products)")
print("2. import_orders_nigeria.csv (500 order transactions)")