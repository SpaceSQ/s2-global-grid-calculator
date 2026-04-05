# Taohuayuan World Model Whitepaper V1.2: Planetary Pseudo-SSSU and 6-Segment Geographical Positioning

**Date**: April 5, 2026
**Author**: Miles Xiang
**Institution**: Taohuayuan World Model Research Base (Prep)
**Domains**: World Models, Spatial Computing, Embodied AI, Geolocation, Cyber-Physical Systems

## Abstract
The Taohuayuan World Model (TAOHUAYUAN WORLD) previously focused on indoor spaces bounded by architectural containers. However, the operational boundaries of carbon-based and silicon-based lifeforms extend far into the Earth's atmosphere. This whitepaper expands the model to outdoor environments, introducing the **Pseudo-Smart Space Standard Unit (P-SSSU)** as the fundamental discrete grid for planetary continuous physical fields. We define the non-uniformity of Earth's environmental element sources, establish "Nomadic Takeover" protocols for AI agents, and formulate cross-boundary gateway rules. Crucially, this paper introduces the **6-Segment Spatial Hex-Code**, fusing WGS84/CGCS2000 geodetic coordinates with millimeter-level Cartesian micro-coordinates, achieving a unified, cross-scale absolute addressing system for the spatial internet.

## 1. Introduction: Breaking the Architectural Container
In the Taohuayuan paradigm, the outdoor space (from the Earth's surface to the troposphere) is not an infinite void, but a **Macro-Container** bounded by the lithosphere and the atmosphere. This container is filled with 14-dimensional spatial tensors (light, air, acoustics, temperature, etc.) that must be computable for silicon-based agents to achieve "Deep-Time Guardianship" across all scenarios.

## 2. Element Dynamics: Earth's Regional Environmental Sources
Unlike indoor spaces governed by explicit building automation hardware (e.g., HVAC, lighting), outdoor elements are supplied by **Earth's Regional Environmental Sources**:
* **Exogenous Sources**: Solar radiation, lunar gravity (tidal fields).
* **Endogenous Sources**: Atmospheric circulation, ocean currents, surface albedo, geothermal radiation, and vegetation transpiration.
Because these sources are highly non-uniform, the elements within P-SSSUs are dynamically assigned via spatial interpolation of macro-climate fields and micro-topographic perturbations, bypassing the computational nightmare of global Navier-Stokes fluid simulations.

## 3. Spatial Deconstruction: The Pseudo-SSSU (P-SSSU)
* **Absolute Slicing**: The planetary surface is rigorously divided along latitude, longitude, and altitude into uniform grids of **2m (L) × 2m (W) × 2.4m (H)**, designated as **P-SSSUs**.
* **Residual Edges (R_out)**: When the grid intersects physical boundaries (e.g., cliffs, building facades), the remaining irregular fragments are designated as outdoor Residual Spaces (R_out). They lack independent supply sources and must "borrow" elements from adjacent P-SSSUs via diffusion or radiation.

## 4. Zero-Boundary Sovereignty: Nomadic Agent Protocols
* **The Habitable Slot**: Outdoor spaces default to having no permanent agent, yet every P-SSSU contains a standard "Habitable Slot".
* **Nomadic Takeover**: When a roaming agent (e.g., a drone or an embodied robot) enters a P-SSSU, it temporarily occupies the slot, assuming sensory and intervention rights.
* **Ripple Expansion & Negotiation**: Agents can automatically expand their jurisdiction into adjacent unoccupied P-SSSUs. When boundaries clash with another agent, decentralized negotiation protocols dictate the final topological borders based on task priority and timestamps.

## 5. Carbon-Based Topology & Gateway Transition
Humans navigating the outdoors are topologically restricted to P-SSSUs or R_out spaces. The capacity limits mirror indoor SSSUs: 1 person (full freedom), 2 persons (restricted freedom), or 4 persons (zero freedom, transient only).
**The Gateway Protocol:** Transitioning from an outdoor P-SSSU to an indoor SSSU via a door/window is a dimensional leap. It requires validation against the indoor space's Dual-Track Authorization system (checking the Owner_Token or BMS Dispatch_Token) to legally transfer the thermodynamic and spatial jurisdiction.

## 6. The Grand Unification: 6-Segment Planetary Hex-Code
To seamlessly unify macro-geography with micro-habitation, we introduce a unified addressing system bridging WGS84 and Cartesian coordinates.

### 6.1 The Macro Anchor (WGS84)
The origin of any P-SSSU is defined as its **bottom-left vertex** (facing north). Its absolute planetary position is recorded via geodetic coordinates: **(Latitude, Longitude, Altitude)**.

### 6.2 The Micro Cartesian Voxel
Within this 2m × 2m × 2.4m container, Earth's curvature is negligible. We establish a micro-Cartesian grid mapped in millimeters:
* X-axis (Easting): `0 to 1999` mm
* Y-axis (Northing): `0 to 1999` mm
* Z-axis (Elevation): `0 to 2399` mm

### 6.3 The 6-Segment Format & Epic Demonstration
Every 1-cubic-millimeter voxel on Earth now possesses a singular, calculable identity:
`Location = (Lat, Lon, Alt, x_mm, y_mm, z_mm)`

**Example (The Roman Forum, Italy):**
`Location = (41.892462, 12.485325, 45.0, 1000, 1000, 1200)`

**Interpretation:** This exact coordinate points to a location **45 meters above the ancient ruins of the Roman Forum in Rome, Italy**. The first three segments anchor the WGS84 origin of the P-SSSU floating in the air. The final three segments `(1000, 1000, 1200)` pinpoint the absolute geometric center of that invisible 2m×2m×2.4m cyber-physical container, down to the exact millimeter.

This 6-Segment Hex-Code decisively eliminates the geographical fault lines of traditional Gauss-Kruger planar projections while maintaining the micro-precision impossible with raw GPS. It is the ultimate coordinate ledger for the Spatial Internet.