from .utils import output_columns, output_link_performance
from .colgen import perform_network_assignment_py
from .dtaapi import perform_network_assignment_DTALite


__all__ = ['perform_network_assignment']


def perform_network_assignment(assignment_mode, iter_num, column_update_num, ui=None):
    """ perform network assignemnt using the selected assignment mode

    WARNING
    -------
    MAKE SURE TO BACKUP agent.csv and link_performance.csv if you have
    called perform_network_assignment() before. Otherwise, they will be
    overwritten by results generated by DTALite.

    Parameters
    ----------
    assignment_mode
        0: Link-based UE
        1: Path-based UE
        2: UE + dynamic traffic assignment
        3: ODME
    
    iter_num
        number of assignment iterations to be performed before optimizing
        column pool
    
    column_update_iter
        number of iterations to be performed on optimizing column pool
    
    ui
        network object generated by pg.read_demand()

    Outputs
    -------
    1. agent.csv: paths/columns
    2. link_performance.csv: assigned volumes and other link attributes on each
       link
    """
    # make sure assignment_mode is right
    assert(assignment_mode in [0, 1, 2, 3])
    # make sure iteration numbers are both non-negative
    assert(iter_num>=0)
    assert(column_update_num>=0)

    if assignment_mode == 1:
        if ui is not None:
            perform_network_assignment_py(assignment_mode, iter_num,
                                          column_update_num, ui)
            # if you do not want to include geometry info in the output file,
            # use pg.output_columns(network, False)
            output_columns(ui)
            output_link_performance(ui)
        else:
            perform_network_assignment_DTALite(assignment_mode, 
                                               iter_num,
                                               column_update_num)
    else:
        perform_network_assignment_DTALite(assignment_mode, 
                                           iter_num,
                                           column_update_num)