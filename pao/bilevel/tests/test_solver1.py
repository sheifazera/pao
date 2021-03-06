#  ___________________________________________________________________________
#
#  Pyomo: Python Optimization Modeling Objects
#  Copyright 2017 National Technology and Engineering Solutions of Sandia, LLC
#  Under the terms of Contract DE-NA0003525 with National Technology and 
#  Engineering Solutions of Sandia, LLC, the U.S. Government retains certain 
#  rights in this software.
#  This software is distributed under the 3-clause BSD License.
#  ___________________________________________________________________________

from pyomo.environ import *
from pao.bilevel import *

# Bounded Example (p17)
#
# Near Optimal Robust Bilevel Optimization
# By M. Besancon, M. Anjos, L. Brotcorne


M = ConcreteModel()
M.x=Var(within=NonNegativeReals,bounds=(0,10000))
#M.xI=Var(within=NonNegativeIntegers,bounds=(0,10000))
M.v=Var(within=NonNegativeReals,bounds=(0,10000))
#M.vI=Var(within=NonNegativeIntegers,bounds=(0,10000))
M.c1 = Constraint(expr=-M.x+4*M.v <= 11)
M.c2 = Constraint(expr= M.x+2*M.v <= 13)
M.o = Objective(expr=M.x-10*M.v,sense=minimize)
    
M.sub = SubModel(fixed=(M.x))
M.sub.o  = Objective(expr=-M.x+10*M.v, sense=minimize) #Interdiction version
M.sub.c3 = Constraint(expr=-2*M.x - M.v <= -5)
M.sub.c4 = Constraint(expr= 5*M.x - 4*M.v <= 30)



from pao.bilevel.solvers.solver1 import BilevelSolver1
opt=BilevelSolver1() # use_dual_objective=True
opt.options.solver="gurobi"
opt.solve(M)
