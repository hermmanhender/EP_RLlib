"""
# Thermal Zones and Surfaces
"""
"""
class GlobalGeometryRules():
    '''
    Specifies the geometric rules used to describe the input of surface vertices and daylighting reference points.
    '''

starting_vertex_position [string]
vertex_entry_direction [string]
coordinate_system [string]
daylighting_reference_point_coordinate_system [string] (Default: Relative)
rectangular_surface_coordinate_system [string] (Default: Relative)

class GeometryTransform():
    '''
    Provides a simple method of altering the footprint geometry of a model. The intent is to provide a single parameter that can be used to reshape the building description contained in the rest of the input file.
    '''

plane_of_transform [string] (Default: XY)
current_aspect_ratio [number]
new_aspect_ratio [number]

class Space():
    '''
    Defines a space (room) in the building. All Spaces are part of a Zone. Every Zone contains one or more spaces. Space is an optional input. If a Zone has no Space(s) specified in input then a default Space named <Zone Name> will be created. If some surfaces in a Zone are assigned to a space and some are not, then a default Space named <Zone Name>-Remainder will be created. Input references to Space Names must have a matching Space object (default space names may not be referenced except in output variable keys).
    '''

zone_name [string]
floor_area [unknown field type] (Default: Autocalculate)
space_type [string] (Default: General)
tags [Array of {tag}]

class SpaceList():
    '''
    Defines a list of Spaces which can be referenced as a group. The SpaceList name may be used elsewhere in the input to apply a parameter to all Spaces in the list. SpaceLists can be used effectively with the following objects: InternalMass, People, Lights, ElectricEquipment, GasEquipment, HotWaterEquipment, and others.
    '''

spaces [Array of {space_name}]

class Zone():
    '''
    Defines a thermal zone of the building. Every zone contains one or more Spaces. Space is an optional input. If a Zone has no Space(s) specified in input then a default Space named <Zone Name> will be created. If some surfaces in a Zone are assigned to a space and some are not, then a default Space named <Zone Name>-Remainder will be created. Input references to Space Names must have a matching Space object (default space names may not be referenced except in output variable keys).
    '''

direction_of_relative_north [number] (Default: 0.0)
x_origin [number] (Default: 0.0)
y_origin [number] (Default: 0.0)
z_origin [number] (Default: 0.0)
type [number] (Default: 1.0)
multiplier [number] (Default: 1.0)
ceiling_height [unknown field type] (Default: Autocalculate)
volume [unknown field type] (Default: Autocalculate)
floor_area [unknown field type] (Default: Autocalculate)
zone_inside_convection_algorithm [string]
zone_outside_convection_algorithm [string]
part_of_total_floor_area [string] (Default: Yes)

class ZoneList():
    '''
    Defines a list of thermal zones which can be referenced as a group. The ZoneList name may be used elsewhere in the input to apply a parameter to all zones in the list. ZoneLists can be used effectively with the following objects: People, Lights, ElectricEquipment, GasEquipment, HotWaterEquipment, ZoneInfiltration:DesignFlowRate, ZoneVentilation:DesignFlowRate, Sizing:Zone, ZoneControl:Thermostat, and others.
    '''

zones [Array of {zone_name}]

class ZoneGroup():
    '''
    Adds a multiplier to a ZoneList. This can be used to reduce the amount of input necessary for simulating repetitive structures, such as the identical floors of a multi-story building.
    '''

zone_list_name [string]
zone_list_multiplier [number] (Default: 1.0)

class BuildingSurface:Detailed():
    '''
    Allows for detailed entry of building heat transfer surfaces. Does not include subsurfaces such as windows or doors.
    '''

surface_type [string]
construction_name [string]
zone_name [string]
space_name [string]
outside_boundary_condition [string]
outside_boundary_condition_object [string]
sun_exposure [string] (Default: SunExposed)
wind_exposure [string] (Default: WindExposed)
view_factor_to_ground [unknown field type] (Default: Autocalculate)
number_of_vertices [unknown field type] (Default: Autocalculate)
vertices [Array of {vertex_x_coordinate, vertex_y_coordinate, vertex_z_coordinate}]

class Wall:Detailed():
    '''
    Allows for detailed entry of wall heat transfer surfaces.
    '''

construction_name [string]
zone_name [string]
space_name [string]
outside_boundary_condition [string]
outside_boundary_condition_object [string]
sun_exposure [string] (Default: SunExposed)
wind_exposure [string] (Default: WindExposed)
view_factor_to_ground [unknown field type] (Default: Autocalculate)
number_of_vertices [unknown field type] (Default: Autocalculate)
vertices [Array of {vertex_x_coordinate, vertex_y_coordinate, vertex_z_coordinate}]

class RoofCeiling:Detailed():
    '''
    Allows for detailed entry of roof/ceiling heat transfer surfaces.
    '''

construction_name [string]
zone_name [string]
space_name [string]
outside_boundary_condition [string]
outside_boundary_condition_object [string]
sun_exposure [string] (Default: SunExposed)
wind_exposure [string] (Default: WindExposed)
view_factor_to_ground [unknown field type] (Default: Autocalculate)
number_of_vertices [unknown field type] (Default: Autocalculate)
vertices [Array of {vertex_x_coordinate, vertex_y_coordinate, vertex_z_coordinate}]

class Floor:Detailed():
    '''
    Allows for detailed entry of floor heat transfer surfaces.
    '''

construction_name [string]
zone_name [string]
space_name [string]
outside_boundary_condition [string]
outside_boundary_condition_object [string]
sun_exposure [string] (Default: SunExposed)
wind_exposure [string] (Default: WindExposed)
view_factor_to_ground [unknown field type] (Default: Autocalculate)
number_of_vertices [unknown field type] (Default: Autocalculate)
vertices [Array of {vertex_x_coordinate, vertex_y_coordinate, vertex_z_coordinate}]

class Wall:Exterior():
    '''
    Allows for simplified entry of exterior walls. View Factor to Ground is automatically calculated.
    '''

construction_name [string]
zone_name [string]
space_name [string]
azimuth_angle [number]
tilt_angle [number] (Default: 90.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class Wall:Adiabatic():
    '''
    Allows for simplified entry of interior walls.
    '''

construction_name [string]
zone_name [string]
space_name [string]
azimuth_angle [number]
tilt_angle [number] (Default: 90.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class Wall:Underground():
    '''
    Allows for simplified entry of underground walls.
    '''

construction_name [string]
zone_name [string]
space_name [string]
azimuth_angle [number]
tilt_angle [number] (Default: 90.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class Wall:Interzone():
    '''
    Allows for simplified entry of interzone walls (walls between zones).
    '''

construction_name [string]
zone_name [string]
space_name [string]
outside_boundary_condition_object [string]
azimuth_angle [number]
tilt_angle [number] (Default: 90.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class Roof():
    '''
    Allows for simplified entry of roofs (exterior). View Factor to Ground is automatically calculated.
    '''

construction_name [string]
zone_name [string]
space_name [string]
azimuth_angle [number]
tilt_angle [number] (Default: 0.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
width [number]

class Ceiling:Adiabatic():
    '''
    Allows for simplified entry of interior ceilings.
    '''

construction_name [string]
zone_name [string]
space_name [string]
azimuth_angle [number]
tilt_angle [number] (Default: 0.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
width [number]

class Ceiling:Interzone():
    '''
    Allows for simplified entry of ceilings using adjacent zone (interzone) heat transfer - adjacent surface should be a floor
    '''

construction_name [string]
zone_name [string]
space_name [string]
outside_boundary_condition_object [string]
azimuth_angle [number]
tilt_angle [number] (Default: 0.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
width [number]

class Floor:GroundContact():
    '''
    Allows for simplified entry of exterior floors with ground contact. View Factors to Ground is automatically calculated.
    '''

construction_name [string]
zone_name [string]
space_name [string]
azimuth_angle [number]
tilt_angle [number] (Default: 180.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
width [number]

class Floor:Adiabatic():
    '''
    Allows for simplified entry of exterior floors ignoring ground contact or interior floors. View Factor to Ground is automatically calculated.
    '''

construction_name [string]
zone_name [string]
space_name [string]
azimuth_angle [number]
tilt_angle [number] (Default: 180.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
width [number]

class Floor:Interzone():
    '''
    Allows for simplified entry of floors using adjacent zone (interzone) heat transfer - adjacent surface should be a ceiling.
    '''

construction_name [string]
zone_name [string]
space_name [string]
outside_boundary_condition_object [string]
azimuth_angle [number]
tilt_angle [number] (Default: 180.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
width [number]

class FenestrationSurface:Detailed():
    '''
    Allows for detailed entry of subsurfaces (windows, doors, glass doors, tubular daylighting devices).
    '''

surface_type [string]
construction_name [string]
building_surface_name [string]
outside_boundary_condition_object [string]
view_factor_to_ground [unknown field type] (Default: Autocalculate)
frame_and_divider_name [string]
multiplier [number] (Default: 1.0)
number_of_vertices [unknown field type] (Default: Autocalculate)
vertex_1_x_coordinate [number]
vertex_1_y_coordinate [number]
vertex_1_z_coordinate [number]
vertex_2_x_coordinate [number]
vertex_2_y_coordinate [number]
vertex_2_z_coordinate [number]
vertex_3_x_coordinate [number]
vertex_3_y_coordinate [number]
vertex_3_z_coordinate [number]
vertex_4_x_coordinate [number]
vertex_4_y_coordinate [number]
vertex_4_z_coordinate [number]

class Window():
    '''
    Allows for simplified entry of Windows.
    '''

construction_name [string]
building_surface_name [string]
frame_and_divider_name [string]
multiplier [number] (Default: 1.0)
starting_x_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class Door():
    '''
    Allows for simplified entry of opaque Doors.
    '''

construction_name [string]
building_surface_name [string]
multiplier [number] (Default: 1.0)
starting_x_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class GlazedDoor():
    '''
    Allows for simplified entry of glass Doors.
    '''

construction_name [string]
building_surface_name [string]
frame_and_divider_name [string]
multiplier [number] (Default: 1.0)
starting_x_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class Window:Interzone():
    '''
    Allows for simplified entry of interzone windows (adjacent to other zones).
    '''

construction_name [string]
building_surface_name [string]
outside_boundary_condition_object [string]
multiplier [number] (Default: 1.0)
starting_x_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class Door:Interzone():
    '''
    Allows for simplified entry of interzone (opaque interior) doors (adjacent to other zones).
    '''

construction_name [string]
building_surface_name [string]
outside_boundary_condition_object [string]
multiplier [number] (Default: 1.0)
starting_x_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class GlazedDoor:Interzone():
    '''
    Allows for simplified entry of interzone (glass interior) doors (adjacent to other zones).
    '''

construction_name [string]
building_surface_name [string]
outside_boundary_condition_object [string]
multiplier [number] (Default: 1.0)
starting_x_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class WindowShadingControl():
    '''
    Specifies the type, location, and controls for window shades, window blinds, and switchable glazing. Referencing the surface objects for exterior windows and glass doors (ref: FenestrationSurface:Detailed, Window, and GlazedDoor).
    '''

zone_name [string]
shading_control_sequence_number [number] (Default: 1.0)
shading_type [string]
construction_with_shading_name [string]
shading_control_type [string]
schedule_name [string]
setpoint [number]
shading_control_is_scheduled [string] (Default: No)
glare_control_is_active [string] (Default: No)
shading_device_material_name [string]
type_of_slat_angle_control_for_blinds [string] (Default: FixedSlatAngle)
slat_angle_schedule_name [string]
setpoint_2 [number]
daylighting_control_object_name [string]
multiple_surface_control_type [string] (Default: Sequential)
fenestration_surfaces [Array of {fenestration_surface_name}]

class WindowProperty:FrameAndDivider():
    '''
    Specifies the dimensions of a window frame, dividers, and inside reveal surfaces. Referenced by the surface objects for exterior windows and glass doors (ref: FenestrationSurface:Detailed, Window, and GlazedDoor).
    '''

frame_width [number] (Default: 0.0)
frame_outside_projection [number] (Default: 0.0)
frame_inside_projection [number] (Default: 0.0)
frame_conductance [number]
ratio_of_frame_edge_glass_conductance_to_center_of_glass_conductance [number] (Default: 1.0)
frame_solar_absorptance [number] (Default: 0.7)
frame_visible_absorptance [number] (Default: 0.7)
frame_thermal_hemispherical_emissivity [number] (Default: 0.9)
divider_type [string] (Default: DividedLite)
divider_width [number] (Default: 0.0)
number_of_horizontal_dividers [number] (Default: 0.0)
number_of_vertical_dividers [number] (Default: 0.0)
divider_outside_projection [number] (Default: 0.0)
divider_inside_projection [number] (Default: 0.0)
divider_conductance [number] (Default: 0.0)
ratio_of_divider_edge_glass_conductance_to_center_of_glass_conductance [number] (Default: 1.0)
divider_solar_absorptance [number] (Default: 0.0)
divider_visible_absorptance [number] (Default: 0.0)
divider_thermal_hemispherical_emissivity [number] (Default: 0.9)
outside_reveal_solar_absorptance [number] (Default: 0.0)
inside_sill_depth [number] (Default: 0.0)
inside_sill_solar_absorptance [number] (Default: 0.0)
inside_reveal_depth [number] (Default: 0.0)
inside_reveal_solar_absorptance [number] (Default: 0.0)

class WindowProperty:AirflowControl():
    '''
    Used to control forced airflow through a gap between glass layers
    '''

airflow_source [string] (Default: IndoorAir)
airflow_destination [string] (Default: OutdoorAir)
maximum_flow_rate [number] (Default: 0.0)
airflow_control_type [string] (Default: AlwaysOnAtMaximumFlow)
airflow_is_scheduled [string] (Default: No)
airflow_multiplier_schedule_name [string]
airflow_return_air_node_name [string]

class WindowProperty:StormWindow():
    '''
    This is a movable exterior glass layer that is usually applied in the winter and removed in the summer.
    '''

window_name [string]
storm_glass_layer_name [string]
distance_between_storm_glass_layer_and_adjacent_glass [number] (Default: 0.05)
month_that_storm_glass_layer_is_put_on [number]
day_of_month_that_storm_glass_layer_is_put_on [number]
month_that_storm_glass_layer_is_taken_off [number]
day_of_month_that_storm_glass_layer_is_taken_off [number]

class InternalMass():
    '''
    Used to describe internal zone surface area that does not need to be part of geometric representation. This should be the total surface area exposed to the zone air. If you use a ZoneList in the Zone or ZoneList name field then this definition applies to all the zones in the ZoneList. Likewise for SpaceList.
    '''

construction_name [string]
zone_or_zonelist_name [string]
space_or_spacelist_name [string]
surface_area [number]

class Shading:Site():
    '''
    used for shading elements such as trees these items are fixed in space and would not move with relative geometry
    '''

azimuth_angle [number]
tilt_angle [number] (Default: 90.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class Shading:Building():
    '''
    used for shading elements such as trees, other buildings, parts of this building not being modeled these items are relative to the current building and would move with relative geometry
    '''

azimuth_angle [number]
tilt_angle [number] (Default: 90.0)
starting_x_coordinate [number]
starting_y_coordinate [number]
starting_z_coordinate [number]
length [number]
height [number]

class Shading:Site:Detailed():
    '''
    used for shading elements such as trees these items are fixed in space and would not move with relative geometry
    '''

transmittance_schedule_name [string]
number_of_vertices [unknown field type] (Default: Autocalculate)
vertices [Array of {vertex_x_coordinate, vertex_y_coordinate, vertex_z_coordinate}]

class Shading:Building:Detailed():
    '''
    used for shading elements such as trees, other buildings, parts of this building not being modeled these items are relative to the current building and would move with relative geometry
    '''

transmittance_schedule_name [string]
number_of_vertices [unknown field type] (Default: Autocalculate)
vertices [Array of {vertex_x_coordinate, vertex_y_coordinate, vertex_z_coordinate}]

class Shading:Overhang():
    '''
    Overhangs are usually flat shading surfaces that reference a window or door.
    '''

window_or_door_name [string]
height_above_window_or_door [number]
tilt_angle_from_window_door [number] (Default: 90.0)
left_extension_from_window_door_width [number]
right_extension_from_window_door_width [number]
depth [number]

class Shading:Overhang:Projection():
    '''
    Overhangs are typically flat shading surfaces that reference a window or door.
    '''

window_or_door_name [string]
height_above_window_or_door [number]
tilt_angle_from_window_door [number] (Default: 90.0)
left_extension_from_window_door_width [number]
right_extension_from_window_door_width [number]
depth_as_fraction_of_window_door_height [number]

class Shading:Fin():
    '''
    Fins are usually shading surfaces that are perpendicular to a window or door.
    '''

window_or_door_name [string]
left_extension_from_window_door [number]
left_distance_above_top_of_window [number]
left_distance_below_bottom_of_window [number]
left_tilt_angle_from_window_door [number] (Default: 90.0)
left_depth [number]
right_extension_from_window_door [number]
right_distance_above_top_of_window [number]
right_distance_below_bottom_of_window [number]
right_tilt_angle_from_window_door [number] (Default: 90.0)
right_depth [number]

class Shading:Fin:Projection():
    '''
    Fins are usually shading surfaces that are perpendicular to a window or door.
    '''

window_or_door_name [string]
left_extension_from_window_door [number]
left_distance_above_top_of_window [number]
left_distance_below_bottom_of_window [number]
left_tilt_angle_from_window_door [number] (Default: 90.0)
left_depth_as_fraction_of_window_door_width [number]
right_extension_from_window_door [number]
right_distance_above_top_of_window [number]
right_distance_below_bottom_of_window [number]
right_tilt_angle_from_window_door [number] (Default: 90.0)
right_depth_as_fraction_of_window_door_width [number]

class Shading:Zone:Detailed():
    '''
    used For fins, overhangs, elements that shade the building, are attached to the building but are not part of the heat transfer calculations
    '''

base_surface_name [string]
transmittance_schedule_name [string]
number_of_vertices [unknown field type] (Default: Autocalculate)
vertices [Array of {vertex_x_coordinate, vertex_y_coordinate, vertex_z_coordinate}]

class ShadingProperty:Reflectance():
    '''
    If this object is not defined for a shading surface the default values listed in following fields will be used in the solar reflection calculation.
    '''

shading_surface_name [string]
diffuse_solar_reflectance_of_unglazed_part_of_shading_surface [number] (Default: 0.2)
diffuse_visible_reflectance_of_unglazed_part_of_shading_surface [number] (Default: 0.2)
fraction_of_shading_surface_that_is_glazed [number] (Default: 0.0)
glazing_construction_name [string]
"""