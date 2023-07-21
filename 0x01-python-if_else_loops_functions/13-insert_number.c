#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * insert_node - inserts a no into sorted singly linked list
 * @head: head of the node
 * @number: number to be inserted
 * Return: address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = add_nodeint_end(number);

	if (*head == NULL || number < (*head)->data)
