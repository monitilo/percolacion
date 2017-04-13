void escribir(char* s, float p, int m , int z, int n){
	FILE*fp;
	fp=fopen(s,"a");

		fprintf(fp,"%d",n);
		fprintf(fp,"%s",";");
		fprintf(fp,"%f",p);
		fprintf(fp,"%s",";");
		fprintf(fp,"%d\n",m);

fclose(fp);

}
