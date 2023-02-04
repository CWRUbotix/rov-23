from task_selector.manual_control_node import l2_r2_math


def test_manual_control_l2_r2_math():
    # When unpressed should do nothing
    assert 0 == l2_r2_math(1, 1)
    # When r2 pressed should spin right
    assert 1 == l2_r2_math(1, -1)
    # When l2 pressed should spin left
    assert -1 == l2_r2_math(-1, 1)
    # When both pressed should do nothing
    assert 0 == l2_r2_math(-1, -1)
