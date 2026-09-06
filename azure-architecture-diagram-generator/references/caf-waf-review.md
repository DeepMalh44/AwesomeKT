# CAF and WAF Architecture Review

Use this checklist to review design intent. It does not certify compliance, operational readiness, or implementation correctness. Apply only relevant checks, state missing evidence, and identify tradeoffs.

## Cloud Adoption Framework

- Tenant and billing: tenant ownership, billing scope, and environment separation are understood.
- Identity and access: human and workload identities, privileged access, RBAC scope, and trust boundaries are visible or documented.
- Resource organization: management groups, subscriptions, resource groups, naming, tagging, and policy scope are appropriate to the diagram's level.
- Network topology and connectivity: ingress, egress, DNS, segmentation, hybrid connectivity, routing, and private access are explicit.
- Security: protection controls, secrets, encryption boundaries, threat detection, and security operations integrations are represented where material.
- Management: logs, metrics, traces, alerting, backup, recovery, inventory, and operational ownership are accounted for.
- Governance: policy guardrails, compliance boundaries, data residency, and exceptions are identified when applicable.
- Platform automation and DevOps: IaC, deployment path, environments, approvals, rollback, and configuration ownership are considered.

## Well-Architected Framework

### Reliability

- Show regions/zones, redundancy, health probes, scaling, queues, retry boundaries, backups, failover, and recovery paths when relevant.
- Identify single points of failure and unproven RTO/RPO assumptions.

### Security

- Show identity flows, trust boundaries, public/private exposure, filtering, secrets, encryption, and least-privilege boundaries.
- Identify missing threat controls or ambiguous data classification.

### Cost Optimization

- Identify major cost drivers, duplicated capacity, data transfer paths, environment isolation, scaling model, and retention choices.
- Record unresolved SKU, commitment, or utilization assumptions without inventing costs.

### Operational Excellence

- Show telemetry, alerting, deployment automation, configuration/secret management, health signals, incident dependencies, and ownership.
- Identify manual operations and missing rollback or runbook paths.

### Performance Efficiency

- Show scale units, caches, asynchronous boundaries, latency-sensitive paths, throughput bottlenecks, partitioning, and load distribution.
- Record unvalidated capacity, latency, or load assumptions.

## Review Output

Report findings as:

- `Observed`: supported by source material.
- `Assumption`: used to complete the diagram but not verified.
- `Risk`: likely material impact if unresolved.
- `Decision needed`: owner or requirement is missing.
- `Tradeoff`: improvement in one pillar affects another.
