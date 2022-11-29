#include "lists.h"

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: The singly linked list to check
 *
 * Return: 1 if has a cycle in it or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;
	int found = 0;

	while ((slow && fast) && fast->next)
	{
		slow = slow->next;

		if (fast->next || fast->next->next)
			fast = fast->next->next;
		else
			break;

		if (slow == fast)
		{
			found = 1;
			break;
		}
	}

	return (found);
}
