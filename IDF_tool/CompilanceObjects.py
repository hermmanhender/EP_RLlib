'''
# Compilance objects
'''
class Compliance_Building():
    """
    Building level inputs related to compliance to building standards, building codes, and beyond energy code programs.
    """
    def building_rotation_for_appendix_g(epJSON, data=0.0):
        epJSON["Compliance:Building"]["Compliance:Building 1"]["building_rotation_for_appendix_g"] = data # [data] (Default: 0.0)
        return epJSON