"""Top-level package for quad_mpc.

This module exposes high-level classes and utilities for building
model predictive control solutions for quadrotors.  The package follows
an object-oriented design so that controllers, models, and simulation
utilities can be composed and extended in user projects.
"""

from .controllers.mpc import MPCController

__all__ = ["MPCController"]

__version__ = "0.1.0"
