import matplotlib.pyplot as plt
import numpy as np


def display(signal, true_chg_pts, computed_chg_pts=None, **kwargs):
    """
    Display a signal and the change points provided.
    """
    if signal.ndim == 1:
        s = signal.reshape(-1, 1)
    else:
        s = signal

    # let's set all options
    figsize = (20, 10 * s.shape[1])  # figure size
    alpha = 0.2  # transparency of the colored background
    color = "k"  # color of the lines indicating the computed_chg_pts
    linewidth = 3   # linewidth of the lines indicating the computed_chg_pts
    linestyle = "--"   # linestyle of the lines indicating the computed_chg_pts

    if "figsize" in kwargs:
        figsize = kwargs["figsize"]
    if "alpha" in kwargs:
        alpha = kwargs["alpha"]
    if "color" in kwargs:
        color = kwargs["color"]
    if "linewidth" in kwargs:
        linewidth = kwargs["linewidth"]
    if "linestyle" in kwargs:
        linestyle = kwargs["linestyle"]

    fig, axarr = plt.subplots(s.shape[1], figsize=figsize, sharex=True)
    if s.shape[1] == 1:
        axarr = [axarr]

    for ax, sig in zip(axarr, s.T):
        color_cycle = ax._get_lines.prop_cycler
        # plot s
        ax.plot(range(s.shape[0]), sig)

        # color each (true) regime
        ends = sorted(true_chg_pts)
        starts = np.append(0, [t + 1 for t in ends[:-1]])

        for (start, end), c in zip(zip(starts, ends), color_cycle):
            ax.axvspan(start, end, facecolor=c["color"], alpha=alpha)

        # vertical lines to mark the computed_chg_pts
        if computed_chg_pts is not None:
            starts = np.sort(computed_chg_pts)
            for start in starts:
                if start != 0:  # no need to put a vertical line at x=0
                    ax.axvline(x=start, color=color, linewidth=linewidth,
                               linestyle=linestyle)

    fig.tight_layout()

    return fig, axarr
