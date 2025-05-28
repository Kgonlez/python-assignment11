import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('../db/lesson.db')

query = """
SELECT last_name, SUM (price* quantity) AS revenue
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
JOIN line_items l on o.order_id = l.order_id
JOIN products p on l.product_id = p.product_id
GROUP BY e.employee_id
"""

employee_results = pd.read_sql_query(query,conn)
conn.close()

employee_results.plot(
    kind ='bar',
    x='last_name',
    y='revenue',
    color='skyblue',
    title='Revenue by Employee'
)

plt.xlabel('Employee Last Name')
plt.ylabel('Total Revenue')
plt.tight_layout()
plt.show()