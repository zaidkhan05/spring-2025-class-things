/*
  Sorting using B-tree
  Interface package for indexed files
  The data file is read only
  using the PBL btree library
  May 2021. J Garrido
  File:  indxsF.c
*/  

#include "indxsF2.h"

// Create an index/key file  
// No data file created
int idxsFCreate(indxsT * idxfp,  char * dfilepath, char * datafilen, 
        FILE * dataFilep, void * filesettag )  {
   
    /*
    Ok, create the key file
    */
	
	// printf("(idxsFCreate) %s %s %ld \n", dfilepath, datafilen, dataFilep);
	strcpy(idxfp->keyFileName, dfilepath);
	strcpy(idxfp->dataFileName, datafilen);
	idxfp->dataFilep = dataFilep;
	
    // printf(" Index file: %s \n", dfilepath);
	// printf(" Index file: %s \n", idxfp->keyFileName);
    // printf("(idxFCreate) idxfp->keyFile: %d file: %s \n", idxfp->keyFile, idxfp->keyFileName);
    //
    idxfp->keyFile = pblKfCreate( idxfp->keyFileName, NULL );
    // printf("(idxFCreate) created idxfp->keyFile: %d file: %s \n", idxfp->keyFile, idxfp->keyFileName);
    if( idxfp->keyFile )
    {
          // printf( "Key file: %s created ok!\n", idxFileName);               
    }
    else
    {
          printf("Check whether there is already an index file with same name \n");
          printf( "Error creating key file: %s \n", idxfp->keyFileName );
          return -1;          
    }
    return 0;
} // end idxsFCreate
/*
  Open the key file and data file
  update = 1;     // to write or update. otherwise is 0
*/
int idxsFOpen(indxsT * idxfp, char * openMode, int update )  {
    /*
	// Open data file, openMode is "br" for read only
    strcpy( openMode, "br");
    idxfp->dataFilep = fopen(idxfp->dataFileName, openMode);
    if ((idxfp->dataFilep) == NULL){
        printf("Error! opening data file: %s \n", idxfp->dataFileName);
        // Program exits if the file pointer returns NULL.
        return -1;
    }
    */
    //
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
} // end idxsFOpen  

// Write  key record
int idxsFWrite(indxsT * idxfp)  {
   long rc = 0;
    
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

//
// Read the next record from data file, by key value
int idxsFReadNext(indxsT * idxfp)  { 
      
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
         
         // printf("(idxFReadNext) Read data recno %s, reclen %d, \n", precPtr->recno, precPtr->recnolen);
         sscanf(idxfp->recno, "%d", &irecno);
         // printf("(idxFReadNext) after pblKfRead %d %u \n", irecno, precPtr->recnolen);
            
         // seek the record on the data file using offset
         bytepos = idxfp->datareclen * (irecno - 1);
                    
         fseek(idxfp->dataFilep, bytepos, SEEK_SET);
         // printf("(idxFReadNext) after fseek bytepos: %d \n", bytepos);
         
         fread(idxfp->datarec, idxfp->datareclen, idxfp->numblk, idxfp->dataFilep);
         // printf("(idxFReadNext) precPtr->datarec %x \n", precPtr->datarec);
         
         return 0;
} // end idxFReadNext

//
// Read the first record from data file and key file
int idxsFReadFirst(indxsT * idxfp)  {    

   unsigned irecno;
   unsigned bytepos;
   long rc = 0;
   
      
   rc = pblKfFirst(idxfp->keyFile, idxfp->keyf, & idxfp->keyflen);
   if (rc < 0) {
        printf("Error ReadFirst %ld \n", rc);
        return -1;
   }
    
// printf("(idxsFReadFirst) A %s %d\n", precPtr->keyf, precPtr->keyflen);
      
   rc = pblKfRead(idxfp->keyFile, idxfp->recno, idxfp->recnolen);
   if (rc < 0) {
        printf("kfRead error %ld \n", rc);
        return -1;
   }
   
   // printf( "(idxsFReadFirst) B %s, reclen %d, \n", precPtr->recno, precPtr->recnolen);
   
   sscanf(idxfp->recno, "%d", &irecno);
   // printf("(idxFReadFirst) C %s %d \n", idxfp->recno, irecno);
            
   // seek the record on the data file using offset
   bytepos = idxfp->datareclen * (irecno - 1);
            
   fseek(idxfp->dataFilep, bytepos, SEEK_SET);
   // printf("(idxFReadFirst) after fseek %d %d \n", bytepos, irecno);

  
   fread( idxfp->datarec, idxfp->datareclen, idxfp->numblk, idxfp->dataFilep);
   // printf("(idxFReadFirst) E %x %ld \n", idxfp->dataFilep, bytepos);
   
   return 0;
}   

// close key file and data file
int idxsFClose (indxsT * idxfp) {
    pblKfClose (idxfp->keyFile);
    fclose(idxfp->dataFilep); 
    return 0;
}   
    