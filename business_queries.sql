-- Query 1: Profit Margin and Revenue by Product Category

SELECT 
    p.category,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_revenue_ngn) AS gross_revenue_ngn,
    SUM(o.net_profit_ngn) AS net_profit_ngn,
    ROUND((SUM(o.net_profit_ngn) / SUM(o.total_revenue_ngn)) * 100, 2) AS profit_margin_pct
FROM ImportOrders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY net_profit_ngn DESC;

-- Query 2: Air vs Sea Freight Efficiency and Cost Comparison

SELECT 
    shipping_method,
    COUNT(order_id) AS order_count,
    ROUND(AVG(lead_time_days), 1) AS avg_delivery_days,
    ROUND(AVG(shipping_cost_ngn / quantity), 2) AS avg_shipping_cost_per_unit
FROM ImportOrders
GROUP BY shipping_method;

-- Query 3: Top 5 Chinese Suppliers by Order Volume

SELECT 
    p.supplier_name,
    COUNT(o.order_id) AS total_orders_fulfilled,
    SUM(o.total_cost_rmb) AS total_spend_rmb,
    SUM(o.net_profit_ngn) AS net_profit_generated_ngn
FROM ImportOrders o
JOIN Products p ON o.product_id = p.product_id
GROUP BY p.supplier_name
ORDER BY total_orders_fulfilled DESC
LIMIT 5;