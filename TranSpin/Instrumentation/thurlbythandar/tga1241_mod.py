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


class TTiTGA1241(Instrument):
    """ 
    Class for the use of the waveform generator Thurlby Thandar TGA1241
    """
    
    id = Instrument.measurement(
       "*IDN?",
       """ Reads the instrument identification """
    )
    
    """
    
    FREQUENCY AND PERIOS COMMANDS
    
    """
    
    freq = Instrument.control(
        "WAVFREQ?","WAVFREQ %g",
        """Sets the frequency of the wave function in Hz"""
    )
    
    
    period = Instrument.control(
        "WAVPER?","WAVPER %g",
        """Sets the period of the wave function in s"""
    )
    

    clkFreq = Instrument.control(
        "CLKFREQ?","CLKFREQ %g",
        """Sets the frequency of the arbitrary sample clock in Hz"""
    )
    

    clkPeriod = Instrument.control(
        "CLKPER?","CLKPER %g",
        """Sets the period of the arbitrary sample clock in s"""
    )
    
    """
    
    AMPLITUDE AND DC OFFSET COMMANDS
    
    """

    amplitude = Instrument.control(
        "AMPL?","AMPL %g",
        """Sets the amplitude in the units as specified by amplitudeUnits"""
    )
    

    amplitudeUnits = Instrument.control(
        "AMPUNIT?","AMPUNIT %s",
        """Sets the amplitude units to VPP, VRMS or DBM""",
        validator = strict_discrete_set,
        values = ["VPP","VRMS","DBM"]        
    )
    
    outputLoad = Instrument.control(
        "ZLOAD?","ZLOAD %s",
        """ Set the output load, which the generator is to ssume for amplitude 
        and dc offset entries, to <50>(50 ohms), <600>(600ohms) or <OPEN>""",
        validator = strict_discrete_set,
        values = ["50","600","OPEN"]
    )
    
    dcOffset = Instrument.control(
        "DCOFFS?","DCOFFS %g",
        """
        Sets the dc offset in Volts
        """
    )
    
    
    """
    
    WAVEFORM SELECTION COMMANDS
    
    """
    
    waveForm = Instrument.control(
        "WAVE?","WAVE %s",
        """
        Select the output waveform as SINE, SQUARE, TRIANG, DC, POSRMP, NEGRMP,
        COSINE, HAVSIN, HAVCOS, SINC, PULSE, PULSTRN, ARB or SEQ
        """,
        validator = strict_discrete_set,
        values = ["SINE","SQUARE","TRIANG","DC","POSRMP","NEGRAMP","COSINE",
                  "HAVSIN","HAVCOS","SINC","PULSE","PULSETRN","ARB","SEQ"]
    )
    
    
    pulsePeriod = Instrument.control(
        "PULSPER?","PULSPER &g",
        """
        Sets the pulse period in seconds
        """
    )
    
    
    pulseWidth = Instrument.control(
        "PULSWID?","PULSWID %g",
        """
        Sets the pulse width in seconds
        """  
    )
    
    
    pulseDelay = Instrument.control(
        "PULSDLY?","PULSDLY %g",
        """
        Sets the pulse delay in seconds
        """
    )
    
    
    pulseTrainLength = Instrument.control(
        "PULSTRNLEN?","PULSETRNLEN %g",
        """
        Sets the number of pulses in the pulse-train
        """
    )
    
    
    pulseTrainPeriod = Instrument.control(
        "PULSTRNPER?","PULSETRNPER %g",
        """
        Sets the period of the pulse-train in seconds
        """
    )
    
    
    pulseTrainBaseLine = Instrument.control(
        "PULSTRNBASE?","PULSTRNBASE %g",
        """
        Sets the base line for the pulse-train in Volts
        """
    )
    
    
    pulseTrainLevel = Instrument.control(
        "PULSTRNLEV?","PULSTRNLEV %g,%g",
        """
        Sets the level of pulse-train pulse number val1 to val2 Volts
        """
    )
    
    
    pulseTrainWidth = Instrument.control(
        "PULSTRNWID?","PULSTRNWID %g,%g",
        """
        Sets the width of pulse number val 1 in tghe pulse-train to val2 in s
        """
    )
    
    
    pulseTrainDelay = Instrument.control(
        "PULSTRNDLY?","PULSETRNDLY %g,%g",
        """
        Sets the delay of pulse number var1 in pulse-train to val2 in s 
        """
    )
    
    
    pulseTrainMake = Instrument.control(
        "PULSTRNMAKE?","PULSTRNMAKE",
        """
        Makes the pulse-train and runs it. Similar to wavePulseTrain 
        """
    )
    def waveform_start(self):
        self.write("OUTPUT ON")
        
    def shutdown(self):
        self.write("OUTPUT OFF")
    
    def __init__(self, adapter, baud_rate = 9600, **kwargs):
        super().__init__(
            adapter,
            "TTi TGA1241",
            gpib = {'read_termination':'\r\n'},
            asrl = {'baud_rate':baud_rate,'read_termination':'\r\n'},
            **kwargs
        )

    