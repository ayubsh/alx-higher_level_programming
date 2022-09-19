#include "lists.h"

/**
 * check_cycle - checks wheather a linked list has cycle in it
 * @list: ptr to the head of linked list
 * Return: returns 0 is there is cycle, otherwise 1
 */
int check_cycle(listint_t *list)
{
	listint_t *f, *s;

	if (list == NULL)
		return (0);
	f = list->next;
	s = list;

	while (f != NULL && f->next != NULL && s != NULL)
	{
		if (f == s)
			return (1);
		f = f->next->next;
		s = s->next;
	}

	return (0);
}
