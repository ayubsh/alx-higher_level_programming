#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts new node in sorted linked list
 * @head: ptr to the head of linked list
 * @number: the new number to be inserted
 * Return: returns ptr to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new;

	curr = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= new->n)
	{
		new->next = *head;
		*head = new;
	}
	else
	{

		curr = *head;

		while (curr->next != NULL && curr->next->n < new->n)
		{
			curr = curr->next;
		}
		new->next = curr->next;
		curr->next = new;
	}
	return (new);
}

