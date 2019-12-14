#include <Python.h>
#if PY_VERSION_HEX >= 0x03000000
extern "C" {

PyObject * PyInit__m38b66de29ff08c23d587b5d094a0723b(void) ; /* /home/caci114/Simulation_Practice/SIM_lander/S_source.hh */
PyObject * PyInit__m496ab9d9ae3d6a89daf6de4a1204eb3a(void) ; /* /home/caci114/Simulation_Practice/SIM_lander/models/lander/include/lander.h */
PyObject * PyInit__sim_services(void) ;
PyObject * PyInit__top(void) ;
PyObject * PyInit__swig_double(void) ;
PyObject * PyInit__swig_int(void) ;
PyObject * PyInit__swig_ref(void) ;

void init_swig_modules(void) {

    PyImport_AppendInittab("_m496ab9d9ae3d6a89daf6de4a1204eb3a", PyInit__m496ab9d9ae3d6a89daf6de4a1204eb3a) ;
    PyImport_AppendInittab("_m38b66de29ff08c23d587b5d094a0723b", PyInit__m38b66de29ff08c23d587b5d094a0723b) ;
    PyImport_AppendInittab("_sim_services", PyInit__sim_services) ;
    PyImport_AppendInittab("_top", PyInit__top) ;
    PyImport_AppendInittab("_swig_double", PyInit__swig_double) ;
    PyImport_AppendInittab("_swig_int", PyInit__swig_int) ;
    PyImport_AppendInittab("_swig_ref", PyInit__swig_ref) ;
    return ;
}

}
#else
extern "C" {

void init_m38b66de29ff08c23d587b5d094a0723b(void) ; /* /home/caci114/Simulation_Practice/SIM_lander/S_source.hh */
void init_m496ab9d9ae3d6a89daf6de4a1204eb3a(void) ; /* /home/caci114/Simulation_Practice/SIM_lander/models/lander/include/lander.h */
void init_sim_services(void) ;
void init_top(void) ;
void init_swig_double(void) ;
void init_swig_int(void) ;
void init_swig_ref(void) ;

void init_swig_modules(void) {

    init_m496ab9d9ae3d6a89daf6de4a1204eb3a() ;
    init_m38b66de29ff08c23d587b5d094a0723b() ;
    init_sim_services() ;
    init_top() ;
    init_swig_double() ;
    init_swig_int() ;
    init_swig_ref() ;
    return ;
}

}
#endif
