void escribir(char* s, float* p, int m , int z, int n){
	int i;
	FILE*fp;
	fp=fopen(s,"a");
	fprintf(fp,"%s","el tamaño de la red es");
	fprintf(fp,"%d\n",n);
	fprintf(fp,"%s"," L ;");
	fprintf(fp,"%s","  p ;");
	fprintf(fp,"%s\n"," M ;");

	for(i=0;i<z;i++){
		fprintf(fp,"%d",n);
		fprintf(fp,"%s",";");
		fprintf(fp,"%f",*(p+i));
		fprintf(fp,"%s",";");
		fprintf(fp,"%d\n",m);
		fprintf(fp,"%s\n","facu gato");


	}
fclose(fp);

}

