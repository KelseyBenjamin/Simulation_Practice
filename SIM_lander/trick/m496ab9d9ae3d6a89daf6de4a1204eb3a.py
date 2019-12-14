# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_m496ab9d9ae3d6a89daf6de4a1204eb3a', [dirname(__file__)])
        except ImportError:
            import _m496ab9d9ae3d6a89daf6de4a1204eb3a
            return _m496ab9d9ae3d6a89daf6de4a1204eb3a
        if fp is not None:
            try:
                _mod = imp.load_module('_m496ab9d9ae3d6a89daf6de4a1204eb3a', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _m496ab9d9ae3d6a89daf6de4a1204eb3a = swig_import_helper()
    del swig_import_helper
else:
    import _m496ab9d9ae3d6a89daf6de4a1204eb3a
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _m496ab9d9ae3d6a89daf6de4a1204eb3a.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_value(self)
    def incr(self, n=1): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_equal(self, *args)
    def copy(self): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_copy(self)
    def next(self): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_next(self)
    def __next__(self): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator___next__(self)
    def previous(self): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_previous(self)
    def advance(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _m496ab9d9ae3d6a89daf6de4a1204eb3a.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    all_keys = [attr for attr in dir(class_type) if not attr.startswith('__')and attr != '_s' ]
    data_keys = sorted(class_type.__swig_setmethods__.keys())
    method_keys = [ x for x in all_keys if x not in data_keys ]
    raise AttributeError("Type %s does not contain member %s.\n%s data = %s\n%s methods = %s" %
     (self.__class__.__name__,name,self.__class__.__name__,data_keys,self.__class__.__name__,method_keys))

def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        # this line is changed to handle older swigs that used PySwigObject instead of the current SwigPyObject
        if type(value).__name__ == 'SwigPyObject' or type(value).__name__ == 'PySwigObject' :
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        all_keys = [attr for attr in dir(class_type) if not attr.startswith('__') and attr != '_s' ]
        data_keys = sorted(class_type.__swig_setmethods__.keys())
        method_keys = [ x for x in all_keys if x not in data_keys ]
        raise AttributeError("Type %s does not contain member %s.\n%s data = %s\n%s methods = %s" %
         (self.__class__.__name__,name,self.__class__.__name__,data_keys,self.__class__.__name__,method_keys))

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,1)

import sim_services
class Lander(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Lander, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Lander, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pos"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_pos_set
    __swig_getmethods__["pos"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_pos_get
    if _newclass:pos = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_pos_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_pos_set)
    __swig_setmethods__["vel"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_vel_set
    __swig_getmethods__["vel"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_vel_get
    if _newclass:vel = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_vel_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_vel_set)
    __swig_setmethods__["acc"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_acc_set
    __swig_getmethods__["acc"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_acc_get
    if _newclass:acc = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_acc_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_acc_set)
    __swig_setmethods__["angle"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angle_set
    __swig_getmethods__["angle"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angle_get
    if _newclass:angle = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angle_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angle_set)
    __swig_setmethods__["angleDot"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angleDot_set
    __swig_getmethods__["angleDot"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angleDot_get
    if _newclass:angleDot = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angleDot_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angleDot_set)
    __swig_setmethods__["angleDDot"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angleDDot_set
    __swig_getmethods__["angleDDot"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angleDDot_get
    if _newclass:angleDDot = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angleDDot_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_angleDDot_set)
    __swig_setmethods__["thrust"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_thrust_set
    __swig_getmethods__["thrust"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_thrust_get
    if _newclass:thrust = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_thrust_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_thrust_set)
    __swig_setmethods__["throttle"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_throttle_set
    __swig_getmethods__["throttle"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_throttle_get
    if _newclass:throttle = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_throttle_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_throttle_set)
    __swig_setmethods__["rcs_command"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_rcs_command_set
    __swig_getmethods__["rcs_command"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_rcs_command_get
    if _newclass:rcs_command = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_rcs_command_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_rcs_command_set)
    __swig_setmethods__["thrust_max"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_thrust_max_set
    __swig_getmethods__["thrust_max"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_thrust_max_get
    if _newclass:thrust_max = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_thrust_max_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_thrust_max_set)
    __swig_setmethods__["rcs_torque"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_rcs_torque_set
    __swig_getmethods__["rcs_torque"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_rcs_torque_get
    if _newclass:rcs_torque = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_rcs_torque_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_rcs_torque_set)
    __swig_setmethods__["mass"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_mass_set
    __swig_getmethods__["mass"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_mass_get
    if _newclass:mass = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_mass_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_mass_set)
    __swig_setmethods__["moment_of_inertia"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_moment_of_inertia_set
    __swig_getmethods__["moment_of_inertia"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_moment_of_inertia_get
    if _newclass:moment_of_inertia = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_moment_of_inertia_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_moment_of_inertia_set)
    __swig_setmethods__["g"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_g_set
    __swig_getmethods__["g"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_g_get
    if _newclass:g = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_g_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_g_set)
    __swig_setmethods__["manual_throttle_change_command"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_manual_throttle_change_command_set
    __swig_getmethods__["manual_throttle_change_command"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_manual_throttle_change_command_get
    if _newclass:manual_throttle_change_command = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_manual_throttle_change_command_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_manual_throttle_change_command_set)
    __swig_setmethods__["manual_rcs_command"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_manual_rcs_command_set
    __swig_getmethods__["manual_rcs_command"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_manual_rcs_command_get
    if _newclass:manual_rcs_command = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_manual_rcs_command_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_manual_rcs_command_set)
    __swig_setmethods__["Auto_1"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_Auto_1_set
    __swig_getmethods__["Auto_1"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_Auto_1_get
    if _newclass:Auto_1 = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_Auto_1_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_Auto_1_set)
    __swig_setmethods__["Auto_2"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_Auto_2_set
    __swig_getmethods__["Auto_2"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_Auto_2_get
    if _newclass:Auto_2 = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_Auto_2_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_Auto_2_set)
    __swig_setmethods__["survive"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_survive_set
    __swig_getmethods__["survive"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_survive_get
    if _newclass:survive = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_survive_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_survive_set)
    __swig_setmethods__["good_land"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_good_land_set
    __swig_getmethods__["good_land"] = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_good_land_get
    if _newclass:good_land = _swig_property(_m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_good_land_get, _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_good_land_set)
    def lander_default_data(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_lander_default_data(self, *args)
    def lander_init(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_lander_init(self, *args)
    def lander_deriv(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_lander_deriv(self, *args)
    def lander_integ(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_lander_integ(self, *args)
    def __getitem__(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander___getitem__(self, *args)
    def __len__(self, *args): return _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander___len__(self, *args)
    def __init__(self, **kwargs):
        import _sim_services
        this = _m496ab9d9ae3d6a89daf6de4a1204eb3a.new_Lander()
        try: self.this.append(this)
        except: self.this = this
        if 'TMMName' in kwargs:
            self.this.own(0)
            isThisInMM = _sim_services.get_alloc_info_at(this)
            if isThisInMM:
                _sim_services.set_alloc_name_at(this, kwargs['TMMName'])
            else:
                _sim_services.TMM_declare_ext_var(this, _sim_services.TRICK_STRUCTURED, "Lander", 0, kwargs['TMMName'], 0, None)
            alloc_info = _sim_services.get_alloc_info_at(this)
            alloc_info.stcl = _sim_services.TRICK_LOCAL
            alloc_info.alloc_type = _sim_services.TRICK_ALLOC_NEW


    __swig_destroy__ = _m496ab9d9ae3d6a89daf6de4a1204eb3a.delete_Lander
    __del__ = lambda self : None;
Lander_swigregister = _m496ab9d9ae3d6a89daf6de4a1204eb3a.Lander_swigregister
Lander_swigregister(Lander)


def castAsLander(*args):
  return _m496ab9d9ae3d6a89daf6de4a1204eb3a.castAsLander(*args)
castAsLander = _m496ab9d9ae3d6a89daf6de4a1204eb3a.castAsLander
# This file is compatible with both classic and new-style classes.

