
import pytest
import sys
import os
# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import melt

def test_accumulate_above_threshold():
    """
    Test that accumulation is zero when temperature is above the threshold.
    """
    assert melt.accumulate(5, 10, 0) == 0, "Accumulation should be 0 for T > T_threshold"
 
    
def test_accumulate_below_threshold():
    """
    Test that accumulation is equal to precipitation when temperature is below or equal to the threshold.
    """
    assert melt.accumulate(-5, 10, 0) == 10, "Accumulation should be equal to precipitation for T <= T_threshold"
  
    
def test_melt():
    assert melt.melt(-5, melt_factor=2) == 0, "Test failed: Melt rate should be 0 for T < 0"   
    
    
    