#include<stdio.h>
int queue[100],n,choice,x,i,front,rear;
void insert();
void delete();
void display();
int front = -1;
int rear = -1;
int main()
{
  printf("enter the size of the queue:\n");
  scanf("%d",&n);
  printf("queue operations\n");
  printf("1.insert\n 2.delete\n 3.display\n 4.exit\n");

  do
  {
    printf("enter your choice\n");
    scanf("%d",&choice);
    switch(choice)
    {
      case 1:
      {
        insert();
        break;
      }
      case 2:
      {
        delete();
        break;

      }
      case 3:{
        display();
        break;
      }
      case 4:
      {
        printf("exit point\n");
        break;
      }
      default:
      {
        printf("enter a valid choice:1/2/3/4\n");
        break;
      }
    }
  } while (choice!=4);
    return 0;   
}
void insert()
{
  if(rear>=n-1){
    printf("queue is overflow\n");
  }
  else{
    printf("enter the value to be inserted\n");
    scanf("%d",&x);
    rear++;
    queue[rear]=x;
  }
}
void delete()
{
  if(front==-1)
  {
    printf("queue is underflow\n");
    return;

  }
  else{
    printf("the deleted element is %d\n",queue[front]);
    front++;
  }
}
void display()
{
  if(front==-1){
    printf("the queue is empty\n");
  }
 else{
    printf("the elements in the queue are:\n");
    for(i=front;i<=rear;i++){
      printf("%d\n",queue[i]);
    }
  }
  
}
