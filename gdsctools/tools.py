# -*- python -*-
# -*- coding utf-8 -*-
#
#  This file is part of GDSCTools software
#
#  Copyright (c) 2015 - Wellcome Trust Sanger Institute
#  All rights reserved
#
#  File author(s): Thomas Cokelaer <cokelaer@gmail.comWE HERE>
#
#  Distributed under the BSD 3-Clause License.
#  See accompanying file LICENSE.txt distributed with this software
#
#  website: http://github.com/CancerRxGene/gdsctools
#
##############################################################################
"""Sets of miscellaneous tools"""
import numpy as np
import pylab
import os


class Savefig(object):
    """A simple class to save matploltib figures in the proper place

    .. note:: For developers only
    """
    def __init__(self, verbose=False):
        self.verbose = verbose
        self._directory = None
        #: directory where to save figures
        self.directory = '.'

    def _get_directory(self):
        return self._directory
    def _set_directory(self, directory):
        self._directory = directory
        try:
            if os.path.isdir(directory) is False:
                os.mkdir(self.directory)
                if self.verbose:
                    print("Created directory {}".format(directory))
        except Exception:
            if self.verbose:
                print("Could not create the directory")
    directory = property(_get_directory, _set_directory, doc="")

    def savefig(self, name, size_inches=None,**kargs):
        """Save a matplotlib figure

        :param str filename: where to save the figure.
        :param **kargs: accepts all parameters known by pylab.savefig
        """
        # if not provided, don't do anything.
        if name is None:
            return

        try:
            directory = self.settings.directory
        except:
            directory = self.directory

        filename = directory + os.sep + name
        fig = pylab.gcf()
        if size_inches is not None:
            fig.set_size_inches(size_inches)
        if self.verbose:
            print("saving file in %s" % filename)
        pylab.savefig(filename, **kargs)


class Logistic(object):
    """Simple logistic class to see the curve implied by xmid/scale parameters

    .. plot::
        :include-source:

        from gdsctools.tools import Logistic
        from pylab import legend 
        tl = Logistic(2, 1)
        tl.plot()
        tl.scale = 4
        tl.plot(hold=True)
        legend(['scale=1', 'scale=4'])

    """
    def __init__(self, xmid, scale, Asym=1):
        r""".. rubric:: Constructor

        :param xmid:
        :param scale:
        :param Asym: 

        .. math:: L(x) = \frac{Asym}{1 + exp ((xmid-X)/scale)}
    
        """
        self.xmid = xmid
        self.scale = scale
        self.Asym = Asym
        self._N = 10

    def get_x(self, N=100):
        """Return a sensible linear space of X values """

        dX = abs(self.scale) 
        X = np.linspace(self.xmid - dX * self._N, 
                self.xmid + dX * self._N, N)
        return  X

    def get_y(self, X=None, N=100):
        """Get the Y values given X and the 2 logistic function parameters"""
        if X is None:
            X = self.get_x()
        else:
            X = np.array(X)

        Y = self.Asym / (1.+ np.exp((self.xmid - X)/self.scale))
        return Y

    def plot(self, X=None, N=100, hold=False):
        """Plot the logistic function"""
        Y = self.get_y(X=X, N=N)
        import pylab
        if X is None:
            X = self.get_x()
        if hold is False:
            pylab.clf();
        pylab.plot(X, Y, 'o-')
        pylab.grid(True)
        pylab.xlabel('X')
        pylab.ylabel('Y')
        pylab.axvline(self.xmid, color='r', linestyle='--')
