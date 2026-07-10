"""
example_usage.py -- Demonstrates CustomerTierEvaluatorClient
"""
from client import CustomerTierEvaluatorClient

def main():
    client = CustomerTierEvaluatorClient()
    result = client.evaluate_rfm(
        days_since_last_purchase=15,
        total_orders=12,
        total_spend_usd=600.00
    )
    print("[Customer Segmentation Result]")
    print(f"Score: {result['rfm_score']}")
    print(f"Segment: {result['segment_name']}")

if __name__ == "__main__":
    main()
