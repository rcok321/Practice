from evaluate_logic_exp import Solution

def test_evaluate_logic_exp0():
    s = 'TO(TOFA(TOF))AT'
    assert Solution.evaluate_logic_exp(s) == 'T'

def test_evaluate_logic_exp1():
    s = 'TO(TAT)'
    assert Solution.evaluate_logic_exp(s) == 'T'

def test_evaluate_logic_exp2():
    s = 'TAF'
    assert Solution.evaluate_logic_exp(s) == 'F'

# def test_evaluate_logic_no_bracket():
#     s = 'TOTOFATOFAT'
#     assert Solution.evaluate_logic_no_bracket(s) == 'T'


# def test_evaluate_logic():
#     p1 = 'F'
#     oper = 'A'
#     p2 = 'T'
#     assert Solution.evaluate_logic(p1,p2,oper) == 'F'