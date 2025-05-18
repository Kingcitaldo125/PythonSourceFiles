import math

FLATTENING = 1/298.257223563
EQUATORIAL_RADIUS_M = 6378137
a_sq = EQUATORIAL_RADIUS_M*EQUATORIAL_RADIUS_M
b_sq = (EQUATORIAL_RADIUS_M * (1 - FLATTENING))**2
print(f"b_sq {b_sq}")
e = math.sqrt((a_sq - b_sq) / a_sq)

def lla_to_ecef(lat, lon, alt):
	lat = math.radians(lat)
	lon = math.radians(lon)

	N = EQUATORIAL_RADIUS_M / math.sqrt(1 - (e*e)*math.sin(lat)**2)
	ba_rat = (b_sq/a_sq)

	x = (N + alt) * math.cos(lat) * math.cos(lon)
	y = (N + alt) * math.cos(lat) * math.sin(lon)
	z = (ba_rat * N + alt) * math.sin(lat)

	return [x, y, z]

# 513275.66677608545, -4901334.804270264, 4036958.952150904
print(lla_to_ecef(39.5118978,-84.0216842, 1000.00))
