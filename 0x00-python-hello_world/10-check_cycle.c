#include "lists.h"
#include <stdio.h>
/**
 * check_cycle - checks if singly linked list has a cycle
 * @list: pointer to show the cycle
 * Return: 0 if no cycle, 1 if cycle is present
 */
int check_cycle(listint_t *list)
{
	listint_t *cyc_slow = list;
	listint_t *cyc_fast = list;

	if (list == NULL)
		return (0);
	while (cyc_slow != NULL && cyc_fast != NULL && cyc_fast->next != NULL)
	{
		cyc_slow = cyc_slow->next;
		cyc_fast = cyc_fast->next->next;
		if (cyc_slow == cyc_fast)
		{
			return (1);
		}
	}
	return (0);
}
