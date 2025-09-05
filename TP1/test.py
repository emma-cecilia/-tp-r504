import pytest
import fonctions as f
 

def test_1():
    assert f.puissance(2,3) == 8
    assert f.puissance(2,2) == 4
        
        
def test_2():
    # cas avec puissances négatives / bases négatives
    assert f.puissance(1, 2) == 1          
    assert f.puissance(1, -2) == 1         
    assert f.puissance(2, -1) == 0.5      
    assert f.puissance(-1, 3) == -1        
    assert f.puissance(-1, -1) == -1       
    assert f.puissance(-2, 2) == 4         
    assert f.puissance(-2, -2) == 0.25    
    
