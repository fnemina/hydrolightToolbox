import pint
import numpy as np



def pcolormesh_polar(da, r=None, theta=None, add_labels=False, propagation=True,**kwargs):
    """ This function takes a xarray dataset and plots a polar plot as taken from

        https://stackoverflow.com/questions/64664428/xarray-polar-pcolormesh-with-low-overhead-axis-coordinate-transformation
        
        It uses pint to convert units from degrees to radians.
    """

    ureg = pint.UnitRegistry()

    # Coordinates for looking upwards always
    da = da.assign_coords({"dphi": ("phi", (da["phi"].values+180.0)%360)})
    da["dphi"].attrs = da["phi"].attrs

    # By default theta and phi are the values for r and theta in the polar plot

    if r is None:
        r = "theta"
    if theta is None:
        if propagation: 
            theta = "phi"
            thetadim = "phi"
        else: 
            theta = "dphi"
            thetadim = "phi"
            da = da.sortby("dphi")
    else:
        thetadim = theta
    
    try:
        theta_units = ureg.Unit(da[theta].attrs["units"])
    except KeyError:
        theta_units = ureg.rad

    if theta_units != ureg.rad:
        theta_rad = f"{theta}_rad"
        theta_rad_values = ureg.Quantity(da[theta].values, theta_units).to(ureg.rad).magnitude
        da_plot = da.assign_coords(**{theta_rad: (thetadim, theta_rad_values)})
        da_plot[theta_rad].attrs = da[theta].attrs
        da_plot[theta_rad].attrs["units"] = "rad"
    else:
        theta_rad = theta
        da_plot = da
    
    kwargs["x"] = theta_rad
    kwargs["y"] = r
    kwargs["add_labels"] = add_labels


    try:
        subplot_kws = kwargs["subplot_kws"]
    except KeyError:
        subplot_kws = {}
    subplot_kws["projection"] = "polar"
    
    return da_plot.plot.pcolormesh(
        **kwargs,
        subplot_kws=subplot_kws,
    )