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
	listint_t *node, *match;

	match = list;
	while(match)
	{
		node = match;
		while (node)
		{
			node = node->next;
			if (node == match)
				return (1);
		}
		match = match->next;
	}
	return (0);
}


