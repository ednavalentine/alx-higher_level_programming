#include "Python.h"
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: python object pointer
 * Return: python lists
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *lists = (PyListObject *)p;
	Py_ssize_t sizes = PyList_Size(p);
	Py_ssize_t ink;
	PyObject *element;

	if (!PyList_Check(p))
	{
		printf("[ERROR} Invalid Python object. Not a list.\n");
		return;
	}
	printf("[*] Python list info\n");
	printf("[*] Size of the list: %zd\n", sizes);
	printf("[*] Allocated memory: %zd\n", lists->allocated);
	for (ink = 0; ink < sizes; ink++)
	{
		element = PyList_GetItem(p, ink);
		printf("Element %zd: %s\n", ink, Py_TYPE(element)->tp_name);
	}
}
