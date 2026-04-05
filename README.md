# 🌍 S2-Global-Grid-Calculator (S2 行星网格解算引擎)
**【The Foundation of Spatial Sovereignty in Taohuayuan World Model】**

Welcome to the end of fragmented spatial mapping.

Traditional architects use flat 2D engineering coordinates (like CGCS2000 Gauss-Kruger X/Y), which break apart at projection zones. GPS relies on Lat/Lon, which provides no micro-spatial geometry for indoors. 

The **S2-Global-Grid-Calculator** unites the macro and the micro. It mathematically slices the Earth's atmosphere into infinite 2m × 2m × 2.4m Pseudo-Smart Space Standard Units (P-SSSU). 

## 🚀 The 6-Segment Hex-Code (六段式毫米级定位)
When your OpenClaw Agent encounters any physical coordinate on Earth, this engine dynamically resolves it into the S2 Absolute Hex-Code:
`Location = (Lat_Origin, Lon_Origin, Alt_Origin, x, y, z)`

* **The Macro Anchor (Lat, Lon, Alt):** Locks onto the bottom-left corner of the 2x2x2.4m P-SSSU container using WGS84 geodesy. No projection breaks. No dead zones.
* **The Micro Voxel (x, y, z):** Plunges into the container with an ultra-precise Cartesian grid from `0 to 1999` millimeters. 

## 🛠️ Usage for OpenClaw Agents
Invoke the tool `calculate_s2_planetary_hexcode` to map drones, digital avatars, or real-world IoT sensors to the S2 Spatial Grid.

**Action: `encode_wgs84`**
Input GPS data to retrieve the precise voxel coordinate inside the planetary grid.

**Action: `encode_cgcs2000`**
Input standard CAD engineering coordinates to seamlessly bridge legacy architectural maps into the Taohuayuan continuous planetary space.

> *"We didn't just map the world; we voxelized the causal fabric of reality."* — Miles Xiang