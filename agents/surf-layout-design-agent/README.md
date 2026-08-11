# SURF Layout Design Agent

Designs a screening subsea (SURF) field layout and places the host, from open map, bathymetry and licence-block data.

The agent turns a well count, a reservoir footprint, a water depth and a host concept into a placed and routed architecture: drill centres, wells and Xmas trees, templates and manifolds, PLEMs, riser bases, the host, and every production, injection, service and umbilical line together with the risers. Each line is sized against a velocity target and the API RP 14E erosional limit, and every item carries a latitude and longitude so the layout exports as GeoJSON and renders on a map.

It is the design counterpart to the `subsea-layout-screening-agent`: use this agent to create a layout, and that one to screen it.

## Skills

| Skill | Role |
| --- | --- |
| `neqsim-surf-field-layout-design` | places, routes and sizes the layout; plans the open-data requests |
| `neqsim-subsea-layout-geometry` | screens step-outs and tie-back distances afterwards |
| `neqsim-pipe-route-profile` | puts the routes on a real elevation profile |
| `neqsim-bathymetry-profile-screening` | processes the open bathymetry grid |
| `neqsim-line-velocity-check` | independent check of every selected line size |

## Scope

Concept screening and orientation only. No detailed routing, crossing design, on-bottom stability, free-span, expansion, buckling, installation, mooring or riser-response analysis, and no pressure-containment wall thickness. No proprietary or confidential data. A qualified subsea engineering review is always required.

## Companion Agents

`reservoir-simulator-agent` supplies the well count and rates, `pipe-route-screening-agent` the route profile and arrival pressure, `flow-assurance-engineer-agent` the hydrate, wax and cooldown side, and `asset-economics-agent` turns the quantity take-off into value.
