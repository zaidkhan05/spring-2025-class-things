/*
  Interface package for indexed files
  using the PBL btree library
  May 2021. J Garrido
  File:  indxF.c
*/  

#include "indxF.h"

/* Create a data file and its corresponding intex file  */
int idxFCreate(idxFileT * idxfp, char * dfilepath, void * filesettag )  {
  char idxFileName [30];
  int j = 0;
  
    // copy input file name to output name up to the dot
    while ( dfilepath[j] != '.') {
            idxFileName[j] = dfilepath[j];
            j++;
    }
    idxFileName[j] = '.';
    j++;
    idxFileName[j] = '\0';
    strcat(idxFileName, "idx");
    /*
	Ok, create the key file
	*/
	// printf(" Index file: %s \n", idxFileName);
	// printf("(idxFCreate) idxfp->keyFile: %d file: %s \n", idxfp->keyFile, idxFileName);
	//
	idxfp->keyFile = pblKfCreate( idxFileName, NULL );
	// printf("(idxFCreate) created idxfp->keyFile: %d file: %s \n", idxfp->keyFile, idxFileName);
	if( idxfp->keyFile )
    {
          // printf( "Key file: %s created ok!\n", idxFileName);               
    }
    else
    {
		  printf("Check whether there is already an index file with same name \n");
          printf( "Error creating key file: %s \n", idxFileName );
          return -1;		  
    }
	strcpy(idxfp->dataFileName, dfilepath);
	strcpy(idxfp->keyFileName, idxFileName);
	return 0;
} // end idxFCreate
/*
  Open the data file and corresponding key file
  update = 1;     // to write or update. otherwise is 0
*/
int idxFOpen(idxFileT * idxfp, char * openMode, int update )  {
	/* Open data file, openMode is "br", "bw", "brw" */
	idxfp->dataFilep = fopen(idxfp->dataFileName, openMode);
	if ((idxfp->dataFilep) == NULL){
        printf("Error! opening data file: %s \n", idxfp->dataFileName);
        // Program exits if the file pointer returns NULL.
        return -1;
    }
	
	/* Open key file   */
	
    idxfp->keyFile = pblKfOpen( idxfp->keyFileName, update, NULL );
    if( idxfp->keyFile )
    {
       // printf( "Open key file: %s ok!\n", idxfp->keyFileName );    
    }
    else
     {
       printf( "Error opening key file: %s\n", idxfp->keyFileName );
     }
	return 0;
} // end idxFOpen	

// Write data record and corresponding key record
int idxFWrite(idxFileT * idxfp)  {
   long rc = 0;
   // write data record
   fwrite(idxfp->datarec, idxfp->datareclen, idxfp->numblk, idxfp->dataFilep);
   //
   // write to key file
   rc = pblKfInsert(idxfp->keyFile, idxfp->keyf, (size_t) idxfp->keyflen,
                           idxfp->recno, (size_t) idxfp->recnolen);
   if( rc != 0 ) {
          printf( "Error Insert key file\n" ); 
          return -1;
   }
   return 0;
} // end idxFWrite
//
// Given a key value, find and read the record from data file
int idxFReadRec(idxFileT * idxfp)  {
	 unsigned int irecno;
	 unsigned bytepos;
	 long     rc = 0;
	 char key[8];
	 char recno[8];
	 
     rc = pblKfFind(idxfp->keyFile, idxfp->ival, idxfp->keyf, idxfp->keyflen, (void *) idxfp->recno, &(idxfp->recnolen));
	 if (rc < 0) {
			printf("kfFind error %ld \n", rc);
			return -1;
	 }
	 strcpy (key, idxfp->keyf);
	 // printf("(idxFReadRec) Found key %s \n", key);
  	 rc = pblKfRead(idxfp->keyFile, idxfp->recno, idxfp->recnolen);
	 if (rc < 0) {
	    printf("kfRead error %ld \n", rc);
		return -1;
	 }
	 strcpy(recno, idxfp->recno);
	 // printf("(idxFReadRec) Found recno %s \n", recno);
	 
	 sscanf(idxfp->recno, "%d", &irecno);
	 // printf("After pblKfRead %d 
	 // seek the record on the data file using offset
	 bytepos = idxfp->datareclen * (irecno - 1);	
	 // printf("(idxFReadRec) recnolen: %d bytepos: %d \n", idxfp->datareclen, bytepos);
	 fseek(idxfp->dataFilep, bytepos, SEEK_SET);
	 // printf("(idxFReadRec) fseek ok  \n");
	 // fread(& idxfp->datarec, idxfp->datareclen, idxfp->numblk, idxfp->dataFilep); 
	 
	 fread(idxfp->datarec, idxfp->datareclen, idxfp->numblk, idxfp->dataFilep);
	 
	 
	 return 0;
} // end idxFReadRec

