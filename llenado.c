
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void llenar (int* red,int n, int m, float p);

int main()
{
   time_t t;
   /* Intializes random number generator */
   srand((unsigned) time(&t));
	int* red;
	int n;
	int m;
	float p;
	p= 0.1	;
	n=70 ;
	m=15 ;
	red=malloc(n*m* sizeof(int));

	llenar(red,n,m,p);

   
   return(0);
}

void llenar (int*red,int n, int m, float p){
	int i;
	int j;
	int r;

	for (i=0;i<n*m;i++){

	    r=rand() % 100;	

		if (r>p*100){ //esto hace un if

			red[i]=0;
		}
		else {
			red[i]=1;
		}
	}
	for(i=0 ;i<m;i=i+1){

		for(j=0;j<n;j=j+1){ 

			printf("%d", red[i*n+j]);
		}
		printf("\n");
	}
}

