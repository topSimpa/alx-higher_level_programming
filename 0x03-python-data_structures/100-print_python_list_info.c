#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 *print_python_list_info - this print python list info
 *
 *@p: the Python list object
 *Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t len, elem = 0;

	if (PyList_Check(p))
	{
		len = PyList_Size(p);
		printf("[*] Size of the Python List = %li\n", len);
		printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

		for (; elem < len; elem++)
		{
			if (PyLong_Check(PyList_GetItem(p, elem)))
				printf("Element %li: int\n", elem);
			else if (PyList_Check(PyList_GetItem(p, elem)))
				printf("Element %li: list\n", elem);
			else if (PyBool_Check(PyList_GetItem(p, elem)))
				printf("Element %li: bool\n", elem);
			else if (PyFloat_Check(PyList_GetItem(p, elem)))
				printf("Element %li: float\n", elem);
			else if (PyComplex_Check(PyList_GetItem(p, elem)))
				printf("Element %li: complex\n", elem);
			else if (PyTuple_Check(PyList_GetItem(p, elem)))
				printf("Element %li: tuple\n", elem);
			else if (PyDict_Check(PyList_GetItem(p, elem)))
				printf("Element %li: dictionary\n", elem);
			else if (PySet_Check(PyList_GetItem(p, elem)))
				printf("Element %li: set\n", elem);
			else if (PyUnicode_Check(PyList_GetItem(p, elem)))
				printf("Element %li: str\n", elem);
		}
	}
}
