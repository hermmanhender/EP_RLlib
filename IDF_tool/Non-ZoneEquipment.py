"""
Non-Zone Equipment
"""
"""
LoadProfile:Plant
Used to simulate a scheduled plant loop demand profile. Load and flow rate are specified using schedules. Positive values are heating loads, and negative values are cooling loads. The actual load met is dependent on the performance of the supply loop components.

Fields

inlet_node_name [string]
outlet_node_name [string]
load_schedule_name [string]
peak_flow_rate [number]
flow_rate_fraction_schedule_name [string]
"""