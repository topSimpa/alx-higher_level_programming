#include <python3.4/Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
#include <assert.h>
#include "main.h"

/**
 *print_python_list_info - this print python list info
 *
 *@p: the Python list object
 *Return: void
 */

void print_python_list_info(PyObject *p)
{
	py_ssize_t len, elem = 0;

	if (PyList_check(*P))
	{
		len = PyList_Size(*p)
		printf("[*] Size of the Python List = %li", len);
		for (; elem < len; elem++)
		{
			printf("Element %d: %s", elem, PyList_GetItem(elem));
		}
	}
}
