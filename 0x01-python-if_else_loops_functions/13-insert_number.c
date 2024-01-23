#include "lists.h"
#include <stdio.h>
#include <stddef.h>
/**
 * insert_node - function that inserts a number into
 * a sorted linked list
 * @head : head node of the sorted linked list
 * @number : number to be added to the sorted
 * linked list
 * Return:address of the new node, NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *curr;
	listint_t *temp;

	curr = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	
	if (*head == NULL)
	{
		*head = new;
	}
	else if (curr->n > number)
	{
		new->next = curr;
		*head = new;
	}
	else
	{
		while (curr->next != NULL && curr->n < number)
		{
			temp = curr;
			curr = curr->next;
		}
		if (curr->next == NULL)
		{
			curr->next = new;
			return (new);
		}
		temp->next = new;
		new->next = curr;
	}
	return (new);
}
