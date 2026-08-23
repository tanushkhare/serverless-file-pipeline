import uuid
import random
from backend.app.schemas.edge import EdgeInvocationRequest, EdgeInvocationResponse, RegionalEdgeMetric

class ServerlessEdgeEngine:
    @staticmethod
    def route_invocation(payload: EdgeInvocationRequest) -> EdgeInvocationResponse:
        regions = [
            RegionalEdgeMetric(region_code="us-east-1", edge_location="Ashburn (IAD)", latency_ms=8.2, cold_start=False, status="WARM"),
            RegionalEdgeMetric(region_code="eu-central-1", edge_location="Frankfurt (FRA)", latency_ms=14.1, cold_start=False, status="WARM"),
            RegionalEdgeMetric(region_code="ap-southeast-1", edge_location="Singapore (SIN)", latency_ms=22.4, cold_start=True, status="COLD_START"),
            RegionalEdgeMetric(region_code="us-west-2", edge_location="Oregon (PDX)", latency_ms=11.6, cold_start=False, status="WARM")
        ]

        selected = min(regions, key=lambda r: r.latency_ms)
        memory_mb = round(random.uniform(48.5, 92.4), 1)

        return EdgeInvocationResponse(
            invocation_id=f"EDGE-{uuid.uuid4().hex[:8].upper()}",
            routed_region=f"{selected.region_code} ({selected.edge_location})",
            execution_time_ms=selected.latency_ms,
            memory_used_mb=memory_mb,
            cold_start_detected=selected.cold_start,
            active_edge_nodes=regions
        )

edge_service = ServerlessEdgeEngine()
