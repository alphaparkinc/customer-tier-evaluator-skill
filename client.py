"""
customer-tier-evaluator-skill: Client SDK
Evaluates RFM dimensions to compile profile classifications.
"""
from __future__ import annotations
from typing import Optional


class CustomerTierEvaluatorClient:
    """
    SDK for customer profiling metrics.
    """

    def evaluate_rfm(
        self,
        days_since_last_purchase: int,
        total_orders: int,
        total_spend_usd: float,
    ) -> dict:
        # Recency scoring (1 to 5, higher is closer)
        if days_since_last_purchase <= 30: r = 5
        elif days_since_last_purchase <= 90: r = 4
        elif days_since_last_purchase <= 180: r = 3
        elif days_since_last_purchase <= 365: r = 2
        else: r = 1

        # Frequency scoring (1 to 5)
        if total_orders >= 10: f = 5
        elif total_orders >= 5: f = 4
        elif total_orders >= 3: f = 3
        elif total_orders >= 2: f = 2
        else: f = 1

        # Monetary scoring (1 to 5)
        if total_spend_usd >= 500.0: m = 5
        elif total_spend_usd >= 200.0: m = 4
        elif total_spend_usd >= 100.0: m = 3
        elif total_spend_usd >= 50.0: m = 2
        else: m = 1

        rfm = f"{r}{f}{m}"
        
        # Segment map
        if rfm in ("555", "554", "455", "545"):
            segment = "Champion"
        elif r <= 2:
            segment = "At Churn Risk"
        elif f >= 4:
            segment = "Loyal Customer"
        else:
            segment = "General Customer"

        return {
            "rfm_score": rfm,
            "segment_name": segment
        }
