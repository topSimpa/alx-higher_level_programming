#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check for a cyclic single linked list
 * @list: the single list head
 *
 * Return: 0 false 1 true
 */

int check_cycle(listint_t *list)
{
	listint_t *node;

	node = list;

	while (node)
	{
		node = node->next;
		if (node == list)
			return (1);
	}
	return (0);
}


