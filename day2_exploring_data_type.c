#include<stdio.h>
int main(int argc, char *a[])
{
	char str[100]; int i; int dot=0;
	fgets(str, sizeof(str), stdin);
	if(isdigit(str[0])|| '-' == str[0]){}
	else if(isalpha(str[0]))
	{
	   printf("This input is of type string.");
	   exit(0);
	}
	else
	{
	   printf("This is something else.");
	   exit(0);
	}
 
	for(i=1; str[i]!='\0'; i++)
	{
	   if(isdigit(str[i]) || '.' == str[i])
	   {
	        if(str[i] == '.')
	        {
	            dot++;
	        }
	   }
	   else if(isalpha(str[i]))
	   {
	       printf("This input is of type string.");
	       exit(0);
	   }
	   else
	   {
	       printf("This is something else.");
	       exit(0);
	   }
 
	}
	if(dot==1)
    	printf("This input is of type Float.");
    else
        printf("This input is of type Integer.");
}