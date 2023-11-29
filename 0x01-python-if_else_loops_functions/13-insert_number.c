#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
*insert_node-inserts a number into a sorted list.
*@head:ptr the head of the list
*@number:number to insert
*Return:if function fails return  NULL or ptr to the new node
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *nnode = *head, *new;
new = malloc(sizeof(listint_t));
if (new == NULL)
{
return (NULL);
}
new->n = number;
if (nnode == NULL || nnode->n >= number)
{
new->next = nnode;
*head = new;
return (new);
}
while (nnode && nnode->next && nnode->next->n < number)
{
nnode = nnode->next;
}
new->next = nnode->next;
nnode->next = new;
return (new);
}
