"""
# Surface Construction Elements
"""

"""
class Material():
    '''
    Regular materials described with full set of thermal properties
    '''

roughness [string]
thickness [number]
conductivity [number]
density [number]
specific_heat [number]
thermal_absorptance [number] (Default: 0.9)
solar_absorptance [number] (Default: 0.7)
visible_absorptance [number] (Default: 0.7)

class Material:NoMass():
    '''
    Regular materials properties described whose principal description is R (Thermal Resistance)
    '''

roughness [string]
thermal_resistance [number]
thermal_absorptance [number] (Default: 0.9)
solar_absorptance [number] (Default: 0.7)
visible_absorptance [number] (Default: 0.7)

class Material:InfraredTransparent():
    '''
    Special infrared transparent material. Similar to a Material:Nomass with low thermal resistance. High absorptance in both wavelengths. Area will be doubled internally to make internal radiant exchange accurate. Should be only material in single layer surface construction. All thermal properties are set internally. User needs only to supply name. Cannot be used with ConductionFiniteDifference solution algorithms
    '''

class Material:AirGap():
    '''
    Air Space in Opaque Construction
    '''

thermal_resistance [number]

class Material:RoofVegetation():
    '''
    EcoRoof model, plant layer plus soil layer Implemented by Portland State University (Sailor et al., January, 2007) only one material must be referenced per simulation though the same EcoRoof material could be used in multiple constructions. New moisture redistribution scheme (2010) requires higher number of timesteps per hour (minimum 12 recommended).
    '''

height_of_plants [number] (Default: 0.2)
leaf_area_index [number] (Default: 1.0)
leaf_reflectivity [number] (Default: 0.22)
leaf_emissivity [number] (Default: 0.95)
minimum_stomatal_resistance [number] (Default: 180.0)
soil_layer_name [string] (Default: Green Roof Soil)
roughness [string] (Default: MediumRough)
thickness [number] (Default: 0.1)
conductivity_of_dry_soil [number] (Default: 0.35)
density_of_dry_soil [number] (Default: 1100.0)
specific_heat_of_dry_soil [number] (Default: 1200.0)
thermal_absorptance [number] (Default: 0.9)
solar_absorptance [number] (Default: 0.7)
visible_absorptance [number] (Default: 0.75)
saturation_volumetric_moisture_content_of_the_soil_layer [number] (Default: 0.3)
residual_volumetric_moisture_content_of_the_soil_layer [number] (Default: 0.01)
initial_volumetric_moisture_content_of_the_soil_layer [number] (Default: 0.1)
moisture_diffusion_calculation_method [string] (Default: Advanced)

class WindowMaterial:SimpleGlazingSystem():
    '''
    Alternate method of describing windows This window material object is used to define an entire glazing system using simple performance parameters.
    '''

u_factor [number]
solar_heat_gain_coefficient [number]
visible_transmittance [number]

class WindowMaterial:Glazing():
    '''
    Glass material properties for Windows or Glass Doors Transmittance/Reflectance input method.
    '''

optical_data_type [string]
window_glass_spectral_data_set_name [string]
thickness [number]
solar_transmittance_at_normal_incidence [number]
front_side_solar_reflectance_at_normal_incidence [number]
back_side_solar_reflectance_at_normal_incidence [number]
visible_transmittance_at_normal_incidence [number]
front_side_visible_reflectance_at_normal_incidence [number]
back_side_visible_reflectance_at_normal_incidence [number]
infrared_transmittance_at_normal_incidence [number] (Default: 0.0)
front_side_infrared_hemispherical_emissivity [number] (Default: 0.84)
back_side_infrared_hemispherical_emissivity [number] (Default: 0.84)
conductivity [number] (Default: 0.9)
dirt_correction_factor_for_solar_and_visible_transmittance [number] (Default: 1.0)
solar_diffusing [string] (Default: No)
young_s_modulus [number] (Default: 72000000000.0)
poisson_s_ratio [number] (Default: 0.22)
window_glass_spectral_and_incident_angle_transmittance_data_set_table_name [string]
window_glass_spectral_and_incident_angle_front_reflectance_data_set_table_name [string]
window_glass_spectral_and_incident_angle_back_reflectance_data_set_table_name [string]

class WindowMaterial:GlazingGroup:Thermochromic():
    '''
    thermochromic glass at different temperatures
    '''

temperature_data [Array of {optical_data_temperature, window_material_glazing_name}]

class WindowMaterial:Glazing:RefractionExtinctionMethod():
    '''
    Glass material properties for Windows or Glass Doors Index of Refraction/Extinction Coefficient input method Not to be used for coated glass
    '''

thickness [number]
solar_index_of_refraction [number]
solar_extinction_coefficient [number]
visible_index_of_refraction [number]
visible_extinction_coefficient [number]
infrared_transmittance_at_normal_incidence [number] (Default: 0.0)
infrared_hemispherical_emissivity [number] (Default: 0.84)
conductivity [number] (Default: 0.9)
dirt_correction_factor_for_solar_and_visible_transmittance [number] (Default: 1.0)
solar_diffusing [string] (Default: No)

class WindowMaterial:Gas():
    '''
    Gas material properties that are used in Windows or Glass Doors
    '''

gas_type [string]
thickness [number]
conductivity_coefficient_a [number]
conductivity_coefficient_b [number]
conductivity_coefficient_c [number]
viscosity_coefficient_a [number]
viscosity_coefficient_b [number]
viscosity_coefficient_c [number]
specific_heat_coefficient_a [number]
specific_heat_coefficient_b [number]
specific_heat_coefficient_c [number]
molecular_weight [number]
specific_heat_ratio [number]

class WindowGap:SupportPillar():
    '''
    used to define pillar geometry for support pillars
    '''

spacing [number] (Default: 0.04)
radius [number] (Default: 0.0004)

class WindowGap:DeflectionState():
    '''
    Used to enter data describing deflection state of the gap. It is referenced from WindowMaterial:Gap object only and it is used only when deflection model is set to MeasuredDeflection, otherwise it is ignored.
    '''

deflected_thickness [number] (Default: 0.0)
initial_temperature [number] (Default: 25.0)
initial_pressure [number] (Default: 101325.0)

class WindowMaterial:GasMixture():
    '''
    Gas mixtures that are used in Windows or Glass Doors
    '''

thickness [number]
number_of_gases_in_mixture [number]
gas_1_type [string]
gas_1_fraction [number]
gas_2_type [string]
gas_2_fraction [number]
gas_3_type [string]
gas_3_fraction [number]
gas_4_type [string]
gas_4_fraction [number]

class WindowMaterial:Gap():
    '''
    Used to define the gap between two layers in a complex fenestration system, where the Construction:ComplexFenestrationState object is used. It is referenced as a layer in the Construction:ComplexFenestrationState object. It cannot be referenced as a layer from the Construction object.
    '''

thickness [number]
gas_or_gas_mixture_ [string]
pressure [number] (Default: 101325.0)
deflection_state [string]
support_pillar [string]

class WindowMaterial:Shade():
    '''
    Specifies the properties of window shade materials. Reflectance and emissivity properties are assumed to be the same on both sides of the shade. Shades are considered to be perfect diffusers (all transmitted and reflected radiation is hemispherically-diffuse) independent of angle of incidence.
    '''

solar_transmittance [number]
solar_reflectance [number]
visible_transmittance [number]
visible_reflectance [number]
infrared_hemispherical_emissivity [number]
infrared_transmittance [number]
thickness [number]
conductivity [number]
shade_to_glass_distance [number] (Default: 0.05)
top_opening_multiplier [number] (Default: 0.5)
bottom_opening_multiplier [number] (Default: 0.5)
left_side_opening_multiplier [number] (Default: 0.5)
right_side_opening_multiplier [number] (Default: 0.5)
airflow_permeability [number] (Default: 0.0)

class WindowMaterial:ComplexShade():
    '''
    Complex window shading layer thermal properties
    '''

layer_type [string] (Default: OtherShadingType)
thickness [number] (Default: 0.002)
conductivity [number] (Default: 1.0)
ir_transmittance [number] (Default: 0.0)
front_emissivity [number] (Default: 0.84)
back_emissivity [number] (Default: 0.84)
top_opening_multiplier [number] (Default: 0.0)
bottom_opening_multiplier [number] (Default: 0.0)
left_side_opening_multiplier [number] (Default: 0.0)
right_side_opening_multiplier [number] (Default: 0.0)
front_opening_multiplier [number] (Default: 0.05)
slat_width [number] (Default: 0.016)
slat_spacing [number] (Default: 0.012)
slat_thickness [number] (Default: 0.0006)
slat_angle [number] (Default: 90.0)
slat_conductivity [number] (Default: 160.0)
slat_curve [number] (Default: 0.0)

class WindowMaterial:Blind():
    '''
    Window blind thermal properties
    '''

slat_orientation [string] (Default: Horizontal)
slat_width [number]
slat_separation [number]
slat_thickness [number] (Default: 0.00025)
slat_angle [number] (Default: 45.0)
slat_conductivity [number] (Default: 221.0)
slat_beam_solar_transmittance [number] (Default: 0.0)
front_side_slat_beam_solar_reflectance [number]
back_side_slat_beam_solar_reflectance [number]
slat_diffuse_solar_transmittance [number] (Default: 0.0)
front_side_slat_diffuse_solar_reflectance [number]
back_side_slat_diffuse_solar_reflectance [number]
slat_beam_visible_transmittance [number]
front_side_slat_beam_visible_reflectance [number]
back_side_slat_beam_visible_reflectance [number]
slat_diffuse_visible_transmittance [number] (Default: 0.0)
front_side_slat_diffuse_visible_reflectance [number]
back_side_slat_diffuse_visible_reflectance [number]
slat_infrared_hemispherical_transmittance [number] (Default: 0.0)
front_side_slat_infrared_hemispherical_emissivity [number] (Default: 0.9)
back_side_slat_infrared_hemispherical_emissivity [number] (Default: 0.9)
blind_to_glass_distance [number] (Default: 0.05)
blind_top_opening_multiplier [number] (Default: 0.5)
blind_bottom_opening_multiplier [number] (Default: 0.0)
blind_left_side_opening_multiplier [number] (Default: 0.5)
blind_right_side_opening_multiplier [number] (Default: 0.5)
minimum_slat_angle [number] (Default: 0.0)
maximum_slat_angle [number] (Default: 180.0)

class WindowMaterial:Screen():
    '''
    Window screen physical properties. Can only be located on the exterior side of a window construction.
    '''

reflected_beam_transmittance_accounting_method [string] (Default: ModelAsDiffuse)
diffuse_solar_reflectance [number]
diffuse_visible_reflectance [number]
thermal_hemispherical_emissivity [number] (Default: 0.9)
conductivity [number] (Default: 221.0)
screen_material_spacing [number]
screen_material_diameter [number]
screen_to_glass_distance [number] (Default: 0.025)
top_opening_multiplier [number] (Default: 0.0)
bottom_opening_multiplier [number] (Default: 0.0)
left_side_opening_multiplier [number] (Default: 0.0)
right_side_opening_multiplier [number] (Default: 0.0)
angle_of_resolution_for_screen_transmittance_output_map [unknown field type] (Default: 0.0)

class WindowMaterial:Shade:EquivalentLayer():
    '''
    Specifies the properties of equivalent layer window shade material Shades are considered to be perfect diffusers (all transmitted and reflected radiation is hemispherically-diffuse) independent of angle of incidence. Shade represents roller blinds.
    '''

shade_beam_beam_solar_transmittance [number] (Default: 0.0)
front_side_shade_beam_diffuse_solar_transmittance [number]
back_side_shade_beam_diffuse_solar_transmittance [number]
front_side_shade_beam_diffuse_solar_reflectance [number]
back_side_shade_beam_diffuse_solar_reflectance [number]
shade_beam_beam_visible_transmittance_at_normal_incidence [number]
shade_beam_diffuse_visible_transmittance_at_normal_incidence [number]
shade_beam_diffuse_visible_reflectance_at_normal_incidence [number]
shade_material_infrared_transmittance [number] (Default: 0.05)
front_side_shade_material_infrared_emissivity [number] (Default: 0.91)
back_side_shade_material_infrared_emissivity [number] (Default: 0.91)

class WindowMaterial:Drape:EquivalentLayer():
    '''
    Specifies the properties of equivalent layer drape fabric materials. Shades are considered to be perfect diffusers (all transmitted and reflected radiation is hemispherically-diffuse) independent of angle of incidence. unpleated drape fabric is treated as thin and flat layer.
    '''

drape_beam_beam_solar_transmittance_at_normal_incidence [number] (Default: 0.0)
front_side_drape_beam_diffuse_solar_transmittance [number]
back_side_drape_beam_diffuse_solar_transmittance [number]
front_side_drape_beam_diffuse_solar_reflectance [number]
back_side_drape_beam_diffuse_solar_reflectance [number]
drape_beam_beam_visible_transmittance [number]
drape_beam_diffuse_visible_transmittance [number]
drape_beam_diffuse_visible_reflectance [number]
drape_material_infrared_transmittance [number] (Default: 0.05)
front_side_drape_material_infrared_emissivity [number] (Default: 0.87)
back_side_drape_material_infrared_emissivity [number] (Default: 0.87)
width_of_pleated_fabric [number] (Default: 0.0)
length_of_pleated_fabric [number] (Default: 0.0)

class WindowMaterial:Blind:EquivalentLayer():
    '''
    Window equivalent layer blind slat optical and thermal properties. The model assumes that slats are thin and flat, applies correction empirical correlation to account for curvature effect. Slats are assumed to transmit and reflect diffusely.
    '''

slat_orientation [string] (Default: Horizontal)
slat_width [number]
slat_separation [number]
slat_crown [number] (Default: 0.0015)
slat_angle [number] (Default: 45.0)
front_side_slat_beam_diffuse_solar_transmittance [number] (Default: 0.0)
back_side_slat_beam_diffuse_solar_transmittance [number] (Default: 0.0)
front_side_slat_beam_diffuse_solar_reflectance [number]
back_side_slat_beam_diffuse_solar_reflectance [number]
front_side_slat_beam_diffuse_visible_transmittance [number] (Default: 0.0)
back_side_slat_beam_diffuse_visible_transmittance [number] (Default: 0.0)
front_side_slat_beam_diffuse_visible_reflectance [number]
back_side_slat_beam_diffuse_visible_reflectance [number]
slat_diffuse_diffuse_solar_transmittance [number] (Default: 0.0)
front_side_slat_diffuse_diffuse_solar_reflectance [number]
back_side_slat_diffuse_diffuse_solar_reflectance [number]
slat_diffuse_diffuse_visible_transmittance [number]
front_side_slat_diffuse_diffuse_visible_reflectance [number]
back_side_slat_diffuse_diffuse_visible_reflectance [number]
slat_infrared_transmittance [number] (Default: 0.0)
front_side_slat_infrared_emissivity [number] (Default: 0.9)
back_side_slat_infrared_emissivity [number] (Default: 0.9)
slat_angle_control [string] (Default: FixedSlatAngle)

class WindowMaterial:Screen:EquivalentLayer():
    '''
    Equivalent layer window screen physical properties. Can only be located on the exterior side of a window construction.
    '''

screen_beam_beam_solar_transmittance [unknown field type] (Default: Autocalculate)
screen_beam_diffuse_solar_transmittance [number]
screen_beam_diffuse_solar_reflectance [number]
screen_beam_beam_visible_transmittance [number]
screen_beam_diffuse_visible_transmittance [number]
screen_beam_diffuse_visible_reflectance [number]
screen_infrared_transmittance [number] (Default: 0.02)
screen_infrared_emissivity [number] (Default: 0.93)
screen_wire_spacing [number] (Default: 0.025)
screen_wire_diameter [number] (Default: 0.005)

class WindowMaterial:Glazing:EquivalentLayer():
    '''
    Glass material properties for Windows or Glass Doors Transmittance/Reflectance input method.
    '''

optical_data_type [string] (Default: SpectralAverage)
window_glass_spectral_data_set_name [string]
front_side_beam_beam_solar_transmittance [number]
back_side_beam_beam_solar_transmittance [number]
front_side_beam_beam_solar_reflectance [number]
back_side_beam_beam_solar_reflectance [number]
front_side_beam_beam_visible_solar_transmittance [number]
back_side_beam_beam_visible_solar_transmittance [number]
front_side_beam_beam_visible_solar_reflectance [number]
back_side_beam_beam_visible_solar_reflectance [number]
front_side_beam_diffuse_solar_transmittance [number] (Default: 0.0)
back_side_beam_diffuse_solar_transmittance [number] (Default: 0.0)
front_side_beam_diffuse_solar_reflectance [number] (Default: 0.0)
back_side_beam_diffuse_solar_reflectance [number] (Default: 0.0)
front_side_beam_diffuse_visible_solar_transmittance [number] (Default: 0.0)
back_side_beam_diffuse_visible_solar_transmittance [number] (Default: 0.0)
front_side_beam_diffuse_visible_solar_reflectance [number] (Default: 0.0)
back_side_beam_diffuse_visible_solar_reflectance [number] (Default: 0.0)
diffuse_diffuse_solar_transmittance [unknown field type] (Default: Autocalculate)
front_side_diffuse_diffuse_solar_reflectance [unknown field type] (Default: Autocalculate)
back_side_diffuse_diffuse_solar_reflectance [unknown field type] (Default: Autocalculate)
diffuse_diffuse_visible_solar_transmittance [unknown field type] (Default: Autocalculate)
front_side_diffuse_diffuse_visible_solar_reflectance [unknown field type] (Default: Autocalculate)
back_side_diffuse_diffuse_visible_solar_reflectance [unknown field type] (Default: Autocalculate)
infrared_transmittance_applies_to_front_and_back_ [number] (Default: 0.0)
front_side_infrared_emissivity [number] (Default: 0.84)
back_side_infrared_emissivity [number] (Default: 0.84)
thermal_resistance [number] (Default: 0.158)

class WindowMaterial:Gap:EquivalentLayer():
    '''
    Gas material properties that are used in Windows Equivalent Layer References only WindowMaterial:Gas properties
    '''

gas_type [string]
thickness [number]
gap_vent_type [string]
conductivity_coefficient_a [number]
conductivity_coefficient_b [number]
conductivity_coefficient_c [number]
viscosity_coefficient_a [number]
viscosity_coefficient_b [number]
viscosity_coefficient_c [number]
specific_heat_coefficient_a [number]
specific_heat_coefficient_b [number]
specific_heat_coefficient_c [number]
molecular_weight [number]
specific_heat_ratio [number]

class MaterialProperty:MoisturePenetrationDepth:Settings():
    '''
    Additional properties for moisture using EMPD procedure HeatBalanceAlgorithm choice=MoisturePenetrationDepthConductionTransferFunction only Has no effect with other HeatBalanceAlgorithm solution algorithms
    '''

water_vapor_diffusion_resistance_factor [number]
moisture_equation_coefficient_a [number]
moisture_equation_coefficient_b [number]
moisture_equation_coefficient_c [number]
moisture_equation_coefficient_d [number]
surface_layer_penetration_depth [unknown field type] (Default: Autocalculate)
deep_layer_penetration_depth [unknown field type] (Default: Autocalculate)
coating_layer_thickness [number]
coating_layer_water_vapor_diffusion_resistance_factor [number]

class MaterialProperty:PhaseChange():
    '''
    Additional properties for temperature dependent thermal conductivity and enthalpy for Phase Change Materials (PCM) HeatBalanceAlgorithm = CondFD(ConductionFiniteDifference) solution algorithm only. Constructions with this should use the detailed CondFD process. Has no effect with other HeatBalanceAlgorithm solution algorithms

temperature_coefficient_for_thermal_conductivity [number] (Default: 0.0)
temperature_1 [number]
enthalpy_1 [number]
temperature_2 [number]
enthalpy_2 [number]
temperature_3 [number]
enthalpy_3 [number]
temperature_4 [number]
enthalpy_4 [number]
temperature_5 [number]
enthalpy_5 [number]
temperature_6 [number]
enthalpy_6 [number]
temperature_7 [number]
enthalpy_7 [number]
temperature_8 [number]
enthalpy_8 [number]
temperature_9 [number]
enthalpy_9 [number]
temperature_10 [number]
enthalpy_10 [number]
temperature_11 [number]
enthalpy_11 [number]
temperature_12 [number]
enthalpy_12 [number]
temperature_13 [number]
enthalpy_13 [number]
temperature_14 [number]
enthalpy_14 [number]
temperature_15 [number]
enthalpy_15 [number]
temperature_16 [number]
enthalpy_16 [number]

class MaterialProperty:PhaseChangeHysteresis():
    '''
    Additional properties for temperature dependent thermal conductivity and enthalpy for Phase Change Materials (PCM) with separate melting and freezing curves. HeatBalanceAlgorithm = CondFD (ConductionFiniteDifference) solution algorithm only. Constructions with this should use the detailed CondFD process. Has no effect with other HeatBalanceAlgorithm solution algorithms.
    '''

latent_heat_during_the_entire_phase_change_process [number]
liquid_state_thermal_conductivity [number]
liquid_state_density [number]
liquid_state_specific_heat [number]
high_temperature_difference_of_melting_curve [number]
peak_melting_temperature [number]
low_temperature_difference_of_melting_curve [number]
solid_state_thermal_conductivity [number]
solid_state_density [number]
solid_state_specific_heat [number]
high_temperature_difference_of_freezing_curve [number]
peak_freezing_temperature [number]
low_temperature_difference_of_freezing_curve [number]

class MaterialProperty:VariableThermalConductivity():
    '''
    Additional properties for temperature dependent thermal conductivity using piecewise linear temperature-conductivity function. HeatBalanceAlgorithm = CondFD(ConductionFiniteDifference) solution algorithm only. Has no effect with other HeatBalanceAlgorithm solution algorithms
    '''

temperature_1 [number]
thermal_conductivity_1 [number]
temperature_2 [number]
thermal_conductivity_2 [number]
temperature_3 [number]
thermal_conductivity_3 [number]
temperature_4 [number]
thermal_conductivity_4 [number]
temperature_5 [number]
thermal_conductivity_5 [number]
temperature_6 [number]
thermal_conductivity_6 [number]
temperature_7 [number]
thermal_conductivity_7 [number]
temperature_8 [number]
thermal_conductivity_8 [number]
temperature_9 [number]
thermal_conductivity_9 [number]
temperature_10 [number]
thermal_conductivity_10 [number]

class MaterialProperty:HeatAndMoistureTransfer:Settings():
    '''
    HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only. Additional material properties for surfaces. Has no effect with other HeatBalanceAlgorithm solution algorithms
    '''

material_name [string]
porosity [number]
initial_water_content_ratio [number] (Default: 0.2)

class MaterialProperty:HeatAndMoistureTransfer:SorptionIsotherm():
    '''
    HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only. Relationship between moisture content and relative humidity fraction. Has no effect with other HeatBalanceAlgorithm solution algorithms
    '''

material_name [string]
number_of_isotherm_coordinates [number]
relative_humidity_fraction_1 [number]
moisture_content_1 [number]
relative_humidity_fraction_2 [number]
moisture_content_2 [number]
relative_humidity_fraction_3 [number]
moisture_content_3 [number]
relative_humidity_fraction_4 [number]
moisture_content_4 [number]
relative_humidity_fraction_5 [number]
moisture_content_5 [number]
relative_humidity_fraction_6 [number]
moisture_content_6 [number]
relative_humidity_fraction_7 [number]
moisture_content_7 [number]
relative_humidity_fraction_8 [number]
moisture_content_8 [number]
relative_humidity_fraction_9 [number]
moisture_content_9 [number]
relative_humidity_fraction_10 [number]
moisture_content_10 [number]
relative_humidity_fraction_11 [number]
moisture_content_11 [number]
relative_humidity_fraction_12 [number]
moisture_content_12 [number]
relative_humidity_fraction_13 [number]
moisture_content_13 [number]
relative_humidity_fraction_14 [number]
moisture_content_14 [number]
relative_humidity_fraction_15 [number]
moisture_content_15 [number]
relative_humidity_fraction_16 [number]
moisture_content_16 [number]
relative_humidity_fraction_17 [number]
moisture_content_17 [number]
relative_humidity_fraction_18 [number]
moisture_content_18 [number]
relative_humidity_fraction_19 [number]
moisture_content_19 [number]
relative_humidity_fraction_20 [number]
moisture_content_20 [number]
relative_humidity_fraction_21 [number]
moisture_content_21 [number]
relative_humidity_fraction_22 [number]
moisture_content_22 [number]
relative_humidity_fraction_23 [number]
moisture_content_23 [number]
relative_humidity_fraction_24 [number]
moisture_content_24 [number]
relative_humidity_fraction_25 [number]
moisture_content_25 [number]

class MaterialProperty:HeatAndMoistureTransfer:Suction():
    '''
    HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only. Relationship between liquid suction transport coefficient and moisture content Has no effect with other HeatBalanceAlgorithm solution algorithms
    '''

material_name [string]
number_of_suction_points [number]
moisture_content_1 [number]
liquid_transport_coefficient_1 [number]
moisture_content_2 [number]
liquid_transport_coefficient_2 [number]
moisture_content_3 [number]
liquid_transport_coefficient_3 [number]
moisture_content_4 [number]
liquid_transport_coefficient_4 [number]
moisture_content_5 [number]
liquid_transport_coefficient_5 [number]
moisture_content_6 [number]
liquid_transport_coefficient_6 [number]
moisture_content_7 [number]
liquid_transport_coefficient_7 [number]
moisture_content_8 [number]
liquid_transport_coefficient_8 [number]
moisture_content_9 [number]
liquid_transport_coefficient_9 [number]
moisture_content_10 [number]
liquid_transport_coefficient_10 [number]
moisture_content_11 [number]
liquid_transport_coefficient_11 [number]
moisture_content_12 [number]
liquid_transport_coefficient_12 [number]
moisture_content_13 [number]
liquid_transport_coefficient_13 [number]
moisture_content_14 [number]
liquid_transport_coefficient_14 [number]
moisture_content_15 [number]
liquid_transport_coefficient_15 [number]
moisture_content_16 [number]
liquid_transport_coefficient_16 [number]
moisture_content_17 [number]
liquid_transport_coefficient_17 [number]
moisture_content_18 [number]
liquid_transport_coefficient_18 [number]
moisture_content_19 [number]
liquid_transport_coefficient_19 [number]
moisture_content_20 [number]
liquid_transport_coefficient_20 [number]
moisture_content_21 [number]
liquid_transport_coefficient_21 [number]
moisture_content_22 [number]
liquid_transport_coefficient_22 [number]
moisture_content_23 [number]
liquid_transport_coefficient_23 [number]
moisture_content_24 [number]
liquid_transport_coefficient_24 [number]
moisture_content_25 [number]
liquid_transport_coefficient_25 [number]

class MaterialProperty:HeatAndMoistureTransfer:Redistribution():
    '''
    HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only. Relationship between liquid transport coefficient and moisture content Has no effect with other HeatBalanceAlgorithm solution algorithms
    '''

material_name [string]
number_of_redistribution_points [number]
moisture_content_1 [number]
liquid_transport_coefficient_1 [number]
moisture_content_2 [number]
liquid_transport_coefficient_2 [number]
moisture_content_3 [number]
liquid_transport_coefficient_3 [number]
moisture_content_4 [number]
liquid_transport_coefficient_4 [number]
moisture_content_5 [number]
liquid_transport_coefficient_5 [number]
moisture_content_6 [number]
liquid_transport_coefficient_6 [number]
moisture_content_7 [number]
liquid_transport_coefficient_7 [number]
moisture_content_8 [number]
liquid_transport_coefficient_8 [number]
moisture_content_9 [number]
liquid_transport_coefficient_9 [number]
moisture_content_10 [number]
liquid_transport_coefficient_10 [number]
moisture_content_11 [number]
liquid_transport_coefficient_11 [number]
moisture_content_12 [number]
liquid_transport_coefficient_12 [number]
moisture_content_13 [number]
liquid_transport_coefficient_13 [number]
moisture_content_14 [number]
liquid_transport_coefficient_14 [number]
moisture_content_15 [number]
liquid_transport_coefficient_15 [number]
moisture_content_16 [number]
liquid_transport_coefficient_16 [number]
moisture_content_17 [number]
liquid_transport_coefficient_17 [number]
moisture_content_18 [number]
liquid_transport_coefficient_18 [number]
moisture_content_19 [number]
liquid_transport_coefficient_19 [number]
moisture_content_20 [number]
liquid_transport_coefficient_20 [number]
moisture_content_21 [number]
liquid_transport_coefficient_21 [number]
moisture_content_22 [number]
liquid_transport_coefficient_22 [number]
moisture_content_23 [number]
liquid_transport_coefficient_23 [number]
moisture_content_24 [number]
liquid_transport_coefficient_24 [number]
moisture_content_25 [number]
liquid_transport_coefficient_25 [number]

class MaterialProperty:HeatAndMoistureTransfer:Diffusion():
    '''
    HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only. Relationship between water vapor diffusion and relative humidity fraction Has no effect with other HeatBalanceAlgorithm solution algorithms
    '''

material_name [string]
number_of_data_pairs [number]
relative_humidity_fraction_1 [number]
water_vapor_diffusion_resistance_factor_1 [number]
relative_humidity_fraction_2 [number]
water_vapor_diffusion_resistance_factor_2 [number]
relative_humidity_fraction_3 [number]
water_vapor_diffusion_resistance_factor_3 [number]
relative_humidity_fraction_4 [number]
water_vapor_diffusion_resistance_factor_4 [number]
relative_humidity_fraction_5 [number]
water_vapor_diffusion_resistance_factor_5 [number]
relative_humidity_fraction_6 [number]
water_vapor_diffusion_resistance_factor_6 [number]
relative_humidity_fraction_7 [number]
water_vapor_diffusion_resistance_factor_7 [number]
relative_humidity_fraction_8 [number]
water_vapor_diffusion_resistance_factor_8 [number]
relative_humidity_fraction_9 [number]
water_vapor_diffusion_resistance_factor_9 [number]
relative_humidity_fraction_10 [number]
water_vapor_diffusion_resistance_factor_10 [number]
relative_humidity_fraction_11 [number]
water_vapor_diffusion_resistance_factor_11 [number]
relative_humidity_fraction_12 [number]
water_vapor_diffusion_resistance_factor_12 [number]
relative_humidity_fraction_13 [number]
water_vapor_diffusion_resistance_factor_13 [number]
relative_humidity_fraction_14 [number]
water_vapor_diffusion_resistance_factor_14 [number]
relative_humidity_fraction_15 [number]
water_vapor_diffusion_resistance_factor_15 [number]
relative_humidity_fraction_16 [number]
water_vapor_diffusion_resistance_factor_16 [number]
relative_humidity_fraction_17 [number]
water_vapor_diffusion_resistance_factor_17 [number]
relative_humidity_fraction_18 [number]
water_vapor_diffusion_resistance_factor_18 [number]
relative_humidity_fraction_19 [number]
water_vapor_diffusion_resistance_factor_19 [number]
relative_humidity_fraction_20 [number]
water_vapor_diffusion_resistance_factor_20 [number]
relative_humidity_fraction_21 [number]
water_vapor_diffusion_resistance_factor_21 [number]
relative_humidity_fraction_22 [number]
water_vapor_diffusion_resistance_factor_22 [number]
relative_humidity_fraction_23 [number]
water_vapor_diffusion_resistance_factor_23 [number]
relative_humidity_fraction_24 [number]
water_vapor_diffusion_resistance_factor_24 [number]
relative_humidity_fraction_25 [number]
water_vapor_diffusion_resistance_factor_25 [number]

class MaterialProperty:HeatAndMoistureTransfer:ThermalConductivity():
    '''
    HeatBalanceAlgorithm = CombinedHeatAndMoistureFiniteElement solution algorithm only. Relationship between thermal conductivity and moisture content Has no effect with other HeatBalanceAlgorithm solution algorithms
    '''

material_name [string]
number_of_thermal_coordinates [number]
moisture_content_1 [number]
thermal_conductivity_1 [number]
moisture_content_2 [number]
thermal_conductivity_2 [number]
moisture_content_3 [number]
thermal_conductivity_3 [number]
moisture_content_4 [number]
thermal_conductivity_4 [number]
moisture_content_5 [number]
thermal_conductivity_5 [number]
moisture_content_6 [number]
thermal_conductivity_6 [number]
moisture_content_7 [number]
thermal_conductivity_7 [number]
moisture_content_8 [number]
thermal_conductivity_8 [number]
moisture_content_9 [number]
thermal_conductivity_9 [number]
moisture_content_10 [number]
thermal_conductivity_10 [number]
moisture_content_11 [number]
thermal_conductivity_11 [number]
moisture_content_12 [number]
thermal_conductivity_12 [number]
moisture_content_13 [number]
thermal_conductivity_13 [number]
moisture_content_14 [number]
thermal_conductivity_14 [number]
moisture_content_15 [number]
thermal_conductivity_15 [number]
moisture_content_16 [number]
thermal_conductivity_16 [number]
moisture_content_17 [number]
thermal_conductivity_17 [number]
moisture_content_18 [number]
thermal_conductivity_18 [number]
moisture_content_19 [number]
thermal_conductivity_19 [number]
moisture_content_20 [number]
thermal_conductivity_20 [number]
moisture_content_21 [number]
thermal_conductivity_21 [number]
moisture_content_22 [number]
thermal_conductivity_22 [number]
moisture_content_23 [number]
thermal_conductivity_23 [number]
moisture_content_24 [number]
thermal_conductivity_24 [number]
moisture_content_25 [number]
thermal_conductivity_25 [number]

class MaterialProperty:GlazingSpectralData():
    '''
    Name is followed by up to 800 sets of normal-incidence measured values of [wavelength, transmittance, front reflectance, back reflectance] for wavelengths covering the solar spectrum (from about 0.25 to 2.5 microns)
    '''

wavelength_1 [number]
transmittance_1 [number]
front_reflectance_1 [number]
back_reflectance_1 [number]
wavelength_2 [number]
transmittance_2 [number]
front_reflectance_2 [number]
back_reflectance_2 [number]
wavelength_3 [number]
transmittance_3 [number]
front_reflectance_3 [number]
back_reflectance_3 [number]
wavelength_4 [number]
transmittance_4 [number]
front_reflectance_4 [number]
back_reflectance_4 [number]
extensions [Array of {wavelength, transmittance, front_reflectance, back_reflectance}]

class Construction():
    '''
    Start with outside layer and work your way to the inside layer Up to 10 layers total, 8 for windows Enter the material name for each layer
    '''

outside_layer [string]
layer_2 [string]
layer_3 [string]
layer_4 [string]
layer_5 [string]
layer_6 [string]
layer_7 [string]
layer_8 [string]
layer_9 [string]
layer_10 [string]

class Construction:CfactorUndergroundWall():
    '''
    Alternate method of describing underground wall constructions
    '''

c_factor [number]
height [number]

class Construction:FfactorGroundFloor():
    '''
    Alternate method of describing slab-on-grade or underground floor constructions
    '''

f_factor [number]
area [number]
perimeterexposed [number]

class ConstructionProperty:InternalHeatSource():
    '''
    Internal heat source to be attached to a construction layer
    '''

construction_name [string]
thermal_source_present_after_layer_number [number]
temperature_calculation_requested_after_layer_number [number]
dimensions_for_the_ctf_calculation [number]
tube_spacing [number]
two_dimensional_temperature_calculation_position [number] (Default: 0.0)

class Construction:AirBoundary():
    '''
    Indicates an open boundary between two zones. It may be used for base surfaces and fenestration surfaces. The two adjacent zones are grouped together for solar, daylighting and radiant exchange. When this construction type is used, the Outside Boundary Condition of the surface (or the base surface of a fenestration surface) must be either Surface or Zone. A base surface with Construction:AirBoundary cannot hold any fenestration surfaces.
    '''

air_exchange_method [string] (Default: None)
simple_mixing_air_changes_per_hour [number] (Default: 0.5)
simple_mixing_schedule_name [string]

class WindowThermalModel:Params():
    '''
    object is used to select which thermal model should be used in tarcog simulations
    '''

standard [string] (Default: ISO15099)
thermal_model [string] (Default: ISO15099)
sdscalar [number] (Default: 1.0)
deflection_model [string] (Default: NoDeflection)
vacuum_pressure_limit [number] (Default: 13.238)
initial_temperature [number] (Default: 25.0)
initial_pressure [number] (Default: 101325.0)

class WindowsCalculationEngine():
    '''
    Describes which window model will be used in calculations. Built in windows model will use algorithms that are part of EnergyPlus, while ExternalWindowsModel will use Windows-CalcEngine library to perform optical and thermal performances of windows and doors.
    '''

windows_engine [string] (Default: BuiltInWindowsModel)

class Construction:ComplexFenestrationState():
    '''
    Describes one state for a complex glazing system These input objects are typically generated by using WINDOW software and export to IDF syntax
    '''

basis_type [string] (Default: LBNLWINDOW)
basis_symmetry_type [string] (Default: None)
window_thermal_model [string]
basis_matrix_name [string]
solar_optical_complex_front_transmittance_matrix_name [string]
solar_optical_complex_back_reflectance_matrix_name [string]
visible_optical_complex_front_transmittance_matrix_name [string]
visible_optical_complex_back_transmittance_matrix_name [string]
outside_layer_name [string]
outside_layer_directional_front_absoptance_matrix_name [string]
outside_layer_directional_back_absoptance_matrix_name [string]
gap_1_name [string]
cfs_gap_1_directional_front_absoptance_matrix_name [string]
cfs_gap_1_directional_back_absoptance_matrix_name [string]
layer_2_name [string]
layer_2_directional_front_absoptance_matrix_name [string]
layer_2_directional_back_absoptance_matrix_name [string]
gap_2_name [string]
gap_2_directional_front_absoptance_matrix_name [string]
gap_2_directional_back_absoptance_matrix_name [string]
layer_3_name [string]
layer_3_directional_front_absoptance_matrix_name [string]
layer_3_directional_back_absoptance_matrix_name [string]
gap_3_name [string]
gap_3_directional_front_absoptance_matrix_name [string]
gap_3_directional_back_absoptance_matrix_name [string]
layer_4_name [string]
layer_4_directional_front_absoptance_matrix_name [string]
layer_4_directional_back_absoptance_matrix_name [string]
gap_4_name [string]
gap_4_directional_front_absoptance_matrix_name [string]
gap_4_directional_back_absoptance_matrix_name [string]
layer_5_name [string]
layer_5_directional_front_absoptance_matrix_name [string]
layer_5_directional_back_absoptance_matrix_name [string]

class Construction:WindowEquivalentLayer():
    '''
    Start with outside layer and work your way to the inside Layer Up to 11 layers total. Up to six solid layers and up to five gaps. Enter the material name for each layer
    '''

outside_layer [string]
layer_2 [string]
layer_3 [string]
layer_4 [string]
layer_5 [string]
layer_6 [string]
layer_7 [string]
layer_8 [string]
layer_9 [string]
layer_10 [string]
layer_11 [string]

class Construction:WindowDataFile():
    '''
    Initiates search of the Window data file for a window called Name.
    '''

file_name [string]
"""