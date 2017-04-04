
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void llenar (int* red,int n, int m, float p); //para poblar la red de n*m con proba p en cada punto
void print_red (int* red,int n, int m);				//para printear la red en forma de matriz en la consola

int main()
{

   time_t t;
   /* Intializes random number generator */
   srand((unsigned) time(&t));

	int* red; //Marcador de memoria para crear la matiz de la red
	int n;     //cantidad de filas
	int m;			// cantidad de columnas
	float p;			//porbabilidad de poblar un lugar (entre 0 y 1)
	p= 0.5	;
	n=10 ;
	m=10 ;
	red=malloc(n*m* sizeof(int));

	llenar(red,n,m,p);
	print_red(red,n,m);
   	free(red);
	
   return(0);
}

void llenar (int*red,int n, int m, float p){
	int i;
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

}

void print_red(int* red, int n, int m)
{
	int i;
	int j;
	for(i=0 ;i<n;i=i+1){

		for(j=0;j<m;j=j+1){ 

			printf("%d", red[i*m+j]);
		}
		printf("\n");
	}
}