// Given a key value, find and delete the record from data file
//  and from the key file
int idxFDeleteRec(idxFileT * idxfp)  {
	 unsigned int irecno;
	 unsigned bytepos;
	 long  rc = 0;
	 
     rc = pblKfFind(idxfp->keyFile, PBLEQ, idxfp->keyf, idxfp->keyflen, (void *) idxfp->recno, &(idxfp->recnolen));
	 if (rc < 0) {
			printf("kfFind error %ld \n", rc);
			return -1;
	 }

	 // printf("Found key %s \n", keyf);
  	 rc = pblKfRead(idxfp->keyFile, idxfp->recno, idxfp->recnolen);
	 if (rc < 0) {
	    printf("kfRead error %ld \n", rc);
		return -1;
	 }
	
	 sscanf(idxfp->recno, "%d", &irecno);
	 // printf("After pblKfRead %d 
	 // seek the record on the data file using offset
	 bytepos = idxfp->datareclen * (irecno - 1);
	 
	 fseek(idxfp->dataFilep, bytepos, SEEK_SET);
	 fread(& idxfp->datarec, idxfp->datareclen, idxfp->numblk, idxfp->dataFilep); 
	 idxfp->datarec = NULL;
	 
	 fseek(idxfp->dataFilep, bytepos, SEEK_SET);
	 // write data record
     fwrite(idxfp->datarec, idxfp->datareclen, idxfp->numblk, idxfp->dataFilep);
	 
	 // printf("Found key %s \n", key);
  	 rc = pblKfDelete(idxfp->keyFile); 
	 if (rc != 0) {
	    printf("kf Delete error %ld \n", rc);
		return -1;
	 }
	 return 0;
} // end idxFDeleteRec
//
// Read the next record from data file, by key value
int idxFReadNext(idxFileT * idxfp)  {	
	  
         unsigned irecno;
		 unsigned bytepos;
		 long rc = 0;
		 
         rc = pblKfNext(idxfp->keyFile, idxfp->keyf, & idxfp->keyflen);
         if (rc < 0) {
            printf("Error idxFReadNext %ld \n", rc);
			return rc;
		 }
         
		 //  read the record number of the data file
         rc = pblKfRead(idxfp->keyFile, idxfp->recno, idxfp->recnolen);
         if (rc < 0) {
             printf("Read error %ld \n", rc);
             return rc;
		 }
		 // printf("(idxFReadNext) Read data recno %s, reclen %d, \n", idxfp->recno, idxfp->recnolen);
         sscanf(idxfp->recno, "%d", &irecno);
         // printf("(idxFReadNext) after pblKfRead %d %u \n", irecno, idxfp->recnolen);
            
         // seek the record on the data file using offset
         bytepos = idxfp->datareclen * (irecno - 1);
                    
         fseek(idxfp->dataFilep, bytepos, SEEK_SET);
         // printf("(idxFReadNext) after fseek bytepos: %d \n", bytepos);
		 
         fread(idxfp->datarec, idxfp->datareclen, idxfp->numblk, idxfp->dataFilep);
		 // printf("(idxFReadNext) idxfp->datarec %x \n", idxfp->datarec);
		 return 0;
} // end idxFReadNext

//
// Read the first record from data file and key file
int idxFReadFirst(idxFileT * idxfp)  {	

   unsigned irecno;
   unsigned bytepos;
   long rc = 0;
   
      
   rc = pblKfFirst(idxfp->keyFile, idxfp->keyf, & idxfp->keyflen);
   if (rc < 0) {
        printf("Error ReadFirst %ld \n", rc);
		return -1;
   }
	
   // printf("(idxFReadFirst) found %s %d\n", idxfp->keyf, idxfp->keyflen);
      
   rc = pblKfRead(idxfp->keyFile, idxfp->recno, idxfp->recnolen);
   if (rc < 0) {
        printf("kfRead error %ld \n", rc);
		return -1;
   }
      
   // printf( "(idxFReadFirst) Read data recno %s, reclen %d, \n", idxfp->recno, idxfp->recnolen);
   
   sscanf(idxfp->recno, "%d", &irecno);
   // printf("(idxFReadFirst) After pblKfRead %s %d \n", idxfp->recno, irecno);
            
   // seek the record on the data file using offset
   bytepos = idxfp->datareclen * (irecno - 1);
            
   fseek(idxfp->dataFilep, bytepos, SEEK_SET);
   // printf("(idxFReadFirst) after fseek %d %d \n", bytepos, irecno);

  
   fread( idxfp->datarec, idxfp->datareclen, idxfp->numblk, idxfp->dataFilep);
   // printf("(idxFReadFirst) idxfp->datarec %x \n", idxfp->datarec);
   return 0;
}   

// close data file and thye corresponding key file 
int idxFClose (idxFileT * idxfp) {
    pblKfClose (idxfp->keyFile);
	fclose(idxfp->dataFilep); 
	return 0;
}	
	