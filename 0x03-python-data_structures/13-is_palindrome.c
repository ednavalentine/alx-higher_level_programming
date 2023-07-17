#include "lists.h"
#include <string.h>
#include <stddef.h>
/**
 * reverse_list - reverses a singly linked list
 * @head: pointer to head of the singly linked list
 * Return: pointer to new head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *previous = NULL;
	listint_t *curr = head;
	listint_t *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = previous;
		previous = curr;
		curr = next;
	}
	return (previous);
}

/**
 * is_palindrome - check if singly list is a palindrome
 * @head: parameter to be used
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow;
	listint_t *fast;
	listint_t *second_half;
	listint_t *first_half;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	slow = *head;
	fast = *head;
	while (fast->next != NULL && fast->next->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	second_half = reverse_list(slow->next);
	first_half = *head;
	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
			return (0);
		first_half = first_half->next;
		second_half = second_half->next;
	}
	return (1);
}
