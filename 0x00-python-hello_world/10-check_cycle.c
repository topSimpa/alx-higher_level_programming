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
	int count, out = 0;

	node = list;
	while (node)
	{
		match = list;
		node = node->next;
		out++, count = 0;
		do {
			if (node == match)
				return (1);
			match = match->next;
		} while (++count < out);
	}
	return (0);
}


