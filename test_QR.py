import LA
import QR
import pytest

def test_GramSchmidt_unstable():
    matrix_a = [[-1,10,1],[2,2,10],[3,-4,3]]
    matrix_b = [[1,2,3],[4,2,-4],[12,0,0]]
    assert QR.GramSchmidt_unstable(matrix_a) == ([[[-0.09901475429766744, 0.9901475429766744, 0.09901475429766744],
      [0.2270950318479295, -0.07439320008811488, 0.9710270327290779], [0.9688260550487688, 0.1186317618427069, -0.21749156337829528]],
      [[10.099504938362077, 0, 0], [2.7724131203346882, 10.015673990810408, 0], [-3.9605901719066976, 3.8919389940834814, 1.7794764276405965]]])

    assert QR.GramSchmidt_unstable(matrix_b) == ([[[0.2672612419124244, 0.5345224838248488, 0.8017837257372732], [0.7259008777437409, 0.4355405266462446, -0.53232731034541], [0.6337502222976297, -0.7242859683401485, 0.27160723812755555]], 
    [[3.7416573867739413, 0, 0], [-1.0690449676496976, 5.903993805649092, 0], [3.2071349029490928, 8.71081053292489, 7.605002667571556]]])

def test_GramSchmidt_stable():
