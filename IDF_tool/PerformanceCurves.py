"""
# Performance Curves
"""
"""
Curve:Linear
Linear curve with one independent variable. Input for the linear curve consists of a curve name, the two coefficients, and the maximum and minimum valid independent variable values. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*x

Fields

coefficient1_constant [number]
coefficient2_x [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:QuadLinear
Linear curve with four independent variables. Input for the linear curve consists of a curve name, the two coefficients, and the maximum and minimum valid independent variable values. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*w + C3*x + C4*y + C5*z

Fields

coefficient1_constant [number]
coefficient2_w [number]
coefficient3_x [number]
coefficient4_y [number]
coefficient5_z [number]
minimum_value_of_w [number]
maximum_value_of_w [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_value_of_y [number]
maximum_value_of_y [number]
minimum_value_of_z [number]
maximum_value_of_z [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_w [string] (Default: Dimensionless)
input_unit_type_for_x [string] (Default: Dimensionless)
input_unit_type_for_y [string] (Default: Dimensionless)
input_unit_type_for_z [string] (Default: Dimensionless)
Curve:QuintLinear
Linear curve with five independent variables. Input for the linear curve consists of a curve name, the two coefficients, and the maximum and minimum valid independent variable values. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*v + C3*w + C4*x + C5*y + C6*z

Fields

coefficient1_constant [number]
coefficient2_v [number]
coefficient3_w [number]
coefficient4_x [number]
coefficient5_y [number]
coefficient6_z [number]
minimum_value_of_v [number]
maximum_value_of_v [number]
minimum_value_of_w [number]
maximum_value_of_w [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_value_of_y [number]
maximum_value_of_y [number]
minimum_value_of_z [number]
maximum_value_of_z [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_v [string] (Default: Dimensionless)
input_unit_type_for_w [string] (Default: Dimensionless)
input_unit_type_for_x [string] (Default: Dimensionless)
input_unit_type_for_y [string] (Default: Dimensionless)
input_unit_type_for_z [string] (Default: Dimensionless)
Curve:Quadratic
Quadratic curve with one independent variable. Input for a quadratic curve consists of the curve name, the three coefficients, and the maximum and minimum valid independent variable values. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*x + C3*x**2

Fields

coefficient1_constant [number]
coefficient2_x [number]
coefficient3_x_2 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:Cubic
Cubic curve with one independent variable. Input for a cubic curve consists of the curve name, the 4 coefficients, and the maximum and minimum valid independent variable values. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*x + C3*x**2 + C4*x**3

Fields

coefficient1_constant [number]
coefficient2_x [number]
coefficient3_x_2 [number]
coefficient4_x_3 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:Quartic
Quartic (fourth order polynomial) curve with one independent variable. Input for a Quartic curve consists of the curve name, the five coefficients, and the maximum and minimum valid independent variable values. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*x + C3*x**2 + C4*x**3 + C5*x**4

Fields

coefficient1_constant [number]
coefficient2_x [number]
coefficient3_x_2 [number]
coefficient4_x_3 [number]
coefficient5_x_4 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:Exponent
Exponent curve with one independent variable. Input for a exponent curve consists of the curve name, the 3 coefficients, and the maximum and minimum valid independent variable values. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*x**C3 The independent variable x is raised to the C3 power, multiplied by C2, and C1 is added to the result.

Fields

coefficient1_constant [number]
coefficient2_constant [number]
coefficient3_constant [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:Bicubic
Cubic curve with two independent variables. Input consists of the curve name, the ten coefficients, and the minimum and maximum values for each of the independent variables. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*x + C3*x**2 + C4*y + C5*y**2 + C6*x*y + C7*x**3 + C8*y**3 + C9*x**2*y + C10*x*y**2

Fields

coefficient1_constant [number]
coefficient2_x [number]
coefficient3_x_2 [number]
coefficient4_y [number]
coefficient5_y_2 [number]
coefficient6_x_y [number]
coefficient7_x_3 [number]
coefficient8_y_3 [number]
coefficient9_x_2_y [number]
coefficient10_x_y_2 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_value_of_y [number]
maximum_value_of_y [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
input_unit_type_for_y [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:Biquadratic
Quadratic curve with two independent variables. Input consists of the curve name, the six coefficients, and min and max values for each of the independent variables. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*x + C3*x**2 + C4*y + C5*y**2 + C6*x*y

Fields

coefficient1_constant [number]
coefficient2_x [number]
coefficient3_x_2 [number]
coefficient4_y [number]
coefficient5_y_2 [number]
coefficient6_x_y [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_value_of_y [number]
maximum_value_of_y [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
input_unit_type_for_y [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:QuadraticLinear
Quadratic-linear curve with two independent variables. Input consists of the curve name, the six coefficients, and min and max values for each of the independent variables. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = (C1 + C2*x + C3*x**2) + (C4 + C5*x + C6*x**2)*y

Fields

coefficient1_constant [number]
coefficient2_x [number]
coefficient3_x_2 [number]
coefficient4_y [number]
coefficient5_x_y [number]
coefficient6_x_2_y [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_value_of_y [number]
maximum_value_of_y [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
input_unit_type_for_y [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:CubicLinear
Cubic-linear curve with two independent variables. Input consists of the curve name, the six coefficients, and min and max values for each of the independent variables. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = (C1 + C2*x + C3*x**2 + C4*x**3) + (C5 + C6*x)*y

Fields

coefficient1_constant [number]
coefficient2_x [number]
coefficient3_x_2 [number]
coefficient4_x_3 [number]
coefficient5_y [number]
coefficient6_x_y [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_value_of_y [number]
maximum_value_of_y [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
input_unit_type_for_y [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:Triquadratic
Quadratic curve with three independent variables. Input consists of the curve name, the twenty seven coefficients, and min and max values for each of the independent variables. Optional inputs for curve minimum and maximum may be used to limit the output of the performance curve. curve = a0 + a1*x**2 + a2*x + a3*y**2 + a4*y + a5*z**2 + a6*z + a7*x**2*y**2 + a8*x*y + a9*x*y**2 + a10*x**2*y + a11*x**2*z**2 + a12*x*z + a13*x*z**2 + a14*x**2*z + a15*y**2*z**2 + a16*y*z + a17*y*z**2 + a18*y**2*z + a19*x**2*y**2*z**2 + a20*x**2*y**2*z + a21*x**2*y*z**2 + a22*x*y**2*z**2 + a23*x**2*y*z + a24*x*y**2*z + a25*x*y*z**2 +a26*x*y*z

Fields

coefficient1_constant [number]
coefficient2_x_2 [number]
coefficient3_x [number]
coefficient4_y_2 [number]
coefficient5_y [number]
coefficient6_z_2 [number]
coefficient7_z [number]
coefficient8_x_2_y_2 [number]
coefficient9_x_y [number]
coefficient10_x_y_2 [number]
coefficient11_x_2_y [number]
coefficient12_x_2_z_2 [number]
coefficient13_x_z [number]
coefficient14_x_z_2 [number]
coefficient15_x_2_z [number]
coefficient16_y_2_z_2 [number]
coefficient17_y_z [number]
coefficient18_y_z_2 [number]
coefficient19_y_2_z [number]
coefficient20_x_2_y_2_z_2 [number]
coefficient21_x_2_y_2_z [number]
coefficient22_x_2_y_z_2 [number]
coefficient23_x_y_2_z_2 [number]
coefficient24_x_2_y_z [number]
coefficient25_x_y_2_z [number]
coefficient26_x_y_z_2 [number]
coefficient27_x_y_z [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_value_of_y [number]
maximum_value_of_y [number]
minimum_value_of_z [number]
maximum_value_of_z [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
input_unit_type_for_y [string] (Default: Dimensionless)
input_unit_type_for_z [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:Functional:PressureDrop
Sets up curve information for minor loss and/or friction calculations in plant pressure simulations Expression: DeltaP = {K + f*(L/D)} * (rho * V^2) / 2

Fields

diameter [number]
minor_loss_coefficient [number]
length [number]
roughness [number]
fixed_friction_factor [number]
Curve:FanPressureRise
Special curve type with two independent variables. Input for the fan total pressure rise curve consists of the curve name, the four coefficients, and the maximum and minimum valid independent variable values. Optional inputs for the curve minimum and maximum may be used to limit the output of the performance curve. curve = C1*Qfan**2+C2*Qfan+C3*Qfan*(Psm-Po)**0.5+C4*(Psm-Po) Po assumed to be zero See InputOut Reference for curve details

Fields

coefficient1_c1 [number]
coefficient2_c2 [number]
coefficient3_c3 [number]
coefficient4_c4 [number]
minimum_value_of_qfan [number]
maximum_value_of_qfan [number]
minimum_value_of_psm [number]
maximum_value_of_psm [number]
minimum_curve_output [number]
maximum_curve_output [number]
Curve:ExponentialSkewNormal
Exponential-modified skew normal curve with one independent variable. Input consists of the curve name, the four coefficients, and the maximum and minimum valid independent variable values. Optional inputs for the curve minimum and maximum may be used to limit the output of the performance curve. curve = see Input Output Reference

Fields

coefficient1_c1 [number]
coefficient2_c2 [number]
coefficient3_c3 [number]
coefficient4_c4 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:Sigmoid
Sigmoid curve with one independent variable. Input consists of the curve name, the five coefficients, and the maximum and minimum valid independent variable values. Optional inputs for the curve minimum and maximum may be used to limit the output of the performance curve. curve = C1+C2/[1+exp((C3-x)/C4)]**C5

Fields

coefficient1_c1 [number]
coefficient2_c2 [number]
coefficient3_c3 [number]
coefficient4_c4 [number]
coefficient5_c5 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:RectangularHyperbola1
Rectangular hyperbola type 1 curve with one independent variable. Input consists of the curve name, the three coefficients, and the maximum and minimum valid independent variable values. Optional inputs for the curve minimum and maximum may be used to limit the output of the performance curve. curve = ((C1*x)/(C2+x))+C3

Fields

coefficient1_c1 [number]
coefficient2_c2 [number]
coefficient3_c3 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:RectangularHyperbola2
Rectangular hyperbola type 2 curve with one independent variable. Input consists of the curve name, the three coefficients, and the maximum and minimum valid independent variable values. Optional inputs for the curve minimum and maximum may be used to limit the output of the performance curve. curve = ((C1*x)/(C2+x))+(C3*x)

Fields

coefficient1_c1 [number]
coefficient2_c2 [number]
coefficient3_c3 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:ExponentialDecay
Exponential decay curve with one independent variable. Input consists of the curve name, the three coefficients, and the maximum and minimum valid independent variable values. Optional inputs for the curve minimum and maximum may be used to limit the output of the performance curve. curve = C1+C2*exp(C3*x)

Fields

coefficient1_c1 [number]
coefficient2_c2 [number]
coefficient3_c3 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:DoubleExponentialDecay
Double exponential decay curve with one independent variable. Input consists of the curve name, the five coefficients, and the maximum and minimum valid independent variable values. Optional inputs for the curve minimum and maximum may be used to limit the output of the performance curve. curve = C1+C2*exp(C3*x)+C4*exp(C5*x)

Fields

coefficient1_c1 [number]
coefficient2_c2 [number]
coefficient3_c3 [number]
coefficient4_c4 [number]
coefficient5_c5 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
Curve:ChillerPartLoadWithLift
This chiller part-load performance curve has three independent variables. Input consists of the curve name, the twelve coefficients, and the maximum and minimum valid independent variable values. Optional inputs for the curve minimum and maximum may be used to limit the output of the performance curve. curve = C1 + C2*x + C3*x**2 + C4*y + C5*y**2 + C6*x*y + C7*x**3 + C8*y**3 + C9*x**2*y + C10*x*y**2 + C11*x**2*y**2 + C12*z*y**3 x = dT* = normalized fractional Lift = dT / dTref y = PLR = part load ratio (cooling load/steady state capacity) z = Tdev* = normalized Tdev = Tdev / dTref Where: dT = Lift = Leaving Condenser Water Temperature - Leaving Chilled Water Temperature dTref = dT at the reference condition Tdev = Leaving Chilled Water Temperature - Reference Chilled Water Temperature

Fields

coefficient1_c1 [number]
coefficient2_c2 [number]
coefficient3_c3 [number]
coefficient4_c4 [number]
coefficient5_c5 [number]
coefficient6_c6 [number]
coefficient7_c7 [number]
coefficient8_c8 [number]
coefficient9_c9 [number]
coefficient10_c10 [number]
coefficient11_c11 [number]
coefficient12_c12 [number]
minimum_value_of_x [number]
maximum_value_of_x [number]
minimum_value_of_y [number]
maximum_value_of_y [number]
minimum_value_of_z [number]
maximum_value_of_z [number]
minimum_curve_output [number]
maximum_curve_output [number]
input_unit_type_for_x [string] (Default: Dimensionless)
input_unit_type_for_y [string] (Default: Dimensionless)
input_unit_type_for_z [string] (Default: Dimensionless)
output_unit_type [string] (Default: Dimensionless)
"""