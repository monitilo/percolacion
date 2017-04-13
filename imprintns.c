
void imprintns(char* s,float* ns, int n,int z){
	int i;
	FILE*fp;
	fp=fopen(s,"a");
	for(i=0;i<n*n;i++){
		fprintf(fp,"%f\n",*(ns+i));
	}
fclose(fp);
