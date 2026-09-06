# Diagram Set Decision Guide

| User need | Primary page | Add pages when needed |
| --- | --- | --- |
| Executive or solution overview | Component/context diagram | Deployment or flow page for material detail |
| Connectivity, segmentation, or private access | Network topology | DNS, routing, or ingress/egress detail |
| Service responsibilities and dependencies | Component diagram | Data flow and deployment topology |
| Request, event, or order lifecycle | Flow or sequence diagram | Component overview for ownership context |
| Landing zone or enterprise platform | CAF-aligned scope/topology diagram | Identity, management, connectivity, and governance pages |
| Resilience or disaster recovery | Deployment/failover diagram | Normal and degraded request flows |

## Overview Page

Show actors, Azure scopes, major workload components, external dependencies, principal data paths, identity, observability, and regional placement. Avoid resource-instance detail that obscures the system story.

## Network Page

Show public entry points, DNS, edge protection, VNets, peering or Virtual WAN, subnets, NSGs, route tables, Azure Firewall/NVA, NAT/egress, private endpoints, private DNS, on-premises or partner links, and source/destination direction. Add CIDRs when known; use `CIDR TBD` rather than inventing values.

## Component Page

Show runtime boundaries, APIs, workers, messaging, state stores, managed identities, secrets, external dependencies, telemetry, and deployment ownership. Separate Azure services from custom application components.

## Flow Page

Number or clearly order interactions. Label protocol or message type. Distinguish synchronous calls, asynchronous messages, callbacks, retries, dead-letter paths, and state transitions. Mark trust-boundary crossings and authentication/authorization decisions.

## Multi-Page Rules

- Give each page one question to answer.
- Repeat only enough context to orient the reader.
- Keep names and connector semantics consistent across pages.
- Put assumptions and unresolved gaps on the page they affect.
