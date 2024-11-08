class VHS:
    def __init__(self):
        dref = None
        Tref = None
        omega = None
        alpha = None
        Zrotinf = None
        Tstar = None
        C1 = None
        C2 = None

class Vibmode:
    def __init__(self):
        self.theta = 0
        self.degen = 0
        self.Z = 0

class Gas:
    def __init__(self):
        self.name = ""
        self.mass = 0
        self.dof_rot = 0
        self.dof_vib = 0
        self.Zrot = 0
        self.vhs = VHS()
        self.vibmodes = []