# Sino-Nigeria Cross-Border E-Commerce Supply Chain Analytics

An SQL and Power BI analysis of revenue, net profit, freight cost and shipping method for goods imported from China (1688) into Nigeria.

> **Data note:** This project uses a **simulated dataset** that I designed to model a China-to-Nigeria import business, based on my experience importing directly from 1688. It does not contain real customer, supplier or financial records. The values are modelled at a larger scale than my own business and are meant to demonstrate analytical method and dashboard design, so they should not be read as real market or business figures.

---

## Business Problem

Small importers who buy from Chinese platforms such as 1688 make constant decisions about **what to restock, how to ship and how to price**. Margins can be cut sharply by freight cost and shipping method, yet many small traders track these in separate notes.

This project brings the data into one view to answer:

1. Which product categories generate the most net profit?
2. How much does transportation cost eat into each category?
3. How are orders split between sea and air freight, and how heavy is each one's freight cost burden?
4. How does revenue move across the year?
5. Which categories and suppliers should be prioritised?

## Dataset

| Item | Detail |
|---|---|
| Type | Simulated transactional data |
| Size | 500 orders |
| Period | 12 months (January to December) |
| Categories | Home & Kitchen, Phone Accessories, Beauty Tools, Electronics, Fashion & Apparel |
| Key fields | order ID, date, product, category, supplier, units, weight per unit, shipping method, freight cost, revenue, net profit] |
| Currency | Nigerian Naira (₦) |

## Tools Used

- **Python 
- **SQL ([MSSQL):
- **Power BI Desktop

## SQL Analysis

All queries are in the `sql/` folder.

| Business question | SQL concepts used |
|---|---|
| What is the net profit by product category? | Aggregation, GROUP BY |
| How are orders split between sea and air freight? | COUNT, GROUP BY |
| How much transportation cost does each category carry? | SUM, GROUP BY, ORDER BY |
| How many units were sold per category? | Aggregation |
| How does revenue change by month? | Date functions, GROUP BY |
| Which suppliers account for the most orders and cost? | JOIN, COUNT, HAVING |

## Power BI Dashboard

**KPI cards:** Total Revenue, Total Net Profit, Profit Margin %, Total Orders

**Visuals**

| Visual | Purpose |
|---|---|
| Total Net Profit by Category (waterfall) | Shows each category's contribution to total net profit |
| Total Orders by Shipping Method (donut) | Compares sea freight and air freight order share |
| Revenue Trend (column chart) | Shows monthly revenue across the year |
| Transportation Cost by Category (donut) | Shows how transport spend is distributed |
| Total Units Sold by Category (bar) | Shows sales volume by category |
| Freight Cost Burden (scatter) | Compares the freight burden of air and sea shipments |

**Slicers:** Top 8 Products, Supplier Name, Weight per Unit

## Key Metrics (Simulated Data)

| Metric | Value |
|---|---|
| Total Revenue | ₦5.52bn |
| Total Net Profit | ₦1.94bn |
| Profit Margin | 35.15% |
| Total Orders | 500 |
| Sea freight orders | 254 (50.8%) |
| Air freight orders | 246 (49.2%) |

## Key Findings

1. **Profitability:** the simulated business earns a **35.15% profit margin** on ₦5.52bn revenue, giving ₦1.94bn net profit.
2. **Shipping mix is almost even:** sea freight carries 50.8% of orders and air freight 49.2%, so the business depends heavily on both channels.
3. **Transport cost is concentrated:** Phone Accessories (about ₦275M) and Home & Kitchen (about ₦272M) together account for roughly half of all transportation cost.
4. **Volume leaders:** Home & Kitchen and Phone Accessories sell the most units, at roughly 20,000 and 19,000, well ahead of Beauty Tools, Electronics and Fashion & Apparel.
5. **Freight cost burden differs by shipping method:** air and sea shipments form two clearly separate clusters. [Add your reading in one sentence, for example what the two axes show and which method carries the heavier burden.]
6. **Revenue is fairly steady:** monthly revenue moves between roughly ₦0.38bn and ₦0.52bn, with no single dominant peak.

## Insights and Recommendations

- Consider moving heavier, less urgent items to sea freight to protect margins.
- Review pricing on categories where transportation cost takes a large share of revenue.
- Plan restocking around the lower revenue months so cash is not tied up in unsold stock.

```

## Limitations

- The data is simulated, so patterns reflect my assumptions and not real market behaviour.
- The model does not include customs delays, exchange-rate movements or supplier quality problems, which affect real importers.

## Future Improvements

- Add CNY to NGN exchange-rate tracking and its effect on landed cost.
- Add supplier scoring (lead time, defect rate).
- Add a demand forecasting view for restocking.
- Replace the simulated data with anonymised real order data from my own import business.

## Connection to My Research Interests

This project reflects my interest in **data-driven decision-making in small and medium-sized enterprises (SMEs)**, particularly in cross-border trade between China and Africa, and in how digital sourcing platforms and analytics can improve SME performance.

## Author

**Salome Lamosi Bello**
Operations professional | Business and data analytics
GitHub: [github.com/Salome-Bello](https://github.com/Salome-Bello)
Email: bellosalome108@gmail.com
