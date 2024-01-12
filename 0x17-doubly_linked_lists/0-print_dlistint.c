#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/**
 * print_dlistint - function that prints all the elements of a dlistint_t list
 * @h : Points to the head node of the list
 * Return: number of elements in the list
 */

size_t print_dlistint(const dlistint_t *h)
{
	dlistint_t *new;
	int size = 0;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
	{
		return (EXIT_FAILURE);
	}
	*new = *h;
	while (new)
	{
		size++;
		printf("%d\n", new->n);
		new = new->next;
	}
	return (size);
}
