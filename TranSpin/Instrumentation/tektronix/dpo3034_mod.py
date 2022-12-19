#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2022 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from pymeasure.instruments import Instrument
from pymeasure.instruments.validators import strict_discrete_set, strict_range
import numpy as np


class DPO3034(Instrument):
    """ 
    Class for the use of the waveform generator Thurlby Thandar TGA1241
    """
    
    id = Instrument.measurement(
       "*IDN?",
       """ Reads the instrument identification """
    )
    
    acquisition_mode = Instrument.control(
        "ACQ:MOD?","ACQ:MOD %s",
        """
        Sets or gets the acquisition mode of the oscilloscope
        """,
        validator = strict_discrete_set,
        values = ["SAM","PEAK","HIR","AVE","ENV"]
    )
    
    num_averaged_curves = Instrument.control(
        "ACQ:NUMAVg?","ACQ:NUMAVg %i",
        """
        Sets or gets the number of curves averaged
        """,
        validator = strict_discrete_set,
        values = [2,4,8,16,32,64,128,256,512]
    )
    
    data_channel = Instrument.control(
        ":DAT:SOU CH?",":DAT:SOU CH%s",
        """
        Sets or gets the current selected channel
        """,
        validator = strict_discrete_set,
        values = ["1","2","3","4"]
    )
    
    data_start = Instrument.control(
        ":DAT:START?",":DAT:START %s",
        """
        Sets the initial data point to be received
        """
    )
    
    data_stop = Instrument.control(
        ":DAT:STOP?",":DAT:STOP %s",
        """
        Sets the final data point to be received
        """
    )
    
    vertical_scale = Instrument.control(
        "CH%s:SCA?","CH%s:SCA %s",
        """
        Sets or gets the vertical scale
        """
    )
    
    horizontal_scale = Instrument.control(
        "HOR:SCA?","HOR:SCA %s",
        """
        Sets or gets the vertical scale
        """
    )
    
    offset = Instrument.control(
        "CH%s:OFFS?","CH%s:OFFS %g",
        """
        Sets or gets the offset of the channel
        """
    )
    
    def get_curve(self):
        auxCurve = self.ask("CURV?")
        auxCurve = np.array(auxCurve.split(","),np.float64)
        return auxCurve
    
    def get_curve_info(self):
        auxAnsw = self.ask("WFMO?").split(";")
        auxInfo = {}
        auxInfo['Ref Level'] = np.float64(auxAnsw.pop())
        auxInfo['Span'] = np.float64(auxAnsw.pop())
        auxInfo['Center Frequency'] = np.float64(auxAnsw.pop())
        auxInfo['Waveform Type'] = auxAnsw.pop()
        auxInfo['Domain Time'] = auxAnsw.pop()
        auxInfo['Y Zero'] = np.float64(auxAnsw.pop())
        auxInfo['Y Offset'] = np.float64(auxAnsw.pop())
        auxInfo['Y Multiplier'] = np.float64(auxAnsw.pop())
        auxInfo['Y Unit'] = auxAnsw.pop()
        auxInfo['Pt Off'] = np.int(auxAnsw.pop())
        auxInfo['X Zero'] = np.float64(auxAnsw.pop())
        auxInfo['X Increment'] = np.float64(auxAnsw.pop())
        auxInfo['Y Unit'] = auxAnsw.pop()
        auxInfo['Pt Order'] = auxAnsw.pop()
        auxInfo['Pt Format'] = auxAnsw.pop()
        auxInfo['Nr Points'] = np.int(auxAnsw.pop())
        auxInfo['Waveform ID'] = auxAnsw.pop()
        auxInfo['Byte Order'] = auxAnsw.pop()
        auxInfo['Binary Format'] = auxAnsw.pop()
        auxInfo['Encodeg'] = auxAnsw.pop()
        auxInfo['Nr Bits'] = np.int(auxAnsw.pop())
        auxInfo['Nr Bytes'] = np.int(auxAnsw.pop())
        return auxInfo

    def get_vertical_scale(self,channel=1):
        return np.float64(self.ask("CH{}:SCA?".format(channel)))

    def get_horizontal_scale(self):
        return np.float64(self.ask("HOR:SCA?"))
    
    def get_first_point(self):
        return np.int(self.ask(":DAT:START?"))
    
    def get_last_point(self):
        return np.int(self.ask(":DAT:STOP?"))


    def __init__(self, adapter, baud_rate = 9600, **kwargs):
        super().__init__(
            adapter,
            "TEKTRONIX DPO3034",
            gpib = {'read_termination':'\r\n'},
            asrl = {'baud_rate':baud_rate,'read_termination':'\r\n'},
            **kwargs
        )

    