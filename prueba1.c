
#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define N     6        // cantidad de filas PERO ES CUADRADA DESPUES!!!		
#define M     6         //cantidad de columnas
#define P     0.9	//porbabilidad de poblar un lugar (entre 0 y 1)

void llenar (int* red,int n, int m, float p); //para poblar la red de n*m con proba p en cada punto
void print_red (int* red,int n, int m);	      //para printear la red en forma de matriz en la consola
int  actualizar(int *red,int *clase,int s,int frag);	 //cambia la red por numeros de etiqueta
void etiqueta_falsa(int *red,int *clase,int s1,int s2); //corrije coincidencias de etiquetas
void corregir_etiqueta(int *red,int *clase,int n);	 //reetiqueta la red con los numeros bien
int  hoshen(int *red,int n);             	//asigna etiquetas



int main()
{

   time_t t;
   /* Intializes random number generator */
   srand((unsigned) time(&t));

	int* red; //Marcador de memoria para crear la matiz de la red
	int n;     //cantidad de filas
	int m;			// cantidad de columnas
	float p;			//porbabilidad de poblar un lugar (entre 0 y 1)
	p= P	;
	n=N ;
	m=M ;
	red=malloc(n*m* sizeof(int));

	llenar(red,n,m,p);
	print_red(red,n,m);  //printea la red de 1 y 0
	hoshen(red,n);
	printf("\n");        // agrega un espacio entre redes
	print_red(red,n,m);	 // printea la red con numeros


   	free(red);
	
   return(0);
}
//--------------------------------------------------------------------------------------------------------------------------------------------//
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

//--------------------------------------------------------------------------------------------------------------------------------------------//

void print_red(int* red, int n, int m)
{
	int i;
	int j;
	for(i=0 ;i<n;i=i+1){

		for(j=0;j<m;j=j+1){ 

			printf("%d ", red[i*m+j]);
		}
		printf("\n");
	}
}

//--------------------------------------------------------------------------------------------------------------------------------------------//

int actualizar(int *red,int *clase,int s,int frag){	 //cambia la red por numeros de etiqueta

	if (s==0){
		frag++;
		clase[frag]=frag;
		*red=frag;
	}
	else{
		*red=frag;
	}
	return frag;
}

//--------------------------------------------------------------------------------------------------------------------------------------------//

void  etiqueta_falsa(int *red,int *clase,int s1,int s2){ //corrique coincidencias de etiquetas

	while(clase[s1]<0) s1=-clase[s1];

	while (clase[s1]<0)	s2=-clase[s2];

	if(s1<s2){
		clase[s2]=-s1;
		clase[s1]=s1;
		*red=s1;
	}
}
//--------------------------------------------------------------------------------------------------------------------------------------------//

void  corregir_etiqueta(int *red,int *clase,int n){	 //reetiqueta la red con los numeros bien
	int i ;
	int s ;

	for(i=0;i<n*n;i++){

			s=red[i];
			while(clase[s]<0) s=-clase[s];
			red[i] =s ;
	}
}

//--------------------------------------------------------------------------------------------------------------------------------------------//
int hoshen(int *red,int n)
{
  /*
    Esta funcion implementa en algoritmo de Hoshen-Kopelman.
    Recibe el puntero que apunta a la red y asigna etiquetas 
    a cada fragmento de red. 
  */

  int i,j,k,s1,s2,frag;
  int *clase;

  frag=0;
  
  clase=(int *)malloc(n*n*sizeof(int));

  for(k=0;k<n*n;k++) *(clase+k)=frag;
  
  // primer elemento de la red

  s1=0;
  frag=2;
  if (*red) frag=actualizar(red,clase,s1,frag);
  
  // primera fila de la red

  for(i=1;i<n;i++) 
    {
      if (*(red+i)) 
         {
           s1=*(red+i-1);  
           frag=actualizar(red+i,clase,s1,frag);
         }
    }
  

  // el resto de las filas 

  for(i=n;i<n*n;i=i+n)
    {

      // primer elemento de cada fila

      if (*(red+i)) 
         {
           s1=*(red+i-n); 
           frag=actualizar(red+i,clase,s1,frag);
         }

      for(j=1;j<n;j++)
	if (*(red+i+j))
	  {
	    s1=*(red+i+j-1); 
            s2=*(red+i+j-n);

	    if (s1*s2>0)
	      {
		etiqueta_falsa(red+i+j,clase,s1,s2);
	      }
	    else 
	      { if (s1!=0) frag=actualizar(red+i+j,clase,s1,frag);
	        else       frag=actualizar(red+i+j,clase,s2,frag);
	      }
	  }
    }


  //corregir_etiqueta(red,clase,n);

  free(clase);

  return 0;
}

