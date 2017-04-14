#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define P			16					// 1/2^P, P=16
#define Z			27000			// iteraciones
#define N			4					// lado de la red simulada


void llenar (int* red,int n, float p); 										//para poblar la red cuadrada con proba p en cada punto
void print_red (int* red,int n);	      									//para printear la red en forma de matriz en la consola
int   hoshen(int *red,int n);  														//asigna etiquetas
int   actualizar(int *red,int *clase,int s,int frag);  		//cambia la red por numeros de etiqueta
void  etiqueta_falsa(int *red,int *clase,int s1,int s2);	//corrije coincidencias de etiquetas
void  corregir_etiqueta(int *red,int *clase,int n); 			//reetiqueta la red con los numeros bien
int  percola(int *red,int n,int frag);
void escribir(char* s, float p, int M ,int n);
void escribirns(char* sns,int* ns, int n,float pmean);
void clusterSize(int *red, int n, int frag, int *fragsz, int *ns);




int main(int argc,char *argv[])
{
  int    n,z,i,j,*red;
  float  prob,denominador;
	int frag; 		//guardo la etiqueta mas grande que pone hoshen
	float pmean=0;
	//float *pc;
	char* lpm="L;P;M 3";
	char* sns="ns(n) 3";
	int m;
	int *fragsz;	//variable donde voy a guardar el tamaño de cada fragmento
	int* ns;		//variable donde guardo la distribucion de fragmentos, salvo en ns[0] que encuentro el tamaño del fragmento mas grande


  n=N;
  z=Z;

	//pc=malloc(sizeof(float)*z);


	ns = malloc(n*n*sizeof(int));  //ns[i] devuelve la cantidad de fragmentos de tamaño i
	
	for(i=0;i<n*n;i++) ns[i] = 0; 	   //inicializo en 0


	if (argc==3) 
     {
       sscanf(argv[1],"%d",&n);
       sscanf(argv[2],"%d",&z);
     }

    
	red=(int *)malloc(n*n*sizeof(int));

	srand(time(NULL));

	for(i=0;i<z;i++)
		{
			prob=0.5;
			denominador=2.0;
 
		for(j=0;j<P;j++)
				{
          llenar(red,n,prob);
      
          frag = hoshen(red,n);
        
          denominador=2.0*denominador;
          if (percola(red,n,frag)!=0)
             prob+=(-1.0/denominador);
					
          else prob+=(1.0/denominador);
        }//fin del for de P----------------------------------
			llenar(red,n,prob);
      
      frag = hoshen(red,n);

			fragsz = malloc(frag*sizeof(int)); // fragsz[i] devuelve el tamaño del i-esimo fragmento, etiquetados por hoshen
			for(j=0;j<frag;j++) fragsz[j] = 0; //inicializo en 0
					
			
			clusterSize(red,n,frag,fragsz,ns); 

			m = fragsz[percola(red,n,frag)]; //guardo el tamaño del cluster percolante, lo que sería el M o Minf

			//pc[i]=prob;
			pmean=prob+pmean;
			escribir(lpm,prob,m,n); // imprime L;P;M en este orden
		
			free(fragsz);

		//printf("%f\n", prob); 


    }		//fin del for de z---------------------------
	
	escribirns(sns,ns, n, pmean/z);


/*	print_red(red,n);
	printf("\n"); 
	printf("%d\n", percola(red,n,frag)); 

	printf("%f\n", prob);

	printf("\n"); 
	printf("%f\n", pmean/Z);
	printf("\n"); 						*/


	free(ns);
  free(red);

  return 0;
}


//--------------------------------------------------------------------------------------------------------------------------------------------//
void llenar (int*red,int n, float p){
	int i;
	int r;

	for (i=0;i<n*n;i++){

	    r=rand() % 100;	

		if (r>p*100){ 

			red[i]=0;
		}
		else {
			red[i]=1;
		}
	}

}
//--------------------------------------------------------------------------------------------------------
void escribir(char* cha, float p, int m , int n){
	FILE*fp;
	fp=fopen(cha,"a");

		fprintf(fp,"%d",n);
		fprintf(fp,"%s",";");
		fprintf(fp,"%f",p);
		fprintf(fp,"%s",";");
		fprintf(fp,"%d\n",m);

fclose(fp);

}

//--------------------------------------------------------------------------------------------------------
void escribirns(char* sns,int* ns, int n,float pmean){
	int i;
	FILE*fp;
	fp=fopen(sns,"a");
	
	fprintf(fp,"%s","promedio todos los <p> = ");
	fprintf(fp,"%f",pmean);
	fprintf(fp,"%s","; largo de red =");
	fprintf(fp,"%d\n",n);
	for(i=0;i<n*n;i++){
		fprintf(fp,"%d\n",*(ns+i));
	}
fclose(fp);

}

//--------------------------------------------------------------------------------------------------------
void clusterSize(int *red, int n, int frag, int *fragsz, int *ns){

	int i;
	int mayor;  // voy a guardar el tamaño del fragmento mas grande

	for(i=0 ; i<n*n; i++) fragsz[red[i]] = fragsz[red[i]] + 1;
	fragsz[0] = 0;  //lo pongo a 0 a mano, ya que conte cuantos 0 hay en la red

	mayor = ns[0];
	for(i=1 ; i<frag; i++){ 

		ns[fragsz[i]] = ns[fragsz[i]] + 1; // arranca en i=1, pues fragsz[0] contiene la cantidad de '0's que encontro en la red
		
		if(fragsz[i]>mayor) mayor = fragsz[i]; //si el fragmento i-esimo es mas grande, lo guardo en mayor

	}	

	//ns[0] = mayor;  //en ns[0] ubico el tamaño del fragmento mas grande

}  

//--------------------------------------------------------------------------------------------------------------------------------------------//

void print_red(int* red, int n)
{
	int i;
	int j;
	for(i=0 ;i<n;i=i+1){

		for(j=0;j<n;j=j+1){ 

			printf("%d ", red[i*n+j]); //dibujo la fila
		}
		printf("\n");                //bajo a la siguiente fila
	}
}

//--------------------------------------------------------------------------------------------------------------------------------------------//

int actualizar(int *red,int *clase,int s,int frag){	 //cambia la red por numeros de etiqueta

	if (s==0){
		clase[frag]=frag;
		*red=frag;
		frag++;
	}
	else{
		*red=s;
	}
	return frag;
}

//--------------------------------------------------------------------------------------------------------------------------------------------//

void  etiqueta_falsa(int *red,int *clase,int s1,int s2){ //corrique coincidencias de etiquetas

	while(clase[s1]<0) s1=-clase[s1];

	while (clase[s2]<0)	s2=-clase[s2];

	if(s1<s2){
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

int percola(int *red,int n, int frag){ //saco los if que tardan mucho

	int* fila1;
	int* filan;
	fila1=malloc(frag*sizeof(int));
	filan=malloc(frag*sizeof(int));
	int i;
	int a;

	for(i=0;i<frag;i++){
		fila1[i]=0;
		filan[i]=0;
	}	
	for(i=0;i<n;i++){
		fila1[red[i]]=1;
		filan[red[i+n*(n-1)]]=1;
	}	

	fila1[0]=0;
	filan[0]=0;
	a=0;

	for(i=0;i<frag;i++){
		a=fila1[i]*filan[i]+a;
	}
	free(fila1);
	free(filan);
return a;

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


  corregir_etiqueta(red,clase,n);

  free(clase);

  return frag;
}

