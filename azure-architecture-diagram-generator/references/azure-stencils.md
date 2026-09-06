# Azure Stencils and Icon Rules

## Source Priority

1. Use draw.io's current Azure 2 library when its image path is verified in the editor or upstream `Sidebar-Azure2.js` catalog.
2. Use the official Microsoft Azure SVG icon package when the built-in library lacks a current service icon.
3. Use the legacy `mxgraph.azure.*` stencil library only when it accurately represents the current service.
4. Use a neutral, clearly labeled placeholder only when none of these sources can be verified. Add the missing icon to `Assumptions / Design gaps`.

Never guess an image path or shape key. Verify it in draw.io or the upstream catalog.

## Rules

- Put the official Azure product name beside each icon.
- Preserve the icon's aspect ratio and appearance. Do not crop, rotate, flip, recolor, or distort it.
- Use Azure icons only for the Azure services they represent.
- Use neutral shapes for users, devices, external systems, custom code, logical processing steps, notes, and boundaries.
- Use containers and labels for tenant, management group, subscription, resource group, region, availability zone, virtual network, subnet, and Kubernetes namespace scope. These are boundaries, not service icons.
- Do not mix AWS, GCP, or unrelated vendor stencils into an Azure-only solution unless the requested architecture genuinely integrates that external platform; label it as external.

## draw.io Usage

In the editor, choose **More Shapes > Networking > Azure**. Current Azure 2 cells use official SVG assets bundled with draw.io:

```xml
<mxCell id="service" value="Azure service name"
  style="image;aspect=fixed;html=1;points=[];align=center;verticalLabelPosition=bottom;verticalAlign=top;image=img/lib/azure2/app_services/App_Services.svg;"
        vertex="1" parent="1">
  <mxGeometry x="200" y="160" width="64" height="64" as="geometry" />
</mxCell>
```

Verified upstream examples include:

- `img/lib/azure2/app_services/API_Management_Services.svg`
- `img/lib/azure2/app_services/App_Services.svg`
- `img/lib/azure2/containers/Kubernetes_Services.svg`
- `img/lib/azure2/databases/Azure_Cosmos_DB.svg`
- `img/lib/azure2/general/Service_Bus.svg`
- `img/lib/azure2/networking/Load_Balancers.svg`

Paths are case-sensitive and must be copied from a rendered stencil or upstream source. The library changes over time, so verify less common services instead of extrapolating a filename. Keep the service name in the icon cell with the label positioned below, or use a separate nearby text cell.

## Visual Conventions

- Azure service icon: `48-72 px`, fixed aspect ratio, label below or beside it.
- Scope boundary: unfilled or lightly filled rectangle with a clear header.
- Trust boundary: dashed stroke and explicit label.
- Synchronous path: solid directional connector.
- Asynchronous event/message path: dashed directional connector.
- Failover or replication path: distinct dashed connector with a label.
- Risk or unknown: amber note; do not encode status using icon color changes.

Microsoft's [official icon terms and current downloads](https://learn.microsoft.com/azure/architecture/icons/) are maintained on Microsoft Learn.
