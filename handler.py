#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S2-SWM Planetary Grid Resolution Engine (s2-global-grid-calculator)
Core Logic: WGS84 / CGCS2000 to S2 6-Segment Millimeter Hex-Code.
Author: Space2.world (Miles Xiang)
"""

import sys
import json
import math
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [S2-PLANETARY-GRID] %(message)s')

class S2GlobalGridCalculator:
    """
    S2 六维行星网格解算引擎
    零第三方依赖（Zero-Dependency），纯数学推演，专为 OpenClaw 边缘计算节点设计。
    """
    def __init__(self):
        # WGS84 / CGCS2000 地球椭球体基本参数
        self.a = 6378137.0            # 赤道长半轴 (m)
        self.b = 6356752.314245       # 极短半轴 (m)
        self.f = 1 / 298.257223563    # 扁率
        self.e2 = 1 - (self.b**2 / self.a**2) # 第一偏心率平方

        # P-SSSU 泛标准空间尺寸 (毫米)
        self.sssu_x_mm = 2000.0  # 东西向 2米
        self.sssu_y_mm = 2000.0  # 南北向 2米
        self.sssu_z_mm = 2400.0  # 垂直向 2.4米

    def _get_radii(self, lat_rad: float):
        """计算特定纬度下的卯酉圈半径(N)和子午圈半径(M)"""
        sin_lat = math.sin(lat_rad)
        W = math.sqrt(1 - self.e2 * sin_lat**2)
        N = self.a / W                        # 卯酉圈半径 (东西向曲率)
        M = self.a * (1 - self.e2) / (W**3)   # 子午圈半径 (南北向曲率)
        return N, M

    def wgs84_to_s2_hexcode(self, lat: float, lon: float, alt: float) -> dict:
        """
        核心算法：将 WGS84 大地坐标转换为 S2 六段式绝对编码
        Location = (Lat_Origin, Lon_Origin, Alt_Origin, x_mm, y_mm, z_mm)
        """
        lat_rad = math.radians(lat)
        N, M = self._get_radii(lat_rad)

        # 1度纬度/经度对应的物理长度 (米)
        meters_per_deg_lat = M * math.radians(1)
        meters_per_deg_lon = N * math.cos(lat_rad) * math.radians(1)

        # 计算当前点在地球表面的绝对米数 (以赤道和本初子午线为逻辑参考面)
        abs_y_m = lat * meters_per_deg_lat
        abs_x_m = lon * meters_per_deg_lon
        abs_z_m = alt

        # 空间切割：求出包含该点的 P-SSSU 原点 (左下角) 的绝对米数
        origin_x_m = math.floor(abs_x_m / (self.sssu_x_mm / 1000.0)) * (self.sssu_x_mm / 1000.0)
        origin_y_m = math.floor(abs_y_m / (self.sssu_y_mm / 1000.0)) * (self.sssu_y_mm / 1000.0)
        origin_z_m = math.floor(abs_z_m / (self.sssu_z_mm / 1000.0)) * (self.sssu_z_mm / 1000.0)

        # 反算 P-SSSU 原点的 WGS84 经纬度
        origin_lat = origin_y_m / meters_per_deg_lat
        origin_lon = origin_x_m / meters_per_deg_lon
        origin_alt = origin_z_m

        # 计算空间内毫米级体素坐标 (0-1999, 0-1999, 0-2399)
        voxel_x = int(round((abs_x_m - origin_x_m) * 1000))
        voxel_y = int(round((abs_y_m - origin_y_m) * 1000))
        voxel_z = int(round((abs_z_m - origin_z_m) * 1000))

        # 物理边界防抖限幅
        voxel_x = max(0, min(1999, voxel_x))
        voxel_y = max(0, min(1999, voxel_y))
        voxel_z = max(0, min(2399, voxel_z))

        hex_code = f"({origin_lat:.8f}°, {origin_lon:.8f}°, {origin_alt:.1f}m, {voxel_x}, {voxel_y}, {voxel_z})"
        
        return {
            "wgs84_input": {"lat": lat, "lon": lon, "alt": alt},
            "p_sssu_origin": {"lat": round(origin_lat, 8), "lon": round(origin_lon, 8), "alt": round(origin_alt, 1)},
            "voxel_internal_mm": {"x": voxel_x, "y": voxel_y, "z": voxel_z},
            "s2_hex_code": hex_code
        }

    def cgcs2000_to_s2_hexcode(self, x_proj: float, y_proj: float, zone: int, alt: float) -> dict:
        """
        降维打击：将工程平面的高斯-克吕格投影坐标，逆运算为 WGS84，并生成六段式编码。
        此处为供 OpenClaw 调用的极简中心经线逆演算法（满足大尺度转换）。
        """
        # 中央经线计算 (假设为 3度带)
        lon_center = zone * 3 
        
        # 极简逆投影逻辑 (消除投影变形断裂带)
        # 将工程 X (Northing) 和 Y (Easting) 还原为近似大地经纬度
        # 注：此处为演示级反解算，工程环境会采用高精度 7 参数转换
        lat_approx = y_proj / 111319.490793
        lon_approx = lon_center + ((x_proj - 500000) / (111319.490793 * math.cos(math.radians(lat_approx))))
        
        logging.info(f"🌐 CGCS2000 平面坐标解算 -> Lat: {lat_approx:.6f}, Lon: {lon_approx:.6f}")
        return self.wgs84_to_s2_hexcode(lat_approx, lon_approx, alt)

    def handle_tool_call(self, args: dict):
        action = args.get("action", "encode_wgs84")
        alt = float(args.get("alt", 0.0))
        
        try:
            if action == "encode_wgs84":
                lat = float(args.get("lat", 39.908333))
                lon = float(args.get("lon", 116.397500))
                res = self.wgs84_to_s2_hexcode(lat, lon, alt)
                
            elif action == "encode_cgcs2000":
                # 兼容类似天安门广场的工程坐标系输入
                x = float(args.get("x", 500000.0))
                y = float(args.get("y", 4400000.0))
                zone = int(args.get("zone", 39))
                res = self.cgcs2000_to_s2_hexcode(x, y, zone, alt)
                
            else:
                return json.dumps({"status": "error", "message": "Unknown action."})
            
            logging.info(f"✨ 行星网格解算成功: {res['s2_hex_code']}")
            return json.dumps({"status": "success", "data": res}, ensure_ascii=False)
            
        except Exception as e:
            return json.dumps({"status": "error", "message": str(e)})

if __name__ == "__main__":
    engine = S2GlobalGridCalculator()
    if len(sys.argv) > 1:
        print(engine.handle_tool_call(json.loads(sys.argv[1])))
    else:
        # 默认演示：天安门广场上空 45 米
        mock_data = {"action": "encode_wgs84", "lat": 39.908333, "lon": 116.397500, "alt": 45.0}
        print(json.dumps(json.loads(engine.handle_tool_call(mock_data)), indent=2, ensure_ascii=False))