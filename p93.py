def vout_function(vin, vx, vy):
    """
    Function to calculate the output voltage of a PWM modulator
    from the values of vin and the reference voltages vx and vy.
    This function arbitrarily assumes that VDC = 100 V.
    
    Parameters:
    vin: Input voltage
    vx: x reference
    vy: y reference
    
    Returns:
    vout: Output voltage
    vu: Component of output voltage for vx
    vv: Component of output voltage for vy
    """
    # Initialize vu and vv
    if vin > vx:
        vu = 100
    else:
        vu = 0
        
    if vin >= vy:
        vv = 0
    else:
        vv = 100
    
    # Calculate vout
    vout = vv - vu
    
    return vout, vu, vv
