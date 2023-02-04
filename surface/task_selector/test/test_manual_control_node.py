from task_selector.manual_control_node import ControlNode


def manual_control_buttons():
    node = ControlNode()
    node.passing = True

    # When unpressed should do nothing
    assert 0 == node.l2_r2_math(1, 1)
    # When r2 pressed should spin right
    assert 1 == node.l2_r2_math(1, -1)
    # When l2 pressed should spin left
    assert -1 == node.l2_r2_math(-1, 1)
    # When both pressed should do nothing
    assert 0 == node.l2_r2_math(-1, -1)
