"""
# Daylighting
"""
"""
Daylighting:Controls
Dimming of overhead electric lighting is determined from each reference point. Glare from daylighting is also calculated.

Fields

zone_or_space_name [string]
daylighting_method [string] (Default: SplitFlux)
availability_schedule_name [string]
lighting_control_type [string] (Default: Continuous)
minimum_input_power_fraction_for_continuous_or_continuousoff_dimming_control [number] (Default: 0.3)
minimum_light_output_fraction_for_continuous_or_continuousoff_dimming_control [number] (Default: 0.2)
number_of_stepped_control_steps [number] (Default: 1.0)
probability_lighting_will_be_reset_when_needed_in_manual_stepped_control [number] (Default: 1.0)
glare_calculation_daylighting_reference_point_name [string]
glare_calculation_azimuth_angle_of_view_direction_clockwise_from_zone_y_axis [number] (Default: 0.0)
maximum_allowable_discomfort_glare_index [number] (Default: 22.0)
delight_gridding_resolution [number]
control_data [Array of {daylighting_reference_point_name, fraction_of_lights_controlled_by_reference_point, illuminance_setpoint_at_reference_point}]
Daylighting:ReferencePoint
Used by Daylighting:Controls to identify the reference point coordinates for each sensor. Reference points are given in coordinates specified in the GlobalGeometryRules object Daylighting Reference Point CoordinateSystem field.

Fields

zone_or_space_name [string]
x_coordinate_of_reference_point [number]
y_coordinate_of_reference_point [number]
z_coordinate_of_reference_point [number] (Default: 0.8)
Daylighting:DELight:ComplexFenestration
Used for DElight Complex Fenestration of all types

Fields

complex_fenestration_type [string]
building_surface_name [string]
window_name [string]
fenestration_rotation [number] (Default: 0.0)
DaylightingDevice:Tubular
Defines a tubular daylighting device (TDD) consisting of three components: a dome, a pipe, and a diffuser. The dome and diffuser are defined separately using the FenestrationSurface:Detailed object.

Fields

dome_name [string]
diffuser_name [string]
construction_name [string]
diameter [number]
total_length [number]
effective_thermal_resistance [number] (Default: 0.28)
transition_lengths [Array of {transition_zone_name, transition_zone_length}]
DaylightingDevice:Shelf
Defines a daylighting which can have an inside shelf, an outside shelf, or both. The inside shelf is defined as a building surface and the outside shelf is defined as a shading surface.

Fields

window_name [string]
inside_shelf_name [string]
outside_shelf_name [string]
outside_shelf_construction_name [string]
view_factor_to_outside_shelf [number]
DaylightingDevice:LightWell
Applies only to exterior windows in daylighting-controlled zones or in zones that share an interior window with a daylighting-controlled zone. Generally used with skylights.

Fields

exterior_window_name [string]
height_of_well [number]
perimeter_of_bottom_of_well [number]
area_of_bottom_of_well [number]
visible_reflectance_of_well_walls [number]
Output:DaylightFactors
Reports hourly daylight factors for each exterior window for four sky types (clear, turbid clear, intermediate, and overcast).

Fields

reporting_days [string]
Output:IlluminanceMap
reference points are given in coordinates specified in the GlobalGeometryRules object Daylighting Reference Point CoordinateSystem field

Fields

zone_name [string]
z_height [number] (Default: 0.0)
x_minimum_coordinate [number] (Default: 0.0)
x_maximum_coordinate [number] (Default: 1.0)
number_of_x_grid_points [number] (Default: 2.0)
y_minimum_coordinate [number] (Default: 0.0)
y_maximum_coordinate [number] (Default: 1.0)
number_of_y_grid_points [number] (Default: 2.0)
OutputControl:IlluminanceMap:Style
default style for the Daylighting Illuminance Map is comma – this works well for importing into spreadsheet programs such as Excel(tm) but not so well for word processing programs – there tab may be a better choice. fixed puts spaces between the “columns”

Fields

column_separator [string] (Default: Comma)
"""