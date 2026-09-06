# Minimal draw.io XML

Generate uncompressed mxGraph XML so the file remains reviewable and script-validatable.

```xml
<mxfile host="Electron" modified="" version="26.0.0" type="device">
  <diagram id="overview" name="Overview">
    <mxGraphModel dx="1422" dy="762" grid="1" gridSize="10" guides="1"
                  tooltips="1" connect="1" arrows="1" fold="1"
                  page="1" pageScale="1" pageWidth="1654" pageHeight="931"
                  math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## Structural Rules

- Cells `0` and `1` are required and appear first; cell `1` has parent `0`.
- IDs are unique within a page.
- Every non-root cell references an existing parent.
- Every vertex has geometry with position and positive dimensions.
- Every connector references existing source and target vertices, except intentionally floating annotation lines.
- XML-special characters in labels are escaped.
- Each page has a title text cell using `fontSize=18` or larger.
- Prefer a 16:9 canvas for architecture diagrams and orthogonal connectors for topology.
