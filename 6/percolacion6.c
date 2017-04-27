#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define Z 100000

void print_grid(int* red, int n);
int hoshen(int *red,int n, float p); //devuelve el numero de "fragmentos"
int actualizar(int *red,int *clase,int s,int frag); 
void etiqueta_falsa(int *red,int *clase,int s1,int s2);
void corregir_etiqueta(int *red,int *clase,int n);
void percola(int *red, int n, int frag, int *percolantes); // percolantes[i] guarda 1 o 0 si el fragmento de etiqueta i no/si percolo respectivamente
void clusterSize(int *red, int n, int frag, int *fragsz, int *ns, int *percolantes);	//exploro la red y guardo en ns[i] cuantos fragmentos de tamaño i hay

int main(int argc,char *argv[]){
	
/* DECLARACION DE VARIABLES */

	int *red;
	int n = 4;			//guardo los distintos tamanios la red
	float p = 0;		//guardo las diferentes probabilidades de llenado
	int frag;		//guardo la etiqueta mas grande que pone hoshen
	int *fragsz;	//variable donde voy a guardar el tamaño de cada fragmento
	int *ns;		//variable donde guardo la distribucion de fragmentos, salvo en ns[0] que encuentro el tamaño del fragmento mas grande
	int *percolantes;
	int k,r;
	char name[100]; //voy a guardar el nombre del archivo a exportar
	int m2 = 0;
	FILE *fs;

	if(argc==3){

		sscanf(argv[1],"%d",&n);
		sscanf(argv[2],"%f",&p);
	}

	srand(time(NULL));

	red = malloc(n*n*sizeof(int));


	ns = malloc(n*n*sizeof(int));  //ns[i-1] devuelve la cantidad de fragmentos de tamaño i>=1
	for(k=0;k<n*n;k++) ns[k] = 0; 	   //inicializo en 0			
	printf("L = %d, p = %f\n",n,p);

	for(r=0;r<Z;r++){
	
		frag = hoshen(red,n,p);	
		fragsz = malloc(frag*sizeof(int)); // fragsz[i] devuelve el tamaño del i-esimo fragmento
		percolantes = malloc(frag*sizeof(int)); 
		for(k=0;k<frag;k++){
			fragsz[k] = 0; //inicializo en 0
			percolantes[k] = 0;
		}
		percola(red,n,frag,percolantes);
		clusterSize(red,n,frag,fragsz,ns,percolantes);
			

		free(fragsz);

	}
	
	for(k=0;k<n*n;k++) m2 = ns[k] * (k+1) * (k+1) + m2;
	

	//grabo el dato de m2(p)
	
	sprintf(name,"m2(p),L%d.txt",n);
	fs = fopen(name,"a");
	if(!ftell(fs)){
		fprintf(fs,"/* L %d Z %d */\n",n,Z);
		fprintf(fs,"/* probabilidad; segundo momento */\n");
	}

	fprintf(fs,"%f;%d\n",p,m2);

	fclose(fs);
	free(red);
	free(ns);
	
	return 0;

}

void print_grid(int* red, int n){

	int i;
	int j;

	for(i = 0; i < n; i++){

		for(j = 0; j < n; j++){

			printf("%d ", red[i*n+j]);
		
		}

		printf("\n");
	}	
}

int hoshen(int *red,int n, float p)
{
  /*
    Esta funcion implementa en algoritmo de Hoshen-Kopelman.
    Recibe el puntero que apunta a la red, llena la red y asigna etiquetas 
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
  red[0] = ((float)rand() / (float)RAND_MAX) < p;
  if (*red) frag=actualizar(red,clase,s1,frag);
  
  // primera fila de la red

  for(i=1;i<n;i++) 
    {
	  red[i] = ((float)rand() / (float)RAND_MAX) < p;
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
	  red[i] = ((float)rand() / (float)RAND_MAX) < p;
      if (*(red+i)) 
         {
           s1=*(red+i-n); 
           frag=actualizar(red+i,clase,s1,frag);
         }

      for(j=1;j<n;j++){

			red[i+j] = ((float)rand() / (float)RAND_MAX) < p;
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
    }

  
  corregir_etiqueta(red,clase,n);

  free(clase);

  return frag;
}

int actualizar(int *red,int *clase,int s,int frag){
	
	if(s==0){

		clase[frag]=frag;	
		*red=frag;
		frag++;
	}
	else{
		*red=s;	
	}

	return frag;	

}

void etiqueta_falsa(int *red,int *clase,int s1,int s2){

	while(clase[s1]<0) s1=-clase[s1];
	while(clase[s2]<0) s2=-clase[s2];

	if(s1<s2) {
		clase[s2]=-s1;
		clase[s1]=s1;
		*red=s1;
	}
	else{
		clase[s1]=-s2;
		clase[s2]=s2;
		*red=s2;
	}

}

void corregir_etiqueta(int *red,int *clase,int n){
	
	int i;
	int s;

	for(i=0; i<n*n; i++){
		
		s=red[i];
		while(clase[s]<0) s=-clase[s];
		red[i]=s;

	}
	
}

void percola(int *red, int n, int frag, int *percolantes){
	
	int *fila1;
	int *filan;
	fila1=malloc(frag*sizeof(int));
	filan=malloc(frag*sizeof(int));
	int i;

	for(i=0;i<frag;i++){

		fila1[i]=0;
		filan[i]=0;

	}
	
	for(i=0;i<n;i++){
	
		fila1[red[i]]=1;
		filan[red[(n-1)*n+i]]=1;

	}
	
	i=2; //que arranque desde 2, pues solo me interesa ver a partir de la etiqueta 2
	for(i=2;i<frag;i++){

		percolantes[i] = !(fila1[i] && filan[i]) ; //1 si no percolo, 0 si percolo

	}	

	free(filan);
	free(fila1);
}

void clusterSize(int *red, int n, int frag, int *fragsz, int *ns, int *percolantes){

	int i;
	for(i=0 ; i<n*n; i++) fragsz[red[i]] = (fragsz[red[i]] + 1) * percolantes[red[i]]; //solo guardo los no-percolantes
	fragsz[0] = 0;  //lo pongo a 0 a mano, ya que conte cuantos 0 hay en la red

	for(i=2 ; i<frag; i++) if(fragsz[i]!=0) ns[fragsz[i]-1] = ns[fragsz[i]-1] + 1; // las etiquetas relevantes arrancan en i=2

}






