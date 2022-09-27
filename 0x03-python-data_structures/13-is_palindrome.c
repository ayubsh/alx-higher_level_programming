#include "lists.h"

/**
 * reversed - reverses the second half of linked list
 * @s: ptr to the middle of linked list
 * Return: returns ptr to the end of linked list
 */

listint_t *reversed(listint_t *s)
{
	listint_t *prev, *tmp;

	prev = NULL;

	while (s != NULL)
	{
		tmp = s->next;
		s->next = prev;
		prev = s;
		s = tmp;
	}

	return (prev);
}

/**
 * is_palindrome - checks weather a linked list is palindrome
 * @head: ptr to the head of linkedlist
 * Return: returns 1 is linked list is palindrome otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *f, *s, *second;

	if (*head == NULL)
		return (1);

	f = *head;
	s = *head;

	while (f != NULL && f->next != NULL)
	{
		f = f->next->next;
		s = s->next;
	}

	f = *head;
	second = reversed(s);

	while (second != NULL)
	{
		if (second->n != f->n)
		{
			return (0);
		}

		f = f->next;
		second = second->next;
	}
	return (1);
}
