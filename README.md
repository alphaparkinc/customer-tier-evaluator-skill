# customer-tier-evaluator-skill

> **GenPark AI Agent Skill** -- RFM customer database segmentation analyzer.

## Quick Start

```python
from client import CustomerTierEvaluatorClient
client = CustomerTierEvaluatorClient()
res = client.evaluate_rfm(10, 5, 250)
print(res["segment_name"])
```
