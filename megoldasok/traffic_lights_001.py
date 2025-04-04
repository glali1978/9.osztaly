from bisect import bisect_left, insort
from sortedcontainers import SortedList

def traffic_lights(x, positions):
    lights = SortedList([0, x])  # kezdő lámpák a két végponton
    segments = SortedList([x])   # egyetlen szakasz: a teljes hossz

    result = []

    for p in positions:
        idx = lights.bisect(p)
        left = lights[idx - 1]
        right = lights[idx]

        # Az eddigi szakasz hosszát kivesszük
        segments.remove(right - left)
        # Az új két szakaszt betesszük
        segments.add(p - left)
        segments.add(right - p)

        # A lámpát betesszük
        lights.add(p)

        # A leghosszabb szakasz hossza
        result.append(segments[-1])

    return result

# Példa futtatás:
x = 8
n = 3
positions = [3, 6, 2]
output = traffic_lights(x, positions)
print(*output)  # Output: 5 3 3
